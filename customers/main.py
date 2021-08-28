from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtWidgets

from customers.view import CustomersMainWindow
from customers.ui.LoginDialog.LoginMain import LoginDialog
from customers.database import updateDB

from .database import createConnection
import sys
import os

class Windows():

    def __init__(self, daily_con, archive_con, app):
        
        self.daily_con = daily_con
        self.archive_con = archive_con
        self.app = app

        self.login_win = LoginDialog(self.daily_con)
        self.main_win = CustomersMainWindow(self.daily_con, self.archive_con, self.login_win.getSupervisorJobType())

        self.handleButtons()
        self.initialMainWind()

    def handleButtons(self):
        self.login_win.enter_btn.clicked.connect(self.initialMainWind)
        self.main_win.logout_btn.clicked.connect(self.main_win.hide)


    def initialMainWind(self):
        if(self.login_win.exec_() == QDialog.Accepted):    
    
            self.main_win.show()

        else:
            QtCore.QTimer.singleShot(0, lambda : self.app.exit(1))

def main():

    # Adjust window to screen
    os.environ["QtCore.QT_AUTO_SCREEN_SCALE_FACTOR"] = '1'
    # Enable High DPI display with PyQt5
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
    
    # Create the application
    app = QApplication(sys.argv)


    path = QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.AppDataLocation)
    path = '/'.join(path.split('/')[:-1]) + '/StudyZone/Database'

    # Create Database folder
    if not os.path.exists(path):
        os.makedirs(path)


    # Connect to the database before creating any window
    daily_db_path = path + '/Daily.db'
    archive_db_path = path + '/Archive.db'
    daily_con, archive_con = createConnection(daily_db_path, archive_db_path)
    if not (daily_con and archive_con):
        sys.exit(1)
    

    # Create the main window if the connection succeeded
    login_win = LoginDialog(daily_con)

    # if(login_win.exec_() == QDialog.Accepted):    
    
    #     main_win = CustomersMainWindow(daily_con, archive_con, login_win.getSupervisorJobType())
    #     main_win.show()

   
    # else:
    #     QtCore.QTimer.singleShot(0, lambda : app.exit(1))
    
    main_win = CustomersMainWindow(daily_con, archive_con, login_win.getSupervisorJobType())
    main_win.show()


    # Run the event loop
    sys.exit(app.exec_())