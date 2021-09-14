# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/nicola/AppData/Local/Temp/mainUIufDQHW.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1480, 1127)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"QMainWindow {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.107955 rgba(0, 31, 98, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QMessageBox {\n"
"    background-color: rgb(100, 100, 100);\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QLabel {\n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"    color: rgb(255,255,255);\n"
"    \n"
"    background-color: rgb(47, 113, 255);\n"
"}\n"
"\n"
"QTableView{\n"
"    \n"
"    alternate-background-color : rgb(220, 220, 220); \n"
"    selection-background-color :     rgb(174, 174, 174);     \n"
"\n"
"\n"
"    gridline-color: rgb(0, 31, 98);\n"
"\n"
"    font: 16pt \"Arial\";\n"
"    \n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius:4px;\n"
"\n"
"    border-color: rgb(244, 154, 32);\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(0, 31, 98) ;\n"
"    color: white;\n"
"    padding-left: 0px;\n"
"    border: 4px solid #6c6c6c;\n"
"    font: 75 18pt \"Arial\";\n"
"\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"    border-radius:4px;\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: rgb(255, 170, 0);\n"
"    border-radius:4px;\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #fffff8;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"    border-radius:4px;\n"
"}\n"
"\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"    background:  rgb(244, 154, 32);\n"
"    border: 2px outset red;\n"
"    image:url(:/icons/icons/checkmark.svg)\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QTreeView {\n"
"    show-decoration-selected:1;\n"
"    \n"
"    font: 16pt \"Times New Roman\";\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-radius:4px;\n"
"\n"
"    border-color: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QTreeView::item {\n"
"     border: 1px solid #d9d9d9;\n"
"    border-top-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);\n"
"    border: 1px solid #bfcde4;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    border: 1px solid #567dbc;\n"
"}\n"
"\n"
"QTreeView::item:selected:active{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);\n"
"}\n"
"\n"
"QTreeView::item:selected:!active {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);\n"
"}\n"
"\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"    border-image:url(:/icons/icons/vline.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/icons/icons/branch-more.png)  0;\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/icons/icons/branch-end.png) 0;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"        border-image: none;\n"
"        image:url(:/icons/icons/branch-closed.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings  {\n"
"        border-image: none;\n"
"        image: url(:/icons/icons/branch-open.png);\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox{\n"
"    \n"
"    font-size:25px;\n"
"}\n"
"\n"
"QGroupBox{\n"
"    font-size: 14px;\n"
"    font-family: Arial, Helvetica, sans-serif;\n"
"    font-weight: bold;\n"
"    color: rgb(95, 95, 95);\n"
"    border: 1px solid gray;\n"
"      padding:  1em 1em;\n"
"      border-radius: 16px;\n"
" }\n"
"\n"
"QTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(0,0,0);\n"
"    padding: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-width: 4px; \n"
"    border-radius: 8px;\n"
"    border-style: solid;\n"
"    border-color: rgb(150,150,150);\n"
"    font-size: 25px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border-color: rgb(244, 154, 32);\n"
"    selection-background-color: darkgray;\n"
"}\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 25px;\n"
"\n"
"}\n"
"QSpinBox {\n"
"    padding-right: 10px; /* make room for the arrows */\n"
"    border-width: 6;\n"
"}\n"
"QSpinBox::up-arrow {\n"
"    width: 7px;\n"
"    height: 7px;\n"
"}\n"
"\n"
"QToolTip {\n"
"    font: 12pt \"Times New Roman\";\n"
"    border: 2px solid rgb(174,174,174);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QRadioButton {\n"
"    color: rgb(147, 147, 147);\n"
"    padding: 1px;\n"
"    font-size:25px;\n"
"\n"
"}\n"
"QRadioButton:checked{\n"
"        color: rgb(244, 154, 32);\n"
"\n"
"}\n"
"QRadioButton::indicator {\n"
"    height: 10px;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"    \n"
"    border: 3px solid;\n"
"    border-radius:15px;\n"
"    border-color: rgb(147, 147, 147);\n"
"    padding: 8px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover {\n"
"    \n"
"    border-color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked:pressed {\n"
"\n"
"    border-color:  rgb(244, 154, 32);\n"
"    background-color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    \n"
"    border: 3px solid;\n"
"    border-radius:15px;\n"
"    border-color: rgb(147, 147, 147);\n"
"    padding: 8px;\n"
"    \n"
"    border-color:  rgb(244, 154, 32);\n"
"    background-color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
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
"\n"
"QPushButton:disabled{\n"
"    border-style:  solid;\n"
"    border-color: rgb(174, 174, 174);\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    padding: 10px;\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"\n"
"QDateEdit\n"
"{\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QDateEdit::drop-down {\n"
"    width:30px;\n"
"    subcontrol-position: right top;\n"
"    subcontrol-origin:margin;\n"
"    background-color: rgb(244, 154, 32);\n"
"    image:url(:/icons/icons/branch-open.png);\n"
"\n"
"}\n"
"\n"
"QLCDNumber {\n"
"    color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(240, 240, 240);\n"
"    border-width: 1px; \n"
"    border-radius: 10px;\n"
"    border-color: rgb(230, 230, 230);\n"
"    border-style: solid;\n"
"    background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"    border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"    color: #000000;\n"
"      spacing: 3px;\n"
"      padding: 1px 4px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"      background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"    border-bottom-color: transparent;\n"
"    border-left-width: 2px;\n"
"    color: #000000;\n"
"    padding-left:15px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"    border-style: solid;\n"
"    border-top-color: transparent;\n"
"    border-right-color: transparent;\n"
"    border-left-color: transparent;\n"
"    border-bottom-color: transparent;\n"
"    border-bottom-width: 1px;\n"
"    color: #000000;\n"
"    padding-left:17px;\n"
"    padding-top:4px;\n"
"    padding-bottom:4px;\n"
"    padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"    color:rgb(0,0,0);\n"
"    \n"
"    background-color: rgb(224, 224, 224);\n"
"    \n"
"    \n"
"}\n"
"QTabWidget::pane {\n"
"        border-color: rgb(223,223,223);\n"
"        background-color:rgb(226,226,226);\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"    border-style: solid;\n"
"    border-left-width:1px;\n"
"    border-right-width:0px;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"    border-style: solid;\n"
"    border-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"    border-style: solid;\n"
"    border-top-width:1px;\n"
"    border-bottom-width:1px;\n"
"    border-left-width:1px;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #000000;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"      border-style: solid;\n"
"      border-left-width:1px;\n"
"      border-bottom-width:1px;\n"
"      border-top-width:1px;\n"
"    border-right-color: transparent;\n"
"    border-top-color: rgb(209,209,209);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"    border-bottom-color: rgb(229,229,229);\n"
"    color: #FFFFFF;\n"
"    padding: 3px;\n"
"    margin-left:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"\n"
"QStatusBar {\n"
"    color:#027f7f;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QToolBox {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"    color: #a9b7c6;\n"
"    background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"    color: #FFFFFF;\n"
"    background-color:#000000;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    width: 12px;\n"
"    margin: -5px 0;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background: rgb(253,253,253);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    height: 12px;\n"
"    margin: 0 -5px;\n"
"    border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollArea { \n"
"    background: transparent; \n"
"    border:none;\n"
"}\n"
"QScrollArea > QWidget > QWidget { \n"
"    background: transparent; \n"
"}\n"
"QScrollArea > QWidget > QScrollBar { \n"
"    background: palette(base); \n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    max-width: 30px;\n"
"    border: 1px transparent black;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    max-width: 30px;\n"
"    border: 1px transparent black;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(150,150,150);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(150,150,150);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(207,207,207);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 2px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   background: rgb(150,150,150);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"      border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   background: rgb(150,150,150);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 2px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   background: rgb(150,150,150);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   background: rgb(150,150,150);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   background: rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 8px;\n"
"   height: 8px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 8px;\n"
"   height: 8px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 8px;\n"
"   height: 8px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 8px;\n"
"   height: 8px;\n"
"   background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setAnimated(True)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_buttons_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_buttons_frame.sizePolicy().hasHeightForWidth())
        self.main_buttons_frame.setSizePolicy(sizePolicy)
        self.main_buttons_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.main_buttons_frame.setMaximumSize(QtCore.QSize(0, 16777215))
        self.main_buttons_frame.setMouseTracking(True)
        self.main_buttons_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_buttons_frame.setStyleSheet("")
        self.main_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_buttons_frame.setObjectName("main_buttons_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_buttons_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_btn = QtWidgets.QPushButton(self.main_buttons_frame)
        self.menu_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.menu_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    padding: 4px;\n"
"    background-color: transparent;\n"
"    image: url(:/icons/icons/menu1.svg);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    image: url(:/icons/icons/menu2.svg);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    image: url(:/icons/icons/menu2.svg);\n"
"}\n"
"\n"
"")
        self.menu_btn.setText("")
        self.menu_btn.setObjectName("menu_btn")
        self.verticalLayout_2.addWidget(self.menu_btn)
        self.buttons_stackedWidget = QtWidgets.QStackedWidget(self.main_buttons_frame)
        self.buttons_stackedWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.buttons_stackedWidget.setStyleSheet("#buttons_stackedWidget{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-style: solid;\n"
"border-width: 5px px 0px 0px;\n"
"border-radius: 0px;\n"
"border-color: rgb(244, 154, 32);\n"
"\n"
"}")
        self.buttons_stackedWidget.setObjectName("buttons_stackedWidget")
        self.dailyAndarchive_buttons_tab = QtWidgets.QWidget()
        self.dailyAndarchive_buttons_tab.setObjectName("dailyAndarchive_buttons_tab")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.dailyAndarchive_buttons_tab)
        self.verticalLayout_17.setContentsMargins(0, 11, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_4 = QtWidgets.QFrame(self.dailyAndarchive_buttons_tab)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.daily_customers_btn = QtWidgets.QPushButton(self.frame_4)
        self.daily_customers_btn.setEnabled(True)
        self.daily_customers_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.daily_customers_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/customer1.png);\n"
"    background-repeat:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/customer2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/customer2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/customer2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.daily_customers_btn.setObjectName("daily_customers_btn")
        self.verticalLayout_6.addWidget(self.daily_customers_btn)
        self.monthly_subscrib_btn = QtWidgets.QPushButton(self.frame_4)
        self.monthly_subscrib_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.monthly_subscrib_btn.setStyleSheet("QPushButton{\n"
"\n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/monthly1.png);\n"
"    background-repeat:none;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/monthly2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/monthly2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/monthly2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.monthly_subscrib_btn.setObjectName("monthly_subscrib_btn")
        self.verticalLayout_6.addWidget(self.monthly_subscrib_btn)
        self.orders_btn = QtWidgets.QPushButton(self.frame_4)
        self.orders_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.orders_btn.setStyleSheet("QPushButton{\n"
"\n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/order1.png);\n"
"    background-repeat:none;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/order2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/order2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/order2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.orders_btn.setObjectName("orders_btn")
        self.verticalLayout_6.addWidget(self.orders_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.verticalLayout_17.addWidget(self.frame_4)
        self.buttons_stackedWidget.addWidget(self.dailyAndarchive_buttons_tab)
        self.settings_buttons_tab = QtWidgets.QWidget()
        self.settings_buttons_tab.setObjectName("settings_buttons_tab")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.settings_buttons_tab)
        self.verticalLayout_23.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_18 = QtWidgets.QFrame(self.settings_buttons_tab)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.warehouse_btn = QtWidgets.QPushButton(self.frame_18)
        self.warehouse_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.warehouse_btn.setStyleSheet("QPushButton{\n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/warehouse1.png);\n"
"    background-repeat:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/warehouse2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/warehouse2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/warehouse2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.warehouse_btn.setObjectName("warehouse_btn")
        self.verticalLayout_26.addWidget(self.warehouse_btn)
        self.reports_btn = QtWidgets.QPushButton(self.frame_18)
        self.reports_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.reports_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/report1.png);\n"
"    background-repeat:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/report2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/report2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/report2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.reports_btn.setObjectName("reports_btn")
        self.verticalLayout_26.addWidget(self.reports_btn)
        self.offers_btn = QtWidgets.QPushButton(self.frame_18)
        self.offers_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.offers_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/offers1.png);\n"
"    background-repeat:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/offers2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/offers2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/offers2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.offers_btn.setObjectName("offers_btn")
        self.verticalLayout_26.addWidget(self.offers_btn)
        self.employees_btn = QtWidgets.QPushButton(self.frame_18)
        self.employees_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.employees_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/employee1.png);\n"
"    background-repeat:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/employee2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/employee2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/employee2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.employees_btn.setObjectName("employees_btn")
        self.verticalLayout_26.addWidget(self.employees_btn)
        self.shifts_btn = QtWidgets.QPushButton(self.frame_18)
        self.shifts_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.shifts_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/shifts1.png);\n"
"    background-repeat:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/shifts2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/shifts2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/shifts2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.shifts_btn.setObjectName("shifts_btn")
        self.verticalLayout_26.addWidget(self.shifts_btn)
        self.copy_delete_btn = QtWidgets.QPushButton(self.frame_18)
        self.copy_delete_btn.setMinimumSize(QtCore.QSize(300, 75))
        self.copy_delete_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    padding-left:70px;\n"
"    background-color:  none;\n"
"    background-image: url(:/icons/icons/files1.png);\n"
"    background-repeat:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-image: url(:/icons/icons/files2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-image: url(:/icons/icons/files2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"    background-image: url(:/icons/icons/files2.png);\n"
"    background-repeat:none;\n"
"    color:  rgb(244, 154, 32);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"    border-width: 0px 5px 0px 0px;\n"
"    border-radius: 2px;\n"
"    color: #808086;\n"
"    padding-right: 2px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.copy_delete_btn.setObjectName("copy_delete_btn")
        self.verticalLayout_26.addWidget(self.copy_delete_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_26.addItem(spacerItem1)
        self.verticalLayout_23.addWidget(self.frame_18)
        self.buttons_stackedWidget.addWidget(self.settings_buttons_tab)
        self.verticalLayout_2.addWidget(self.buttons_stackedWidget)
        self.logout_btn = QtWidgets.QPushButton(self.main_buttons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logout_btn.sizePolicy().hasHeightForWidth())
        self.logout_btn.setSizePolicy(sizePolicy)
        self.logout_btn.setMinimumSize(QtCore.QSize(90, 60))
        self.logout_btn.setMaximumSize(QtCore.QSize(16777215, 60))
        self.logout_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logout_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-width: 0px 0px 0px 0px;\n"
"    color: #808086;\n"
"    padding: 2px;\n"
"\n"
"    background-color: rgba(255,255,255,0);\n"
"\n"
"    image: url(:/icons/icons/back1.svg);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style:  solid;\n"
"        \n"
"    border-width: 0px 0px 0px 0px;\n"
"    padding-right: 10px;\n"
"    background-color: rgba(255,255,255,0);\n"
"\n"
"    image: url(:/icons/icons/back2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style:  solid;\n"
"        \n"
"    border-width: 0px 0px 0px 0px;\n"
"    padding-right: 10px;\n"
"    background-color: rgba(255,255,255,0);\n"
"\n"
"    image: url(:/icons/icons/back2.svg);\n"
"}\n"
"\n"
"")
        self.logout_btn.setObjectName("logout_btn")
        self.verticalLayout_2.addWidget(self.logout_btn)
        self.gridLayout.addWidget(self.main_buttons_frame, 0, 0, 3, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_55 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName("verticalLayout_55")
        self.panel_title_lbl = QtWidgets.QLabel(self.frame_5)
        self.panel_title_lbl.setMinimumSize(QtCore.QSize(0, 80))
        self.panel_title_lbl.setMaximumSize(QtCore.QSize(16777215, 80))
        self.panel_title_lbl.setStyleSheet("QLabel{\n"
"    font: 75 italic 36pt \"Times New Roman\";\n"
"    color:  rgb(244, 154, 32);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"    \n"
"}")
        self.panel_title_lbl.setText("")
        self.panel_title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.panel_title_lbl.setObjectName("panel_title_lbl")
        self.verticalLayout_55.addWidget(self.panel_title_lbl)
        self.error_frame = QtWidgets.QFrame(self.frame_5)
        self.error_frame.setMaximumSize(QtCore.QSize(16777215, 0))
        self.error_frame.setStyleSheet("QFrame{\n"
"    border:2px solid rgb(244, 154, 32);\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLabel{\n"
"    border:none;\n"
"    font: 20pt \"MS Shell Dlg 2\";\n"
"    color: rgb(244, 154, 32);\n"
"}")
        self.error_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.error_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error_frame.setObjectName("error_frame")
        self.verticalLayout_47 = QtWidgets.QVBoxLayout(self.error_frame)
        self.verticalLayout_47.setObjectName("verticalLayout_47")
        self.error_lbl = QtWidgets.QLabel(self.error_frame)
        self.error_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.error_lbl.setObjectName("error_lbl")
        self.verticalLayout_47.addWidget(self.error_lbl)
        self.verticalLayout_55.addWidget(self.error_frame)
        self.frame_29 = QtWidgets.QFrame(self.frame_5)
        self.frame_29.setMinimumSize(QtCore.QSize(40, 40))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setSpacing(11)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_29)
        self.stackedWidget.setMaximumSize(QtCore.QSize(0, 16777215))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.daily_customers_properties_panel = QtWidgets.QWidget()
        self.daily_customers_properties_panel.setStyleSheet("")
        self.daily_customers_properties_panel.setObjectName("daily_customers_properties_panel")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.daily_customers_properties_panel)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem2)
        self.frame_10 = QtWidgets.QFrame(self.daily_customers_properties_panel)
        self.frame_10.setAutoFillBackground(False)
        self.frame_10.setStyleSheet("")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.daily_customer_add_btn2 = QtWidgets.QPushButton(self.frame_10)
        self.daily_customer_add_btn2.setMinimumSize(QtCore.QSize(70, 70))
        self.daily_customer_add_btn2.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"        \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/icons/icons/add-user.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/add-user2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/add-user2.svg);\n"
"}\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.daily_customer_add_btn2.setText("")
        self.daily_customer_add_btn2.setIconSize(QtCore.QSize(40, 40))
        self.daily_customer_add_btn2.setObjectName("daily_customer_add_btn2")
        self.verticalLayout_3.addWidget(self.daily_customer_add_btn2)
        self.daily_customer_remove_btn = QtWidgets.QPushButton(self.frame_10)
        self.daily_customer_remove_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.daily_customer_remove_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image:url(:/icons/icons/remove-user.svg)\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/remove-user2.svg)\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image:url(:/icons/icons/remove-user2.svg);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.daily_customer_remove_btn.setText("")
        self.daily_customer_remove_btn.setIconSize(QtCore.QSize(40, 40))
        self.daily_customer_remove_btn.setObjectName("daily_customer_remove_btn")
        self.verticalLayout_3.addWidget(self.daily_customer_remove_btn)
        self.daily_customer_add_order = QtWidgets.QPushButton(self.frame_10)
        self.daily_customer_add_order.setMinimumSize(QtCore.QSize(70, 70))
        self.daily_customer_add_order.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/add-order.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/add-order2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/add-order2.svg);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.daily_customer_add_order.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/add order.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.daily_customer_add_order.setIcon(icon)
        self.daily_customer_add_order.setIconSize(QtCore.QSize(40, 40))
        self.daily_customer_add_order.setObjectName("daily_customer_add_order")
        self.verticalLayout_3.addWidget(self.daily_customer_add_order)
        self.daily_customer_search_btn = QtWidgets.QPushButton(self.frame_10)
        self.daily_customer_search_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.daily_customer_search_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/loupe1.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.daily_customer_search_btn.setText("")
        self.daily_customer_search_btn.setObjectName("daily_customer_search_btn")
        self.verticalLayout_3.addWidget(self.daily_customer_search_btn)
        self.daily_customer_export_btn = QtWidgets.QPushButton(self.frame_10)
        self.daily_customer_export_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.daily_customer_export_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/export1.png)\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/export2.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/export2.png);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.daily_customer_export_btn.setText("")
        self.daily_customer_export_btn.setIconSize(QtCore.QSize(40, 40))
        self.daily_customer_export_btn.setObjectName("daily_customer_export_btn")
        self.verticalLayout_3.addWidget(self.daily_customer_export_btn)
        self.daily_customer_edit_price_btn = QtWidgets.QPushButton(self.frame_10)
        self.daily_customer_edit_price_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.daily_customer_edit_price_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/edit1.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/edit2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/edit2.svg);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.daily_customer_edit_price_btn.setText("")
        self.daily_customer_edit_price_btn.setIconSize(QtCore.QSize(40, 40))
        self.daily_customer_edit_price_btn.setObjectName("daily_customer_edit_price_btn")
        self.verticalLayout_3.addWidget(self.daily_customer_edit_price_btn)
        self.daily_customer_remove_btn.raise_()
        self.daily_customer_add_btn2.raise_()
        self.daily_customer_export_btn.raise_()
        self.daily_customer_add_order.raise_()
        self.daily_customer_edit_price_btn.raise_()
        self.daily_customer_search_btn.raise_()
        self.verticalLayout_7.addWidget(self.frame_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.daily_customers_properties_panel)
        self.orders_properties_panel = QtWidgets.QWidget()
        self.orders_properties_panel.setStyleSheet("")
        self.orders_properties_panel.setObjectName("orders_properties_panel")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.orders_properties_panel)
        self.verticalLayout_28.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_28.setSpacing(2)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        spacerItem4 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_28.addItem(spacerItem4)
        self.frame_17 = QtWidgets.QFrame(self.orders_properties_panel)
        self.frame_17.setAutoFillBackground(False)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.order_add_btn2 = QtWidgets.QPushButton(self.frame_17)
        self.order_add_btn2.setMinimumSize(QtCore.QSize(70, 70))
        self.order_add_btn2.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.order_add_btn2.setText("")
        self.order_add_btn2.setIconSize(QtCore.QSize(40, 40))
        self.order_add_btn2.setObjectName("order_add_btn2")
        self.verticalLayout_9.addWidget(self.order_add_btn2)
        self.order_remove_btn = QtWidgets.QPushButton(self.frame_17)
        self.order_remove_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.order_remove_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image: url(:/icons/icons/trash-can-with-cover.svg) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"     \n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/trash-can-with-cover.svg);\n"
"    background-color: rgb(200, 200, 200);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/open-trash-can.svg);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.order_remove_btn.setText("")
        self.order_remove_btn.setIconSize(QtCore.QSize(40, 40))
        self.order_remove_btn.setObjectName("order_remove_btn")
        self.verticalLayout_9.addWidget(self.order_remove_btn)
        self.order_search_btn = QtWidgets.QPushButton(self.frame_17)
        self.order_search_btn.setEnabled(True)
        self.order_search_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.order_search_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/loupe1.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.order_search_btn.setText("")
        self.order_search_btn.setObjectName("order_search_btn")
        self.verticalLayout_9.addWidget(self.order_search_btn)
        self.order_show_btn = QtWidgets.QPushButton(self.frame_17)
        self.order_show_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.order_show_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/loupe1.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.order_show_btn.setText("")
        self.order_show_btn.setObjectName("order_show_btn")
        self.verticalLayout_9.addWidget(self.order_show_btn)
        self.order_export_btn = QtWidgets.QPushButton(self.frame_17)
        self.order_export_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.order_export_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/export1.png)\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/export2.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/export2.png);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.order_export_btn.setText("")
        self.order_export_btn.setIconSize(QtCore.QSize(40, 40))
        self.order_export_btn.setObjectName("order_export_btn")
        self.verticalLayout_9.addWidget(self.order_export_btn)
        self.verticalLayout_28.addWidget(self.frame_17)
        spacerItem5 = QtWidgets.QSpacerItem(20, 253, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem5)
        self.stackedWidget.addWidget(self.orders_properties_panel)
        self.monthly_customers_properties_panel = QtWidgets.QWidget()
        self.monthly_customers_properties_panel.setObjectName("monthly_customers_properties_panel")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.monthly_customers_properties_panel)
        self.verticalLayout_30.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_30.setSpacing(2)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        spacerItem6 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_30.addItem(spacerItem6)
        self.frame_20 = QtWidgets.QFrame(self.monthly_customers_properties_panel)
        self.frame_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_20.setAutoFillBackground(False)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.monthly_customer_add_btn2 = QtWidgets.QPushButton(self.frame_20)
        self.monthly_customer_add_btn2.setMinimumSize(QtCore.QSize(70, 70))
        self.monthly_customer_add_btn2.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"    padding: 10px;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/add-user.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style:  solid;\n"
"    border-color: rgb(174, 174, 174);\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    \n"
"    image: url(:/icons/icons/add-user2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    border-style:  solid;\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/add-user2.svg);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    border-style:  solid;\n"
"    border-color: rgb(174, 174, 174);\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    padding: 10px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.monthly_customer_add_btn2.setText("")
        self.monthly_customer_add_btn2.setIconSize(QtCore.QSize(40, 40))
        self.monthly_customer_add_btn2.setObjectName("monthly_customer_add_btn2")
        self.verticalLayout.addWidget(self.monthly_customer_add_btn2)
        self.monthly_customer_remove_btn = QtWidgets.QPushButton(self.frame_20)
        self.monthly_customer_remove_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.monthly_customer_remove_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image:url(:/icons/icons/remove-user.svg)\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style:  solid;\n"
"    border-color: rgb(174, 174, 174);\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    \n"
"    image: url(:/icons/icons/remove-user2.svg)\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    border-style:  solid;\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    background-color: rgb(100, 100, 100);\n"
"    image:url(:/icons/icons/remove-user2.svg);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    border-style:  solid;\n"
"    border-color: rgb(174, 174, 174);\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    padding: 10px;\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.monthly_customer_remove_btn.setText("")
        self.monthly_customer_remove_btn.setIconSize(QtCore.QSize(40, 40))
        self.monthly_customer_remove_btn.setObjectName("monthly_customer_remove_btn")
        self.verticalLayout.addWidget(self.monthly_customer_remove_btn)
        self.monthly_customer_update_btn = QtWidgets.QPushButton(self.frame_20)
        self.monthly_customer_update_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.monthly_customer_update_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/refresh.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    image: url(:/icons/icons/refresh2.svg)\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/refresh2.svg)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.monthly_customer_update_btn.setText("")
        self.monthly_customer_update_btn.setIconSize(QtCore.QSize(40, 40))
        self.monthly_customer_update_btn.setObjectName("monthly_customer_update_btn")
        self.verticalLayout.addWidget(self.monthly_customer_update_btn)
        self.monthly_customer_search_btn = QtWidgets.QPushButton(self.frame_20)
        self.monthly_customer_search_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.monthly_customer_search_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/loupe1.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(142,142,142);\n"
"}")
        self.monthly_customer_search_btn.setText("")
        self.monthly_customer_search_btn.setObjectName("monthly_customer_search_btn")
        self.verticalLayout.addWidget(self.monthly_customer_search_btn)
        self.monthly_customer_export_btn = QtWidgets.QPushButton(self.frame_20)
        self.monthly_customer_export_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.monthly_customer_export_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/export1.png)\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/export2.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/export2.png);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.monthly_customer_export_btn.setText("")
        self.monthly_customer_export_btn.setIconSize(QtCore.QSize(40, 40))
        self.monthly_customer_export_btn.setObjectName("monthly_customer_export_btn")
        self.verticalLayout.addWidget(self.monthly_customer_export_btn)
        self.monthly_customer_edit_cost_btn = QtWidgets.QPushButton(self.frame_20)
        self.monthly_customer_edit_cost_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.monthly_customer_edit_cost_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/edit1.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    image: url(:/icons/icons/edit2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/edit2.svg);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.monthly_customer_edit_cost_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.monthly_customer_edit_cost_btn.setIcon(icon1)
        self.monthly_customer_edit_cost_btn.setIconSize(QtCore.QSize(40, 40))
        self.monthly_customer_edit_cost_btn.setObjectName("monthly_customer_edit_cost_btn")
        self.verticalLayout.addWidget(self.monthly_customer_edit_cost_btn)
        self.verticalLayout_30.addWidget(self.frame_20)
        spacerItem7 = QtWidgets.QSpacerItem(20, 253, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_30.addItem(spacerItem7)
        self.stackedWidget.addWidget(self.monthly_customers_properties_panel)
        self.warehouse_properties_panel = QtWidgets.QWidget()
        self.warehouse_properties_panel.setObjectName("warehouse_properties_panel")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.warehouse_properties_panel)
        self.verticalLayout_37.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_37.setSpacing(2)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        spacerItem8 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_37.addItem(spacerItem8)
        self.frame_7 = QtWidgets.QFrame(self.warehouse_properties_panel)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(4)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.warehouse_item_add_btn2 = QtWidgets.QPushButton(self.frame_7)
        self.warehouse_item_add_btn2.setMinimumSize(QtCore.QSize(70, 70))
        self.warehouse_item_add_btn2.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style:  solid;\n"
"    border-color: rgb(174, 174, 174);\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    border-style:  solid;\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"")
        self.warehouse_item_add_btn2.setText("")
        self.warehouse_item_add_btn2.setIconSize(QtCore.QSize(60, 60))
        self.warehouse_item_add_btn2.setObjectName("warehouse_item_add_btn2")
        self.verticalLayout_15.addWidget(self.warehouse_item_add_btn2)
        self.warehouse_item_remove_btn = QtWidgets.QPushButton(self.frame_7)
        self.warehouse_item_remove_btn.setEnabled(True)
        self.warehouse_item_remove_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.warehouse_item_remove_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image: url(:/icons/icons/trash-can-with-cover.svg) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"     \n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/trash-can-with-cover.svg);\n"
"    background-color: rgb(200, 200, 200);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/open-trash-can.svg);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.warehouse_item_remove_btn.setText("")
        self.warehouse_item_remove_btn.setIconSize(QtCore.QSize(30, 30))
        self.warehouse_item_remove_btn.setObjectName("warehouse_item_remove_btn")
        self.verticalLayout_15.addWidget(self.warehouse_item_remove_btn)
        self.warehouse_update_current_items_btn = QtWidgets.QPushButton(self.frame_7)
        self.warehouse_update_current_items_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.warehouse_update_current_items_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image:url(:/icons/icons/reset-warehouse1.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"     \n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    image:url(:/icons/icons/reset-warehouse2.png);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/reset-warehouse2.png);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.warehouse_update_current_items_btn.setText("")
        self.warehouse_update_current_items_btn.setObjectName("warehouse_update_current_items_btn")
        self.verticalLayout_15.addWidget(self.warehouse_update_current_items_btn)
        self.verticalLayout_37.addWidget(self.frame_7)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_37.addItem(spacerItem9)
        self.stackedWidget.addWidget(self.warehouse_properties_panel)
        self.reports_properties_panel = QtWidgets.QWidget()
        self.reports_properties_panel.setObjectName("reports_properties_panel")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.reports_properties_panel)
        self.verticalLayout_44.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_44.setSpacing(2)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_44.addItem(spacerItem10)
        self.frame_8 = QtWidgets.QFrame(self.reports_properties_panel)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.report_remove_btn = QtWidgets.QPushButton(self.frame_8)
        self.report_remove_btn.setEnabled(True)
        self.report_remove_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.report_remove_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image: url(:/icons/icons/trash-can-with-cover.svg) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"     \n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/trash-can-with-cover.svg);\n"
"    background-color: rgb(200, 200, 200);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/open-trash-can.svg);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.report_remove_btn.setText("")
        self.report_remove_btn.setIconSize(QtCore.QSize(30, 30))
        self.report_remove_btn.setObjectName("report_remove_btn")
        self.verticalLayout_14.addWidget(self.report_remove_btn)
        self.report_export_btn = QtWidgets.QPushButton(self.frame_8)
        self.report_export_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.report_export_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/export1.png)\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/export2.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/export2.png);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.report_export_btn.setText("")
        self.report_export_btn.setIconSize(QtCore.QSize(40, 40))
        self.report_export_btn.setObjectName("report_export_btn")
        self.verticalLayout_14.addWidget(self.report_export_btn)
        self.report_search_btn = QtWidgets.QPushButton(self.frame_8)
        self.report_search_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.report_search_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"    image: url(:/icons/icons/loupe1.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style:  solid;\n"
"    border-color: rgb(174, 174, 174);\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    \n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    border-style:  solid;\n"
"    border-width: 5px;\n"
"    border-radius: 35px;\n"
"    padding: 10px;\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/loupe2.svg);\n"
"}\n"
"")
        self.report_search_btn.setText("")
        self.report_search_btn.setObjectName("report_search_btn")
        self.verticalLayout_14.addWidget(self.report_search_btn)
        self.verticalLayout_44.addWidget(self.frame_8)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_44.addItem(spacerItem11)
        self.stackedWidget.addWidget(self.reports_properties_panel)
        self.employees_properties_panel = QtWidgets.QWidget()
        self.employees_properties_panel.setObjectName("employees_properties_panel")
        self.verticalLayout_49 = QtWidgets.QVBoxLayout(self.employees_properties_panel)
        self.verticalLayout_49.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_49.setSpacing(2)
        self.verticalLayout_49.setObjectName("verticalLayout_49")
        spacerItem12 = QtWidgets.QSpacerItem(20, 220, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_49.addItem(spacerItem12)
        self.frame_2 = QtWidgets.QFrame(self.employees_properties_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.employee_add_btn2 = QtWidgets.QPushButton(self.frame_2)
        self.employee_add_btn2.setMinimumSize(QtCore.QSize(70, 70))
        self.employee_add_btn2.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"")
        self.employee_add_btn2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.employee_add_btn2.setIcon(icon2)
        self.employee_add_btn2.setIconSize(QtCore.QSize(60, 60))
        self.employee_add_btn2.setAutoRepeat(False)
        self.employee_add_btn2.setObjectName("employee_add_btn2")
        self.verticalLayout_13.addWidget(self.employee_add_btn2)
        self.employee_remove_btn = QtWidgets.QPushButton(self.frame_2)
        self.employee_remove_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.employee_remove_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image: url(:/icons/icons/trash-can-with-cover.svg) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"     \n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/trash-can-with-cover.svg);\n"
"    background-color: rgb(200, 200, 200);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/open-trash-can.svg);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.employee_remove_btn.setText("")
        self.employee_remove_btn.setIconSize(QtCore.QSize(30, 30))
        self.employee_remove_btn.setObjectName("employee_remove_btn")
        self.verticalLayout_13.addWidget(self.employee_remove_btn)
        self.verticalLayout_49.addWidget(self.frame_2)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_49.addItem(spacerItem13)
        self.stackedWidget.addWidget(self.employees_properties_panel)
        self.shifts_properties_panel = QtWidgets.QWidget()
        self.shifts_properties_panel.setObjectName("shifts_properties_panel")
        self.verticalLayout_69 = QtWidgets.QVBoxLayout(self.shifts_properties_panel)
        self.verticalLayout_69.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_69.setSpacing(2)
        self.verticalLayout_69.setObjectName("verticalLayout_69")
        spacerItem14 = QtWidgets.QSpacerItem(20, 220, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_69.addItem(spacerItem14)
        self.frame_54 = QtWidgets.QFrame(self.shifts_properties_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_54.sizePolicy().hasHeightForWidth())
        self.frame_54.setSizePolicy(sizePolicy)
        self.frame_54.setStyleSheet("")
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.verticalLayout_58 = QtWidgets.QVBoxLayout(self.frame_54)
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_58.setSpacing(4)
        self.verticalLayout_58.setObjectName("verticalLayout_58")
        self.shift_add_btn2 = QtWidgets.QPushButton(self.frame_54)
        self.shift_add_btn2.setMinimumSize(QtCore.QSize(70, 70))
        self.shift_add_btn2.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"")
        self.shift_add_btn2.setText("")
        self.shift_add_btn2.setAutoRepeat(False)
        self.shift_add_btn2.setObjectName("shift_add_btn2")
        self.verticalLayout_58.addWidget(self.shift_add_btn2)
        self.shift_remove_btn = QtWidgets.QPushButton(self.frame_54)
        self.shift_remove_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.shift_remove_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image: url(:/icons/icons/trash-can-with-cover.svg) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"     \n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/trash-can-with-cover.svg);\n"
"    background-color: rgb(200, 200, 200);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/open-trash-can.svg);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.shift_remove_btn.setText("")
        self.shift_remove_btn.setObjectName("shift_remove_btn")
        self.verticalLayout_58.addWidget(self.shift_remove_btn)
        self.shift_start_btn = QtWidgets.QPushButton(self.frame_54)
        self.shift_start_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.shift_start_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image: url(:/icons/icons/start1.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/start2.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/start2.png);\n"
"\n"
"}\n"
"\n"
"")
        self.shift_start_btn.setText("")
        self.shift_start_btn.setObjectName("shift_start_btn")
        self.verticalLayout_58.addWidget(self.shift_start_btn)
        self.shift_stop_btn = QtWidgets.QPushButton(self.frame_54)
        self.shift_stop_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.shift_stop_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image: url(:/icons/icons/stop1.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"     \n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/stop2.png);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/stop2.png);\n"
"\n"
"}\n"
"\n"
"")
        self.shift_stop_btn.setText("")
        self.shift_stop_btn.setObjectName("shift_stop_btn")
        self.verticalLayout_58.addWidget(self.shift_stop_btn)
        self.verticalLayout_69.addWidget(self.frame_54)
        spacerItem15 = QtWidgets.QSpacerItem(20, 539, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_69.addItem(spacerItem15)
        self.stackedWidget.addWidget(self.shifts_properties_panel)
        self.offers_properties_panel = QtWidgets.QWidget()
        self.offers_properties_panel.setObjectName("offers_properties_panel")
        self.verticalLayout_53 = QtWidgets.QVBoxLayout(self.offers_properties_panel)
        self.verticalLayout_53.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_53.setSpacing(2)
        self.verticalLayout_53.setObjectName("verticalLayout_53")
        spacerItem16 = QtWidgets.QSpacerItem(20, 220, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_53.addItem(spacerItem16)
        self.frame_55 = QtWidgets.QFrame(self.offers_properties_panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy)
        self.frame_55.setStyleSheet("")
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.verticalLayout_65 = QtWidgets.QVBoxLayout(self.frame_55)
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_65.setSpacing(4)
        self.verticalLayout_65.setObjectName("verticalLayout_65")
        self.offer_add_btn2 = QtWidgets.QPushButton(self.frame_55)
        self.offer_add_btn2.setMinimumSize(QtCore.QSize(70, 70))
        self.offer_add_btn2.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"    \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"")
        self.offer_add_btn2.setText("")
        self.offer_add_btn2.setAutoRepeat(False)
        self.offer_add_btn2.setObjectName("offer_add_btn2")
        self.verticalLayout_65.addWidget(self.offer_add_btn2)
        self.offer_remove_btn = QtWidgets.QPushButton(self.frame_55)
        self.offer_remove_btn.setEnabled(True)
        self.offer_remove_btn.setMinimumSize(QtCore.QSize(70, 70))
        self.offer_remove_btn.setStyleSheet("QPushButton{\n"
"\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:35px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 10px;\n"
"\n"
"    \n"
"    image: url(:/icons/icons/trash-can-with-cover.svg) ;\n"
"    background-color: rgb(255, 255, 255);\n"
"     \n"
"\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    image: url(:/icons/icons/trash-can-with-cover.svg);\n"
"    background-color: rgb(200, 200, 200);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(100, 100, 100);\n"
"    image: url(:/icons/icons/open-trash-can.svg);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    \n"
"    background-color: rgb(142,142,142);\n"
"}\n"
"")
        self.offer_remove_btn.setText("")
        self.offer_remove_btn.setObjectName("offer_remove_btn")
        self.verticalLayout_65.addWidget(self.offer_remove_btn)
        self.verticalLayout_53.addWidget(self.frame_55)
        spacerItem17 = QtWidgets.QSpacerItem(20, 585, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_53.addItem(spacerItem17)
        self.stackedWidget.addWidget(self.offers_properties_panel)
        self.horizontalLayout_33.addWidget(self.stackedWidget)
        self.date_treeview_panel = QtWidgets.QFrame(self.frame_29)
        self.date_treeview_panel.setMinimumSize(QtCore.QSize(0, 0))
        self.date_treeview_panel.setMaximumSize(QtCore.QSize(0, 16777215))
        self.date_treeview_panel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date_treeview_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.date_treeview_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.date_treeview_panel.setObjectName("date_treeview_panel")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.date_treeview_panel)
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.date_treeView = QtWidgets.QTreeView(self.date_treeview_panel)
        self.date_treeView.setMinimumSize(QtCore.QSize(190, 0))
        self.date_treeView.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.date_treeView.setObjectName("date_treeView")
        self.verticalLayout_31.addWidget(self.date_treeView)
        self.horizontalLayout_33.addWidget(self.date_treeview_panel)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_29)
        self.tabWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Main_tab = QtWidgets.QWidget()
        self.Main_tab.setStyleSheet("")
        self.Main_tab.setObjectName("Main_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Main_tab)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_17 = QtWidgets.QLabel(self.Main_tab)
        self.label_17.setStyleSheet("QLabel{\n"
"    color:rgb(244, 154, 32);\n"
"    \n"
"    font: 100 italic 13pt \"Segoe UI\";\n"
"    padding:5px;\n"
"    background-color: rgba(255, 255, 255, 40);\n"
"}")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 4, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem18, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.Main_tab)
        self.frame.setMinimumSize(QtCore.QSize(600, 120))
        self.frame.setMaximumSize(QtCore.QSize(600, 120))
        self.frame.setStyleSheet("QFrame{\n"
"    border-style: solid;\n"
"    border-width: 10px;\n"
"    border-radius: 60px;\n"
"    \n"
"    border-color: rgb(244, 154, 32);\n"
"    \n"
"    \n"
"    background-color: transparent;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.daily_btn = QtWidgets.QPushButton(self.frame)
        self.daily_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.daily_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.daily_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:10px;\n"
"    \n"
"    background-color: rgba(243, 243, 243,0);\n"
"    \n"
"    image:url(:/icons/icons/calendar1.svg);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"        border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:10px;\n"
"    \n"
"    background-color:  rgba(230, 230, 230,0);\n"
"\n"
"    image:url(:/icons/icons/calendar2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"        border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:15px;\n"
"    \n"
"\n"
"    background-color:  rgba(230, 230, 230,0);\n"
"\n"
"    image:url(:/icons/icons/calendar2.svg);\n"
"}\n"
"")
        self.daily_btn.setText("")
        self.daily_btn.setObjectName("daily_btn")
        self.horizontalLayout_8.addWidget(self.daily_btn)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.archive_btn = QtWidgets.QPushButton(self.frame)
        self.archive_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.archive_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.archive_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:10px;\n"
"    \n"
"    background-color:  rgba(230, 230, 230,0);\n"
"    \n"
"    image:url(:/icons/icons/inbox1.svg);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"        border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:10px;\n"
"    \n"
"    background-color:  rgba(230, 230, 230,0);\n"
"\n"
"    image: url(:/icons/icons/inbox2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"        border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:15px;\n"
"    \n"
"\n"
"    background-color:  rgba(230, 230, 230,0);\n"
"\n"
"    image: url(:/icons/icons/inbox2.svg);\n"
"}\n"
"")
        self.archive_btn.setText("")
        self.archive_btn.setObjectName("archive_btn")
        self.horizontalLayout_8.addWidget(self.archive_btn)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_8.addWidget(self.line_2)
        self.settings_btn = QtWidgets.QPushButton(self.frame)
        self.settings_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.settings_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.settings_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:10px;\n"
"    \n"
"    background-color:  rgba(230, 230, 230,0);\n"
"    \n"
"    image:url(:/icons/icons/settings1.svg);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"        border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:10px;\n"
"    \n"
"    background-color:  rgba(230, 230, 230,0);\n"
"\n"
"    image:url(:/icons/icons/settings2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"        border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:15px;\n"
"    \n"
"\n"
"    background-color:  rgba(230, 230, 230,0);\n"
"\n"
"    image:url(:/icons/icons/settings2.svg);\n"
"}\n"
"")
        self.settings_btn.setObjectName("settings_btn")
        self.horizontalLayout_8.addWidget(self.settings_btn)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_8.addWidget(self.line_3)
        self.exit_btn = QtWidgets.QPushButton(self.frame)
        self.exit_btn.setMinimumSize(QtCore.QSize(100, 100))
        self.exit_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:15px;\n"
"    \n"
"    background-color:  rgba(230, 230, 230,0);\n"
"    \n"
"    image:url(:/icons/icons/logout1.svg);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"        border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:15px;;\n"
"    \n"
"    background-color:  rgba(230, 230, 230,0);\n"
"\n"
"    image:url(:/icons/icons/logout2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"        border-style: solid;\n"
"    border-right-color:  rgb(172, 159, 184);\n"
"    border-width: 0px 0px 0px 0px;\n"
"    border-radius: 0px;\n"
"    \n"
"    padding:20px;\n"
"    \n"
"\n"
"    background-color:  rgba(230, 230, 230,0);\n"
"\n"
"    image:url(:/icons/icons/logout2.svg);\n"
"}\n"
"")
        self.exit_btn.setText("")
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout_8.addWidget(self.exit_btn)
        self.gridLayout_2.addWidget(self.frame, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.logo_frame = QtWidgets.QFrame(self.Main_tab)
        self.logo_frame.setMinimumSize(QtCore.QSize(600, 600))
        self.logo_frame.setMaximumSize(QtCore.QSize(600, 600))
        self.logo_frame.setStyleSheet("#logo_frame{\n"
"\n"
"    image: url(:/icons/icons/studyzone-logo.png);\n"
"\n"
"}")
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.logo_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2.addWidget(self.logo_frame, 1, 1, 1, 1)
        self.tabWidget.addTab(self.Main_tab, "")
        self.daily_customers_tab = QtWidgets.QWidget()
        self.daily_customers_tab.setObjectName("daily_customers_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.daily_customers_tab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.daily_customers_tab)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_6.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"    \n"
"}")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 4, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.daily_customers_tab)
        self.frame_19.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_19.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_5.setContentsMargins(0, 120, 0, 0)
        self.verticalLayout_5.setSpacing(11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_19)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        self.label_5.setStyleSheet("QLabel{\n"
"    border-style: solid;\n"
"    border-width: 0px 0px 3px 0px;\n"
"    border-bottom-color: rgb(174, 174, 174);\n"
"    padding: px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.frame_19)
        self.label_12.setMinimumSize(QtCore.QSize(200, 0))
        self.label_12.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_12.setStyleSheet("QLabel{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.daily_customer_name_txt = QtWidgets.QLineEdit(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily_customer_name_txt.sizePolicy().hasHeightForWidth())
        self.daily_customer_name_txt.setSizePolicy(sizePolicy)
        self.daily_customer_name_txt.setMinimumSize(QtCore.QSize(250, 40))
        self.daily_customer_name_txt.setStyleSheet("")
        self.daily_customer_name_txt.setClearButtonEnabled(True)
        self.daily_customer_name_txt.setObjectName("daily_customer_name_txt")
        self.horizontalLayout_6.addWidget(self.daily_customer_name_txt)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.frame_19)
        self.label_14.setMinimumSize(QtCore.QSize(200, 0))
        self.label_14.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_14.setStyleSheet("QLabel{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.daily_customer_monthID_txt = QtWidgets.QLineEdit(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily_customer_monthID_txt.sizePolicy().hasHeightForWidth())
        self.daily_customer_monthID_txt.setSizePolicy(sizePolicy)
        self.daily_customer_monthID_txt.setMinimumSize(QtCore.QSize(100, 40))
        self.daily_customer_monthID_txt.setMaximumSize(QtCore.QSize(100, 16777215))
        self.daily_customer_monthID_txt.setClearButtonEnabled(True)
        self.daily_customer_monthID_txt.setObjectName("daily_customer_monthID_txt")
        self.horizontalLayout_10.addWidget(self.daily_customer_monthID_txt)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem19)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_42 = QtWidgets.QLabel(self.frame_19)
        self.label_42.setMinimumSize(QtCore.QSize(200, 0))
        self.label_42.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_30.addWidget(self.label_42)
        self.daily_customer_cusType_comboBox = QtWidgets.QComboBox(self.frame_19)
        self.daily_customer_cusType_comboBox.setMinimumSize(QtCore.QSize(250, 40))
        self.daily_customer_cusType_comboBox.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.daily_customer_cusType_comboBox.setObjectName("daily_customer_cusType_comboBox")
        self.daily_customer_cusType_comboBox.addItem("")
        self.daily_customer_cusType_comboBox.setItemText(0, "")
        self.daily_customer_cusType_comboBox.addItem("")
        self.horizontalLayout_30.addWidget(self.daily_customer_cusType_comboBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_30)
        self.daily_customer_add_btn = QtWidgets.QPushButton(self.frame_19)
        self.daily_customer_add_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.daily_customer_add_btn.setStyleSheet("QPushButton{\n"
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
"}")
        self.daily_customer_add_btn.setObjectName("daily_customer_add_btn")
        self.verticalLayout_5.addWidget(self.daily_customer_add_btn)
        self.gridLayout_3.addWidget(self.frame_19, 2, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.daily_customers_tab)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25.setSpacing(11)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.frame_14 = QtWidgets.QFrame(self.frame_3)
        self.frame_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_14.setStyleSheet("#frame_14{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(247,174,0);\n"
"    border-radius:4px;\n"
"    \n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_24 = QtWidgets.QLabel(self.frame_14)
        self.label_24.setStyleSheet("QLabel{\n"
"background-color: rgb(244, 154, 32);\n"
"    \n"
"    font: 100 20pt \"Times New Roman\";\n"
"    \n"
" \n"
"}")
        self.label_24.setObjectName("label_24")
        self.verticalLayout_19.addWidget(self.label_24)
        self.frame_26 = QtWidgets.QFrame(self.frame_14)
        self.frame_26.setStyleSheet("")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_18.setSpacing(30)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_15 = QtWidgets.QLabel(self.frame_26)
        self.label_15.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_12.addWidget(self.label_15)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.daily_customer_name_filter_txt = QtWidgets.QLineEdit(self.frame_26)
        self.daily_customer_name_filter_txt.setMinimumSize(QtCore.QSize(300, 40))
        self.daily_customer_name_filter_txt.setMaximumSize(QtCore.QSize(300, 16777215))
        self.daily_customer_name_filter_txt.setClearButtonEnabled(True)
        self.daily_customer_name_filter_txt.setObjectName("daily_customer_name_filter_txt")
        self.horizontalLayout.addWidget(self.daily_customer_name_filter_txt)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.horizontalLayout_18.addLayout(self.verticalLayout_12)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setSpacing(7)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_32 = QtWidgets.QLabel(self.frame_26)
        self.label_32.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_32.setObjectName("label_32")
        self.verticalLayout_27.addWidget(self.label_32)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(4)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.daily_customer_subsType_filter_comboBox = QtWidgets.QComboBox(self.frame_26)
        self.daily_customer_subsType_filter_comboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.daily_customer_subsType_filter_comboBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.daily_customer_subsType_filter_comboBox.setObjectName("daily_customer_subsType_filter_comboBox")
        self.daily_customer_subsType_filter_comboBox.addItem("")
        self.daily_customer_subsType_filter_comboBox.setItemText(0, "")
        self.daily_customer_subsType_filter_comboBox.addItem("")
        self.daily_customer_subsType_filter_comboBox.addItem("")
        self.daily_customer_subsType_filter_comboBox.addItem("")
        self.daily_customer_subsType_filter_comboBox.addItem("")
        self.horizontalLayout_17.addWidget(self.daily_customer_subsType_filter_comboBox)
        self.verticalLayout_27.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18.addLayout(self.verticalLayout_27)
        self.daily_customer_clear_btn = QtWidgets.QPushButton(self.frame_26)
        self.daily_customer_clear_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.daily_customer_clear_btn.setObjectName("daily_customer_clear_btn")
        self.horizontalLayout_18.addWidget(self.daily_customer_clear_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem20)
        self.verticalLayout_19.addWidget(self.frame_26)
        self.verticalLayout_25.addWidget(self.frame_14)
        self.daily_customers_tableView = QtWidgets.QTableView(self.frame_3)
        self.daily_customers_tableView.setFrameShape(QtWidgets.QFrame.Box)
        self.daily_customers_tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.daily_customers_tableView.setAlternatingRowColors(True)
        self.daily_customers_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.daily_customers_tableView.setObjectName("daily_customers_tableView")
        self.daily_customers_tableView.verticalHeader().setDefaultSectionSize(40)
        self.daily_customers_tableView.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout_25.addWidget(self.daily_customers_tableView)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_54 = QtWidgets.QLabel(self.frame_3)
        self.label_54.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_54.setStyleSheet("QLabel{\n"
"    color:rgb(244, 154, 32);\n"
"    \n"
"}")
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_41.addWidget(self.label_54)
        self.daily_customers_count_lbl = QtWidgets.QLabel(self.frame_3)
        self.daily_customers_count_lbl.setStyleSheet("QLabel{\n"
"    color:rgb(244, 154, 32);\n"
"    \n"
"}")
        self.daily_customers_count_lbl.setObjectName("daily_customers_count_lbl")
        self.horizontalLayout_41.addWidget(self.daily_customers_count_lbl)
        self.verticalLayout_25.addLayout(self.horizontalLayout_41)
        self.gridLayout_3.addWidget(self.frame_3, 2, 4, 2, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem21, 3, 2, 1, 1)
        self.tabWidget.addTab(self.daily_customers_tab, "")
        self.orders_tab = QtWidgets.QWidget()
        self.orders_tab.setObjectName("orders_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.orders_tab)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setHorizontalSpacing(7)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label = QtWidgets.QLabel(self.orders_tab)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_8.addWidget(self.label, 0, 1, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.orders_tab)
        self.frame_11.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(11)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setStyleSheet("QLabel{\n"
"border-style: solid;\n"
"border-width: 0px 0px 3px 0px;\n"
"border-bottom-color: rgb(174, 174, 174);\n"
"padding: 2px;\n"
"\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_16.addWidget(self.label_7)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        self.label_3.setMinimumSize(QtCore.QSize(200, 0))
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_3.setStyleSheet("QLabel{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_11.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft)
        self.customer_name_txt2 = QtWidgets.QLineEdit(self.frame_11)
        self.customer_name_txt2.setMinimumSize(QtCore.QSize(250, 40))
        self.customer_name_txt2.setClearButtonEnabled(True)
        self.customer_name_txt2.setObjectName("customer_name_txt2")
        self.horizontalLayout_11.addWidget(self.customer_name_txt2, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_16.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_30 = QtWidgets.QLabel(self.frame_11)
        self.label_30.setMinimumSize(QtCore.QSize(200, 0))
        self.label_30.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_4.addWidget(self.label_30, 0, QtCore.Qt.AlignLeft)
        self.order_sell_type_comboBox = QtWidgets.QComboBox(self.frame_11)
        self.order_sell_type_comboBox.setMinimumSize(QtCore.QSize(250, 40))
        self.order_sell_type_comboBox.setObjectName("order_sell_type_comboBox")
        self.order_sell_type_comboBox.addItem("")
        self.order_sell_type_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.order_sell_type_comboBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.plus_order_btn = QtWidgets.QPushButton(self.frame_11)
        self.plus_order_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.plus_order_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.plus_order_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 5px;;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding:5px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding:10px;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.plus_order_btn.setText("")
        self.plus_order_btn.setIcon(icon2)
        self.plus_order_btn.setIconSize(QtCore.QSize(50, 50))
        self.plus_order_btn.setObjectName("plus_order_btn")
        self.horizontalLayout_2.addWidget(self.plus_order_btn)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem22)
        self.verticalLayout_16.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_11)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 45, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setContentsMargins(0, 0, 25, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.orders_items_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.orders_items_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.orders_items_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.orders_items_frame.setObjectName("orders_items_frame")
        self.verticalLayout_70 = QtWidgets.QVBoxLayout(self.orders_items_frame)
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.verticalLayout_8.addWidget(self.orders_items_frame)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem23)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_16.addWidget(self.scrollArea)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_28 = QtWidgets.QLabel(self.frame_11)
        self.label_28.setMinimumSize(QtCore.QSize(200, 0))
        self.label_28.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_28.setStyleSheet("QLabel{\n"
"    \n"
"    color: rgb(244, 154, 32);\n"
"    font: 75 22pt \"Times New Roman\";\n"
"}\n"
"")
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_19.addWidget(self.label_28)
        self.total_price_lbl = QtWidgets.QLabel(self.frame_11)
        self.total_price_lbl.setMinimumSize(QtCore.QSize(300, 0))
        self.total_price_lbl.setStyleSheet("QLabel{\n"
"    \n"
"    color: rgb(244, 154, 32);\n"
"    font: 75 22pt \"Times New Roman\";\n"
"}\n"
"")
        self.total_price_lbl.setObjectName("total_price_lbl")
        self.horizontalLayout_19.addWidget(self.total_price_lbl)
        self.verticalLayout_16.addLayout(self.horizontalLayout_19)
        self.order_add_btn = QtWidgets.QPushButton(self.frame_11)
        self.order_add_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.order_add_btn.setStyleSheet("")
        self.order_add_btn.setObjectName("order_add_btn")
        self.verticalLayout_16.addWidget(self.order_add_btn)
        self.gridLayout_8.addWidget(self.frame_11, 1, 0, 1, 1, QtCore.Qt.AlignTop)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem24, 2, 0, 1, 1)
        self.frame_12 = QtWidgets.QFrame(self.orders_tab)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(11)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_35 = QtWidgets.QFrame(self.frame_12)
        self.frame_35.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_35.setStyleSheet("#frame_36{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(247,174,0);\n"
"    border-radius:4px;\n"
"    \n"
"}")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_35)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.label_37 = QtWidgets.QLabel(self.frame_35)
        self.label_37.setStyleSheet("QLabel{\n"
"background-color: rgb(244, 154, 32);\n"
"    \n"
"    font: 100 20pt \"Times New Roman\";\n"
"    \n"
" \n"
"}")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_34.addWidget(self.label_37)
        self.frame_36 = QtWidgets.QFrame(self.frame_35)
        self.frame_36.setStyleSheet("")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_36)
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.verticalLayout_38.setSpacing(7)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.label_41 = QtWidgets.QLabel(self.frame_36)
        self.label_41.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_41.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_41.setObjectName("label_41")
        self.verticalLayout_38.addWidget(self.label_41)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(4)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.orders_customer_name_filter_txt = QtWidgets.QLineEdit(self.frame_36)
        self.orders_customer_name_filter_txt.setMinimumSize(QtCore.QSize(300, 40))
        self.orders_customer_name_filter_txt.setMaximumSize(QtCore.QSize(300, 16777215))
        self.orders_customer_name_filter_txt.setClearButtonEnabled(True)
        self.orders_customer_name_filter_txt.setObjectName("orders_customer_name_filter_txt")
        self.horizontalLayout_20.addWidget(self.orders_customer_name_filter_txt)
        self.verticalLayout_38.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_12.addLayout(self.verticalLayout_38)
        self.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.verticalLayout_43.setSpacing(7)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.label_45 = QtWidgets.QLabel(self.frame_36)
        self.label_45.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_45.setObjectName("label_45")
        self.verticalLayout_43.addWidget(self.label_45)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setSpacing(4)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.orders_type_filter_comboBox = QtWidgets.QComboBox(self.frame_36)
        self.orders_type_filter_comboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.orders_type_filter_comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.orders_type_filter_comboBox.setObjectName("orders_type_filter_comboBox")
        self.orders_type_filter_comboBox.addItem("")
        self.orders_type_filter_comboBox.setItemText(0, "")
        self.orders_type_filter_comboBox.addItem("")
        self.orders_type_filter_comboBox.addItem("")
        self.horizontalLayout_25.addWidget(self.orders_type_filter_comboBox)
        self.verticalLayout_43.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_12.addLayout(self.verticalLayout_43)
        self.order_clear_btn = QtWidgets.QPushButton(self.frame_36)
        self.order_clear_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.order_clear_btn.setObjectName("order_clear_btn")
        self.horizontalLayout_12.addWidget(self.order_clear_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem25)
        self.verticalLayout_34.addWidget(self.frame_36)
        self.verticalLayout_20.addWidget(self.frame_35)
        self.orders_tableView = QtWidgets.QTableView(self.frame_12)
        self.orders_tableView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.orders_tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.orders_tableView.setAlternatingRowColors(True)
        self.orders_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.orders_tableView.setObjectName("orders_tableView")
        self.orders_tableView.verticalHeader().setDefaultSectionSize(40)
        self.orders_tableView.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout_20.addWidget(self.orders_tableView)
        self.horizontalLayout_42 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.label_57 = QtWidgets.QLabel(self.frame_12)
        self.label_57.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_57.setStyleSheet("QLabel{\n"
"    color:rgb(244, 154, 32);\n"
"    \n"
"}")
        self.label_57.setObjectName("label_57")
        self.horizontalLayout_42.addWidget(self.label_57)
        self.orders_count_lbl = QtWidgets.QLabel(self.frame_12)
        self.orders_count_lbl.setStyleSheet("QLabel{\n"
"    color:rgb(244, 154, 32);\n"
"    \n"
"}")
        self.orders_count_lbl.setObjectName("orders_count_lbl")
        self.horizontalLayout_42.addWidget(self.orders_count_lbl)
        self.verticalLayout_20.addLayout(self.horizontalLayout_42)
        self.gridLayout_8.addWidget(self.frame_12, 1, 1, 2, 1)
        self.tabWidget.addTab(self.orders_tab, "")
        self.monthly_tab = QtWidgets.QWidget()
        self.monthly_tab.setObjectName("monthly_tab")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.monthly_tab)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setVerticalSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.frame_15 = QtWidgets.QFrame(self.monthly_tab)
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_24.setSpacing(11)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.frame_27 = QtWidgets.QFrame(self.frame_15)
        self.frame_27.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_27.setStyleSheet("#frame_27{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(247,174,0);\n"
"    border-radius:4px;\n"
"    \n"
"}")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_26 = QtWidgets.QLabel(self.frame_27)
        self.label_26.setStyleSheet("QLabel{\n"
"background-color: rgb(244, 154, 32);\n"
"    \n"
"    font: 100 20pt \"Times New Roman\";\n"
"    \n"
" \n"
"}")
        self.label_26.setObjectName("label_26")
        self.verticalLayout_21.addWidget(self.label_26)
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        self.frame_28.setStyleSheet("")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_26.setSpacing(30)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setSpacing(7)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_27 = QtWidgets.QLabel(self.frame_28)
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_27.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_27.setObjectName("label_27")
        self.verticalLayout_22.addWidget(self.label_27)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.monthly_customer_name_filter_txt = QtWidgets.QLineEdit(self.frame_28)
        self.monthly_customer_name_filter_txt.setMinimumSize(QtCore.QSize(300, 40))
        self.monthly_customer_name_filter_txt.setMaximumSize(QtCore.QSize(300, 16777215))
        self.monthly_customer_name_filter_txt.setClearButtonEnabled(True)
        self.monthly_customer_name_filter_txt.setObjectName("monthly_customer_name_filter_txt")
        self.horizontalLayout_3.addWidget(self.monthly_customer_name_filter_txt)
        self.verticalLayout_22.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_26.addLayout(self.verticalLayout_22)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setSpacing(7)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_33 = QtWidgets.QLabel(self.frame_28)
        self.label_33.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_33.setObjectName("label_33")
        self.verticalLayout_29.addWidget(self.label_33)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setSpacing(4)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.monthly_customer_subsState_filter_comboBox = QtWidgets.QComboBox(self.frame_28)
        self.monthly_customer_subsState_filter_comboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.monthly_customer_subsState_filter_comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.monthly_customer_subsState_filter_comboBox.setObjectName("monthly_customer_subsState_filter_comboBox")
        self.horizontalLayout_28.addWidget(self.monthly_customer_subsState_filter_comboBox)
        self.verticalLayout_29.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_26.addLayout(self.verticalLayout_29)
        self.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.verticalLayout_39.setSpacing(7)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.label_34 = QtWidgets.QLabel(self.frame_28)
        self.label_34.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_34.setObjectName("label_34")
        self.verticalLayout_39.addWidget(self.label_34)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setSpacing(4)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.monthly_customer_subsType_filter_comboBox = QtWidgets.QComboBox(self.frame_28)
        self.monthly_customer_subsType_filter_comboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.monthly_customer_subsType_filter_comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.monthly_customer_subsType_filter_comboBox.setObjectName("monthly_customer_subsType_filter_comboBox")
        self.horizontalLayout_29.addWidget(self.monthly_customer_subsType_filter_comboBox)
        self.verticalLayout_39.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_26.addLayout(self.verticalLayout_39)
        self.monthly_customer_clear_btn = QtWidgets.QPushButton(self.frame_28)
        self.monthly_customer_clear_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.monthly_customer_clear_btn.setObjectName("monthly_customer_clear_btn")
        self.horizontalLayout_26.addWidget(self.monthly_customer_clear_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem26)
        self.verticalLayout_21.addWidget(self.frame_28)
        self.verticalLayout_24.addWidget(self.frame_27)
        self.monthly_customers_tableView = QtWidgets.QTableView(self.frame_15)
        self.monthly_customers_tableView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.monthly_customers_tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.monthly_customers_tableView.setAlternatingRowColors(True)
        self.monthly_customers_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.monthly_customers_tableView.setObjectName("monthly_customers_tableView")
        self.monthly_customers_tableView.verticalHeader().setDefaultSectionSize(40)
        self.monthly_customers_tableView.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout_24.addWidget(self.monthly_customers_tableView)
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.label_69 = QtWidgets.QLabel(self.frame_15)
        self.label_69.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_69.setStyleSheet("QLabel{\n"
"    color:rgb(244, 154, 32);\n"
"    \n"
"}")
        self.label_69.setObjectName("label_69")
        self.horizontalLayout_43.addWidget(self.label_69)
        self.monthly_customers_count_lbl = QtWidgets.QLabel(self.frame_15)
        self.monthly_customers_count_lbl.setStyleSheet("QLabel{\n"
"    color:rgb(244, 154, 32);\n"
"    \n"
"}")
        self.monthly_customers_count_lbl.setObjectName("monthly_customers_count_lbl")
        self.horizontalLayout_43.addWidget(self.monthly_customers_count_lbl)
        self.verticalLayout_24.addLayout(self.horizontalLayout_43)
        self.gridLayout_18.addWidget(self.frame_15, 1, 1, 2, 1)
        self.frame_21 = QtWidgets.QFrame(self.monthly_tab)
        self.frame_21.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_21.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_10.setContentsMargins(0, 120, 0, 0)
        self.verticalLayout_10.setSpacing(11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_18 = QtWidgets.QLabel(self.frame_21)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.label_18.setStyleSheet("QLabel{\n"
"border-style: solid;\n"
"border-width: 0px 0px 3px 0px;\n"
"border-bottom-color: rgb(174, 174, 174);\n"
"padding: 2px;\n"
"\n"
"\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_10.addWidget(self.label_18)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_16.setSpacing(7)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_25 = QtWidgets.QLabel(self.frame_21)
        self.label_25.setMinimumSize(QtCore.QSize(200, 0))
        self.label_25.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_25.setStyleSheet("QLabel{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_16.addWidget(self.label_25)
        self.monthly_customer_name_txt = QtWidgets.QLineEdit(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monthly_customer_name_txt.sizePolicy().hasHeightForWidth())
        self.monthly_customer_name_txt.setSizePolicy(sizePolicy)
        self.monthly_customer_name_txt.setMinimumSize(QtCore.QSize(250, 40))
        self.monthly_customer_name_txt.setClearButtonEnabled(True)
        self.monthly_customer_name_txt.setObjectName("monthly_customer_name_txt")
        self.horizontalLayout_16.addWidget(self.monthly_customer_name_txt, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_10.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_29 = QtWidgets.QLabel(self.frame_21)
        self.label_29.setMinimumSize(QtCore.QSize(200, 0))
        self.label_29.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_24.addWidget(self.label_29)
        self.monthly_customer_subscritption_comboBox = QtWidgets.QComboBox(self.frame_21)
        self.monthly_customer_subscritption_comboBox.setMinimumSize(QtCore.QSize(250, 40))
        self.monthly_customer_subscritption_comboBox.setObjectName("monthly_customer_subscritption_comboBox")
        self.monthly_customer_subscritption_comboBox.addItem("")
        self.monthly_customer_subscritption_comboBox.setItemText(0, "")
        self.monthly_customer_subscritption_comboBox.addItem("")
        self.monthly_customer_subscritption_comboBox.addItem("")
        self.monthly_customer_subscritption_comboBox.addItem("")
        self.horizontalLayout_24.addWidget(self.monthly_customer_subscritption_comboBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout_24)
        self.monthly_customer_add_btn = QtWidgets.QPushButton(self.frame_21)
        self.monthly_customer_add_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.monthly_customer_add_btn.setStyleSheet("#monthly_customer_add_btn{\n"
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
"#monthly_customer_add_btn:hover{\n"
"    border-style:  solid;\n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(150,150,150);\n"
"}\n"
"#monthly_customer_add_btn:pressed{\n"
"    border-style:  solid;\n"
"    \n"
"    border-width: 0px;\n"
"    border-radius: 5px;\n"
"    padding: 3px;\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(174,174,174);\n"
"}\n"
"")
        self.monthly_customer_add_btn.setObjectName("monthly_customer_add_btn")
        self.verticalLayout_10.addWidget(self.monthly_customer_add_btn)
        self.gridLayout_18.addWidget(self.frame_21, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.monthly_tab)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_10.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"    \n"
"}")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_18.addWidget(self.label_10, 0, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem27, 2, 0, 1, 1)
        self.tabWidget.addTab(self.monthly_tab, "")
        self.warehouse_tab = QtWidgets.QWidget()
        self.warehouse_tab.setObjectName("warehouse_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.warehouse_tab)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setVerticalSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_39 = QtWidgets.QLabel(self.warehouse_tab)
        self.label_39.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_39.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"\n"
"}")
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_10.addWidget(self.label_39, 0, 1, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.warehouse_tab)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setSpacing(11)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_31 = QtWidgets.QFrame(self.frame_16)
        self.frame_31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_31.setStyleSheet("#frame_31{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(247,174,0);\n"
"    border-radius:4px;\n"
"    \n"
"}")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_35 = QtWidgets.QLabel(self.frame_31)
        self.label_35.setStyleSheet("QLabel{\n"
"background-color: rgb(244, 154, 32);\n"
"    \n"
"    font: 100 20pt \"Times New Roman\";\n"
"    \n"
" \n"
"}")
        self.label_35.setObjectName("label_35")
        self.verticalLayout_32.addWidget(self.label_35)
        self.frame_32 = QtWidgets.QFrame(self.frame_31)
        self.frame_32.setStyleSheet("")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setSpacing(7)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_36 = QtWidgets.QLabel(self.frame_32)
        self.label_36.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_36.setObjectName("label_36")
        self.verticalLayout_33.addWidget(self.label_36)
        self.warehouse_item_name_filter_txt = QtWidgets.QLineEdit(self.frame_32)
        self.warehouse_item_name_filter_txt.setMinimumSize(QtCore.QSize(300, 40))
        self.warehouse_item_name_filter_txt.setMaximumSize(QtCore.QSize(300, 16777215))
        self.warehouse_item_name_filter_txt.setClearButtonEnabled(True)
        self.warehouse_item_name_filter_txt.setObjectName("warehouse_item_name_filter_txt")
        self.verticalLayout_33.addWidget(self.warehouse_item_name_filter_txt)
        self.horizontalLayout_7.addLayout(self.verticalLayout_33)
        self.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.verticalLayout_35.setSpacing(7)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.label_38 = QtWidgets.QLabel(self.frame_32)
        self.label_38.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_38.setObjectName("label_38")
        self.verticalLayout_35.addWidget(self.label_38)
        self.warehouse_item_type_filter_comboBox = QtWidgets.QComboBox(self.frame_32)
        self.warehouse_item_type_filter_comboBox.setMinimumSize(QtCore.QSize(300, 40))
        self.warehouse_item_type_filter_comboBox.setObjectName("warehouse_item_type_filter_comboBox")
        self.verticalLayout_35.addWidget(self.warehouse_item_type_filter_comboBox)
        self.horizontalLayout_7.addLayout(self.verticalLayout_35)
        self.warehouse_clear_btn = QtWidgets.QPushButton(self.frame_32)
        self.warehouse_clear_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.warehouse_clear_btn.setObjectName("warehouse_clear_btn")
        self.horizontalLayout_7.addWidget(self.warehouse_clear_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem28)
        self.verticalLayout_32.addWidget(self.frame_32)
        self.verticalLayout_36.addWidget(self.frame_31)
        self.warehouse_tableView = QtWidgets.QTableView(self.frame_16)
        self.warehouse_tableView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.warehouse_tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.warehouse_tableView.setAlternatingRowColors(True)
        self.warehouse_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.warehouse_tableView.setObjectName("warehouse_tableView")
        self.warehouse_tableView.verticalHeader().setDefaultSectionSize(40)
        self.warehouse_tableView.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout_36.addWidget(self.warehouse_tableView)
        self.gridLayout_10.addWidget(self.frame_16, 1, 1, 3, 1)
        self.frame_24 = QtWidgets.QFrame(self.warehouse_tab)
        self.frame_24.setMaximumSize(QtCore.QSize(0, 400))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem29 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem29)
        self.label_23 = QtWidgets.QLabel(self.frame_24)
        self.label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.label_23.setStyleSheet("QLabel{\n"
"border-style: solid;\n"
"border-width: 0px 0px 3px 0px;\n"
"border-bottom-color: rgb(174, 174, 174);\n"
"padding: 2px;\n"
"\n"
"}")
        self.label_23.setObjectName("label_23")
        self.verticalLayout_11.addWidget(self.label_23)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frame_24)
        self.label_9.setMinimumSize(QtCore.QSize(150, 0))
        self.label_9.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9, 0, QtCore.Qt.AlignLeft)
        self.warehouse_item_name_txt = QtWidgets.QLineEdit(self.frame_24)
        self.warehouse_item_name_txt.setMinimumSize(QtCore.QSize(300, 0))
        self.warehouse_item_name_txt.setClearButtonEnabled(True)
        self.warehouse_item_name_txt.setObjectName("warehouse_item_name_txt")
        self.horizontalLayout_9.addWidget(self.warehouse_item_name_txt)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(150, 0))
        self.label_11.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11, 0, QtCore.Qt.AlignLeft)
        self.warehouse_item_price_txt = QtWidgets.QLineEdit(self.frame_24)
        self.warehouse_item_price_txt.setMinimumSize(QtCore.QSize(150, 0))
        self.warehouse_item_price_txt.setMaximumSize(QtCore.QSize(150, 16777215))
        self.warehouse_item_price_txt.setClearButtonEnabled(True)
        self.warehouse_item_price_txt.setObjectName("warehouse_item_price_txt")
        self.horizontalLayout_13.addWidget(self.warehouse_item_price_txt)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem30)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(150, 0))
        self.label_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.warehouse_item_quantity_txt = QtWidgets.QLineEdit(self.frame_24)
        self.warehouse_item_quantity_txt.setMinimumSize(QtCore.QSize(150, 0))
        self.warehouse_item_quantity_txt.setMaximumSize(QtCore.QSize(150, 16777215))
        self.warehouse_item_quantity_txt.setClearButtonEnabled(True)
        self.warehouse_item_quantity_txt.setObjectName("warehouse_item_quantity_txt")
        self.horizontalLayout_14.addWidget(self.warehouse_item_quantity_txt)
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem31)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_16 = QtWidgets.QLabel(self.frame_24)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(150, 0))
        self.label_16.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_15.addWidget(self.label_16, 0, QtCore.Qt.AlignLeft)
        self.warehouse_item_type_comboBox = QtWidgets.QComboBox(self.frame_24)
        self.warehouse_item_type_comboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.warehouse_item_type_comboBox.setObjectName("warehouse_item_type_comboBox")
        self.warehouse_item_type_comboBox.addItem("")
        self.warehouse_item_type_comboBox.setItemText(0, "")
        self.warehouse_item_type_comboBox.addItem("")
        self.warehouse_item_type_comboBox.addItem("")
        self.horizontalLayout_15.addWidget(self.warehouse_item_type_comboBox)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.warehouse_item_add_btn = QtWidgets.QPushButton(self.frame_24)
        self.warehouse_item_add_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.warehouse_item_add_btn.setShortcut("")
        self.warehouse_item_add_btn.setObjectName("warehouse_item_add_btn")
        self.verticalLayout_11.addWidget(self.warehouse_item_add_btn)
        self.gridLayout_10.addWidget(self.frame_24, 1, 0, 1, 1)
        self.tabWidget.addTab(self.warehouse_tab, "")
        self.reports_tab = QtWidgets.QWidget()
        self.reports_tab.setObjectName("reports_tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.reports_tab)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setVerticalSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_8 = QtWidgets.QLabel(self.reports_tab)
        self.label_8.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"\n"
"}")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_11.addWidget(self.label_8, 0, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.reports_tab)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setSpacing(11)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.frame_34 = QtWidgets.QFrame(self.frame_13)
        self.frame_34.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_34.setStyleSheet("#frame_34{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(247,174,0);\n"
"    border-radius:4px;\n"
"    \n"
"}")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_34)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.label_31 = QtWidgets.QLabel(self.frame_34)
        self.label_31.setStyleSheet("QLabel{\n"
"background-color: rgb(244, 154, 32);\n"
"    \n"
"    font: 100 20pt \"Times New Roman\";\n"
"    \n"
" \n"
"}")
        self.label_31.setObjectName("label_31")
        self.verticalLayout_40.addWidget(self.label_31)
        self.frame_37 = QtWidgets.QFrame(self.frame_34)
        self.frame_37.setStyleSheet("")
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_37)
        self.horizontalLayout_31.setSpacing(30)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.verticalLayout_48 = QtWidgets.QVBoxLayout()
        self.verticalLayout_48.setSpacing(7)
        self.verticalLayout_48.setObjectName("verticalLayout_48")
        self.label_40 = QtWidgets.QLabel(self.frame_37)
        self.label_40.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_40.setObjectName("label_40")
        self.verticalLayout_48.addWidget(self.label_40)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setSpacing(4)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.report_search_type_comboBox = QtWidgets.QComboBox(self.frame_37)
        self.report_search_type_comboBox.setObjectName("report_search_type_comboBox")
        self.report_search_type_comboBox.addItem("")
        self.report_search_type_comboBox.setItemText(0, "")
        self.report_search_type_comboBox.addItem("")
        self.report_search_type_comboBox.addItem("")
        self.report_search_type_comboBox.addItem("")
        self.report_search_type_comboBox.addItem("")
        self.horizontalLayout_32.addWidget(self.report_search_type_comboBox)
        self.verticalLayout_48.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_31.addLayout(self.verticalLayout_48)
        self.report_clear_btn = QtWidgets.QPushButton(self.frame_37)
        self.report_clear_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.report_clear_btn.setObjectName("report_clear_btn")
        self.horizontalLayout_31.addWidget(self.report_clear_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_31.addItem(spacerItem32)
        self.verticalLayout_40.addWidget(self.frame_37)
        self.verticalLayout_42.addWidget(self.frame_34)
        self.reports_tableView = QtWidgets.QTableView(self.frame_13)
        self.reports_tableView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.reports_tableView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.reports_tableView.setAlternatingRowColors(True)
        self.reports_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.reports_tableView.setCornerButtonEnabled(False)
        self.reports_tableView.setObjectName("reports_tableView")
        self.verticalLayout_42.addWidget(self.reports_tableView)
        self.gridLayout_11.addWidget(self.frame_13, 1, 0, 1, 1)
        self.tabWidget.addTab(self.reports_tab, "")
        self.employees_tab = QtWidgets.QWidget()
        self.employees_tab.setObjectName("employees_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.employees_tab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_22 = QtWidgets.QFrame(self.employees_tab)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_22.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_22)
        self.verticalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.verticalLayout_4.setSpacing(11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_19 = QtWidgets.QLabel(self.frame_22)
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setStyleSheet("QLabel{\n"
"border-style: solid;\n"
"border-width: 0px 0px 3px 0px;\n"
"border-bottom-color: rgb(174, 174, 174);\n"
"padding: 2px;\n"
"\n"
"}")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_4.addWidget(self.label_19)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_20 = QtWidgets.QLabel(self.frame_22)
        self.label_20.setMinimumSize(QtCore.QSize(200, 0))
        self.label_20.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_21.addWidget(self.label_20, 0, QtCore.Qt.AlignLeft)
        self.employee_name_txt = QtWidgets.QLineEdit(self.frame_22)
        self.employee_name_txt.setMinimumSize(QtCore.QSize(250, 40))
        self.employee_name_txt.setClearButtonEnabled(True)
        self.employee_name_txt.setObjectName("employee_name_txt")
        self.horizontalLayout_21.addWidget(self.employee_name_txt, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_22)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_18.setSpacing(7)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.employee_manager_btn = QtWidgets.QRadioButton(self.frame_22)
        self.employee_manager_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.employee_manager_btn.setObjectName("employee_manager_btn")
        self.verticalLayout_18.addWidget(self.employee_manager_btn)
        self.employee_worker_btn = QtWidgets.QRadioButton(self.frame_22)
        self.employee_worker_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.employee_worker_btn.setObjectName("employee_worker_btn")
        self.verticalLayout_18.addWidget(self.employee_worker_btn)
        self.horizontalLayout_5.addLayout(self.verticalLayout_18)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_53 = QtWidgets.QLabel(self.frame_22)
        self.label_53.setMinimumSize(QtCore.QSize(200, 0))
        self.label_53.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_53.setObjectName("label_53")
        self.horizontalLayout_40.addWidget(self.label_53, 0, QtCore.Qt.AlignLeft)
        self.employee_gender_comboBox = QtWidgets.QComboBox(self.frame_22)
        self.employee_gender_comboBox.setMinimumSize(QtCore.QSize(250, 40))
        self.employee_gender_comboBox.setObjectName("employee_gender_comboBox")
        self.employee_gender_comboBox.addItem("")
        self.employee_gender_comboBox.addItem("")
        self.horizontalLayout_40.addWidget(self.employee_gender_comboBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_40)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_21 = QtWidgets.QLabel(self.frame_22)
        self.label_21.setMinimumSize(QtCore.QSize(200, 0))
        self.label_21.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_22.addWidget(self.label_21, 0, QtCore.Qt.AlignLeft)
        self.employee_username_txt = QtWidgets.QLineEdit(self.frame_22)
        self.employee_username_txt.setMinimumSize(QtCore.QSize(250, 40))
        self.employee_username_txt.setClearButtonEnabled(True)
        self.employee_username_txt.setObjectName("employee_username_txt")
        self.horizontalLayout_22.addWidget(self.employee_username_txt, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_22 = QtWidgets.QLabel(self.frame_22)
        self.label_22.setMinimumSize(QtCore.QSize(200, 0))
        self.label_22.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_23.addWidget(self.label_22, 0, QtCore.Qt.AlignLeft)
        self.employee_password_txt = QtWidgets.QLineEdit(self.frame_22)
        self.employee_password_txt.setMinimumSize(QtCore.QSize(250, 40))
        self.employee_password_txt.setClearButtonEnabled(True)
        self.employee_password_txt.setObjectName("employee_password_txt")
        self.horizontalLayout_23.addWidget(self.employee_password_txt, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addLayout(self.horizontalLayout_23)
        self.employee_add_btn = QtWidgets.QPushButton(self.frame_22)
        self.employee_add_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.employee_add_btn.setStyleSheet("QPushButton{\n"
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
"}")
        self.employee_add_btn.setObjectName("employee_add_btn")
        self.verticalLayout_4.addWidget(self.employee_add_btn)
        spacerItem33 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem33)
        self.gridLayout_4.addWidget(self.frame_22, 0, 0, 1, 1)
        self.frame_23 = QtWidgets.QFrame(self.employees_tab)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_68 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_68.setSpacing(11)
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.label_55 = QtWidgets.QLabel(self.frame_23)
        self.label_55.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"    \n"
"}")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_68.addWidget(self.label_55)
        self.frame_30 = QtWidgets.QFrame(self.frame_23)
        self.frame_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_30.setStyleSheet("#frame_30{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(247,174,0);\n"
"    border-radius:4px;\n"
"    \n"
"}")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_50 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName("verticalLayout_50")
        self.label_48 = QtWidgets.QLabel(self.frame_30)
        self.label_48.setStyleSheet("QLabel{\n"
"background-color: rgb(244, 154, 32);\n"
"    \n"
"    font: 100 20pt \"Times New Roman\";\n"
"    \n"
" \n"
"}")
        self.label_48.setObjectName("label_48")
        self.verticalLayout_50.addWidget(self.label_48)
        self.frame_38 = QtWidgets.QFrame(self.frame_30)
        self.frame_38.setStyleSheet("")
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_38)
        self.horizontalLayout_37.setSpacing(30)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.verticalLayout_51 = QtWidgets.QVBoxLayout()
        self.verticalLayout_51.setSpacing(7)
        self.verticalLayout_51.setObjectName("verticalLayout_51")
        self.label_49 = QtWidgets.QLabel(self.frame_38)
        self.label_49.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_49.setObjectName("label_49")
        self.verticalLayout_51.addWidget(self.label_49)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_38.setSpacing(4)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.employees_employee_name_filter_txt = QtWidgets.QLineEdit(self.frame_38)
        self.employees_employee_name_filter_txt.setMinimumSize(QtCore.QSize(300, 40))
        self.employees_employee_name_filter_txt.setMaximumSize(QtCore.QSize(300, 16777215))
        self.employees_employee_name_filter_txt.setClearButtonEnabled(True)
        self.employees_employee_name_filter_txt.setObjectName("employees_employee_name_filter_txt")
        self.horizontalLayout_38.addWidget(self.employees_employee_name_filter_txt)
        self.verticalLayout_51.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_37.addLayout(self.verticalLayout_51)
        self.verticalLayout_52 = QtWidgets.QVBoxLayout()
        self.verticalLayout_52.setSpacing(7)
        self.verticalLayout_52.setObjectName("verticalLayout_52")
        self.label_50 = QtWidgets.QLabel(self.frame_38)
        self.label_50.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_50.setObjectName("label_50")
        self.verticalLayout_52.addWidget(self.label_50)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_39.setSpacing(4)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.employees_job_type_filter_comberoBox = QtWidgets.QComboBox(self.frame_38)
        self.employees_job_type_filter_comberoBox.setMinimumSize(QtCore.QSize(300, 40))
        self.employees_job_type_filter_comberoBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.employees_job_type_filter_comberoBox.setObjectName("employees_job_type_filter_comberoBox")
        self.employees_job_type_filter_comberoBox.addItem("")
        self.employees_job_type_filter_comberoBox.setItemText(0, "")
        self.employees_job_type_filter_comberoBox.addItem("")
        self.employees_job_type_filter_comberoBox.addItem("")
        self.horizontalLayout_39.addWidget(self.employees_job_type_filter_comberoBox)
        self.verticalLayout_52.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_37.addLayout(self.verticalLayout_52)
        self.employees_clear_btn = QtWidgets.QPushButton(self.frame_38)
        self.employees_clear_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.employees_clear_btn.setObjectName("employees_clear_btn")
        self.horizontalLayout_37.addWidget(self.employees_clear_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem34)
        self.verticalLayout_50.addWidget(self.frame_38)
        self.verticalLayout_68.addWidget(self.frame_30)
        self.employees_tableView = QtWidgets.QTableView(self.frame_23)
        self.employees_tableView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.employees_tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.employees_tableView.setAlternatingRowColors(True)
        self.employees_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.employees_tableView.setObjectName("employees_tableView")
        self.employees_tableView.verticalHeader().setVisible(False)
        self.verticalLayout_68.addWidget(self.employees_tableView)
        self.gridLayout_4.addWidget(self.frame_23, 0, 1, 1, 1)
        self.tabWidget.addTab(self.employees_tab, "")
        self.offers_tab = QtWidgets.QWidget()
        self.offers_tab.setObjectName("offers_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.offers_tab)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem35, 1, 0, 1, 1)
        self.frame_33 = QtWidgets.QFrame(self.offers_tab)
        self.frame_33.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_46 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_46.setContentsMargins(0, 30, 0, 0)
        self.verticalLayout_46.setSpacing(11)
        self.verticalLayout_46.setObjectName("verticalLayout_46")
        self.label_43 = QtWidgets.QLabel(self.frame_33)
        self.label_43.setMinimumSize(QtCore.QSize(0, 0))
        self.label_43.setStyleSheet("QLabel{\n"
"border-style: solid;\n"
"border-width: 0px 0px 3px 0px;\n"
"border-bottom-color: rgb(174, 174, 174);\n"
"padding: 2px;\n"
"\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_43.setObjectName("label_43")
        self.verticalLayout_46.addWidget(self.label_43)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_44 = QtWidgets.QLabel(self.frame_33)
        self.label_44.setMinimumSize(QtCore.QSize(200, 0))
        self.label_44.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_44.setStyleSheet("QLabel{\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_34.addWidget(self.label_44, 0, QtCore.Qt.AlignLeft)
        self.offer_name_txt = QtWidgets.QLineEdit(self.frame_33)
        self.offer_name_txt.setMinimumSize(QtCore.QSize(250, 40))
        self.offer_name_txt.setMaximumSize(QtCore.QSize(250, 16777215))
        self.offer_name_txt.setClearButtonEnabled(True)
        self.offer_name_txt.setObjectName("offer_name_txt")
        self.horizontalLayout_34.addWidget(self.offer_name_txt, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_46.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_47 = QtWidgets.QLabel(self.frame_33)
        self.label_47.setMinimumSize(QtCore.QSize(200, 0))
        self.label_47.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_47.setObjectName("label_47")
        self.horizontalLayout_35.addWidget(self.label_47, 0, QtCore.Qt.AlignLeft)
        self.offer_price_txt = QtWidgets.QLineEdit(self.frame_33)
        self.offer_price_txt.setMinimumSize(QtCore.QSize(140, 0))
        self.offer_price_txt.setMaximumSize(QtCore.QSize(140, 40))
        self.offer_price_txt.setClearButtonEnabled(True)
        self.offer_price_txt.setObjectName("offer_price_txt")
        self.horizontalLayout_35.addWidget(self.offer_price_txt)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem36)
        self.verticalLayout_46.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_36.setSpacing(10)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_52 = QtWidgets.QLabel(self.frame_33)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QtCore.QSize(200, 0))
        self.label_52.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_52.setObjectName("label_52")
        self.horizontalLayout_36.addWidget(self.label_52)
        self.plus_item_btn = QtWidgets.QPushButton(self.frame_33)
        self.plus_item_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.plus_item_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.plus_item_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 5px;;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding:5px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding:10px;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.plus_item_btn.setText("")
        self.plus_item_btn.setIcon(icon2)
        self.plus_item_btn.setIconSize(QtCore.QSize(50, 50))
        self.plus_item_btn.setObjectName("plus_item_btn")
        self.horizontalLayout_36.addWidget(self.plus_item_btn)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem37)
        self.verticalLayout_46.addLayout(self.horizontalLayout_36)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_33)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollArea_2.setStyleSheet("")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 45, 479))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_41.setContentsMargins(0, 0, 25, 0)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.offers_items_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.offers_items_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.offers_items_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.offers_items_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.offers_items_frame.setObjectName("offers_items_frame")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.offers_items_frame)
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.verticalLayout_41.addWidget(self.offers_items_frame)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_41.addItem(spacerItem38)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_46.addWidget(self.scrollArea_2)
        self.offer_add_btn = QtWidgets.QPushButton(self.frame_33)
        self.offer_add_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.offer_add_btn.setStyleSheet("")
        self.offer_add_btn.setObjectName("offer_add_btn")
        self.verticalLayout_46.addWidget(self.offer_add_btn)
        self.gridLayout_6.addWidget(self.frame_33, 0, 0, 1, 1)
        self.frame_40 = QtWidgets.QFrame(self.offers_tab)
        self.frame_40.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.verticalLayout_54 = QtWidgets.QVBoxLayout(self.frame_40)
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_54.setSpacing(11)
        self.verticalLayout_54.setObjectName("verticalLayout_54")
        self.label_58 = QtWidgets.QLabel(self.frame_40)
        self.label_58.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_58.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"    \n"
"}")
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_54.addWidget(self.label_58)
        self.offers_items_treeView = QtWidgets.QTreeView(self.frame_40)
        self.offers_items_treeView.setObjectName("offers_items_treeView")
        self.verticalLayout_54.addWidget(self.offers_items_treeView)
        self.gridLayout_6.addWidget(self.frame_40, 0, 2, 2, 1)
        self.frame_46 = QtWidgets.QFrame(self.offers_tab)
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.verticalLayout_59 = QtWidgets.QVBoxLayout(self.frame_46)
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_59.setSpacing(11)
        self.verticalLayout_59.setObjectName("verticalLayout_59")
        self.label_59 = QtWidgets.QLabel(self.frame_46)
        self.label_59.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_59.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"    \n"
"}")
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_59.addWidget(self.label_59)
        self.frame_47 = QtWidgets.QFrame(self.frame_46)
        self.frame_47.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_47.setStyleSheet("#frame_47{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(247,174,0);\n"
"    border-radius:4px;\n"
"    \n"
"}")
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.verticalLayout_60 = QtWidgets.QVBoxLayout(self.frame_47)
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName("verticalLayout_60")
        self.label_60 = QtWidgets.QLabel(self.frame_47)
        self.label_60.setStyleSheet("QLabel{\n"
"background-color: rgb(244, 154, 32);\n"
"    \n"
"    font: 100 20pt \"Times New Roman\";\n"
"    \n"
" \n"
"}")
        self.label_60.setObjectName("label_60")
        self.verticalLayout_60.addWidget(self.label_60)
        self.frame_48 = QtWidgets.QFrame(self.frame_47)
        self.frame_48.setStyleSheet("")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.frame_48)
        self.horizontalLayout_46.setSpacing(30)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.verticalLayout_62 = QtWidgets.QVBoxLayout()
        self.verticalLayout_62.setSpacing(7)
        self.verticalLayout_62.setObjectName("verticalLayout_62")
        self.label_62 = QtWidgets.QLabel(self.frame_48)
        self.label_62.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_62.setObjectName("label_62")
        self.verticalLayout_62.addWidget(self.label_62)
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setSpacing(4)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.offers_item_name_filter_txt = QtWidgets.QLineEdit(self.frame_48)
        self.offers_item_name_filter_txt.setMaximumSize(QtCore.QSize(300, 40))
        self.offers_item_name_filter_txt.setClearButtonEnabled(True)
        self.offers_item_name_filter_txt.setObjectName("offers_item_name_filter_txt")
        self.horizontalLayout_48.addWidget(self.offers_item_name_filter_txt)
        self.verticalLayout_62.addLayout(self.horizontalLayout_48)
        self.horizontalLayout_46.addLayout(self.verticalLayout_62)
        self.verticalLayout_61 = QtWidgets.QVBoxLayout()
        self.verticalLayout_61.setSpacing(7)
        self.verticalLayout_61.setObjectName("verticalLayout_61")
        self.label_61 = QtWidgets.QLabel(self.frame_48)
        self.label_61.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_61.setObjectName("label_61")
        self.verticalLayout_61.addWidget(self.label_61)
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setSpacing(4)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.offers_date_filter_dateEdit1 = QtWidgets.QDateEdit(self.frame_48)
        self.offers_date_filter_dateEdit1.setMinimumSize(QtCore.QSize(240, 40))
        self.offers_date_filter_dateEdit1.setCalendarPopup(True)
        self.offers_date_filter_dateEdit1.setObjectName("offers_date_filter_dateEdit1")
        self.horizontalLayout_47.addWidget(self.offers_date_filter_dateEdit1)
        self.verticalLayout_61.addLayout(self.horizontalLayout_47)
        self.horizontalLayout_46.addLayout(self.verticalLayout_61)
        self.offers_clear_btn = QtWidgets.QPushButton(self.frame_48)
        self.offers_clear_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.offers_clear_btn.setObjectName("offers_clear_btn")
        self.horizontalLayout_46.addWidget(self.offers_clear_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_46.addItem(spacerItem39)
        self.verticalLayout_60.addWidget(self.frame_48)
        self.verticalLayout_59.addWidget(self.frame_47)
        self.offers_tableView = QtWidgets.QTableView(self.frame_46)
        self.offers_tableView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.offers_tableView.setFrameShape(QtWidgets.QFrame.Box)
        self.offers_tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.offers_tableView.setAlternatingRowColors(True)
        self.offers_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.offers_tableView.setObjectName("offers_tableView")
        self.offers_tableView.verticalHeader().setDefaultSectionSize(40)
        self.offers_tableView.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout_59.addWidget(self.offers_tableView)
        self.gridLayout_6.addWidget(self.frame_46, 0, 1, 2, 1)
        self.tabWidget.addTab(self.offers_tab, "")
        self.shifts_tab = QtWidgets.QWidget()
        self.shifts_tab.setObjectName("shifts_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.shifts_tab)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_69 = QtWidgets.QFrame(self.shifts_tab)
        self.frame_69.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_69.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.verticalLayout_67 = QtWidgets.QVBoxLayout(self.frame_69)
        self.verticalLayout_67.setContentsMargins(0, 40, 0, 0)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.label_67 = QtWidgets.QLabel(self.frame_69)
        self.label_67.setMinimumSize(QtCore.QSize(0, 0))
        self.label_67.setStyleSheet("QLabel{\n"
"border-style: solid;\n"
"border-width: 0px 0px 3px 0px;\n"
"border-bottom-color: rgb(174, 174, 174);\n"
"padding: 2px;\n"
"\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_67.setObjectName("label_67")
        self.verticalLayout_67.addWidget(self.label_67)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setSpacing(10)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.label_70 = QtWidgets.QLabel(self.frame_69)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy)
        self.label_70.setMinimumSize(QtCore.QSize(200, 0))
        self.label_70.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_70.setObjectName("label_70")
        self.horizontalLayout_52.addWidget(self.label_70)
        self.plus_employee_btn = QtWidgets.QPushButton(self.frame_69)
        self.plus_employee_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.plus_employee_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.plus_employee_btn.setStyleSheet("QPushButton{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding: 5px;;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/plus.svg);\n"
"    \n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding:5px;\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    border-style: solid;    \n"
"    border-width: 5px;\n"
"    border-radius:25px;\n"
"    border-color: rgb(174, 174, 174);\n"
"\n"
"    padding:10px;\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"    image: url(:/icons/icons/plus2.svg);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.plus_employee_btn.setText("")
        self.plus_employee_btn.setIcon(icon2)
        self.plus_employee_btn.setIconSize(QtCore.QSize(50, 50))
        self.plus_employee_btn.setObjectName("plus_employee_btn")
        self.horizontalLayout_52.addWidget(self.plus_employee_btn)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_52.addItem(spacerItem40)
        self.verticalLayout_67.addLayout(self.horizontalLayout_52)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.frame_69)
        self.scrollArea_3.setMinimumSize(QtCore.QSize(500, 400))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_57 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_57.setContentsMargins(0, 0, 25, 0)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName("verticalLayout_57")
        self.shift_employees_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.shift_employees_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shift_employees_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shift_employees_frame.setObjectName("shift_employees_frame")
        self.verticalLayout_98 = QtWidgets.QVBoxLayout(self.shift_employees_frame)
        self.verticalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_98.setSpacing(0)
        self.verticalLayout_98.setObjectName("verticalLayout_98")
        self.verticalLayout_57.addWidget(self.shift_employees_frame)
        spacerItem41 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_57.addItem(spacerItem41)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_67.addWidget(self.scrollArea_3)
        self.shift_add_btn = QtWidgets.QPushButton(self.frame_69)
        self.shift_add_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.shift_add_btn.setStyleSheet("")
        self.shift_add_btn.setObjectName("shift_add_btn")
        self.verticalLayout_67.addWidget(self.shift_add_btn)
        self.gridLayout_7.addWidget(self.frame_69, 0, 0, 1, 1)
        self.frame_50 = QtWidgets.QFrame(self.shifts_tab)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_56 = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_56.setObjectName("verticalLayout_56")
        self.label_63 = QtWidgets.QLabel(self.frame_50)
        self.label_63.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_63.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"    \n"
"}")
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.verticalLayout_56.addWidget(self.label_63)
        self.frame_51 = QtWidgets.QFrame(self.frame_50)
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_63 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_63.setSpacing(11)
        self.verticalLayout_63.setObjectName("verticalLayout_63")
        self.frame_52 = QtWidgets.QFrame(self.frame_51)
        self.frame_52.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_52.setStyleSheet("#frame_52{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: rgb(247,174,0);\n"
"    border-radius:4px;\n"
"    \n"
"}")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.verticalLayout_64 = QtWidgets.QVBoxLayout(self.frame_52)
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName("verticalLayout_64")
        self.label_64 = QtWidgets.QLabel(self.frame_52)
        self.label_64.setStyleSheet("QLabel{\n"
"background-color: rgb(244, 154, 32);\n"
"    \n"
"    font: 100 20pt \"Times New Roman\";\n"
"    \n"
" \n"
"}")
        self.label_64.setObjectName("label_64")
        self.verticalLayout_64.addWidget(self.label_64)
        self.frame_53 = QtWidgets.QFrame(self.frame_52)
        self.frame_53.setStyleSheet("")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.frame_53)
        self.horizontalLayout_49.setSpacing(30)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.verticalLayout_66 = QtWidgets.QVBoxLayout()
        self.verticalLayout_66.setSpacing(7)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.label_66 = QtWidgets.QLabel(self.frame_53)
        self.label_66.setStyleSheet("QLabel{\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.label_66.setObjectName("label_66")
        self.verticalLayout_66.addWidget(self.label_66)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setSpacing(4)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.shifts_date_filter_dateEdit1 = QtWidgets.QDateEdit(self.frame_53)
        self.shifts_date_filter_dateEdit1.setMinimumSize(QtCore.QSize(240, 40))
        self.shifts_date_filter_dateEdit1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.shifts_date_filter_dateEdit1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.shifts_date_filter_dateEdit1.setCalendarPopup(True)
        self.shifts_date_filter_dateEdit1.setObjectName("shifts_date_filter_dateEdit1")
        self.horizontalLayout_51.addWidget(self.shifts_date_filter_dateEdit1)
        self.verticalLayout_66.addLayout(self.horizontalLayout_51)
        self.horizontalLayout_49.addLayout(self.verticalLayout_66)
        self.shifts_clear_btn = QtWidgets.QPushButton(self.frame_53)
        self.shifts_clear_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.shifts_clear_btn.setObjectName("shifts_clear_btn")
        self.horizontalLayout_49.addWidget(self.shifts_clear_btn, 0, QtCore.Qt.AlignBottom)
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem42)
        self.verticalLayout_64.addWidget(self.frame_53)
        self.verticalLayout_63.addWidget(self.frame_52)
        self.shifts_tableView = QtWidgets.QTableView(self.frame_51)
        self.shifts_tableView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.shifts_tableView.setFrameShape(QtWidgets.QFrame.Box)
        self.shifts_tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.shifts_tableView.setAlternatingRowColors(True)
        self.shifts_tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.shifts_tableView.setObjectName("shifts_tableView")
        self.shifts_tableView.verticalHeader().setDefaultSectionSize(40)
        self.shifts_tableView.verticalHeader().setMinimumSectionSize(40)
        self.verticalLayout_63.addWidget(self.shifts_tableView)
        self.verticalLayout_56.addWidget(self.frame_51)
        self.gridLayout_7.addWidget(self.frame_50, 0, 1, 2, 1)
        self.frame_72 = QtWidgets.QFrame(self.shifts_tab)
        self.frame_72.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_72.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.verticalLayout_101 = QtWidgets.QVBoxLayout(self.frame_72)
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_101.setObjectName("verticalLayout_101")
        self.label_68 = QtWidgets.QLabel(self.frame_72)
        self.label_68.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_68.setStyleSheet("QLabel{\n"
"    font: 75 22pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"    padding: 5px;\n"
"    \n"
"    \n"
"}")
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.verticalLayout_101.addWidget(self.label_68)
        self.shifts_supervisors_treeView = QtWidgets.QTreeView(self.frame_72)
        self.shifts_supervisors_treeView.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.shifts_supervisors_treeView.setObjectName("shifts_supervisors_treeView")
        self.verticalLayout_101.addWidget(self.shifts_supervisors_treeView)
        self.gridLayout_7.addWidget(self.frame_72, 0, 2, 2, 1)
        spacerItem43 = QtWidgets.QSpacerItem(20, 731, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem43, 1, 0, 1, 1)
        self.tabWidget.addTab(self.shifts_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1399, 971))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_71 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.employees_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.employees_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.employees_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.employees_frame.setObjectName("employees_frame")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.employees_frame)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem44 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem44, 1, 0, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem45, 0, 1, 1, 1)
        self.employee_detail_frame = QtWidgets.QFrame(self.employees_frame)
        self.employee_detail_frame.setMinimumSize(QtCore.QSize(500, 300))
        self.employee_detail_frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.employee_detail_frame.setStyleSheet("#employee_detail_frame{\n"
"    border-radius:10px;\n"
"    background: rgb(244, 154, 32);\n"
"\n"
"}")
        self.employee_detail_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.employee_detail_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.employee_detail_frame.setObjectName("employee_detail_frame")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.employee_detail_frame)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.verticalLayout_72 = QtWidgets.QVBoxLayout()
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.employee_image_lbl = QtWidgets.QLabel(self.employee_detail_frame)
        self.employee_image_lbl.setMinimumSize(QtCore.QSize(200, 200))
        self.employee_image_lbl.setMaximumSize(QtCore.QSize(200, 200))
        self.employee_image_lbl.setStyleSheet("QLabel{\n"
"    \n"
"    border:2px solid transparent; \n"
"    border-radius: 50px;\n"
"    background-color: transparent;\n"
"\n"
"}")
        self.employee_image_lbl.setText("")
        self.employee_image_lbl.setPixmap(QtGui.QPixmap("../../employees_image/unknown_male.jpg"))
        self.employee_image_lbl.setScaledContents(True)
        self.employee_image_lbl.setObjectName("employee_image_lbl")
        self.verticalLayout_72.addWidget(self.employee_image_lbl)
        self.employee_name_lbl = QtWidgets.QLabel(self.employee_detail_frame)
        self.employee_name_lbl.setStyleSheet("color:rgb(0, 31, 98) ;")
        self.employee_name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.employee_name_lbl.setObjectName("employee_name_lbl")
        self.verticalLayout_72.addWidget(self.employee_name_lbl)
        self.employee_job_type_lbl = QtWidgets.QLabel(self.employee_detail_frame)
        self.employee_job_type_lbl.setStyleSheet("color:rgb(0, 31, 98) ;")
        self.employee_job_type_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.employee_job_type_lbl.setObjectName("employee_job_type_lbl")
        self.verticalLayout_72.addWidget(self.employee_job_type_lbl)
        self.horizontalLayout_27.addLayout(self.verticalLayout_72)
        self.line_4 = QtWidgets.QFrame(self.employee_detail_frame)
        self.line_4.setStyleSheet("border:4px solid rgb(255, 255, 255);\n"
"")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_27.addWidget(self.line_4)
        self.verticalLayout_76 = QtWidgets.QVBoxLayout()
        self.verticalLayout_76.setObjectName("verticalLayout_76")
        self.verticalLayout_73 = QtWidgets.QVBoxLayout()
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName("verticalLayout_73")
        self.label_56 = QtWidgets.QLabel(self.employee_detail_frame)
        self.label_56.setMinimumSize(QtCore.QSize(0, 0))
        self.label_56.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_56.setObjectName("label_56")
        self.verticalLayout_73.addWidget(self.label_56)
        self.employee_username_lbl = QtWidgets.QLabel(self.employee_detail_frame)
        self.employee_username_lbl.setMinimumSize(QtCore.QSize(0, 0))
        self.employee_username_lbl.setMaximumSize(QtCore.QSize(16777215, 40))
        self.employee_username_lbl.setObjectName("employee_username_lbl")
        self.verticalLayout_73.addWidget(self.employee_username_lbl)
        self.verticalLayout_76.addLayout(self.verticalLayout_73)
        self.verticalLayout_74 = QtWidgets.QVBoxLayout()
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName("verticalLayout_74")
        self.label_65 = QtWidgets.QLabel(self.employee_detail_frame)
        self.label_65.setMinimumSize(QtCore.QSize(0, 0))
        self.label_65.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_65.setObjectName("label_65")
        self.verticalLayout_74.addWidget(self.label_65)
        self.employee_password_lbl = QtWidgets.QLineEdit(self.employee_detail_frame)
        self.employee_password_lbl.setMinimumSize(QtCore.QSize(0, 0))
        self.employee_password_lbl.setMaximumSize(QtCore.QSize(16777215, 40))
        self.employee_password_lbl.setStyleSheet("background:transparent;\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.employee_password_lbl.setEchoMode(QtWidgets.QLineEdit.Password)
        self.employee_password_lbl.setReadOnly(True)
        self.employee_password_lbl.setObjectName("employee_password_lbl")
        self.verticalLayout_74.addWidget(self.employee_password_lbl)
        self.verticalLayout_76.addLayout(self.verticalLayout_74)
        self.verticalLayout_75 = QtWidgets.QVBoxLayout()
        self.verticalLayout_75.setSpacing(0)
        self.verticalLayout_75.setObjectName("verticalLayout_75")
        self.label_71 = QtWidgets.QLabel(self.employee_detail_frame)
        self.label_71.setMinimumSize(QtCore.QSize(0, 0))
        self.label_71.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_71.setObjectName("label_71")
        self.verticalLayout_75.addWidget(self.label_71)
        self.employee_num_workdays_lbl = QtWidgets.QLabel(self.employee_detail_frame)
        self.employee_num_workdays_lbl.setMinimumSize(QtCore.QSize(0, 0))
        self.employee_num_workdays_lbl.setMaximumSize(QtCore.QSize(16777215, 40))
        self.employee_num_workdays_lbl.setObjectName("employee_num_workdays_lbl")
        self.verticalLayout_75.addWidget(self.employee_num_workdays_lbl)
        self.verticalLayout_76.addLayout(self.verticalLayout_75)
        self.horizontalLayout_27.addLayout(self.verticalLayout_76)
        self.gridLayout_12.addWidget(self.employee_detail_frame, 0, 0, 1, 1)
        self.verticalLayout_71.addWidget(self.employees_frame)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_9.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout_33.addWidget(self.tabWidget)
        self.verticalLayout_55.addWidget(self.frame_29)
        self.gridLayout.addWidget(self.frame_5, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.buttons_stackedWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)
        self.logout_btn.clicked['bool'].connect(self.daily_btn.setDisabled)
        self.logout_btn.clicked['bool'].connect(self.archive_btn.setDisabled)
        self.logout_btn.clicked['bool'].connect(self.settings_btn.setDisabled)
        self.logout_btn.clicked['bool'].connect(self.exit_btn.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Study Zone"))
        self.daily_customers_btn.setToolTip(_translate("MainWindow", "Daily customers"))
        self.daily_customers_btn.setText(_translate("MainWindow", "Daily Customers"))
        self.monthly_subscrib_btn.setToolTip(_translate("MainWindow", "Monthly customers"))
        self.monthly_subscrib_btn.setText(_translate("MainWindow", "Monthly Customers"))
        self.orders_btn.setToolTip(_translate("MainWindow", "Orders"))
        self.orders_btn.setText(_translate("MainWindow", "Orders"))
        self.warehouse_btn.setToolTip(_translate("MainWindow", "Warehouse"))
        self.warehouse_btn.setText(_translate("MainWindow", "Warehouse"))
        self.reports_btn.setToolTip(_translate("MainWindow", "Reports"))
        self.reports_btn.setText(_translate("MainWindow", "Reports"))
        self.offers_btn.setToolTip(_translate("MainWindow", "Offers"))
        self.offers_btn.setText(_translate("MainWindow", "Offers"))
        self.employees_btn.setToolTip(_translate("MainWindow", "Employees"))
        self.employees_btn.setText(_translate("MainWindow", "Employees"))
        self.shifts_btn.setToolTip(_translate("MainWindow", "Shifts"))
        self.shifts_btn.setText(_translate("MainWindow", "Shifts"))
        self.copy_delete_btn.setToolTip(_translate("MainWindow", "Copy and Delete"))
        self.copy_delete_btn.setText(_translate("MainWindow", "To Archive"))
        self.error_lbl.setText(_translate("MainWindow", "Please start a new shift "))
        self.daily_customer_add_btn2.setToolTip(_translate("MainWindow", "Add customer"))
        self.daily_customer_remove_btn.setToolTip(_translate("MainWindow", "Remove customer"))
        self.daily_customer_add_order.setToolTip(_translate("MainWindow", "Add order"))
        self.daily_customer_search_btn.setToolTip(_translate("MainWindow", "Search date"))
        self.daily_customer_export_btn.setToolTip(_translate("MainWindow", "Export"))
        self.daily_customer_edit_price_btn.setToolTip(_translate("MainWindow", "Edit daily price"))
        self.order_add_btn2.setToolTip(_translate("MainWindow", "Add order"))
        self.order_remove_btn.setToolTip(_translate("MainWindow", "Remove order"))
        self.order_search_btn.setToolTip(_translate("MainWindow", "Search date"))
        self.order_export_btn.setToolTip(_translate("MainWindow", "Export"))
        self.monthly_customer_add_btn2.setToolTip(_translate("MainWindow", "Add customer"))
        self.monthly_customer_remove_btn.setToolTip(_translate("MainWindow", "Remove customer"))
        self.monthly_customer_update_btn.setToolTip(_translate("MainWindow", "Update state"))
        self.monthly_customer_search_btn.setToolTip(_translate("MainWindow", "Search date"))
        self.monthly_customer_export_btn.setToolTip(_translate("MainWindow", "Export"))
        self.monthly_customer_edit_cost_btn.setToolTip(_translate("MainWindow", "Edit monthly price"))
        self.warehouse_item_add_btn2.setToolTip(_translate("MainWindow", "Add item"))
        self.warehouse_item_remove_btn.setToolTip(_translate("MainWindow", "Remove item"))
        self.warehouse_update_current_items_btn.setToolTip(_translate("MainWindow", "Update current items"))
        self.report_remove_btn.setToolTip(_translate("MainWindow", "Remove report"))
        self.report_export_btn.setToolTip(_translate("MainWindow", "Export"))
        self.report_search_btn.setToolTip(_translate("MainWindow", "Search date"))
        self.employee_add_btn2.setToolTip(_translate("MainWindow", "Add supervisor"))
        self.employee_remove_btn.setToolTip(_translate("MainWindow", "Remove supervisor"))
        self.shift_add_btn2.setToolTip(_translate("MainWindow", "Add shift"))
        self.shift_remove_btn.setToolTip(_translate("MainWindow", "Remove shift"))
        self.shift_start_btn.setToolTip(_translate("MainWindow", "Start shift"))
        self.offer_add_btn2.setToolTip(_translate("MainWindow", "Add shift"))
        self.offer_remove_btn.setToolTip(_translate("MainWindow", "Remove shift"))
        self.label_17.setText(_translate("MainWindow", "Created by Eng. Nicola Ibrahim"))
        self.daily_btn.setToolTip(_translate("MainWindow", "Daily"))
        self.archive_btn.setToolTip(_translate("MainWindow", "Archive"))
        self.settings_btn.setToolTip(_translate("MainWindow", "Settings"))
        self.exit_btn.setToolTip(_translate("MainWindow", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main_tab), _translate("MainWindow", "Main page"))
        self.label_6.setText(_translate("MainWindow", "DAILY CUSTOMERS"))
        self.label_5.setText(_translate("MainWindow", "Adding Daily Customer"))
        self.label_12.setText(_translate("MainWindow", "Customer Name"))
        self.label_14.setText(_translate("MainWindow", "Monthly ID"))
        self.label_42.setText(_translate("MainWindow", "Customer type"))
        self.daily_customer_cusType_comboBox.setItemText(1, _translate("MainWindow", "Subscribed to another center"))
        self.daily_customer_add_btn.setText(_translate("MainWindow", "Add"))
        self.daily_customer_add_btn.setShortcut(_translate("MainWindow", "Return"))
        self.label_24.setText(_translate("MainWindow", "Search and Filter"))
        self.label_15.setText(_translate("MainWindow", "By Customer Name"))
        self.label_32.setText(_translate("MainWindow", "By Subscribtion Type"))
        self.daily_customer_subsType_filter_comboBox.setItemText(1, _translate("MainWindow", "Subscribed"))
        self.daily_customer_subsType_filter_comboBox.setItemText(2, _translate("MainWindow", "Not Subscribed"))
        self.daily_customer_subsType_filter_comboBox.setItemText(3, _translate("MainWindow", "Expired"))
        self.daily_customer_subsType_filter_comboBox.setItemText(4, _translate("MainWindow", "Subscribed to another center"))
        self.daily_customer_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label_54.setText(_translate("MainWindow", "Count"))
        self.daily_customers_count_lbl.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.daily_customers_tab), _translate("MainWindow", "Daily customers"))
        self.label.setText(_translate("MainWindow", "ORDERS"))
        self.label_7.setText(_translate("MainWindow", "Adding Order"))
        self.label_3.setText(_translate("MainWindow", "Customer Name"))
        self.label_30.setText(_translate("MainWindow", "Order Type"))
        self.order_sell_type_comboBox.setItemText(0, _translate("MainWindow", "عام"))
        self.order_sell_type_comboBox.setItemText(1, _translate("MainWindow", "ضيافة"))
        self.label_4.setText(_translate("MainWindow", "Add Order"))
        self.plus_order_btn.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.label_28.setText(_translate("MainWindow", "Total price"))
        self.total_price_lbl.setText(_translate("MainWindow", "0"))
        self.order_add_btn.setText(_translate("MainWindow", "Add"))
        self.order_add_btn.setShortcut(_translate("MainWindow", "Return"))
        self.label_37.setText(_translate("MainWindow", "Search and Filter"))
        self.label_41.setText(_translate("MainWindow", "By Customer Name"))
        self.label_45.setText(_translate("MainWindow", "By Order Type"))
        self.orders_type_filter_comboBox.setItemText(1, _translate("MainWindow", "عام"))
        self.orders_type_filter_comboBox.setItemText(2, _translate("MainWindow", "ضيافة"))
        self.order_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label_57.setText(_translate("MainWindow", "Count"))
        self.orders_count_lbl.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.orders_tab), _translate("MainWindow", "Orders"))
        self.label_26.setText(_translate("MainWindow", "Search and Filter"))
        self.label_27.setText(_translate("MainWindow", "By Customer"))
        self.label_33.setText(_translate("MainWindow", "By Subscribtion State"))
        self.label_34.setText(_translate("MainWindow", "By Subscribtion Type"))
        self.monthly_customer_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label_69.setText(_translate("MainWindow", "Count"))
        self.monthly_customers_count_lbl.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Adding Monthly Customer"))
        self.label_25.setText(_translate("MainWindow", "Customer Name"))
        self.label_29.setText(_translate("MainWindow", "Subscription Type"))
        self.monthly_customer_subscritption_comboBox.setItemText(1, _translate("MainWindow", "University fee"))
        self.monthly_customer_subscritption_comboBox.setItemText(2, _translate("MainWindow", "School fee"))
        self.monthly_customer_subscritption_comboBox.setItemText(3, _translate("MainWindow", "VIP"))
        self.monthly_customer_add_btn.setText(_translate("MainWindow", "Add"))
        self.monthly_customer_add_btn.setShortcut(_translate("MainWindow", "Return"))
        self.label_10.setText(_translate("MainWindow", "MONTHLY CUSTOMERS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monthly_tab), _translate("MainWindow", "Monthly customers"))
        self.label_39.setText(_translate("MainWindow", "WAREHOUSE"))
        self.label_35.setText(_translate("MainWindow", "Search and Filter"))
        self.label_36.setText(_translate("MainWindow", "Search By Item"))
        self.label_38.setText(_translate("MainWindow", "Search By Item Type"))
        self.warehouse_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label_23.setText(_translate("MainWindow", "Adding Item"))
        self.label_9.setText(_translate("MainWindow", "Item Name"))
        self.label_11.setText(_translate("MainWindow", "Item Price"))
        self.label_13.setText(_translate("MainWindow", "Quantity"))
        self.label_16.setText(_translate("MainWindow", "Item Type"))
        self.warehouse_item_type_comboBox.setItemText(1, _translate("MainWindow", "Food"))
        self.warehouse_item_type_comboBox.setItemText(2, _translate("MainWindow", "Drink"))
        self.warehouse_item_add_btn.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.warehouse_tab), _translate("MainWindow", "Warehouse"))
        self.label_8.setText(_translate("MainWindow", "REPORTS"))
        self.label_31.setText(_translate("MainWindow", "Search and Filter"))
        self.label_40.setText(_translate("MainWindow", "Search By Report type"))
        self.report_search_type_comboBox.setItemText(1, _translate("MainWindow", "يومي"))
        self.report_search_type_comboBox.setItemText(2, _translate("MainWindow", "شهري"))
        self.report_search_type_comboBox.setItemText(3, _translate("MainWindow", "سنوي"))
        self.report_search_type_comboBox.setItemText(4, _translate("MainWindow", "معدل الزبائن"))
        self.report_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reports_tab), _translate("MainWindow", "Reports"))
        self.label_19.setText(_translate("MainWindow", "Adding Employee"))
        self.label_20.setText(_translate("MainWindow", "Supervisor name"))
        self.label_2.setText(_translate("MainWindow", "Job Type"))
        self.employee_manager_btn.setText(_translate("MainWindow", "Manager"))
        self.employee_worker_btn.setText(_translate("MainWindow", "Employee"))
        self.label_53.setText(_translate("MainWindow", "Gender"))
        self.employee_gender_comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.employee_gender_comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.label_21.setText(_translate("MainWindow", "Username"))
        self.label_22.setText(_translate("MainWindow", "Password"))
        self.employee_add_btn.setText(_translate("MainWindow", "Add"))
        self.label_55.setText(_translate("MainWindow", "EMPLOYEES"))
        self.label_48.setText(_translate("MainWindow", "Search and Filter"))
        self.label_49.setText(_translate("MainWindow", "By Employee Name"))
        self.label_50.setText(_translate("MainWindow", "By Job Type"))
        self.employees_job_type_filter_comberoBox.setItemText(1, _translate("MainWindow", "Manager"))
        self.employees_job_type_filter_comberoBox.setItemText(2, _translate("MainWindow", "Employee"))
        self.employees_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.employees_tab), _translate("MainWindow", "Employees"))
        self.label_43.setText(_translate("MainWindow", "Adding Offer"))
        self.label_44.setText(_translate("MainWindow", "Offer Name"))
        self.label_47.setText(_translate("MainWindow", "Offer Price"))
        self.label_52.setText(_translate("MainWindow", "Add Item"))
        self.plus_item_btn.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.offer_add_btn.setText(_translate("MainWindow", "Add"))
        self.offer_add_btn.setShortcut(_translate("MainWindow", "Return"))
        self.label_58.setText(_translate("MainWindow", "ITEMS"))
        self.label_59.setText(_translate("MainWindow", "OFFERS"))
        self.label_60.setText(_translate("MainWindow", "Search and Filter"))
        self.label_62.setText(_translate("MainWindow", "By Offer Name"))
        self.label_61.setText(_translate("MainWindow", "By Date"))
        self.offers_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.offers_tab), _translate("MainWindow", "Offers"))
        self.label_67.setText(_translate("MainWindow", "Adding Shift"))
        self.label_70.setText(_translate("MainWindow", "Add Employee"))
        self.plus_employee_btn.setShortcut(_translate("MainWindow", "Ctrl+="))
        self.shift_add_btn.setText(_translate("MainWindow", "Add"))
        self.label_63.setText(_translate("MainWindow", "SHIFTS"))
        self.label_64.setText(_translate("MainWindow", "Search and Filter"))
        self.label_66.setText(_translate("MainWindow", "By Date"))
        self.shifts_date_filter_dateEdit1.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.shifts_clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label_68.setText(_translate("MainWindow", "SHIFT EMPLOYEES"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shifts_tab), _translate("MainWindow", "Shifts"))
        self.employee_name_lbl.setText(_translate("MainWindow", "Nicola Ibrahim"))
        self.employee_job_type_lbl.setText(_translate("MainWindow", "Employee"))
        self.label_56.setText(_translate("MainWindow", "username:"))
        self.employee_username_lbl.setText(_translate("MainWindow", "ni"))
        self.label_65.setText(_translate("MainWindow", "password:"))
        self.employee_password_lbl.setText(_translate("MainWindow", "n123"))
        self.label_71.setText(_translate("MainWindow", "Number of workdays:"))
        self.employee_num_workdays_lbl.setText(_translate("MainWindow", "22"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Page"))

from .. import icon_rc
