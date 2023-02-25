from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from .Ui_GraphWidgetUI import Ui_Form

import numpy as np
import random
import matplotlib.pyplot as plt

class GraphWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent= None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.uiChanges()
        
    def uiChanges(self):
        # Centrize the dialog
        r = self.geometry()
        r.moveCenter(QtWidgets.QApplication.desktop().availableGeometry().center()) 
        self.setGeometry(r)
        
    
    def draw(self, date, total):
        
        self.MplFrame.canvas.axes.clear()
        self.MplFrame.canvas.axes.bar(date, total, width=0.6) 
        for x, y in zip(date, total):
            self.MplFrame.canvas.axes.text(x, y+10, y)

        # self.MplFrame.canvas.axes.bar_label(total, padding=3) 

        # self.MplFrame.canvas.axes.legend(('cosinus' ,  'sinus' ),loc = 'upper right') 
        self.MplFrame.canvas.axes.set_title('Total Income') 
        # self.MplFrame.canvas.set_xticks(rotation=20)
        self.MplFrame.canvas.draw()

