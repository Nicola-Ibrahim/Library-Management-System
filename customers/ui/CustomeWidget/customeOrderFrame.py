from PyQt5 import QtWidgets, QtCore, QtGui

class CustomeOrderFrame(QtWidgets.QFrame):
    def __init__(self, ):
        # Create register order panel 
        order_frame = QtWidgets.QFrame(self.orders_items_frame)
        order_frame.setMinimumSize(QtCore.QSize(0, 16777215))
        order_frame.setMaximumSize(QtCore.QSize(1000, 16777215))
        order_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        order_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        order_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        order_frame.setObjectName(f"order_frame_{self._order_item_number}")

        order_frame_verticalLayout = QtWidgets.QVBoxLayout(order_frame)
        order_frame_verticalLayout.setContentsMargins(0, 0, 0, 0)
        order_frame_verticalLayout.setSpacing(2)
        order_frame_verticalLayout.setObjectName("order_frame_verticalLayout")
        
        # Add label to the panel for item number
        item_number_lbl = QtWidgets.QLabel(order_frame)
        item_number_lbl.setStyleSheet("QLabel{\n"
            "\n"
            "color: rgb(255, 255, 255);\n"
            "}")
        item_number_lbl.setObjectName("item_number_lbl")

        _translate = QtCore.QCoreApplication.translate
        item_number_lbl.setText(_translate("MainWindow", f"Item : {self._order_item_number} "))
        order_frame_verticalLayout.addWidget(item_number_lbl)

        # Add layout to the panel
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setSpacing(7)
        horizontalLayout.setObjectName("horizontalLayout")
        
        

        # Add item comboBox to the layout 
        order_item_comboBox = QtWidgets.QComboBox(order_frame)
        order_item_comboBox.setMinimumSize(QtCore.QSize(90, 40))
        order_item_comboBox.setStyleSheet(
            "QComboBox{\n"
            "border-width:0px 0px 4px 0px;\n"
            "border-style: solid;\n"
            "border-radius:0px;\n"
            "border-color: rgb(255, 170, 0);\n"
            "}"
            )
        order_item_comboBox.setEditable(False)
        order_item_comboBox.setObjectName("order_item_comboBox")
        order_item_comboBox.setEditable(True)
        # Set validator on item
        validator = QtGui.QRegularExpressionValidator(QRegularExpression("[a-zA-Zء-ي|\s]+"))
        order_item_comboBox.setValidator(validator)

        horizontalLayout.addWidget(order_item_comboBox)

        # Add price label to the layout
        order_item_price_lbl = QtWidgets.QLabel(order_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(order_item_price_lbl.sizePolicy().hasHeightForWidth())
        # order_item_price_lbl.setSizePolicy(sizePolicy)
        # order_item_price_lbl.setMinimumSize(QtCore.QSize(0, 40))
        order_item_price_lbl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        order_item_price_lbl.setStyleSheet("color:rgb(244, 154, 32);")
        order_item_price_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        order_item_price_lbl.setText("")
        order_item_price_lbl.setAlignment(Qt.AlignHCenter)
        order_item_price_lbl.setObjectName("order_item_price_lbl")
        horizontalLayout.addWidget(order_item_price_lbl)
        
        # Add quantity text to the layout
        order_quantity_txt = QtWidgets.QLineEdit(order_frame)
        order_quantity_txt.setMinimumSize(QtCore.QSize(60, 40))
        order_quantity_txt.setMaximumSize(QtCore.QSize(60, 16777215))
        order_quantity_txt.setStyleSheet(
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
        order_quantity_txt.setObjectName("order_quantity_txt")
        order_quantity_txt.setEnabled(False)

        # Set validator on quantity
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r"[0-9]+"))
        order_quantity_txt.setValidator(validator)

        horizontalLayout.addWidget(order_quantity_txt)
        

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

        # Add layout to the order panel
        order_frame_verticalLayout.addLayout(horizontalLayout)
        
