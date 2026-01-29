# -*- coding: utf-8 -*-

import os
import ffmpeg
import utils.func as func
import re
import json

from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTreeWidgetItem, QTreeWidget, QHeaderView, QDialog
from PySide6.QtCore import QThread, Signal, Qt
from datetime import datetime
from ui.MainWindow_ui import Ui_MainWindow
from FileInfoDialog import FileInfoDialog
from StreamSortDialog import StreamSortDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    '''
    MainWindow类
    '''

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.file_probe_info = None
        self.selected_streams = []

        self.convert_lastest_timestamp = 0.0

        self.inputFileTreeWidget.setEditTriggers(QTreeWidget.NoEditTriggers)
        self.inputFileTreeWidget.setSelectionMode(QTreeWidget.SingleSelection)
        self.inputFileTreeWidget.setIndentation(10)
        self.inputFileTreeWidget.setStyleSheet("""
            QTreeWidget {
                padding: 5px;
            }
            QTreeWidget::item {
                padding: 5px;
            }
        """)
        self.inputFileTreeWidget.header().setStretchLastSection(False)
        self.inputFileTreeWidget.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.videoEncoderBox.insertItem(0, "H264 (hardware)", userData="h264_amf")
        self.videoEncoderBox.insertItem(1, "H264 (software)", userData="libx264")
        self.videoEncoderBox.insertItem(2, "H265 (hardware)", userData="hevc_amf")
        self.videoEncoderBox.insertItem(3, "H265 (software)", userData="libx265")
        self.videoEncoderBox.insertItem(4, "VP8", userData="libvpx")
        self.videoEncoderBox.insertItem(5, "VP9", userData="libvpx-vp9")
        self.videoEncoderBox.insertItem(6, "WebP", userData="libwebp")
        self.videoEncoderBox.setCurrentIndex(0)

        self.videoBitRateBox.insertItem(0, "300k", userData="300k")
        self.videoBitRateBox.insertItem(1, "500k", userData="500k")
        self.videoBitRateBox.insertItem(2, "750k", userData="750k")
        self.videoBitRateBox.insertItem(3, "1m", userData="1000k")
        self.videoBitRateBox.insertItem(4, "1.5m", userData="1500k")
        self.videoBitRateBox.insertItem(5, "2m", userData="2000k")
        self.videoBitRateBox.setCurrentIndex(1)

        self.videoFrameRateBox.insertItem(0, '10', userData="10")
        self.videoFrameRateBox.insertItem(1, '15', userData="15")
        self.videoFrameRateBox.insertItem(2, '20', userData="20")
        self.videoFrameRateBox.insertItem(3, '24', userData="24")
        self.videoFrameRateBox.insertItem(4, '30', userData="30")
        self.videoFrameRateBox.insertItem(5, '60', userData="60")
        self.videoFrameRateBox.setCurrentIndex(2)

        self.videoSizeBox.insertItem(0, '480*270', userData="480")
        self.videoSizeBox.insertItem(1, '640*360', userData="640")
        self.videoSizeBox.insertItem(2, '1024*576', userData="1024")
        self.videoSizeBox.insertItem(3, '1280*720', userData="1280")
        self.videoSizeBox.insertItem(4, '1920*1080', userData="1920")
        self.videoSizeBox.setCurrentIndex(3)

        self.audioEncoderBox.insertItem(0, "AAC", userData="aac")
        self.audioEncoderBox.insertItem(1, "MP3", userData="libmp3lame")
        self.audioEncoderBox.insertItem(1, "Opus", userData="opus")
        self.audioEncoderBox.insertItem(2, "Vorbis", userData="libvorbis")
        self.audioEncoderBox.setCurrentIndex(0)

        self.audioBitRateBox.insertItem(0, "24k", userData="24k")
        self.audioBitRateBox.insertItem(1, "48k", userData="48k")
        self.audioBitRateBox.insertItem(2, "64k", userData="64k")
        self.audioBitRateBox.insertItem(3, "128k", userData="128k")
        self.audioBitRateBox.insertItem(4, "256k", userData="256k")
        self.audioBitRateBox.setCurrentIndex(1)

        self.setControlsEnabled(True)

        # 创建线程
        self.probe_thread = ProbeThread()
        self.probe_thread.finished_event.connect(self.handleProbeFinishedEvent)

        self.convert_thread = ConvertThread()
        self.convert_thread.finished_event.connect(self.handleConvertFinishedEvent)
        self.convert_thread.progress_event.connect(self.handleConvertProgressEvent)

    def closeEvent(self, event):
        '''
        the close event of MainWIndow
        :param event: close event.
        '''
        if QMessageBox.question(self, "Tips", "Are you sure to exit this programs?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:

            # 停止线程
            if self.probe_thread.running:
                self.probe_thread.stop()
                self.probe_thread = None

            if self.convert_thread.running:
                self.convert_thread.stop()
                self.convert_thread = None

            event.accept()
        else:
            event.ignore()

    def onInputFileButtonClicked(self):
        '''
        Select a source video file.
        '''
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)

        file_name, _ = dialog.getOpenFileName(self, "Open", "", "Video Files (*.avi *.mkv *.mp4 *.mov *.flv *.wmv)")
        if not file_name:
            return

        self.inputFileBox.setText(file_name)
        out_file_base_name, dest_file_ext_name = os.path.splitext(file_name)
        out_file_name = out_file_base_name+"_NEW"+dest_file_ext_name
        self.outputFileBox.setText(out_file_name)

        # 创建并启动探测线程
        self.probe_thread.setParams(file_name)
        self.probe_thread.start()

    def onDetailButtonClicked(self):
        '''
        Show the probing information of the video file.
        '''
        if self.file_probe_info:
            dialog = FileInfoDialog(self)
            dialog.setFileInfo(self.file_probe_info)
            dialog.exec()
        else:
            self.infoLabel.setText("Pleast select a source file first.")

    def onOutputFileButtonClicked(self):
        '''
        Select a destination file for saving.
        '''
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setDefaultSuffix(".mp4")
        filename, _ = dialog.getSaveFileName(self, "Save as", "", "All Files (*);;MPEG-4 (*.mp4);;AVI(*.avi);;MKV(*.mkv);;WMV(*.wmv)")

        if filename:
            self.outputFileBox.setText(filename)

    def onConvertButtonClicked(self):
        '''
        Starting to convert.
        '''
        if self.convert_thread.running is False:
            input_file = self.inputFileBox.text()
            output_file = self.outputFileBox.text()

            if func.is_empty_string(input_file) or func.is_empty_string(output_file):
                self.infoLabel.setText('Pleast select a source file and a destination file.')
                return

            convert_params = {"input_file": input_file,
                              "output_file": output_file,
                              "selected_streams": self.selected_streams,
                              "video_encoder": self.videoEncoderBox.currentData(),
                              "video_bitrate": self.videoBitRateBox.currentData(),
                              "video_framerate": self.videoFrameRateBox.currentData(),
                              "video_size": self.videoSizeBox.currentData(),
                              "audio_encoder": self.audioEncoderBox.currentData(),
                              "audio_bitrate": self.audioBitRateBox.currentData()}
            self.convert_thread.setParams(convert_params)
            self.convert_lastest_timestamp = datetime.now().timestamp()
            self.convert_thread.start()
            self.setControlsEnabled(False)
            self.infoLabel.setText("Converting...")
        else:
            self.convert_thread.stop()
            self.setControlsEnabled(True)
            self.infoLabel.setText("Converting stopped!")

    def onSortButtonClicked(self):
        '''
        Sorting the streams
        '''
        dialog = StreamSortDialog(self)
        dialog.setStreamList(self.selected_streams)
        ret = dialog.exec()
        if ret == QDialog.Accepted:
            self.selected_streams = dialog.getStreamList()
            self.streamLabel.setText(f"Selected Streams: {self.selected_streams}")

    def setControlsEnabled(self, status):
        '''
        Set the controls while converting
        :param status: True - All controls is enabled, False - All controls is not enabled.
        '''
        if status is True:
            self.convertButton.setText('Convert')
        else:
            self.convertButton.setText('Stop')

        self.inputGroupBox.setEnabled(status)
        self.outputGroupBox.setEnabled(status)
        self.progressBar.setValue(0)

    def showStreamInfo(self):
        '''
        Show the selected streams while check the TreeWidget
        '''
        self.selected_streams = []

        root_video_item = self.inputFileTreeWidget.topLevelItem(0)
        for index in range(root_video_item.childCount()):
            item = root_video_item.child(index)
            if item.checkState(0) == Qt.CheckState.Checked:
                self.selected_streams.append(f"v:{index}")

        root_audio_item = self.inputFileTreeWidget.topLevelItem(1)
        for index in range(root_audio_item.childCount()):
            item = root_audio_item.child(index)
            if item.checkState(0) == Qt.CheckState.Checked:
                self.selected_streams.append(f"a:{index}")

        self.streamLabel.setText("Selected Streams:")
        self.streamLabel.setText(
            self.streamLabel.text() + f"{self.selected_streams}")

    def onInputTreeItemChanged(self, item, column):
        '''
        Handle the onInputTreeItemChanged event of the TreeWidget
        :param item: the changed item.
        :param column: the column of the item.
        '''
        if item.parent() is None:
            return
        self.showStreamInfo()

    def handleProbeFinishedEvent(self, data):
        '''
        A finished event from then probe thread.
        :param data: A probing data result.
        '''
        if data is None:
            self.infoLabel.setText("not found video information")
            return

        self.file_probe_info = json.dumps(data, indent=4, ensure_ascii=False)

        self.inputFileTreeWidget.clear()
        root_video_item = QTreeWidgetItem()
        root_video_item.setText(0, "Video Streams")
        self.inputFileTreeWidget.insertTopLevelItem(0, root_video_item)

        root_audio_item = QTreeWidgetItem()
        root_audio_item.setText(0, "Audio Streams")
        self.inputFileTreeWidget.insertTopLevelItem(1, root_audio_item)

        streams = data['streams']
        video_streams = [
            stream for stream in streams if stream['codec_type'] == 'video']
        audio_streams = [
            stream for stream in streams if stream['codec_type'] == 'audio']

        # print(f"video_streams count={len(video_streams)}")
        # print(f"audio_streams count={len(audio_streams)}")

        for index, stream in enumerate(video_streams):
            codec_name = stream.get('codec_name', '')
            codec_long_name = stream.get('codec_long_name', '')
            width = stream.get('width', 0)
            height = stream.get('height', 0)
            frame_rate = stream.get('r_frame_rate', '')
            bit_rate = stream.get('bit_rate', 0)

            item = QTreeWidgetItem()
            item.setText(
                0, f"Video Stream: [v:{index}] [Codec:{codec_name} | {codec_long_name}] [Size:{width}x{height}] [Fps:{frame_rate}] [Bitrate:{bit_rate}]")
            item.setCheckState(
                0, Qt.CheckState.Checked if index == 0 else Qt.CheckState.Unchecked)
            self.inputFileTreeWidget.topLevelItem(0).addChild(item)

        for index, stream in enumerate(audio_streams):
            codec_name = stream.get('codec_name', '')
            codec_long_name = stream.get('codec_long_name', '')
            bit_rate = stream.get('bit_rate', 0)
            language = stream.get('tags', {}).get('language', '')

            item = QTreeWidgetItem()
            item.setText(
                0, f"Audio Stream: [a:{index}] [Codec:{codec_name} | {codec_long_name}] [Bitrate:{bit_rate}] [Language:{language}]")
            item.setCheckState(
                0, Qt.CheckState.Checked if index == 0 else Qt.CheckState.Unchecked)
            self.inputFileTreeWidget.topLevelItem(1).addChild(item)

        self.inputFileTreeWidget.expandAll()
        self.showStreamInfo()

    # 转换进程事件
    def handleConvertProgressEvent(self, progress):
        '''
        A progress event from the convert thread.
        :param progress: the progress value of converting.
        '''
        self.progressBar.setValue(int(progress))

        timestamp_diff = datetime.now().timestamp() - self.convert_lastest_timestamp

        if timestamp_diff <= 0.00:
            timestamp_diff = 0.001
        if progress <= 0.00:
            progress = 0.0001

        speed = progress / timestamp_diff
        left_seconds = (100.00 - progress) / speed

        left_time = func.seconds_to_time(left_seconds)
        self.infoLabel.setText(
            f"Progress: {progress:.2f}%, Left: {left_time}")

    def handleConvertFinishedEvent(self):
        self.setControlsEnabled(True)


class ProbeThread(QThread):
    '''
    A probing thread
    '''
    finished_event = Signal(object)

    def __init__(self):
        super().__init__()
        self.running = False

    def setParams(self, filename):
        self.filename = filename

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        try:
            # 在新线程中运行ffmpeg.probe
            probe_result = ffmpeg.probe(self.filename)
            # 发送探测结果
            self.finished_event.emit(probe_result)
        except Exception as e:
            # 如果发生错误，发送错误信息
            print(f"Exception: {e}")
        finally:
            self.running = False


class ConvertThread(QThread):
    '''
    A converting thread
    '''
    finished_event = Signal()
    progress_event = Signal(float)

    def __init__(self):
        super().__init__()
        self.running = False
        self.process = None
        self.params = None

    def setParams(self, params):
        self.params = params

    def stop(self):
        self.running = False
        if self.process is not None:
            self.process.terminate()
            self.process.wait()
            self.process = None
        self.wait()

    def run(self):
        if self.params is None:
            self.finished_event.emit(-1)
            return

        self.running = True

        try:
            input_file = self.params['input_file']
            output_file = self.params['output_file']
            selected_streams = self.params['selected_streams']
            video_encoder = self.params['video_encoder']
            video_bitrate = self.params['video_bitrate']
            video_framerate = self.params['video_framerate']
            video_size = self.params['video_size']
            audio_encoder = self.params['audio_encoder']
            audio_bitrate = self.params['audio_bitrate']

            input_stream = ffmpeg.input(input_file)

            ready_stream = []
            for item in selected_streams:
                stream = input_stream[item]
                if item.startswith("v:"):
                    stream = stream.filter("scale", w=video_size, h=-1)
                ready_stream.append(stream)

            output_stream = (
                ffmpeg.output(
                    *ready_stream,
                    output_file,
                    vcodec=video_encoder,
                    video_bitrate=video_bitrate,
                    r=video_framerate,
                    acodec=audio_encoder,
                    audio_bitrate=audio_bitrate,
                )
                .global_args("-progress", "pipe:2", "-threads", "8", "-preset", "fast")
                .overwrite_output()
            )
            self.process = output_stream.run_async(pipe_stdout=True, pipe_stderr=True)

            duration_time = 0

            # 使用正则表达式提取时间信息
            duration_pattern = re.compile(r"Duration: (\d+:\d+:\d)")
            time_pattern = re.compile(r"time=(\d+:\d+:\d)")

            # 检查线程是否运行中
            while self.running:
                poll = self.process.poll()
                if poll is not None:
                    break

                stderr_line = (
                    self.process.stderr.readline()
                    .decode("utf-8", errors="ignore")
                    .strip()
                )
                if not stderr_line:
                    continue

                # print(stderr_line)

                if duration_time == 0:
                    # 解析视频总时长
                    duration_match = duration_pattern.search(stderr_line)
                    if duration_match is not None:
                        time_str = duration_match.group(1)
                        h, m, s = map(float, time_str.split(":"))
                        duration_time = h * 3600 + m * 60 + s
                        # print(f"视频总时长: {duration_time} 秒")
                else:
                    time_match = time_pattern.search(stderr_line)
                    if time_match and duration_time > 0:
                        time_str = time_match.group(1)
                        h, m, s = map(float, time_str.split(":"))
                        current_time = h * 3600 + m * 60 + s
                        # print(f"当前处理时间: {current_time} 秒")
                        progress = (current_time / duration_time) * 100.0
                        if 0 <= progress <= 100:
                            # print(
                            #     f"进度: {current_time:.2f} / {duration_time:.2f} = {progress:.2f}%"
                            # )
                            self.progress_event.emit(progress)

            self.finished_event.emit()
        except Exception as e:
            print(f"Exception: {e}")
        finally:
            # 确保进程被终止
            if self.process:
                self.process.terminate()
                self.process.wait()
            self.running = False
