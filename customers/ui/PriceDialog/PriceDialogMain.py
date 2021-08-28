from PyQt5 import QtCore, QtWidgets
from customers.database import *

from customers.ui.PriceDialog.ui_priceDialogUI import Ui_Dialog

class PriceDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, db, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.db = db
        self.setupUi(self)
        self.uiChanges()
        self.handleButtons()

    def closeEvent(self, event):
        """UI close envet handler"""
        reply = QtWidgets.QMessageBox.question(
            self,
            "Closing Window",
            "",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        )
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def uiChanges(self):
        # Centrize the dialog
        r = self.geometry()
        r.moveCenter(QtWidgets.QApplication.desktop().availableGeometry().center()) 
        self.setGeometry(r)
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
    def handleButtons(self):
        self.subscribtion_type_comboBox.currentTextChanged['QString'].connect(self.setCost)

    @QtCore.pyqtSlot(str)
    def setCost(self, type):
        """Get the current selected subscription price and add it to label""" 
        cost = retrieveSubsCost(type, db  = self.db)
        self.subscribtion_cost_lbl.setText(str(cost))

    def accept(self):
        """Accept the data provided through the dialog"""

        # Check if the subscribtion type field is empty
        if(not self.subscribtion_type_comboBox.currentText()):
            self.subscribtion_type_comboBox.setFocus()
            QtWidgets.QToolTip.showText(self.subscribtion_type_comboBox.mapToGlobal(QtCore.QPoint(0,10)),"اختر نوع الاشتراك")
            return
        
        # Check if the subscribtion cost field is empty
        if(not self.subscribtion_cost_txt.text()):
            self.subscribtion_cost_txt.setFocus()
            QtWidgets.QToolTip.showText(self.subscribtion_cost_txt.mapToGlobal(QtCore.QPoint(0,10)),"ادخل قيمة الاشتراك")
            return
        
        self.data = [self.subscribtion_type_comboBox.currentText(), int(self.subscribtion_cost_txt.text())]

        if(not self.data):
            return
        
        super().accept()