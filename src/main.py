# -*- coding: utf-8 -*-

import sys

from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow

# 程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
