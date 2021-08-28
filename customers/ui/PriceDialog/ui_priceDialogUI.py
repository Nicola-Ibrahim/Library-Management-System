# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/nicola/AppData/Local/Temp/priceDialogUIsonuIG.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(650, 200)
        Dialog.setMinimumSize(QtCore.QSize(650, 200))
        Dialog.setMaximumSize(QtCore.QSize(650, 200))
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
"")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(11, 11, 1, 11)
        self.gridLayout.setSpacing(11)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setMinimumSize(QtCore.QSize(250, 0))
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_28.addWidget(self.label_28, 0, QtCore.Qt.AlignLeft)
        self.subscribtion_type_comboBox = QtWidgets.QComboBox(self.frame)
        self.subscribtion_type_comboBox.setMinimumSize(QtCore.QSize(260, 40))
        self.subscribtion_type_comboBox.setMaximumSize(QtCore.QSize(260, 16777215))
        self.subscribtion_type_comboBox.setObjectName("subscribtion_type_comboBox")
        self.subscribtion_type_comboBox.addItem("")
        self.subscribtion_type_comboBox.setItemText(0, "")
        self.subscribtion_type_comboBox.addItem("")
        self.subscribtion_type_comboBox.addItem("")
        self.subscribtion_type_comboBox.addItem("")
        self.horizontalLayout_28.addWidget(self.subscribtion_type_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setMinimumSize(QtCore.QSize(200, 0))
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_29.addWidget(self.label_29)
        self.subscribtion_cost_lbl = QtWidgets.QLabel(self.frame)
        self.subscribtion_cost_lbl.setMinimumSize(QtCore.QSize(260, 40))
        self.subscribtion_cost_lbl.setMaximumSize(QtCore.QSize(260, 16777215))
        self.subscribtion_cost_lbl.setText("")
        self.subscribtion_cost_lbl.setObjectName("subscribtion_cost_lbl")
        self.horizontalLayout_29.addWidget(self.subscribtion_cost_lbl)
        self.verticalLayout.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_31 = QtWidgets.QLabel(self.frame)
        self.label_31.setMinimumSize(QtCore.QSize(250, 0))
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_30.addWidget(self.label_31)
        self.subscribtion_cost_txt = QtWidgets.QLineEdit(self.frame)
        self.subscribtion_cost_txt.setMinimumSize(QtCore.QSize(0, 50))
        self.subscribtion_cost_txt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.subscribtion_cost_txt.setObjectName("subscribtion_cost_txt")
        self.horizontalLayout_30.addWidget(self.subscribtion_cost_txt)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_30.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_30)
        self.horizontalLayout.addWidget(self.frame)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_28.setText(_translate("Dialog", "Subscription Type"))
        self.subscribtion_type_comboBox.setItemText(1, _translate("Dialog", "Daily fee"))
        self.subscribtion_type_comboBox.setItemText(2, _translate("Dialog", "University fee"))
        self.subscribtion_type_comboBox.setItemText(3, _translate("Dialog", "School fee"))
        self.label_29.setText(_translate("Dialog", "Current Fee Value"))
        self.label_31.setText(_translate("Dialog", "New Fee Value"))

