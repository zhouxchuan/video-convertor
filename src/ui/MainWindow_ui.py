# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(897, 588)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.inputGroupBox = QGroupBox(self.centralwidget)
        self.inputGroupBox.setObjectName(u"inputGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputGroupBox.sizePolicy().hasHeightForWidth())
        self.inputGroupBox.setSizePolicy(sizePolicy)
        self.inputGroupBox.setMinimumSize(QSize(0, 250))
        self.inputGroupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.verticalLayout = QVBoxLayout(self.inputGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.sourceFileLabel = QLabel(self.inputGroupBox)
        self.sourceFileLabel.setObjectName(u"sourceFileLabel")

        self.horizontalLayout_21.addWidget(self.sourceFileLabel)

        self.inputFileBox = QLineEdit(self.inputGroupBox)
        self.inputFileBox.setObjectName(u"inputFileBox")
        self.inputFileBox.setEnabled(True)
        self.inputFileBox.setFrame(True)
        self.inputFileBox.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.inputFileBox)

        self.inputFileButton = QPushButton(self.inputGroupBox)
        self.inputFileButton.setObjectName(u"inputFileButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputFileButton.sizePolicy().hasHeightForWidth())
        self.inputFileButton.setSizePolicy(sizePolicy1)
        self.inputFileButton.setMaximumSize(QSize(35, 16777215))
        self.inputFileButton.setBaseSize(QSize(0, 0))
        self.inputFileButton.setAutoDefault(False)

        self.horizontalLayout_21.addWidget(self.inputFileButton)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.inputFileTreeWidget = QTreeWidget(self.inputGroupBox)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.inputFileTreeWidget.setHeaderItem(__qtreewidgetitem)
        self.inputFileTreeWidget.setObjectName(u"inputFileTreeWidget")
        self.inputFileTreeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.inputFileTreeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.inputFileTreeWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.inputFileTreeWidget.setIndentation(10)
        self.inputFileTreeWidget.setRootIsDecorated(True)
        self.inputFileTreeWidget.setWordWrap(False)
        self.inputFileTreeWidget.setHeaderHidden(True)

        self.verticalLayout.addWidget(self.inputFileTreeWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.detailButton = QPushButton(self.inputGroupBox)
        self.detailButton.setObjectName(u"detailButton")

        self.horizontalLayout_2.addWidget(self.detailButton)

        self.streamLabel = QLabel(self.inputGroupBox)
        self.streamLabel.setObjectName(u"streamLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.streamLabel.sizePolicy().hasHeightForWidth())
        self.streamLabel.setSizePolicy(sizePolicy2)
        self.streamLabel.setFrameShape(QFrame.Shape.StyledPanel)

        self.horizontalLayout_2.addWidget(self.streamLabel)

        self.sortButton = QPushButton(self.inputGroupBox)
        self.sortButton.setObjectName(u"sortButton")

        self.horizontalLayout_2.addWidget(self.sortButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.inputGroupBox)

        self.outputGroupBox = QGroupBox(self.centralwidget)
        self.outputGroupBox.setObjectName(u"outputGroupBox")
        self.outputGroupBox.setEnabled(True)
        sizePolicy.setHeightForWidth(self.outputGroupBox.sizePolicy().hasHeightForWidth())
        self.outputGroupBox.setSizePolicy(sizePolicy)
        self.outputGroupBox.setMinimumSize(QSize(0, 250))
        self.outputGroupBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.gridLayout = QGridLayout(self.outputGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.destinationFileLabel = QLabel(self.outputGroupBox)
        self.destinationFileLabel.setObjectName(u"destinationFileLabel")

        self.horizontalLayout.addWidget(self.destinationFileLabel)

        self.outputFileBox = QLineEdit(self.outputGroupBox)
        self.outputFileBox.setObjectName(u"outputFileBox")
        self.outputFileBox.setEnabled(True)
        self.outputFileBox.setReadOnly(False)

        self.horizontalLayout.addWidget(self.outputFileBox)

        self.outputFileButton = QPushButton(self.outputGroupBox)
        self.outputFileButton.setObjectName(u"outputFileButton")
        self.outputFileButton.setMaximumSize(QSize(35, 16777215))
        self.outputFileButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.outputFileButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.outputGroupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_3.addWidget(self.label)

        self.videoEncoderBox = QComboBox(self.outputGroupBox)
        self.videoEncoderBox.setObjectName(u"videoEncoderBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.videoEncoderBox.sizePolicy().hasHeightForWidth())
        self.videoEncoderBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.videoEncoderBox)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.outputGroupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.videoBitRateBox = QComboBox(self.outputGroupBox)
        self.videoBitRateBox.setObjectName(u"videoBitRateBox")
        sizePolicy3.setHeightForWidth(self.videoBitRateBox.sizePolicy().hasHeightForWidth())
        self.videoBitRateBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.videoBitRateBox)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.outputGroupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.videoFrameRateBox = QComboBox(self.outputGroupBox)
        self.videoFrameRateBox.setObjectName(u"videoFrameRateBox")
        sizePolicy3.setHeightForWidth(self.videoFrameRateBox.sizePolicy().hasHeightForWidth())
        self.videoFrameRateBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.videoFrameRateBox)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.outputGroupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.videoSizeBox = QComboBox(self.outputGroupBox)
        self.videoSizeBox.setObjectName(u"videoSizeBox")

        self.horizontalLayout_6.addWidget(self.videoSizeBox)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.outputGroupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.audioEncoderBox = QComboBox(self.outputGroupBox)
        self.audioEncoderBox.setObjectName(u"audioEncoderBox")
        sizePolicy3.setHeightForWidth(self.audioEncoderBox.sizePolicy().hasHeightForWidth())
        self.audioEncoderBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.audioEncoderBox)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.outputGroupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(120, 0))
        self.label_8.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_8.addWidget(self.label_8)

        self.audioBitRateBox = QComboBox(self.outputGroupBox)
        self.audioBitRateBox.setObjectName(u"audioBitRateBox")
        sizePolicy3.setHeightForWidth(self.audioBitRateBox.sizePolicy().hasHeightForWidth())
        self.audioBitRateBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.audioBitRateBox)


        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.outputGroupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setMinimumSize(QSize(0, 12))
        self.progressBar.setMaximumSize(QSize(16777215, 12))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.Direction.BottomToTop)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(4, 4, 4, 4)
        self.infoLabel = QLabel(self.centralwidget)
        self.infoLabel.setObjectName(u"infoLabel")
        sizePolicy2.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy2)
        self.infoLabel.setFrameShape(QFrame.Shape.NoFrame)
        self.infoLabel.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.infoLabel)

        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        self.convertButton.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.convertButton)

        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")

        self.horizontalLayout_11.addWidget(self.exitButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exitButton.clicked.connect(MainWindow.close)
        self.inputFileButton.clicked.connect(MainWindow.onInputFileButtonClicked)
        self.outputFileButton.clicked.connect(MainWindow.onOutputFileButtonClicked)
        self.convertButton.clicked.connect(MainWindow.onConvertButtonClicked)
        self.detailButton.clicked.connect(MainWindow.onDetailButtonClicked)
        self.inputFileTreeWidget.itemChanged.connect(MainWindow.onInputTreeItemChanged)
        self.sortButton.clicked.connect(MainWindow.onSortButtonClicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Video Convertor 2.0 by Kenny Copyright@2026", None))
        self.inputGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Source", None))
        self.sourceFileLabel.setText(QCoreApplication.translate("MainWindow", u"Input File:", None))
        self.inputFileButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.detailButton.setText(QCoreApplication.translate("MainWindow", u"Detail...", None))
        self.streamLabel.setText("")
        self.sortButton.setText(QCoreApplication.translate("MainWindow", u"Sort...", None))
        self.outputGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.destinationFileLabel.setText(QCoreApplication.translate("MainWindow", u"Output File:", None))
        self.outputFileButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Video Encoder:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Video Bit Rate:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Video Frame Rate:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Video Size:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Audio Encoder:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Audio Bit Rate:", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.infoLabel.setText("")
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

