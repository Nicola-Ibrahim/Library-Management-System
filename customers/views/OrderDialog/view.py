from customers.views.CustomWidget.customAddOrderFrame import CustomAddOrderFrame
from PyQt5 import QtCore, QtWidgets, sip
from customers.database import *

from customers.views.OrderDialog.ui_orderDialogUI import Ui_Dialog

class OrderDialogView(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, order_id, customer_name, order_type, db, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_type = order_type
        self.db = db
        self._order_item_number = 0

        self.setupUi(self)
        self.uiChanges()
        self.handleButtons()
        self.setOrderDetail()

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
        self.plus_item_btn.clicked.connect(lambda _: self.plusOrder())

    def getOrderDetails(self):
        """Get the entered items which related to specific order""" 
        cost = retrieveOrderItems(self.order_id, db  = self.db)

        self.subscribtion_cost_lbl.setText(str(cost))

    def plusOrder(self, selected_item=None, quantity=None):
        """Adding new order to orders list"""
        self._order_item_number += 1

        order_frame = CustomAddOrderFrame(self._order_item_number, self.order_details_frame)        

        # Add the container frame into parent frame layout
        self.verticalLayout_3.addWidget(order_frame)

        # pass on items comboBox
        order_frame.order_item_comboBox.addItems(['']+retrieveItemNames(name_filter=('',''), db = self.db))


        # Connect each comboBox with its label.
        order_frame.order_item_comboBox.currentTextChanged['QString'].connect(lambda : self.setOrderItemPrice(order_frame.order_item_comboBox, order_frame.order_item_price_lbl, order_frame.order_quantity_txt))
        order_frame.order_item_comboBox.currentTextChanged['QString'].connect(lambda : self.isOrderItemExist(order_frame.order_item_comboBox, order_frame.order_quantity_txt))

        # pass on items comboBox to connect it with its label.
        order_frame.order_quantity_txt.textEdited['QString'].connect(lambda : self.checkOrderItemQauntity(order_frame.order_item_comboBox, order_frame.order_quantity_txt))
        
        if(order_frame.order_item_comboBox and order_frame.order_quantity_txt):
            order_frame.order_item_comboBox.setCurrentText(selected_item)
            order_frame.order_quantity_txt.setText(str(quantity))

        # pass on delete buttons to connect it with its frame.
        order_frame.delete_btn.clicked.connect(lambda : self.deleteOrderFrame(order_frame))

    def isOrderItemExist(self, combo_selected_item, quntity_txt):
        # Check if the item is selected previously 
        combo_selected_items = [item.currentText() for item in self.order_details_frame.findChildren(QtWidgets.QComboBox)]

        if(combo_selected_item.currentText()==''):
            combo_selected_item.setStyleSheet(
            "QComboBox{\n"
            "border-width:0px 0px 4px 0px;\n"
            "border-style: solid;\n"
            "border-radius:0px;\n"
            "border-color: rgb(255, 170, 0);\n"
            "}"
            )
            quntity_txt.setEnabled(False)

        elif(combo_selected_items.count(combo_selected_item.currentText()) > 1):
            QtWidgets.QToolTip.showText(combo_selected_item.mapToGlobal(QtCore.QPoint(0,10)),"Selected previously")
            combo_selected_item.setStyleSheet("border-width:4px 4px 4px 4px;\n"
            "border-style: solid;\n"
            "border-radius:3px;\n"
            "border-color: rgb(255, 0, 0);")

            # Disableediting quantity text 
            quntity_txt.setEnabled(False)
            quntity_txt.setText('')
        
    def setOrderItemPrice(self, combo_selected_item, price_lbl, quntity_txt):
        """Get the item price and add it to label"""

        
        # elif(retrieveItemId(combo_selected_item.currentText(), db = self.db) is None):
        #     QtWidgets.QToolTip.showText(combo_selected_item.mapToGlobal(QtCore.QPoint(0,10)),"غير موجودة")
        #     combo_selected_item.setStyleSheet("border-width:4px 4px 4px 4px;\n"
        #     "border-style: solid;\n"
        #     "border-radius:3px;\n"
        #     "border-color: rgb(255, 0, 0);")

        #     # Disableediting quantity text 
        #     quntity_txt.setEnabled(False)
        #     quntity_txt.setText('')
            
        price = retrieveItemPrice(combo_selected_item.currentText(), self.db)
        price_lbl.setText(str(price)+' L.S')
        combo_selected_item.setStyleSheet(
        "QComboBox{\n"
        "border-width:0px 0px 4px 0px;\n"
        "border-style: solid;\n"
        "border-radius:0px;\n"
        "border-color: rgb(255, 170, 0);\n"
        "}"
        )

        # Allow editing quantity text 
        quntity_txt.setEnabled(True)

    def checkOrderItemQauntity(self, combo_selected_item, quantity_txt):
        if(quantity_txt.text() ==''):
            return

        remain_quantity = retrieveItemAvailabelQuantity(retrieveItemId(combo_selected_item.currentText(), db = self.db), db = self.db)
        # If not enough items exist 
        if(int(quantity_txt.text()) > remain_quantity):
            QtWidgets.QToolTip.showText(quantity_txt.mapToGlobal(QtCore.QPoint(0,10)),f"Exceed {remain_quantity}")
            
            quantity_txt.setStyleSheet("QLineEdit{\n"
            "\n"
            "    border-style: solid;\n"
            "    border-width: 4px 4px 4px 4px;\n"
            "    border-radius: 0px;    \n"
            "    border-color: rgb(255, 0, 0);\n"
            "}\n"
            "")
        else:
            quantity_txt.setStyleSheet("QLineEdit{\n"
            "\n"
            "    border-style: solid;\n"
            "    border-width: 0px 0px 4px 0px;\n"
            "    border-radius: 0px;    \n"
            "    border-color: rgb(255, 170, 0);\n"
            "}\n"
            "")
      
    def deleteOrderFrame(self, frame):
        """Delete frame after clicking"""


        # Keep at least one order that shouldn't be deleted
        if len(self.order_details_frame.findChildren(QtWidgets.QComboBox)) > 1:

            sip.delete(frame) 

            # decrement order number
            self._order_item_number -=1

            # Reset item labels name
            _translate = QtCore.QCoreApplication.translate
            labels = [label for label in self.order_details_frame.findChildren(QtWidgets.QLabel) if(label.objectName() == 'item_number_lbl')]
            for num, label in zip(range(1, self._order_item_number+1),labels): 
                label.setText(_translate("MainWindow", f"Item : {num} "))

    def setOrderDetail(self):
        self.customer_name_txt.setText(self.customer_name)
        self.order_type_txt.setText(self.order_type)
        data = retrieveOrderItems(self.order_id, db = self.db)
        for item_id, quan in data:
            item_name = retrieveItemNames(item_id, db = self.db)[0]
            self.plusOrder(item_name, quan)

    # def accept(self):
    #     """Accept the data provided through the dialog"""

    #     # Check if the subscribtion type field is empty
    #     if(not self.subscribtion_type_comboBox.currentText()):
    #         self.subscribtion_type_comboBox.setFocus()
    #         QtWidgets.QToolTip.showText(self.subscribtion_type_comboBox.mapToGlobal(QtCore.QPoint(0,10)),"اختر نوع الاشتراك")
    #         return
        
    #     # Check if the subscribtion cost field is empty
    #     if(not self.subscribtion_cost_txt.text()):
    #         self.subscribtion_cost_txt.setFocus()
    #         QtWidgets.QToolTip.showText(self.subscribtion_cost_txt.mapToGlobal(QtCore.QPoint(0,10)),"ادخل قيمة الاشتراك")
    #         return
        
    #     self.data = [self.subscribtion_type_comboBox.currentText(), int(self.subscribtion_cost_txt.text())]

    #     if(not self.data):
    #         return
        
    #     super().accept()