# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/nicola/AppData/Local/Temp/progressBarDialogUIFeafbb.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(258, 95)
        Dialog.setMaximumSize(QtCore.QSize(258, 95))
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setStyleSheet("\n"
"QDialog{\n"
"\n"
"background-color: rgb(100, 100, 100);\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"    color: rgb(244, 154, 32);\n"
"    font: 18pt \"Times New Roman\";\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 3px solid  rgb(244, 154, 32);\n"
"    border-radius: 6px;\n"
"    font: 16pt \"Times New Roman\";\n"
"    text-align: center;\n"
"\n"
"    color: rgb(240, 240, 240);\n"
"    background-color:rgb(207,207,207);\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.vboxlayout = QtWidgets.QVBoxLayout(Dialog)
        self.vboxlayout.setContentsMargins(4, 4, 4, 4)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(250, 40))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setMinimumSize(QtCore.QSize(250, 40))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet("")
        self.progressBar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.vboxlayout.addWidget(self.progressBar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Deleting..."))
        self.progressBar.setFormat(_translate("Dialog", "%v"))

