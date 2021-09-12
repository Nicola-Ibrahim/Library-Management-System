from PyQt5 import QtWidgets, QtCore, QtGui

class CustomOfferFrame(QtWidgets.QFrame):


    def __init__(self, item_number, parent):
        super().__init__(parent=parent)

        # Create register order panel 

        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName(f"offer_frame_{item_number}")

        # Add layout to the panel
        horizontalLayout = QtWidgets.QHBoxLayout(self)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(11)
        horizontalLayout.setObjectName("horizontalLayout")

        # Add label to the panel for item number
        self.item_number_lbl = QtWidgets.QLabel(self)
        self.item_number_lbl.setStyleSheet("QLabel{\n"
            "\n"
            "color: rgb(255, 255, 255);\n"
            "}")
        self.item_number_lbl.setObjectName("item_number_lbl")

        _translate = QtCore.QCoreApplication.translate
        self.item_number_lbl.setText(_translate("MainWindow", f"Item : {item_number} "))
        horizontalLayout.addWidget(self.item_number_lbl)

        # Add item comboBox to the layout 
        self.offer_item_comboBox = QtWidgets.QComboBox(self)
        self.offer_item_comboBox.setMinimumSize(QtCore.QSize(90, 40))
        self.offer_item_comboBox.setStyleSheet(
            "QComboBox{\n"
            "border-width:0px 0px 4px 0px;\n"
            "border-style: solid;\n"
            "border-radius:0px;\n"
            "border-color: rgb(255, 170, 0);\n"
            "}"
            )
        self.offer_item_comboBox.setEditable(True)
        self.offer_item_comboBox.setObjectName("offer_item_comboBox")
        self.offer_item_comboBox.setEditable(True)
        # Set validator on item
        # validator = QtGui.QRegularExpressionValidator(QRegularExpression("[a-zA-Zء-ي|\s]+"))
        # self.offer_item_comboBox.setValidator(validator)
        horizontalLayout.addWidget(self.offer_item_comboBox) 

        # Add quantity text to the layout
        self.offer_quantity_txt = QtWidgets.QLineEdit(self)
        self.offer_quantity_txt.setMinimumSize(QtCore.QSize(60, 40))
        self.offer_quantity_txt.setMaximumSize(QtCore.QSize(60, 16777215))
        self.offer_quantity_txt.setStyleSheet(
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
        self.offer_quantity_txt.setObjectName("offer_quantity_txt")
        self.offer_quantity_txt.setEnabled(False)

        # Set validator on quantity
        validator = QtGui.QRegExpValidator(QtCore.QRegExp(r"[0-9]+"))
        self.offer_quantity_txt.setValidator(validator)

        horizontalLayout.addWidget(self.offer_quantity_txt)

        # Add delete current input item button to the layout
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
        

        
