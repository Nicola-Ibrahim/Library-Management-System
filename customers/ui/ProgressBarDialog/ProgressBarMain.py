from PyQt5 import QtCore, QtWidgets
from customers.ui.ProgressBarDialog.ui_progressBarDialogUI import Ui_Dialog

class PorgressBarDialog(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        self.uiChanges()

    def uiChanges(self):
        # Centrize the dialog
        r = self.geometry()
        r.moveCenter(QtWidgets.QApplication.desktop().availableGeometry().center()) 
        self.setGeometry(r)
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    @QtCore.pyqtSlot('int')
    def changeValue(self, num):
        self.progressBar.setValue(num)

  
