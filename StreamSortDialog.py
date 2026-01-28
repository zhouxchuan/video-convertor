# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog, QListWidget, QListWidgetItem
from PySide6.QtCore import Qt
from ui.StreamSortDialog_ui import Ui_Dialog


class StreamSortDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(StreamSortDialog, self).__init__(parent)
        self.setupUi(self)
        self.stream_list = []

    def setStreamList(self, stream_list):
        self.stream_list = stream_list
        self.listWidget.clear()  # 先清空列表
        for item_text in self.stream_list:
            item = QListWidgetItem(item_text)
            item.setFlags(item.flags() | Qt.ItemIsDragEnabled)
            self.listWidget.addItem(item)

    def getStreamList(self):
        return self.stream_list

    def accept(self):
        # 接受对话框前更新stream_list
        self.stream_list = [self.listWidget.item(i).text() for i in range(self.listWidget.count())]
        super(StreamSortDialog, self).accept()
