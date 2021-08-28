import typing
from PyQt5 import QtCore, QtSql

class Worker(QtCore.QThread):
    
    finished = QtCore.pyqtSignal()
    row_num_changed = QtCore.pyqtSignal(int)

    def __init__(self, db, table: str, column: str, rows_indices: list, parent: typing.Optional['QtCore.QObject']= None) :
        super().__init__(parent=parent)
        self.db = db
        self.table = table
        self.column = column
        self.rows_indices = rows_indices

    def run(self):
        query = QtSql.QSqlQuery(self.db)
        for index in sorted(self.rows_indices):
            query.exec(f"""DELETE FROM {self.table} WHERE {self.column} = {index.data()}""")
            self.row_num_changed.emit(index.row())
        
        self.finished.emit()

class ReportsWorker(QtCore.QThread):
    
    finished = QtCore.pyqtSignal()
    row_num_changed = QtCore.pyqtSignal(int)

    def __init__(self, db, table: str, column: str, rows_indices: list, parent: typing.Optional['QtCore.QObject']= None) :
        super().__init__(parent=parent)
        self.db = db
        self.table = table
        self.column = column
        self.rows_indices = rows_indices

    def run(self):
        
        query = QtSql.QSqlQuery(self.db)
        for index in sorted(self.rows_indices):
            date = index.data(QtCore.Qt.DisplayRole)
            if(date is not None):
                deleted_date = ''
            # Daily regex
            if(QtCore.QRegularExpression("(\\d{4})-(\\d{2})-(\\d{2})").match(date).hasMatch()):
                deleted_date = date
            
            # Monthly regex
            elif(QtCore.QRegularExpression("^[0|1]?\\d{1}$").match(date).hasMatch()):
                deleted_date = f'%-{date}-%'

            # Yearly regex
            elif(QtCore.QRegularExpression("^\\d{4}$").match(date).hasMatch()):
                deleted_date = f'{date}-%'

            STATEMENT = \
                f"""
                    DELETE FROM {self.table} WHERE {self.column} LIKE '{deleted_date}'
                """
            

            query.exec(STATEMENT)
            self.row_num_changed.emit(index.row())
        self.finished.emit()