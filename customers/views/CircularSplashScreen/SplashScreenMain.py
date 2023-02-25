

from PyQt5.QtWidgets import QMainWindow
from customers.ui.CircularSplashScreen.ui_splashScreenUI import Ui_splash_screen


class MainSplash(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_splash_screen()
        self.ui.setupUi(self)
    
        self.show()


