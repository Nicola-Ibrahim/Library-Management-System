
from PyQt5 import QtWidgets
from matplotlib import pyplot as plt
from  matplotlib.backends.backend_qt5agg  import  FigureCanvas
from  matplotlib.figure  import  Figure


class MplFrame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.figure = Figure()
        self.figure.set_facecolor("none")
        self.setStyleSheet("background-color:black;")

        self.canvas  =  FigureCanvas(self.figure)

        vertical_layout  =  QtWidgets.QVBoxLayout() 
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes  =  self.canvas.figure.add_subplot(111) 
        self.setLayout(vertical_layout)
