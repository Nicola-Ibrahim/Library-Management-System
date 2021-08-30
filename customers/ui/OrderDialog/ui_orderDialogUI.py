# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/nicola/AppData/Local/Temp/orderDialogUIoZYeMR.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 531)
        Dialog.setStyleSheet("\n"
"/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"\n"
"\n"
"QDialog{    \n"
"    background-color:  rgb(174,174,174);\n"
"    border-style: solid;\n"
"    border-color: red;\n"
"    border-width: 20x;\n"
"    background-color: rgb(100, 100, 100);\n"
"}\n"
"QComboBox{\n"
"    \n"
"    font-size:25px;\n"
"}\n"
"QDialogButtonBox { dialogbuttonbox-buttons-have-icons: 1; }\n"
"\n"
"QPushButton{\n"
"    font-size: 25px;\n"
"\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"    color: rgb(255,255,255);\n"
"    \n"
"    background-color: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-style:  solid;\n"
"    \n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(150,150,150);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style:  solid;\n"
"    \n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(174,174,174);\n"
"}\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-width: 5px; \n"
"    border-radius: 10px;\n"
"    border-style: solid;\n"
"    border-color: rgb(12, 60, 83);\n"
"    font-size: 25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-width: 5px; \n"
"    border-radius: 10px;\n"
"    border-style: solid;\n"
"    border-color: rgb(244, 154, 32);\n"
"    font-size: 30px;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(255,255,255);\n"
"    font-size: 25px;\n"
"    padding-bottom: 10px;\n"
"}\n"
"\n"
"QScrollArea { \n"
"    background: transparent; \n"
"    border:none;\n"
"}\n"
"QScrollArea > QWidget > QWidget { \n"
"    background: transparent; \n"
"}\n"
"QScrollArea > QWidget > QScrollBar { \n"
"    background: palette(base); \n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    max-width: 30px;\n"
"    border: 1px transparent black;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(150,150,150);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    max-width: 30px;\n"
"    border: 1px transparent black;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(150,150,150);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   background: rgb(150,150,150);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   background: rgb(150,150,150);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 8px;\n"
"   height: 8px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 8px;\n"
"   height: 8px;\n"
"   background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(250, 40))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.customer_name_txt = QtWidgets.QLabel(self.frame)
        self.customer_name_txt.setObjectName("customer_name_txt")
        self.horizontalLayout.addWidget(self.customer_name_txt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(250, 40))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.order_type_txt = QtWidgets.QLabel(self.frame)
        self.order_type_txt.setObjectName("order_type_txt")
        self.horizontalLayout_2.addWidget(self.order_type_txt)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 5px;;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding:5px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding:10px;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 519, 307))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.order_details_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.order_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.order_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.order_details_frame.setObjectName("order_details_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.order_details_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.order_details_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.order_details_frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Customer name"))
        self.customer_name_txt.setText(_translate("Dialog", "sdfsd"))
        self.label_3.setText(_translate("Dialog", "Order Type"))
        self.order_type_txt.setText(_translate("Dialog", "sdfsdf"))
        self.label_5.setText(_translate("Dialog", "Adding new item"))
        self.label_2.setText(_translate("Dialog", "Item"))
        self.pushButton.setText(_translate("Dialog", "delete"))

import icon_rc
