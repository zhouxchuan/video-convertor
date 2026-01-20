# -*- coding: utf-8 -*-

import os
import ffmpeg
import func
import subprocess
import time
import io
import json

from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtCore import QThread,Signal,Slot
from datetime import datetime
from ui.MainWindow_ui import Ui_MainWindow

# -------------------------------------------------------------------
# 创建一个新的线程类
class ProbeThread(QThread):
    # 定义一个信号，用于在探测完成时发送结果
    probeFinished = Signal(dict)

    def __init__(self, fileName):
        super().__init__()
        self.fileName = fileName

    def run(self):
        try:
            # 在新线程中运行ffmpeg.probe
            probe = ffmpeg.probe(self.fileName)
            # 发送探测结果
            self.probeFinished.emit(probe)
        except Exception as e:
            # 如果发生错误，发送错误信息
            self.probeFinished.emit({"error": str(e)})

# -------------------------------------------------------------------
# 转换线程类
class ConvertThread(QThread):
    finished_event = Signal(int)
    progress_event = Signal(float)

    def __init__(self):
        super().__init__()
        self.running = False
        self.process = None
        self.params = None

    def setParams(self,params):
        self.params = params
        pass

    # 运行
    def run(self):
        if self.params is None:
            self.finished_event.emit(-1)
            return
        
        self.running = True
            
        input_file = self.params['input_file']
        output_file = self.params['output_file']
        # duration = self.params['duration']
        video_encoder = self.params['video_encoder']
        video_bitrate = self.params['video_bitrate']
        video_framerate = self.params['video_framerate']
        video_size = self.params['video_width']+'x'+self.params['video_height']
        audio_encoder = self.params['audio_encoder']
        audio_bitrate = self.params['audio_bitrate']
        threads = self.params['threads']

        ffmpeg_command = ['ffmpeg','-i',input_file,'-r',video_framerate,'-c:v','libx264','-c:a','aac','-b:v',video_bitrate,'-s',video_size,'-b:a',audio_bitrate,'-threads',threads,'-preset','fast','-progress','pipe:1','-y',output_file]

        # 使用Popen代替run，并设置stderr为STDOUT，以便可以获取FFmpeg的进度信息
        self.process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        std_output = io.TextIOWrapper(self.process.stdout.buffer, encoding='utf-8')
        
        # 实时读取输出信息
        current_time=None

        while self.running:
            poll = self.process.poll()
            if poll is not None:
                break

            try:
                output = std_output.readline()
                if output is None:
                    continue
            except Exception as e:
                print('Exception:',e)
                continue

            output=output.strip()
            indexForTime = output.startswith('out_time=')
            if indexForTime is False:
                continue
                
            current_time_str=output[9:]
            if current_time_str is None:
                continue

            # print('output:',output)
            current_time = func.timestr_to_seconds(current_time_str)
            if current_time > 0:
                self.progress_event.emit(current_time)

            time.sleep(0.1)
        
        self.running = False
        self.finished_event.emit(0)

    # 停止
    def stop(self):
        if self.process is not None:
            try:
                self.process.terminate()
                self.process.wait()
            except Exception as e:
                self.informationBox.appendPlainText(f"converting process terminate error: {e}")

        self.running = False

# -------------------------------------------------------------------
# 主窗口类
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.duration = None
        self.convert_init_timestamp = 0

        self.destVideoEncoderBox.insertItem(0,"mp4")
        self.destVideoEncoderBox.insertItem(1,"avi")
        self.destVideoEncoderBox.insertItem(2,"flv")
        self.destVideoEncoderBox.insertItem(3,"mkv")
        self.destVideoEncoderBox.insertItem(4,"mov")
        self.destVideoEncoderBox.setCurrentIndex(0)
        
        self.destVideoBitrateBox.insertItem(0,"300k")
        self.destVideoBitrateBox.insertItem(1,"400k")
        self.destVideoBitrateBox.insertItem(2,"500k")
        self.destVideoBitrateBox.insertItem(3,"700k")
        self.destVideoBitrateBox.insertItem(4,"1m")
        self.destVideoBitrateBox.insertItem(5,"1.5m")
        self.destVideoBitrateBox.insertItem(6,"2m")
        self.destVideoBitrateBox.setCurrentIndex(2)

        self.destVideoFramerateBox.insertItem(0,'10')
        self.destVideoFramerateBox.insertItem(1,'15')
        self.destVideoFramerateBox.insertItem(2,'20')
        self.destVideoFramerateBox.insertItem(3,'25')
        self.destVideoFramerateBox.insertItem(4,'30')
        self.destVideoFramerateBox.insertItem(5,'40')
        self.destVideoFramerateBox.insertItem(6,'60')
        self.destVideoFramerateBox.setCurrentIndex(2)

        self.destAudioEncoderBox.insertItem(0,"mp3")
        self.destAudioEncoderBox.insertItem(1,"aac")
        self.destAudioEncoderBox.insertItem(2,"ogg")
        self.destAudioEncoderBox.setCurrentIndex(1)

        self.destAudioBitrateBox.insertItem(0,"24k")
        self.destAudioBitrateBox.insertItem(1,"48k")
        self.destAudioBitrateBox.insertItem(2,"64k")
        self.destAudioBitrateBox.insertItem(3,"128k")
        self.destAudioBitrateBox.insertItem(4,"256k")
        self.destAudioBitrateBox.setCurrentIndex(1)

        self.set_control_converting_status(False)

        self.convertThread = ConvertThread()
        self.convertThread.finished_event.connect(self.handleConvertFinishedEvent)
        self.convertThread.progress_event.connect(self.handleConvertProgressEvent)

    # 窗口关闭事件
    def closeEvent(self, event):
        if QMessageBox.question(self, "Tips", "Are you sure to exit this programs?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            
            # 停止线程
            if self.convertThread.running:
                self.convertThread.stop()

            event.accept()
        else:
            event.ignore()

    # 选择源文件
    def onSrcFileButtonPressed(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)

        fileName, _ = dialog.getOpenFileName(self, "Source Video File", "", "Video Files (*.avi *.mkv *.mp4 *.mov *.flv *.wmv)")
        if not fileName:
            return
        
        self.srcFileBox.setText(fileName)
        destFileBaseName,destFileExtName=os.path.splitext(fileName)
        destFileName=destFileBaseName+"(new)"+destFileExtName
        self.destFileBox.setText(destFileName)

        # 创建并启动探测线程
        self.probeThread = ProbeThread(fileName)
        self.probeThread.probeFinished.connect(self.handleProbeFinishedEvent)
        self.probeThread.start()

        # probe = ffmpeg.probe(fileName)
        # video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        # audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)

        # if video_stream is None:
        #     self.infoLabel.setText("not found video information")
        # else:
        #     self.duration = video_stream.get('duration',0)
        #     bitrate = video_stream.get('bit_rate',0)
        #     profile = video_stream.get('profile','')

        #     duration_str=func.seconds_to_time(self.duration)
        #     bitrate_str = func.convert_bytes(bitrate)
        #     self.sourceDurationBox.setText(duration_str)

        #     self.sourceVideoEncoderBox.setText(video_stream["codec_name"]+" ("+profile+")")
        #     self.sourceVideoBitrateBox.setText(bitrate_str)
        #     self.sourceVideoFramerateBox.setText(video_stream["r_frame_rate"])
        #     self.sourceVideoSizeBox.setText(str(video_stream["width"])+"*"+str(video_stream["height"]))

        # if audio_stream is None:
        #     self.infoLabel.setText("not found audio information")
        # else:
        #     bitrate = func.convert_bytes(audio_stream["bit_rate"])
        #     samplerate = float(audio_stream["sample_rate"])
        #     strSamplerate =  "%3.1f" % (samplerate / 1000.0) + "KHz"

        #     self.sourceAudioEncoderBox.setText(audio_stream["codec_name"])
        #     self.sourceAudioBitrateBox.setText(bitrate)
        #     self.sourceAudioSampleBox.setText(strSamplerate)

        # print(json.dumps(probe))

    # 选择目标文件
    def onDestFileButtonPressed(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setDefaultSuffix(".mp4")
        fileName, _ = dialog.getSaveFileName(self, "Destination Video File", "", "All Files (*);;MPEG-4 (*.mp4);;AVI(*.avi);;MKV(*.mkv);;WMV(*.wmv)")

        if fileName:
            self.destFileBox.setText(fileName)

    # 开始转换文件
    def onConvertButtonPressed(self):

        input_file = self.srcFileBox.text()
        output_file = self.destFileBox.text()

        if func.is_empty_string(input_file) or func.is_empty_string(output_file):
            self.infoLabel.setText('Pleast select a source file and a destination file.')
            return

        if self.convertThread.running is False:
            convertParams = {"input_file":input_file,
                             "output_file":output_file,
                            #  "duration":self.duration,
                             "video_encoder":self.destVideoEncoderBox.currentText(),
                             "video_bitrate":self.destVideoBitrateBox.currentText(),
                             "video_framerate":self.destVideoFramerateBox.currentText(),
                             "video_width":self.destVideoWidthBox.text(),
                             "video_height":self.destVideoHeightBox.text(),
                             "audio_encoder":self.destAudioEncoderBox.currentText(),
                             "audio_bitrate":self.destAudioBitrateBox.currentText(),
                             "threads":self.destConvertThreadsBox.text()}
            self.convertThread.setParams(convertParams)
            self.convert_init_timestamp = datetime.now()
            self.convertThread.start()
            self.set_control_converting_status(True)
            self.infoLabel.setText("Converting...")
        else:
            self.convertThread.stop()
            self.set_control_converting_status(False)
            self.infoLabel.setText("Converting stopped!")


    def onConvertButtonClicked(self):
        pass
    
    # 设置控件输入框显示状态
    def set_control_converting_status(self,status):

        if status is True:
            self.convertButton.setText('Stop')
        else:
            self.convertButton.setText('Convert')

        self.srcFileBox.setEnabled(not status)
        self.destFileBox.setEnabled(not status)
        self.srcFileButton.setEnabled(not status)
        self.destFileButton.setEnabled(not status)
        self.destVideoEncoderBox.setEnabled(not status)
        self.destVideoBitrateBox.setEnabled(not status)
        self.destVideoFramerateBox.setEnabled(not status)
        self.destVideoWidthBox.setEnabled(not status)
        self.destVideoHeightBox.setEnabled(not status)
        self.destAudioEncoderBox.setEnabled(not status)
        self.destAudioBitrateBox.setEnabled(not status)
        self.destConvertThreadsBox.setEnabled(not status)

        self.progressLabel.setText('00:00:00 / 00:00:00')
        self.leftTimeLabel.setText('00:00:00')
        self.progressBar.setValue(0)
        self.progressBar.setFormat('0%')

    # 转换结束信号槽
    @Slot(int)
    def handleConvertFinishedEvent(self, errcode):
        # print("errcode:",errcode)
        self.infoLabel.setText("Converting finished!")
        self.set_control_converting_status(False)

    # 转换进程信号槽
    @Slot(float)
    def handleConvertProgressEvent(self, outtime):
        # print("progress:",progress)
        progress=float(outtime) / float(self.duration) * 100
        progressValue = '%.2f'%progress
        if progress > 100.00:
            progressValue = 100
        self.progressBar.setFormat(str(progressValue)+"%")
        self.progressBar.setValue(int(progress))

        progress_up = func.seconds_to_time(outtime)
        progress_down = func.seconds_to_time(self.duration)
        self.progressLabel.setText(progress_up + '/' + progress_down)

        # 估算剩余时间
        spend_time = datetime.now() - self.convert_init_timestamp
        current_process = outtime
        total_process = float(self.duration)

        left_seconds = spend_time.total_seconds() * total_process / current_process - spend_time.total_seconds()

        if left_seconds >= 0:
            left_time_str = func.seconds_to_time(left_seconds)
            self.leftTimeLabel.setText(left_time_str)

    @Slot(dict)
    def handleProbeFinishedEvent(self, probe):
        if "error" in probe:
            self.infoLabel.setText("Error: " + probe["error"])
        else:
            video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
            audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)

            if video_stream is None:
                self.infoLabel.setText("not found video information")
            else:
                self.duration = video_stream.get('duration',0)
                bitrate = video_stream.get('bit_rate',0)
                profile = video_stream.get('profile','')

                duration_str=func.seconds_to_time(self.duration)
                bitrate_str = func.convert_bytes(bitrate)
                self.sourceDurationBox.setText(duration_str)

                self.sourceVideoEncoderBox.setText(video_stream.get('codec_name','')+" ("+profile+")")
                self.sourceVideoBitrateBox.setText(bitrate_str)
                self.sourceVideoFramerateBox.setText(video_stream.get('r_frame_rate',''))
                self.sourceVideoSizeBox.setText(str(video_stream.get('width',0))+"*"+str(video_stream.get('height',0)))

            if audio_stream is None:
                self.infoLabel.setText("not found audio information")
            else:
                bitrate = func.convert_bytes(audio_stream.get('bit_rate',0))
                samplerate = float(audio_stream.get('sample_rate',0))
                strSamplerate =  "%3.1f" % (samplerate / 1000.0) + "KHz"

                self.sourceAudioEncoderBox.setText(audio_stream.get('codec_name',''))
                self.sourceAudioBitrateBox.setText(bitrate)
                self.sourceAudioSampleBox.setText(strSamplerate)

            print(json.dumps(probe))
