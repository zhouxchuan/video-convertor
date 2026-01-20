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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(702, 489)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sourceFileLabel = QLabel(self.centralwidget)
        self.sourceFileLabel.setObjectName(u"sourceFileLabel")

        self.verticalLayout.addWidget(self.sourceFileLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.srcFileBox = QLineEdit(self.centralwidget)
        self.srcFileBox.setObjectName(u"srcFileBox")
        self.srcFileBox.setEnabled(True)
        self.srcFileBox.setReadOnly(True)

        self.horizontalLayout.addWidget(self.srcFileBox)

        self.srcFileButton = QPushButton(self.centralwidget)
        self.srcFileButton.setObjectName(u"srcFileButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.srcFileButton.sizePolicy().hasHeightForWidth())
        self.srcFileButton.setSizePolicy(sizePolicy)
        self.srcFileButton.setMaximumSize(QSize(35, 16777215))
        self.srcFileButton.setBaseSize(QSize(0, 0))
        self.srcFileButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.srcFileButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.destinationFileLabel = QLabel(self.centralwidget)
        self.destinationFileLabel.setObjectName(u"destinationFileLabel")

        self.verticalLayout.addWidget(self.destinationFileLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.destFileBox = QLineEdit(self.centralwidget)
        self.destFileBox.setObjectName(u"destFileBox")
        self.destFileBox.setEnabled(True)
        self.destFileBox.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.destFileBox)

        self.destFileButton = QPushButton(self.centralwidget)
        self.destFileButton.setObjectName(u"destFileButton")
        self.destFileButton.setMaximumSize(QSize(35, 16777215))
        self.destFileButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.destFileButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 6, -1, 6)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 250))
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.sourceDurationLabel = QLabel(self.groupBox_2)
        self.sourceDurationLabel.setObjectName(u"sourceDurationLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sourceDurationLabel.sizePolicy().hasHeightForWidth())
        self.sourceDurationLabel.setSizePolicy(sizePolicy2)
        self.sourceDurationLabel.setMinimumSize(QSize(100, 0))
        self.sourceDurationLabel.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.sourceDurationLabel)

        self.sourceDurationBox = QLineEdit(self.groupBox_2)
        self.sourceDurationBox.setObjectName(u"sourceDurationBox")
        self.sourceDurationBox.setEnabled(False)
        self.sourceDurationBox.setAlignment(Qt.AlignCenter)
        self.sourceDurationBox.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.sourceDurationBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.sourceVideoEncoderLabel = QLabel(self.groupBox_2)
        self.sourceVideoEncoderLabel.setObjectName(u"sourceVideoEncoderLabel")
        self.sourceVideoEncoderLabel.setMinimumSize(QSize(100, 0))
        self.sourceVideoEncoderLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_17.addWidget(self.sourceVideoEncoderLabel)

        self.sourceVideoEncoderBox = QLineEdit(self.groupBox_2)
        self.sourceVideoEncoderBox.setObjectName(u"sourceVideoEncoderBox")
        self.sourceVideoEncoderBox.setEnabled(False)
        self.sourceVideoEncoderBox.setAlignment(Qt.AlignCenter)
        self.sourceVideoEncoderBox.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.sourceVideoEncoderBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.sourceVideoBitrateLabel = QLabel(self.groupBox_2)
        self.sourceVideoBitrateLabel.setObjectName(u"sourceVideoBitrateLabel")
        self.sourceVideoBitrateLabel.setMinimumSize(QSize(100, 0))
        self.sourceVideoBitrateLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_12.addWidget(self.sourceVideoBitrateLabel)

        self.sourceVideoBitrateBox = QLineEdit(self.groupBox_2)
        self.sourceVideoBitrateBox.setObjectName(u"sourceVideoBitrateBox")
        self.sourceVideoBitrateBox.setEnabled(False)
        self.sourceVideoBitrateBox.setAlignment(Qt.AlignCenter)
        self.sourceVideoBitrateBox.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.sourceVideoBitrateBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.sourceVideoFrameLabel = QLabel(self.groupBox_2)
        self.sourceVideoFrameLabel.setObjectName(u"sourceVideoFrameLabel")
        self.sourceVideoFrameLabel.setMinimumSize(QSize(100, 0))
        self.sourceVideoFrameLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_13.addWidget(self.sourceVideoFrameLabel)

        self.sourceVideoFramerateBox = QLineEdit(self.groupBox_2)
        self.sourceVideoFramerateBox.setObjectName(u"sourceVideoFramerateBox")
        self.sourceVideoFramerateBox.setEnabled(False)
        self.sourceVideoFramerateBox.setAlignment(Qt.AlignCenter)
        self.sourceVideoFramerateBox.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.sourceVideoFramerateBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.sourceVideoSizeLabel = QLabel(self.groupBox_2)
        self.sourceVideoSizeLabel.setObjectName(u"sourceVideoSizeLabel")
        self.sourceVideoSizeLabel.setMinimumSize(QSize(100, 0))
        self.sourceVideoSizeLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_14.addWidget(self.sourceVideoSizeLabel)

        self.sourceVideoSizeBox = QLineEdit(self.groupBox_2)
        self.sourceVideoSizeBox.setObjectName(u"sourceVideoSizeBox")
        self.sourceVideoSizeBox.setEnabled(False)
        self.sourceVideoSizeBox.setAlignment(Qt.AlignCenter)
        self.sourceVideoSizeBox.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.sourceVideoSizeBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.sourceAudioEncoderLabel = QLabel(self.groupBox_2)
        self.sourceAudioEncoderLabel.setObjectName(u"sourceAudioEncoderLabel")
        self.sourceAudioEncoderLabel.setMinimumSize(QSize(100, 0))
        self.sourceAudioEncoderLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_15.addWidget(self.sourceAudioEncoderLabel)

        self.sourceAudioEncoderBox = QLineEdit(self.groupBox_2)
        self.sourceAudioEncoderBox.setObjectName(u"sourceAudioEncoderBox")
        self.sourceAudioEncoderBox.setEnabled(False)
        self.sourceAudioEncoderBox.setAlignment(Qt.AlignCenter)
        self.sourceAudioEncoderBox.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.sourceAudioEncoderBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.sourceAudioBitstreamsLabel = QLabel(self.groupBox_2)
        self.sourceAudioBitstreamsLabel.setObjectName(u"sourceAudioBitstreamsLabel")
        self.sourceAudioBitstreamsLabel.setMinimumSize(QSize(100, 0))
        self.sourceAudioBitstreamsLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_16.addWidget(self.sourceAudioBitstreamsLabel)

        self.sourceAudioBitrateBox = QLineEdit(self.groupBox_2)
        self.sourceAudioBitrateBox.setObjectName(u"sourceAudioBitrateBox")
        self.sourceAudioBitrateBox.setEnabled(False)
        self.sourceAudioBitrateBox.setAlignment(Qt.AlignCenter)
        self.sourceAudioBitrateBox.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.sourceAudioBitrateBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.sourceAudioSampleLabel = QLabel(self.groupBox_2)
        self.sourceAudioSampleLabel.setObjectName(u"sourceAudioSampleLabel")
        self.sourceAudioSampleLabel.setMinimumSize(QSize(100, 0))
        self.sourceAudioSampleLabel.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_19.addWidget(self.sourceAudioSampleLabel)

        self.sourceAudioSampleBox = QLineEdit(self.groupBox_2)
        self.sourceAudioSampleBox.setObjectName(u"sourceAudioSampleBox")
        self.sourceAudioSampleBox.setEnabled(False)
        self.sourceAudioSampleBox.setAlignment(Qt.AlignCenter)
        self.sourceAudioSampleBox.setReadOnly(True)

        self.horizontalLayout_19.addWidget(self.sourceAudioSampleBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_18.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(0, 250))
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.label)

        self.destVideoEncoderBox = QComboBox(self.groupBox)
        self.destVideoEncoderBox.setObjectName(u"destVideoEncoderBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.destVideoEncoderBox.sizePolicy().hasHeightForWidth())
        self.destVideoEncoderBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.destVideoEncoderBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.label_2)

        self.destVideoBitrateBox = QComboBox(self.groupBox)
        self.destVideoBitrateBox.setObjectName(u"destVideoBitrateBox")
        sizePolicy3.setHeightForWidth(self.destVideoBitrateBox.sizePolicy().hasHeightForWidth())
        self.destVideoBitrateBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.destVideoBitrateBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.destVideoFramerateBox = QComboBox(self.groupBox)
        self.destVideoFramerateBox.setObjectName(u"destVideoFramerateBox")
        sizePolicy3.setHeightForWidth(self.destVideoFramerateBox.sizePolicy().hasHeightForWidth())
        self.destVideoFramerateBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.destVideoFramerateBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.label_5)

        self.destVideoWidthBox = QLineEdit(self.groupBox)
        self.destVideoWidthBox.setObjectName(u"destVideoWidthBox")

        self.horizontalLayout_6.addWidget(self.destVideoWidthBox)

        self.destVideoHeightBox = QLineEdit(self.groupBox)
        self.destVideoHeightBox.setObjectName(u"destVideoHeightBox")

        self.horizontalLayout_6.addWidget(self.destVideoHeightBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))
        self.label_7.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.destAudioEncoderBox = QComboBox(self.groupBox)
        self.destAudioEncoderBox.setObjectName(u"destAudioEncoderBox")
        sizePolicy3.setHeightForWidth(self.destAudioEncoderBox.sizePolicy().hasHeightForWidth())
        self.destAudioEncoderBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.destAudioEncoderBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))
        self.label_8.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.label_8)

        self.destAudioBitrateBox = QComboBox(self.groupBox)
        self.destAudioBitrateBox.setObjectName(u"destAudioBitrateBox")
        sizePolicy3.setHeightForWidth(self.destAudioBitrateBox.sizePolicy().hasHeightForWidth())
        self.destAudioBitrateBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.destAudioBitrateBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 0))
        self.label_9.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_9.addWidget(self.label_9)

        self.destConvertThreadsBox = QSpinBox(self.groupBox)
        self.destConvertThreadsBox.setObjectName(u"destConvertThreadsBox")
        self.destConvertThreadsBox.setAlignment(Qt.AlignCenter)
        self.destConvertThreadsBox.setMinimum(1)
        self.destConvertThreadsBox.setMaximum(10)
        self.destConvertThreadsBox.setValue(8)

        self.horizontalLayout_9.addWidget(self.destConvertThreadsBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_18.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(15)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.progressLabel_2 = QLabel(self.centralwidget)
        self.progressLabel_2.setObjectName(u"progressLabel_2")

        self.horizontalLayout_20.addWidget(self.progressLabel_2)

        self.progressLabel = QLabel(self.centralwidget)
        self.progressLabel.setObjectName(u"progressLabel")

        self.horizontalLayout_20.addWidget(self.progressLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_20.addWidget(self.label_10)

        self.leftTimeLabel = QLabel(self.centralwidget)
        self.leftTimeLabel.setObjectName(u"leftTimeLabel")
        self.leftTimeLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.leftTimeLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_20)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setMinimumSize(QSize(0, 12))
        self.progressBar.setMaximumSize(QSize(16777215, 12))
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.BottomToTop)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(4, 4, 4, 4)
        self.infoLabel = QLabel(self.centralwidget)
        self.infoLabel.setObjectName(u"infoLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy4)
        self.infoLabel.setFrameShape(QFrame.NoFrame)
        self.infoLabel.setFrameShadow(QFrame.Sunken)

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
        self.exitButton.pressed.connect(MainWindow.close)
        self.srcFileButton.pressed.connect(MainWindow.onSrcFileButtonPressed)
        self.destFileButton.pressed.connect(MainWindow.onDestFileButtonPressed)
        self.convertButton.pressed.connect(MainWindow.onConvertButtonPressed)
        self.convertButton.clicked.connect(MainWindow.onConvertButtonClicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Video Convertor 1.0 by Kenny Copyright@2025", None))
        self.sourceFileLabel.setText(QCoreApplication.translate("MainWindow", u"Source File:", None))
        self.srcFileButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.destinationFileLabel.setText(QCoreApplication.translate("MainWindow", u"Destination File:", None))
        self.destFileButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Source Parameters:", None))
        self.sourceDurationLabel.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.sourceVideoEncoderLabel.setText(QCoreApplication.translate("MainWindow", u"Video Encoder:", None))
        self.sourceVideoEncoderBox.setPlaceholderText("")
        self.sourceVideoBitrateLabel.setText(QCoreApplication.translate("MainWindow", u"Video BitRate:", None))
        self.sourceVideoBitrateBox.setPlaceholderText("")
        self.sourceVideoFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Video FrameRate:", None))
        self.sourceVideoFramerateBox.setPlaceholderText("")
        self.sourceVideoSizeLabel.setText(QCoreApplication.translate("MainWindow", u"Video Size:", None))
        self.sourceAudioEncoderLabel.setText(QCoreApplication.translate("MainWindow", u"Audio Encoder:", None))
        self.sourceAudioEncoderBox.setPlaceholderText("")
        self.sourceAudioBitstreamsLabel.setText(QCoreApplication.translate("MainWindow", u"Audio BitRate:", None))
        self.sourceAudioBitrateBox.setPlaceholderText("")
        self.sourceAudioSampleLabel.setText(QCoreApplication.translate("MainWindow", u"Audio Sample:", None))
        self.sourceAudioSampleBox.setPlaceholderText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Destination Parameters:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Video Encoder:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Video BitRate:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Video FrameRate:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Video Size:", None))
        self.destVideoWidthBox.setText(QCoreApplication.translate("MainWindow", u"640", None))
        self.destVideoHeightBox.setText(QCoreApplication.translate("MainWindow", u"480", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Audio Encoder:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Audio BitRate:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Threads:", None))
        self.progressLabel_2.setText(QCoreApplication.translate("MainWindow", u"Duration progress:", None))
        self.progressLabel.setText(QCoreApplication.translate("MainWindow", u"00:00:00 / 00:00:00", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Left Time:", None))
        self.leftTimeLabel.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"select source file and click \"Convert\" button to execute.", None))
        self.convertButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

