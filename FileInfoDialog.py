# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog
from ui.FileInfoDialog_ui import Ui_Dialog
import json


class FileInfoDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(FileInfoDialog, self).__init__(parent)
        self.setupUi(self)
        # 设置对话框标题
        self.setWindowTitle("Probed File Information")

    def setFileInfo(self, file_info):
        if file_info:
            self.plainTextEdit.setPlainText(file_info)
