# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/nicola/AppData/Local/Temp/splashScreenUIzfRPYw.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_splash_screen(object):
    def setupUi(self, splash_screen):
        splash_screen.setObjectName("splash_screen")
        splash_screen.resize(300, 300)
        splash_screen.setMinimumSize(QtCore.QSize(300, 300))
        splash_screen.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(splash_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.container = QtWidgets.QFrame(self.centralwidget)
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.container)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.circle_bg = QtWidgets.QFrame(self.container)
        self.circle_bg.setStyleSheet("QFrame{\n"
"    background-color : #222222;\n"
"    color: #FFFFFF;\n"
"    border-radius: 120px;\n"
"    font: 8pt \"Segoe UI\";\n"
"}")
        self.circle_bg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circle_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circle_bg.setObjectName("circle_bg")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.circle_bg)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.texts = QtWidgets.QFrame(self.circle_bg)
        self.texts.setMaximumSize(QtCore.QSize(16777215, 180))
        self.texts.setStyleSheet("background:None")
        self.texts.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.texts.setFrameShadow(QtWidgets.QFrame.Raised)
        self.texts.setObjectName("texts")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.texts)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.title_lbl = QtWidgets.QLabel(self.texts)
        self.title_lbl.setMinimumSize(QtCore.QSize(0, 30))
        self.title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.gridLayout.addWidget(self.title_lbl, 0, 0, 1, 1)
        self.loding_lbl = QtWidgets.QLabel(self.texts)
        self.loding_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.loding_lbl.setObjectName("loding_lbl")
        self.gridLayout.addWidget(self.loding_lbl, 3, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.texts)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.version_lbl = QtWidgets.QLabel(self.frame)
        self.version_lbl.setMinimumSize(QtCore.QSize(100, 24))
        self.version_lbl.setMaximumSize(QtCore.QSize(100, 24))
        self.version_lbl.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 0, 127);\n"
"    border-radius: 12px;\n"
"}")
        self.version_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.version_lbl.setObjectName("version_lbl")
        self.verticalLayout_3.addWidget(self.version_lbl, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.texts)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.texts)
        self.horizontalLayout_2.addWidget(self.circle_bg)
        self.horizontalLayout.addWidget(self.container)
        splash_screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splash_screen)
        QtCore.QMetaObject.connectSlotsByName(splash_screen)

    def retranslateUi(self, splash_screen):
        _translate = QtCore.QCoreApplication.translate
        splash_screen.setWindowTitle(_translate("splash_screen", "Loding"))
        self.title_lbl.setText(_translate("splash_screen", "Study"))
        self.loding_lbl.setText(_translate("splash_screen", "Loding..."))
        self.version_lbl.setText(_translate("splash_screen", "Study"))

