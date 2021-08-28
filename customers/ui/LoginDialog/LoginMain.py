from PyQt5 import QtCore, QtGui, QtWidgets
from . Ui_loginDialogUI import Ui_Dialog
from ...database import *

class LoginDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, db, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        self.db = db
        self._supervisor_job_type = None

        
        self.setupUi(self)
        self.uiChanges()
        self.handdleButtons()
        self.regexValidation()
    
    def closeEvent(self, event):
        """UI close envet handler"""
        reply = QtWidgets.QMessageBox.question(
            self,
            "Closing window",
            "Confirm",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()

    def uiChanges(self):
        r = self.geometry()
        r.moveCenter(QtWidgets.QApplication.desktop().availableGeometry().center()) 
        self.setGeometry(r)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # Add shadow to login panel
        # creating a QGraphicsDropShadowEffect object
        shadow = QtWidgets.QGraphicsDropShadowEffect(blurRadius=200,color=QtGui.QColor(255, 255, 255, 255 * 1), xOffset=3, yOffset=3)
        
        # adding shadow to the label
        self.logo_frame.setGraphicsEffect(shadow)

    def regexValidation(self):
        """Apply regular expression to some UI elements"""

        # username and password regular expression
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r"[a-zA-Z|.|@|#|-|_|\d]*"))
        self.account_name_txt.setValidator(validator)
        self.account_pass_txt.setValidator(validator)

    def handdleButtons(self):
        self.enter_btn.clicked.connect(self.Login)
        # self.exit_btn.clicked.connect(self.close)
        # self.login_showPssword_btn.pressed.connect(lambda : self.account_pass_txt.setEchoMode(QtWidgets.QLineEdit.Normal))
        # self.login_showPssword_btn.released.connect(lambda : self.account_pass_txt.setEchoMode(QtWidgets.QLineEdit.Password))
        self.login_showPssword_btn.toggled.connect(self.toggleShowPsswordBtn)

    @QtCore.pyqtSlot(bool)
    def toggleShowPsswordBtn(self, checked):
        if(checked):
            self.account_pass_txt.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.login_showPssword_btn.setStyleSheet("QPushButton{\n"
                                                        "    \n"
                                                        "    image: url(:/icons/icons/visibility.svg);\n"
                                                        "    background-color: rgba(197, 197, 197,30);\n"
                                                        "    border-radius:0px\n"
                                                        "}\n"

                                                        "")
        
        else:
            self.account_pass_txt.setEchoMode(QtWidgets.QLineEdit.Password)
            self.login_showPssword_btn.setStyleSheet("QPushButton{\n"
                                                        "    \n"
                                                        "    image: url(:/icons/icons/invisibility.svg);\n"
                                                        "    background-color: rgba(197, 197, 197,30);\n"
                                                        "    border-radius:0px\n"
                                                        "}\n"

                                                        "")

    def Login(self):
        """handle login process"""

        # if the name text is empty 
        # focus on it
        if(self.account_name_txt.text()==""):
            self.account_name_txt.setFocus()
            QtWidgets.QToolTip.showText(self.account_name_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter name")
            return

        # if the password text is empty 
        # focus on it
        if(self.account_pass_txt.text()==""):
            self.account_pass_txt.setFocus()
            QtWidgets.QToolTip.showText(self.account_pass_txt.mapToGlobal(QtCore.QPoint(0,10)),"Enter password")
            return
            

        ret = checkLoging(self.account_name_txt.text(),self.account_pass_txt.text(), self.db)

        if(ret == True):
            self.username_frame.setStyleSheet("#username_frame {\n"
                                                "background-color: rgba(197, 197, 197,30);\n"
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
            self.password_frame.setStyleSheet("#password_frame {\n"
                                                "background-color: rgba(197, 197, 197,30);\n"
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

            self._supervisor_job_type = retrieveJobType(self.account_name_txt.text(), self.db)
            self.accept()
        
        elif(ret=='username is not true'):
            #    QtWidgets.QToolTip.showText(self.account_name_txt.mapToGlobal(QtCore.QPoint(0,10)),ret)
            self.username_frame.setStyleSheet("#username_frame {\n"
                                                "background-color: rgba(197, 197, 197,30);\n"
                                                "    border-bottom-width: 4px; \n"
                                                "    \n"
                                                "    border-style: solid;\n"
                                                "    border-color: rgb(255, 0, 0);\n"
                                                "    font-size: 25px;\n"
                                                "}\n"
                                                "\n"
                                                "#username_frame:hover{\n"
                                                "    border-color: rgb(255, 0, 0);\n"
                                                "}\n"
                                                "\n"
                                                "#username_frame:focus{\n"
                                                "    border-color: rgb(255, 0, 0);\n"
                                                "}")
            
            self.password_frame.setStyleSheet("#password_frame {\n"
                                                "background-color: rgba(197, 197, 197,30);\n"
                                                "    border-bottom-width: 4px; \n"
                                                "    \n"
                                                "    border-style: solid;\n"
                                                "    border-color: rgb(12, 60, 83);\n"
                                                "    font-size: 25px;\n"
                                                "}\n"
                                                "\n"
                                                "#password_frame:hover{\n"
                                                "border-color: rgba(197, 197, 197,30);\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "#password_frame:focus{\n"
                                                "    border-color: rgba(197, 197, 197,30);\n"
                                                "}")
        
        elif(ret=='password is not true'):
            # QtWidgets.QToolTip.showText(self.account_pass_txt.mapToGlobal(QtCore.QPoint(0,10)),ret)
            self.username_frame.setStyleSheet("#username_frame {\n"
                                                "background-color: rgba(197, 197, 197,30);\n"
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

            self.password_frame.setStyleSheet("#password_frame {\n"
                                                "background-color: rgba(197, 197, 197,30);\n"
                                                "    border-bottom-width: 4px; \n"
                                                "    \n"
                                                "    border-style: solid;\n"
                                                "    border-color: rgb(255, 0, 0);\n"
                                                "    font-size: 25px;\n"
                                                "}\n"
                                                "\n"
                                                "#password_frame:hover{\n"
                                                "border-color: rgb(255, 0, 0);\n"
                                                "\n"
                                                "}\n"
                                                "\n"
                                                "#password_frame:focus{\n"
                                                "    border-color: rgb(255, 0, 0);\n"
                                                "}")

        else:
            return

    def getSupervisorJobType(self):
        return self._supervisor_job_type