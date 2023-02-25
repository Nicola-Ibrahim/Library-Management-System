# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/nicola/AppData/Local/Temp/loginDialogUINyOycA.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 620)
        Dialog.setMinimumSize(QtCore.QSize(450, 620))
        Dialog.setMaximumSize(QtCore.QSize(493, 620))
        Dialog.setStyleSheet("QMessageBox {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    \n"
"    background-color: rgb(47, 113, 255);\n"
"}")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("#frame{\n"
"\n"
"    border: 2px solid transparent;\n"
"    border-radius: 20px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.107955 rgba(0, 31, 98, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: transparent;\n"
"    border-style: solid;\n"
"    font-size: 25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    background-color: transparent;\n"
"    font-size: 30px;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    background-color: transparent;\n"
"    font-size: 30px;\n"
"    selection-background-color: darkgray;\n"
"}\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(12, 60, 83);\n"
"    font-size: 25px;\n"
"    padding-bottom: 10px;\n"
"}\n"
"\n"
"\n"
"QMessageBox {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    \n"
"    background-color: rgb(47, 113, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.navigation_frame = QtWidgets.QFrame(self.frame)
        self.navigation_frame.setMinimumSize(QtCore.QSize(0, 40))
        self.navigation_frame.setStyleSheet("#navigation_frame{\n"
"    background-color: transparent;\n"
"    border-top-left-radius: 17px;\n"
"    border-top-right-radius: 17px;\n"
"\n"
"}\n"
"#navigation_frame:hover{\n"
"    background-color: rgb(245, 154, 34);\n"
"\n"
"}")
        self.navigation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navigation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navigation_frame.setObjectName("navigation_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.navigation_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 4, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.header_frame = QtWidgets.QFrame(self.navigation_frame)
        self.header_frame.setMinimumSize(QtCore.QSize(450, 0))
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addWidget(self.header_frame)
        self.exit_btn = QtWidgets.QPushButton(self.navigation_frame)
        self.exit_btn.setMinimumSize(QtCore.QSize(35, 35))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"    border-radius:5px;\n"
"    padding:2px;\n"
"    image: url(:/icons/icons/close.png);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed{\n"
"        padding:4px;\n"
"}\n"
"\n"
"\n"
"")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_2.addWidget(self.exit_btn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.navigation_frame)
        self.logo_frame = QtWidgets.QFrame(self.frame)
        self.logo_frame.setMinimumSize(QtCore.QSize(250, 250))
        self.logo_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logo_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logo_frame.setStyleSheet("\n"
"QFrame{\n"
"    image: url(:/icons/icons/user1.png);\n"
"    padding:25px;\n"
"    border: 4px solid;\n"
"    border-radius: 120px;\n"
"    border-color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame:hover{\n"
"    image: url(:/icons/icons/user2.png);\n"
"    border-color:rgb(245, 154, 34);\n"
"}\n"
"")
        self.logo_frame.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.logo_frame)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_2.addWidget(self.logo_frame, 0, QtCore.Qt.AlignHCenter)
        self.login_frame = QtWidgets.QFrame(self.frame)
        self.login_frame.setMinimumSize(QtCore.QSize(400, 0))
        self.login_frame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.login_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_frame.setStyleSheet("")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setObjectName("login_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.login_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 22)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_frame = QtWidgets.QFrame(self.login_frame)
        self.username_frame.setStyleSheet("#username_frame {\n"
"    background-color: none;\n"
"    border-bottom-width: 4px; \n"
"    \n"
"    border-style: solid;\n"
"    border-color: rgb(12, 60, 83);\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"#username_frame:hover{\n"
"    border-color: rgb(244, 154, 32);\n"
"}\n"
"\n"
"#username_frame:focus{\n"
"    border-color: rgb(244, 154, 32);\n"
"}")
        self.username_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.username_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.username_frame.setObjectName("username_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.username_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 11)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.username_frame)
        self.label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label.setStyleSheet("QLabel{\n"
"\n"
"image: url(:/icons/icons/user.svg);\n"
"background-color: rgba(197, 197, 197,0);\n"
" \n"
"    padding:1px;\n"
"    padding-right: 2px;\n"
"\n"
"    \n"
"}\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.account_name_txt = QtWidgets.QLineEdit(self.username_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_name_txt.sizePolicy().hasHeightForWidth())
        self.account_name_txt.setSizePolicy(sizePolicy)
        self.account_name_txt.setMinimumSize(QtCore.QSize(150, 40))
        self.account_name_txt.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.account_name_txt.setCursorPosition(0)
        self.account_name_txt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.account_name_txt.setReadOnly(False)
        self.account_name_txt.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.account_name_txt.setObjectName("account_name_txt")
        self.horizontalLayout_4.addWidget(self.account_name_txt)
        self.verticalLayout.addWidget(self.username_frame)
        self.password_frame = QtWidgets.QFrame(self.login_frame)
        self.password_frame.setStyleSheet("#password_frame {\n"
"    background-color:  none;\n"
"    border-bottom-width: 4px; \n"
"    \n"
"    border-style: solid;\n"
"    border-color: rgb(12, 60, 83);\n"
"    font-size: 25px;\n"
"}\n"
"\n"
"#password_frame:hover{\n"
"    border-color: rgb(244, 154, 32);\n"
"\n"
"}\n"
"\n"
"#password_frame:focus{\n"
"    border-color: rgb(244, 154, 32);\n"
"}")
        self.password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.password_frame.setObjectName("password_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.password_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.password_frame)
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"image: url(:/icons/icons/padlock.svg);\n"
"background-color: rgba(197, 197, 197,0);\n"
" \n"
"    padding:1px;\n"
"    padding-right: 2px;\n"
"\n"
"}\n"
"")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.account_pass_txt = QtWidgets.QLineEdit(self.password_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_pass_txt.sizePolicy().hasHeightForWidth())
        self.account_pass_txt.setSizePolicy(sizePolicy)
        self.account_pass_txt.setMinimumSize(QtCore.QSize(150, 40))
        self.account_pass_txt.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.account_pass_txt.setText("")
        self.account_pass_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.account_pass_txt.setCursorPosition(0)
        self.account_pass_txt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.account_pass_txt.setReadOnly(False)
        self.account_pass_txt.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.account_pass_txt.setObjectName("account_pass_txt")
        self.horizontalLayout.addWidget(self.account_pass_txt)
        self.login_showPssword_btn = QtWidgets.QPushButton(self.password_frame)
        self.login_showPssword_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.login_showPssword_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.login_showPssword_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    image: url(:/icons/icons/invisibility.svg);\n"
"    background-color: transparent;\n"
"    border:0px;\n"
"}\n"
"")
        self.login_showPssword_btn.setText("")
        self.login_showPssword_btn.setIconSize(QtCore.QSize(40, 40))
        self.login_showPssword_btn.setCheckable(True)
        self.login_showPssword_btn.setObjectName("login_showPssword_btn")
        self.horizontalLayout.addWidget(self.login_showPssword_btn)
        self.verticalLayout.addWidget(self.password_frame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.enter_btn = QtWidgets.QPushButton(self.login_frame)
        self.enter_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.enter_btn.setStyleSheet("QPushButton{\n"
"    font-size: 25px;\n"
"    border-radius: 25px;\n"
"    padding: 2px;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(12, 60, 83);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    border-radius: 25px;\n"
"    padding: 2px;\n"
"    background-color: rgb(150,150,150);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-radius: 25px;\n"
"    padding: 2px;\n"
"    background-color: rgb(174,174,174);\n"
"}\n"
"")
        self.enter_btn.setObjectName("enter_btn")
        self.verticalLayout.addWidget(self.enter_btn)
        self.verticalLayout_2.addWidget(self.login_frame, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.account_name_txt.setPlaceholderText(_translate("Dialog", "username"))
        self.account_pass_txt.setPlaceholderText(_translate("Dialog", "password"))
        self.enter_btn.setText(_translate("Dialog", "login"))
        self.enter_btn.setShortcut(_translate("Dialog", "Return"))

from .. import icon_rc
