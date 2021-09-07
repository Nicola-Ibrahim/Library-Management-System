from PyQt5 import QtWidgets, QtCore, QtGui

class CustomeOrderFrame(QtWidgets.QFrame):


    def __init__(self, order_item_number, parent):
        super().__init__(parent=parent)

        # Create register order panel 
        self.setMinimumSize(QtCore.QSize(0, 16777215))
        self.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setObjectName(f"order_frame_{order_item_number}")

        self.order_frame_verticalLayout = QtWidgets.QVBoxLayout(self)
        self.order_frame_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.order_frame_verticalLayout.setSpacing(2)
        self.order_frame_verticalLayout.setObjectName("order_frame_verticalLayout")
        
        # Add label to the panel for item number
        item_number_lbl = QtWidgets.QLabel(self)
        item_number_lbl.setStyleSheet("QLabel{\n"
            "\n"
            "color: rgb(255, 255, 255);\n"
            "}")
        item_number_lbl.setObjectName("item_number_lbl")

        _translate = QtCore.QCoreApplication.translate
        item_number_lbl.setText(_translate("MainWindow", f"Item : {order_item_number} "))
        self.order_frame_verticalLayout.addWidget(item_number_lbl)

        # Add layout to the panel
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setSpacing(7)
        horizontalLayout.setObjectName("horizontalLayout")
        
        

        # Add item comboBox to the layout 
        self.order_item_comboBox = QtWidgets.QComboBox(self)
        self.order_item_comboBox.setMinimumSize(QtCore.QSize(90, 40))
        self.order_item_comboBox.setStyleSheet(
            "QComboBox{\n"
            "border-width:0px 0px 4px 0px;\n"
            "border-style: solid;\n"
            "border-radius:0px;\n"
            "border-color: rgb(255, 170, 0);\n"
            "}"
            )
        self.order_item_comboBox.setEditable(False)
        self.order_item_comboBox.setObjectName("order_item_comboBox")
        self.order_item_comboBox.setEditable(True)
        # Set validator on item
        validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[a-zA-Zء-ي|\s]+"))
        self.order_item_comboBox.setValidator(validator)

        horizontalLayout.addWidget(self.order_item_comboBox)

        # Add price label to the layout
        self.order_item_price_lbl = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.order_item_price_lbl.sizePolicy().hasHeightForWidth())
        # self.order_item_price_lbl.setSizePolicy(sizePolicy)
        # self.order_item_price_lbl.setMinimumSize(QtCore.QSize(0, 40))
        self.order_item_price_lbl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.order_item_price_lbl.setStyleSheet("color:rgb(244, 154, 32);")
        self.order_item_price_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.order_item_price_lbl.setText("")
        self.order_item_price_lbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.order_item_price_lbl.setObjectName("order_item_price_lbl")
        horizontalLayout.addWidget(self.order_item_price_lbl)
        
        # Add quantity text to the layout
        self.order_quantity_txt = QtWidgets.QLineEdit(self)
        self.order_quantity_txt.setMinimumSize(QtCore.QSize(60, 40))
        self.order_quantity_txt.setMaximumSize(QtCore.QSize(60, 16777215))
        self.order_quantity_txt.setStyleSheet(
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
        self.order_quantity_txt.setObjectName("order_quantity_txt")
        self.order_quantity_txt.setEnabled(False)

        # Set validator on quantity
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r"[0-9]+"))
        self.order_quantity_txt.setValidator(validator)

        horizontalLayout.addWidget(self.order_quantity_txt)
        

        # Add delete current input order button to the layout
        self.delete_btn = QtWidgets.QPushButton(self)
        self.delete_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.delete_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.delete_btn.setStyleSheet(
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

        horizontalLayout.addWidget(self.delete_btn)

        # Add layout to the order panel
        self.order_frame_verticalLayout.addLayout(horizontalLayout)

        
