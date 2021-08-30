from PyQt5 import QtCore, QtWidgets
from customers.database import *

from customers.ui.OrderDialog.ui_orderDialogUI import Ui_Dialog

class OrderDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, order_id, db, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        self.order_id = order_id
        self.db = db
        self.setupUi(self)
        self.uiChanges()
        self.handleButtons()
        self._order_item_number = 0

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
        self.plus_item_btn.clicked.connect(self.plusOrder)

    def getOrderDetails(self):
        """Get the entered items which related to specific order""" 
        cost = retrieveOrderItems(self.order_id, db  = self.db)

        self.subscribtion_cost_lbl.setText(str(cost))

    def plusOrder(self):
        """Adding new order to orders list"""
        self._order_item_number += 1

        # Create register order panel 
        order_frame = QtWidgets.QFrame(self.order_details_frame)
        order_frame.setMinimumSize(QtCore.QSize(0, 16777215))
        order_frame.setMaximumSize(QtCore.QSize(1000, 16777215))
        order_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        order_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        order_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        order_frame.setObjectName(f"order_frame_{self._order_item_number}")
        
        # Add layout to the panel
        horizontalLayout = QtWidgets.QHBoxLayout(order_frame)
        horizontalLayout.setSpacing(7)
        horizontalLayout.setObjectName("horizontalLayout")

        # Add label to the panel for item number
        item_number_lbl = QtWidgets.QLabel(order_frame)
        item_number_lbl.setStyleSheet("QLabel{\n"
            "\n"
            "color: rgb(255, 255, 255);\n"
            "}")
        item_number_lbl.setObjectName("item_number_lbl")

        _translate = QtCore.QCoreApplication.translate
        item_number_lbl.setText(_translate("MainWindow", f"Item : {self._order_item_number} "))
        horizontalLayout.addWidget(item_number_lbl)
        
        # Add item comboBox to the layout 
        item_comboBox = QtWidgets.QComboBox(order_frame)
        item_comboBox.setMinimumSize(QtCore.QSize(90, 40))
        item_comboBox.setStyleSheet(
            "QComboBox{\n"
            "border-width:0px 0px 4px 0px;\n"
            "border-style: solid;\n"
            "border-radius:0px;\n"
            "border-color: rgb(255, 170, 0);\n"
            "}"
            )
        item_comboBox.setObjectName("item_comboBox")
        item_comboBox.setEditable(True)
        horizontalLayout.addWidget(item_comboBox)

        # Add price label to the layout
        item_price_lbl = QtWidgets.QLabel(order_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(item_price_lbl.sizePolicy().hasHeightForWidth())
        item_price_lbl.setSizePolicy(sizePolicy)
        item_price_lbl.setMinimumSize(QtCore.QSize(0, 40))
        item_price_lbl.setMaximumSize(QtCore.QSize(10000, 16777215))
        item_price_lbl.setStyleSheet("color:rgb(244, 154, 32);")
        item_price_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        item_price_lbl.setText("")
        item_price_lbl.setAlignment(QtCore.Qt.AlignHCenter)
        item_price_lbl.setObjectName("item_price_lbl")
        horizontalLayout.addWidget(item_price_lbl)
        
        # Add quantity text to the layout
        item_quantity = QtWidgets.QLineEdit(order_frame)
        item_quantity.setMinimumSize(QtCore.QSize(60, 40))
        item_quantity.setMaximumSize(QtCore.QSize(60, 16777215))
        item_quantity.setStyleSheet(
            "QLineEdit{\n"
            "    border-style: solid;\n"
            "    border-width: 0px 0px 4px 0px;\n"
            "    border-radius: 0px;    \n"
            "    border-color:  rgb(244, 154, 32);\n"
            "}\n"
            "QLineEdit:disabled{\n"
            "    border-style: solid;\n"
            "    border-width: 0px 0px 4px 0px;\n"
            "    border-radius: 0px;\n"
            "    border-color:  rgb(244, 154, 32);\n"
            "    background-color: rgb(142,142,142);\n"
            "}"
           

            "")
        item_quantity.setObjectName("item_quantity")
        item_quantity.setEnabled(False)

        # Set validator on quantity
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r"[0-9]+"))
        item_quantity.setValidator(validator)

        horizontalLayout.addWidget(item_quantity)
        

        # Add delete current input order button to the layout
        delete_btn = QtWidgets.QPushButton(order_frame)
        delete_btn.setMinimumSize(QtCore.QSize(50, 50))
        delete_btn.setMaximumSize(QtCore.QSize(50, 50))
        delete_btn.setStyleSheet(
            "QPushButton{\n"
            "\n"
            "    border-style: solid;\n"
            "    border-width: 4px 4px 4px 4px;\n"
            "    border-radius: 25px;    \n"
            "    border-color: rgb(174, 174, 174);\n"
            "    background-color: rgb(255, 255, 255);\n"
            "    image: url(:/icons/icons/letter-x2.svg);\n"
            "    padding:9px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    image: url(:/icons/icons/letter-x1.svg);\n"

           
            "}\n"
            "QPushButton:pressed{\n"
            "    padding:14px;\n"
            "}\n"
            "")

        
        horizontalLayout.addWidget(delete_btn)        

        # Add the container frame into parent frame layout
        self.verticalLayout_3.addWidget(order_frame)

        
        # # pass on items comboBox
        
        # item_comboBox.addItems(['']+retrieveItemNames(name_filter=('',''), db = self.daily_conn))

        # # self.changeComboItems(item_comboBox)
        # # item_comboBox.currentTextChanged['QString'].connect(lambda : self.changeComboItems2(item_comboBox))

        # # Connect each comboBox with its label.
        # item_comboBox.currentTextChanged['QString'].connect(lambda : self.setOrderItemPrice(item_comboBox, item_price_lbl, item_quantity))
        # item_comboBox.currentTextChanged['QString'].connect(lambda : self.isOrderItemExist(item_comboBox, item_quantity))
       
        # # pass on items comboBox to connect it with its label.
        # item_quantity.textEdited['QString'].connect(lambda : self.checkOrderItemQauntity(item_comboBox, item_quantity))
        
        
        # # pass on delete buttons to connect it with its frame.
        # delete_btn.clicked.connect(lambda : self.deleteOrderFrame(order_frame))

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