from PyQt5 import QtGui, QtWidgets


class CustomImgaeLabel(QtWidgets.QLabel):
    def __init__(self, *args, antialiasing=True, **kwargs):
        super(CustomImgaeLabel, self).__init__(*args, **kwargs)
        self.Antialiasing = antialiasing
        self.setMaximumSize(200, 200)
        self.setMinimumSize(200, 200)
        self.radius = 100 

        self.target = QtGui.QPixmap(self.size())  
        self.target.fill(QtGui.Qt.transparent)   

        # we can delete aspectRationMode to show the entire image
        image = QtGui.QPixmap("customers/ui/MainUI/20170416_113030.jpg").scaled(  
           self.size(), transformMode= QtGui.Qt.SmoothTransformation)
    
        painter = QtGui.QPainter(self.target)
        if self.Antialiasing:
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
            painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)

        path = QtGui.QPainterPath()
        path.addRoundedRect(
            0, 0, self.width(), self.height(), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, image)
        self.setPixmap(self.target)

