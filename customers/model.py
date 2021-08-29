from datetime import date
import typing
from PyQt5 import QtCore, QtGui
from customers.database import linkShiftSupervisor, retrieveArchiveDays, retrieveArchiveMonths, retrieveArchiveYears, retrieveDailyId, retrieveItemAvailabelQuantity, retrieveItemId, retrieveShiftsSupervisors, updateSubsState
from PyQt5.QtSql import  QSqlDatabase, QSqlError, QSqlQuery, QSqlTableModel, QSqlQueryModel, QSqlRelationalTableModel, QSqlRelation
from PyQt5.QtCore import QAbstractTableModel, QDate, QLocale, QRegularExpression, Qt



###############################################################
############################ Daily ############################
###############################################################

###################
# Daily customers #
###################
class DailyCustomersModel(QSqlRelationalTableModel):
    """ Daily customers model for controlling all transctions"""
        
    def __init__(self, db: QSqlDatabase, parent: typing.Optional[QtCore.QObject]= None):
        super().__init__(parent=parent, db=db)
        self.db = db
        self.showDailyCustomers()

    def showDailyCustomers(self):

        self.setTable("Daily_customers")
        self.setEditStrategy(QSqlTableModel.OnFieldChange)   
        
        # headers = ('رقم الزبون','اسم الزبون','قيمة القطع','حالة الاشتراك الشهري','انتهاء الاشتراك الشهري','التاريخ')
        headers = ('Id','Name','Fee','Monthly subscription state','End monthly subscription','Date')
        for ind, header in enumerate(headers):
            self.setHeaderData(ind, Qt.Horizontal,header)
        
        self.setJoinMode(self.LeftJoin)
        self.setRelation(self.fieldIndex("monthly_id"), QSqlRelation("Monthly_customers", "monthly_id", "end_date"))
        self.setSort(self.fieldIndex("daily_id"), Qt.AscendingOrder)
        self.select()

    def addDailyCustomer(self, data : list) -> bool:

        # Check if the the customer exists previously
        result = None
        STATEMENT = f"""
            SELECT count(*) FROM Daily_customers WHERE daily_name='{data[0]}' AND daily_date = date('now')
        """

        query = QSqlQuery(db= self.db)
        query.exec(STATEMENT)
       
        # Take the last recorde
        if(query.first() == True):
            result = query.value(0)

        # If the record doesn't exist then insert it
        if(result == 0):
            
            # Insert new row
            row = self.rowCount()
            self.insertRows(row, 1)

            # Take only the colums that suitable for data list length
            columns = ['daily_name','subscription_state', 'end_date']

            for col_ind, field in enumerate(data):
                col = self.fieldIndex(columns[col_ind])
                self.setData(self.index(row, col), field, Qt.EditRole)            

                
            # Submit all changes
            ret = self.submitAll()
            self.select()

            return ret
        
        return False
   
    def data(self, index, role) -> None:
        
        if not index.isValid():
            return None

        # if(role == Qt.FontRole):
        #     return QtGui.QFont("Times", 10, QtGui.QFont.Bold)
        
        if(role == Qt.TextAlignmentRole):
            return Qt.AlignHCenter


        if(role == Qt.BackgroundColorRole):
            if(super().data(index, Qt.DisplayRole) in ['Subscribed','Subscribed to another center']):
                return QtGui.QColor(0,255,0,150)

            elif(super().data(index, Qt.DisplayRole) in ['Expired','Not Subscribed']):
                return QtGui.QColor(245,170,0,150)

        
        return super().data(index, role)

    def flags(self, index: QtCore.QModelIndex):
        col = index.column()

        if(self.db.databaseName().split('/')[-1] == 'Daily.db'):
            if (col in [self.fieldIndex('daily_id'), 
                        self.fieldIndex('daily_ticket_cost'),
                        self.fieldIndex('daily_date')]):
                return  Qt.ItemIsSelectable | Qt.ItemIsEnabled
        
        if(self.db.databaseName().split('/')[-1] == 'Archive.db'):
            if (col in [self.fieldIndex('daily_id'), 
                        self.fieldIndex('daily_name'),
                        self.fieldIndex('daily_ticket_cost'),
                        self.fieldIndex('subscription_state'),
                        self.fieldIndex('end_date'), 
                        self.fieldIndex('daily_date')]):
                return  Qt.ItemIsSelectable | Qt.ItemIsEnabled
        

        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable)
    
class DailyCustomersSortModel(QtCore.QSortFilterProxyModel):
    """ Daily customers sorting model"""
    def __init__(self, source_model, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._customer_name_pattern = QRegularExpression()
        self._customer_subsState_pattern =  QRegularExpression()
        self._date_pattern = QRegularExpression()
        
        # Set source model
        self.setSourceModel(source_model)
    
    def setCustomerNameFilter(self, string):
        """Set regex for customer name"""
        self._customer_name_pattern.setPattern(f'{string}')
        self.invalidateFilter()

    def setSubsStateFilter(self, string):
        """Set regex pattern for subscription type"""
        if(string == ''):
            self._customer_subsState_pattern.setPattern(f'')
        else:
            self._customer_subsState_pattern.setPattern(f'^{(string)}$')
            
        self.invalidateFilter()

    def setDateFilter(self, string):
        """Set regex pattern for date type"""   
        self._date_pattern.setPattern(string)
        self.invalidateFilter()
    
    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex):
        
        customer_name_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('daily_name'), source_parent)
        subs_state_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('subscription_state'), source_parent)
        date_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('daily_date'),  source_parent)

        customer_name = self.sourceModel().data(customer_name_index, Qt.DisplayRole)
        subs_state = self.sourceModel().data(subs_state_index, Qt.DisplayRole)
        date = self.sourceModel().data(date_index, Qt.DisplayRole)

        tests =  [
            self._customer_name_pattern.match(customer_name).hasMatch(),
            self._customer_subsState_pattern.match(subs_state).hasMatch(),
            self._date_pattern.match(date).hasMatch()    
        ]
        
        return (not False in tests)


#####################
# Monthly customers #
#####################
class MonthlyCustomersModel(QSqlTableModel):
    """ Monthly customers model for controlling all transctions"""

    def __init__(self, db: QSqlDatabase, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent, db=db)
        self.db = db
        self.showMonthlyCustomers()
    
    def showMonthlyCustomers(self):
        # Update monthly subscribtion state before SELECT  
        updateSubsState(db = self.db)

        self.setTable("Monthly_customers")
        self.setEditStrategy(self.OnFieldChange)
        
        # headers = ('رقم الزبون','اسم الزبون','قيمة الاشتراك','البدء','الانتهاء','الحالة','النوع')
        headers = ('Id','Name','Subscription fee','Starting','Ending','State','Type')
        for ind, header in enumerate(headers):
            self.setHeaderData(ind, Qt.Horizontal,header)
        
        self.setSort(self.fieldIndex("monthly_id"), Qt.AscendingOrder)
        self.select()
        
    def addMonthlyCustomer(self, data : str):
        
        # Check if the the customer exists previously
        result = None
        STATEMENT = f"""
            SELECT count(*) FROM Monthly_customers WHERE monthly_name='{data[0]}'
        """

        query = QSqlQuery(db= self.db)
        query.exec(STATEMENT)
       
        # Take the last recorde
        if(query.first() == True):
            result = query.value(0)

        # If the record doesn't exist then insert it
        if(result == 0):
            
            # Get Available ids for inserting
            table_ids = []
            STATEMENT = f"""
                SELECT monthly_id FROM Monthly_customers
            """

            query = QSqlQuery(db = self.db)
            query.exec(STATEMENT)
            while (query.next()):
                table_ids.append(query.value(0))
            
            if(len(table_ids) > 2):
                table_ids = set(table_ids) # ids in the monthly table
                ids = set(list(range(min(table_ids),max(table_ids)+1))) # range from min to max ids

                # Take the difference between two sets to get available ids to use
                available_ids = list(ids.difference(table_ids))

                # Change data sturcture by adding id field value
                columns = ['monthly_id', 'monthly_name' , 'subsription_type']
                data = [str(available_ids[0])]+ data

            else:
                columns = ['monthly_name' , 'subsription_type']

            record = self.record()

            # Take only the colums that suitable for data list length
            for col_ind, field in enumerate(data):
                col = record.indexOf(columns[col_ind])
                record.setValue(col, field)

            self.insertRecord(-1,record)

            # Submit all changes
            ret = self.submitAll()
            self.select()
            return ret
        
        return False
       
    def data(self, index: QtCore.QModelIndex, role: int):
        row = index.row()
        col = index.column()

        
        if(role == Qt.TextAlignmentRole):
            return Qt.AlignHCenter


        if(role == Qt.BackgroundColorRole):
            if(super().data(index, Qt.DisplayRole) == 'Subscribed'):
                return QtGui.QColor(0,255,0,150)

            elif(super().data(index, Qt.DisplayRole) in ['Expired','Not Subscribed']):
                return QtGui.QColor(255,0,0,150)

        return super().data(index, role=role)

    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        col = index.column()

        if(self.db.databaseName().split('/')[-1] == 'Daily.db'):
            if (col in [ 
                        self.fieldIndex('ticket_monthly_cost'),
                        self.fieldIndex('start_date'),
                        self.fieldIndex('end_date'), self.fieldIndex('subscribtion_state')]):
                return  Qt.ItemIsSelectable | Qt.ItemIsEnabled
        
        elif(self.db.databaseName().split('/')[-1] == 'Archive.db'):
            if (col in [
                        self.fieldIndex('monthly_name'),
                        self.fieldIndex('ticket_monthly_cost'),
                        self.fieldIndex('start_date'),
                        self.fieldIndex('end_date'), 
                        self.fieldIndex('subscribtion_state')]):
                return  Qt.ItemIsSelectable | Qt.ItemIsEnabled

        return super().flags(index)

class MonthlyCustomersSortModel(QtCore.QSortFilterProxyModel):
    """ Monthly customers sorting model"""
    def __init__(self, source_model, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._customer_name_pattern = QRegularExpression()
        self._customer_subsState_pattern =  QRegularExpression()
        self._customer_subsType_pattern =  QRegularExpression()
        self._date_pattern = QRegularExpression()
        
        # Set source model
        self.setSourceModel(source_model)
    
    def setCustomerNameFilter(self, string):
        """Set regex for customer name"""
        self._customer_name_pattern.setPattern('{}'.format(string))
        self.invalidateFilter()

    def setSubsStateFilter(self, string):
        """Set regex pattern for subscription type"""
        self._customer_subsState_pattern.setPattern(f'^{string}')
            
        self.invalidateFilter()

    def setSubsTypeFilter(self, string):
        """Set regex pattern for subscription type"""
        self._customer_subsType_pattern.setPattern(f'^{string}')
            
        self.invalidateFilter()

    def setDateFilter(self, string):
        """Set regex pattern for date type"""   
        self._date_pattern.setPattern(string)
        self.invalidateFilter()
    
    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex) -> bool:
        
        customer_name_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('monthly_name'), source_parent)
        date_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('start_date'),  source_parent)
        subs_state_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('subscribtion_state'), source_parent)
        subs_type_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('subsription_type'), source_parent)

        customer_name = self.sourceModel().data(customer_name_index, Qt.DisplayRole)
        date = self.sourceModel().data(date_index, Qt.DisplayRole)
        subs_state = self.sourceModel().data(subs_state_index, Qt.DisplayRole)
        subs_type = self.sourceModel().data(subs_type_index, Qt.DisplayRole)

        tests =  [
            self._customer_name_pattern.match(customer_name).hasMatch(),
            self._customer_subsState_pattern.match(subs_state).hasMatch(),
            self._customer_subsType_pattern.match(subs_type).hasMatch(),
            self._date_pattern.match(date).hasMatch(),
        ]
        
        return (not False in tests)


##########
# Orders #
##########
class OrdersModel(QSqlRelationalTableModel):

    """ Orders model for controlling all transctions"""

    def __init__(self, db: QSqlDatabase, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent, db=db)
        self.db = db
        self.showOrders()
    
    def showOrders(self):

        self.setTable("Orders")
        self.setEditStrategy(self.OnFieldChange)
        
        # headers = ('رقم الطلب','اسم الزبون','اسم المادة','الكمية','الاجمالي','النوع','التاريخ')
        # headers = ('Id','Customer name','Item name','Quantity','Total','Type','offer_id','Date')
        headers = ('Id','Customer name','Total','Type','Date')
        for ind, header in enumerate(headers):
            self.setHeaderData(ind, Qt.Horizontal,header)
        
        self.setJoinMode(self.LeftJoin)
        self.setRelation(self.fieldIndex("daily_customer_id"), QSqlRelation("Daily_customers", "daily_id", "daily_name"))
        self.setSort(self.fieldIndex("order_id"), Qt.AscendingOrder)
        self.select()
        
    def addOrder(self, data : list):

        customer_id = retrieveDailyId(data[0][0], self.db)
        order_type = data[0][3]
        
        # Itereate to check if any order doesn't verify available quantity in the Warehouse
        for i in range(len(data)):
            item_id = retrieveItemId(data[i][1], self.db)
            quantity = data[i][2]

            # Handle exceed quantity error
            available = retrieveItemAvailabelQuantity(item_id, self.db)
            if(quantity > available):
                # Set SQL Error
                self.setLastError(QSqlError(driverText=f'exceed the available quantity\n{available}'))
                return
            

        for i in range(len(data)):
            item_id = retrieveItemId(data[i][1], self.db)
            quantity = data[i][2]

            # record2 = [customer_id, item_id, quantity, order_type]
            record2 = [customer_id, order_type]
            
            # Set SQL Error to Null
            self.setLastError(QSqlError(driverText=''))

            # Insert new row
            row = self.rowCount()
            self.insertRows(row, 1)

            # Take only the colums that suitable for data list length
            columns = ['daily_name', 'order_type']

            for col_ind, field in enumerate(record2):
                col = self.fieldIndex(columns[col_ind])
                self.setData(self.index(row, col), field, Qt.EditRole)
                
            # Submit all changes
            self.submitAll()
            self.select()

            # Link order with related items and offer
            
            
    def data(self, index: QtCore.QModelIndex, role: int) -> None:
       
        if(role == Qt.TextAlignmentRole):
            return Qt.AlignHCenter

        return super().data(index, role=role)

    def flags(self, index: QtCore.QModelIndex) -> QtCore.Qt.ItemFlags:
        col = index.column()

        if(self.db.databaseName().split('/')[-1] == 'Daily.db'):
            if (col in [self.fieldIndex('order_id'),
                        self.fieldIndex('total_price'),
                        self.fieldIndex('order_date')]):
                return  Qt.ItemIsSelectable | Qt.ItemIsEnabled
        
        elif(self.db.databaseName().split('/')[-1] == 'Archive.db'):
            if (col in [self.fieldIndex('order_id'),
                        self.fieldIndex('daily_name'),
                        self.fieldIndex('total_price'),
                        self.fieldIndex('order_type'),
                        self.fieldIndex('order_date')]):
                return  Qt.ItemIsSelectable | Qt.ItemIsEnabled

        return super().flags(index)

class OrdersSortModel(QtCore.QSortFilterProxyModel):
    """ Orders sorting model"""
    def __init__(self, source_model, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._customer_name_pattern = QRegularExpression()
        self._item_type_pattern = QRegularExpression()
        self._date_pattern = QRegularExpression()
        
        # Set source model
        self.setSourceModel(source_model)
    
    def setCustomerNameFilter(self, string):
        """Set regex for customer name"""
        self._customer_name_pattern.setPattern('{}'.format(string))
        self.invalidateFilter()


    def setItemTypeFilter(self, string):
        """Set regex pattern for subscription type"""
        self._item_type_pattern.setPattern(f'^{string}')
            
        self.invalidateFilter()
    
    def setDateFilter(self, string):
        """Set regex pattern for subscription type"""
        self._date_pattern.setPattern(string)
            
        self.invalidateFilter()

    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex) -> bool:
        
        customer_name_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('daily_name'), source_parent)
        order_type_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('order_type'), source_parent)
        date_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('order_date'), source_parent)

        customer_name = None
        order_type = self.sourceModel().data(order_type_index, Qt.DisplayRole)
        date = self.sourceModel().data(date_index, Qt.DisplayRole)

        if(isinstance(self.sourceModel().data(customer_name_index, Qt.DisplayRole), str)):  
            customer_name = str(self.sourceModel().data(customer_name_index, Qt.DisplayRole))
        
        tests =  [
            self._customer_name_pattern.match(customer_name).hasMatch(),
            self._item_type_pattern.match(order_type).hasMatch(),
            self._date_pattern.match(date).hasMatch()
        ]
        
        return (not False in tests)


#############
# Warehouse #
#############
class WarehouseModel(QSqlTableModel):
    """ Warehouse model for controlling all transctions"""
    def __init__(self, db: QSqlDatabase, parent: typing.Optional[QtCore.QObject] = None) -> None:
        super().__init__(parent=parent, db=db)
        self.db = db
        self.showItems()
    
    def showItems(self):
        self.setTable("Warehouse")
        self.setEditStrategy(self.OnFieldChange)
        
        # headers = ('رقم المادة','اسم المادة','سعر الافرادي','نوع المادة','الكمية المخزنة','الكمية اليومية المستهلكة')
        headers = ('Id','Name','Unit price','Type','Current Quantity','Consumed quantity')
        for ind, header in enumerate(headers):
            self.setHeaderData(ind, Qt.Horizontal,header)
                
        self.setSort(self.fieldIndex("item_id"), Qt.AscendingOrder)
        self.select()
        
    def addItem(self, data : list):
        

        # Check if the the item exists previously
        result = None
        STATEMENT = f"""
            SELECT count(*) FROM Warehouse WHERE item_name='{data[0]}'
        """

        query = QSqlQuery(self.db)
        query.exec(STATEMENT)
       
        # Take the last recorde
        if(query.first() == True): 
            result = query.value(0)
        
        # If the record doesn't exist then insert it 
        if(result == 0):

            # Insert new row
            row = self.rowCount()
            self.insertRows(row, 1)

            # Take only the colums that suitable for data list length
            columns = ['item_name', 'item_price','item_type','current_items_quantity']

            for col_ind, field in enumerate(data):
                col = self.fieldIndex(columns[col_ind])
                self.setData(self.index(row, col), field, Qt.EditRole)
                
            # Submit all changes
            ret = self.submitAll()
            self.select()

            return ret
    
        return False

    def data(self, index: QtCore.QModelIndex, role: int):
        if(role == Qt.TextAlignmentRole):
            return Qt.AlignHCenter

        elif(role == Qt.BackgroundColorRole):
            
            if(index.column()==4 and super().data(index, Qt.DisplayRole) in [0]):
                return QtGui.QColor(255,0,0,150)

        return super().data(index, role=role)

class WarehouseSortModel(QtCore.QSortFilterProxyModel):
    """ Warehouse sorting model"""
    def __init__(self, source_model, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._item_name_pattern =  QRegularExpression()
        self._item_type_pattern = QRegularExpression()
        
        # Set source model
        self.setSourceModel(source_model)
    

    def setItemNameFilter(self, string):
        """Set regex pattern for subscription type"""
        self._item_name_pattern.setPattern(string)
        self.invalidateFilter()

    def setItemTypeFilter(self, string):
        """Set regex pattern for subscription type"""
        self._item_type_pattern.setPattern(f'^{string}')
            
        self.invalidateFilter()
    

    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex) -> bool:
        
        item_name_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('item_name'),  source_parent)
        item_type_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('item_type'), source_parent)

        item_name = self.sourceModel().data(item_name_index, Qt.DisplayRole)
        item_type = self.sourceModel().data(item_type_index, Qt.DisplayRole)

        tests =  [
            self._item_name_pattern.match(item_name).hasMatch(),
            self._item_type_pattern.match(item_type).hasMatch(),
        ]
        
        return (not False in tests)

##########
# Offers #
##########
class OffersModel(QSqlTableModel):
    """ Offers model for controlling all transctions"""
    def __init__(self, db: QSqlDatabase, parent: typing.Optional[QtCore.QObject] = None) -> None:
        super().__init__(parent=parent, db=db)
        self.db = db
        self.showOffers()
    
    def showOffers(self):
        self.setTable("Offers")
        self.setEditStrategy(self.OnFieldChange)
        
        headers = ('Id','Name','Price','Date')
        for ind, header in enumerate(headers):
            self.setHeaderData(ind, Qt.Horizontal,header)
                
        self.setSort(self.fieldIndex("offer_id"), Qt.AscendingOrder)
        self.select()
        
    def addOffer(self, data : list):
    
        # Insert new row
        row = self.rowCount()
        self.insertRows(row, 1)

        columns = ['offer_name', 'offer_price']

        # Take only the colums that suitable for data list length
        for col_ind, field in enumerate(data):
            col = self.fieldIndex(columns[col_ind])
            self.setData(self.index(row, col), field, Qt.EditRole)

        # Submit all changes
        ret = self.submitAll()

        # Link offer with related items

        self.select()

        return ret
    
    def data(self, index: QtCore.QModelIndex, role: int):
        if(role == Qt.TextAlignmentRole):
            return Qt.AlignHCenter

        return super().data(index, role=role)

class OffersSortModel(QtCore.QSortFilterProxyModel):
    """ Offers sorting model"""
    
    def __init__(self, source_model, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._item_name_pattern =  QRegularExpression()
        self._date_pattern = QRegularExpression()
        
        # Set source model
        self.setSourceModel(source_model)
    

    def setItemNameFilter(self, string):
        """Set regex pattern for subscription type"""
        self._item_name_pattern.setPattern(string)
        self.invalidateFilter()

    def setDateFilter(self, date):
        """Set regex pattern for date type""" 
        if(date == ''):
            self._date_pattern.setPattern('')
            
        else:
            date = QLocale(QLocale.English, QLocale.UnitedStates).toString(date, "yyyy-MM-dd")
            self._date_pattern.setPattern(date)

        self.invalidateFilter()
    
    

    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex) -> bool:
        
        offer_name_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('offer_name'),  source_parent)
        date_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('offer_date'),  source_parent)

        offer_name = self.sourceModel().data(offer_name_index, Qt.DisplayRole)
        date = self.sourceModel().data(date_index, Qt.DisplayRole)

        tests =  [
            self._item_name_pattern.match(offer_name).hasMatch(),
            self._date_pattern.match(date).hasMatch()
        ]
        
        return (not False in tests)
 


###############
# Supervisors #
###############
class EmployeesModel(QSqlRelationalTableModel):
    """ Supervisors model for controlling all transctions"""
    def __init__(self, db: QSqlDatabase, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent, db=db)
        self.db = db
        self.showEmployees()
    
    def showEmployees(self):
        self.setTable("Supervisors")
        self.setEditStrategy(self.OnFieldChange)
        
        # headers = ('رقم المشرف','اسم المشرف','طبيعة العمل','اسم المستخدم','كلمة السر')
        headers = ('Id','Name','Job type','Username','password','Number workdays', 'Idle shift')
        for ind, header in enumerate(headers):
            self.setHeaderData(ind, Qt.Horizontal,header)

        self.setJoinMode(self.LeftJoin)
        self.setRelation(self.fieldIndex("shift_id"), QSqlRelation("Shifts", "shift_id", "box"))
        self.setSort(self.fieldIndex("supervisor_id"), Qt.AscendingOrder)

        self.select()
        
    def addEmployee(self, data : list):

        # Check if the the supervisor exists previously
        result = None
        STATEMENT = f"""
            SELECT count(*) FROM Supervisors WHERE supervisor_name='{data[0]}'
        """

        query = QSqlQuery(db=self.db)
        query.exec(STATEMENT)
       
        # Take the last recorde
        if(query.first() == True):
            result = query.value(0)
        
        
        # If the record doesn't exist then insert it 
        if(result == 0):

            # Insert new row
            row = self.rowCount()
            self.insertRows(row, 1)

            # Take only the colums that suitable for data list length
            columns = ['supervisor_name','job_type','username','password']

            for col_ind, field in enumerate(data):
                col = self.fieldIndex(columns[col_ind])
                self.setData(self.index(row, col), field, Qt.EditRole)
                
            # Submit all changes
            ret = self.submitAll()
            self.select()

            return ret
        
        return False

    def data(self, index: QtCore.QModelIndex, role: int):

        if not index.isValid():
            return None

        elif(role == Qt.BackgroundColorRole):
            if(index.column()==self.fieldIndex('current_items_quantity') and super().data(index, Qt.DisplayRole) in [1]):
                return QtGui.QColor(0,255,0,150)

            elif(index.column()==self.fieldIndex('current_items_quantity') and super().data(index, Qt.DisplayRole) in [0]):
                return QtGui.QColor(255,0,0,150)
                
        return super().data(index, role=role)  

class  EmployeesSortModel(QtCore.QSortFilterProxyModel):
    """ Daily customers sorting model"""
    def __init__(self, source_model, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._employee_name_pattern = QRegularExpression()
        self._employee_job_type_pattern =  QRegularExpression()
        # self._date_pattern = QRegularExpression()
        
        # Set source model
        self.setSourceModel(source_model)
    
    def setEmployeeNameFilter(self, string):
        """Set regex for customer name"""
        self._employee_name_pattern.setPattern(f'{string}')
        self.invalidateFilter()

    def setJobTypeFilter(self, string):
        """Set regex pattern for subscription type"""
        self._employee_job_type_pattern.setPattern(f'^{(string)}')
            
        self.invalidateFilter()

    
    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex):
        
        supervisor_name_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('supervisor_name'), source_parent)
        job_type_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('job_type'), source_parent)

        supervisor_name = self.sourceModel().data(supervisor_name_index, Qt.DisplayRole)
        job_type = self.sourceModel().data(job_type_index, Qt.DisplayRole)

        tests =  [
            self._employee_name_pattern.match(supervisor_name).hasMatch(),
            self._employee_job_type_pattern.match(job_type).hasMatch(),
        ]
        
        return (not False in tests)

##########
# Shifts #
##########
class ShiftsModel(QSqlTableModel):
    """Shifts model for controlling all transctions"""

    def __init__(self, db: QSqlDatabase, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent, db=db)
        self.db = db
        self._ADD_FLAG = False
        self.showShifts()

    def showShifts(self):
        self.setTable("Shifts")
        self.setEditStrategy(self.OnFieldChange)
        
        headers = ('Id','Name', 'Start','Finish', 'duration', 'Income', 'State', 'Date')
        for ind, header in enumerate(headers):
            self.setHeaderData(ind, Qt.Horizontal,header)
        
        self.setSort(self.fieldIndex("shift_date"), Qt.DescendingOrder)
        self.select()
    
    def addShift(self, data : list):
        
        self._ADD_FLAG = True
        # INSERT INTO Shifts (supervisor_id) 
        # SELECT 3 WHERE NOT EXISTS (SELECT supervisor_id FROM Shifts WHERE supervisor_id = 3 AND date=date('now'));

        # Insert new row
        row = self.rowCount()
        self.insertRows(row, 1)

        # Take only the colums that suitable for data list length
        columns = ['shift_state']
        state_value = ['Inactive']

        for col_ind, field in enumerate(state_value):
            col = self.fieldIndex(columns[col_ind])
            self.setData(self.index(row, col), field, Qt.EditRole)
        
        # Submit all changes
        ret = self.submitAll()

        # Link the new shift whith related employees
        shift_id = self.query().lastInsertId()
        for supervisor_name in data:
            linkShiftSupervisor(shift_id, supervisor_name, db = self.db)


        self.select()

        self._ADD_FLAG = False

        return ret
 
    def data(self, index, role) -> None:
        
        if not index.isValid():
            return None

        # if(role == Qt.FontRole):
        #     return QtGui.QFont("Times", 10, QtGui.QFont.Bold)
        
        if(role == Qt.TextAlignmentRole):
            return Qt.AlignHCenter


        if(role == Qt.BackgroundColorRole):
            if(super().data(index, Qt.DisplayRole) == 'Active'):
                return QtGui.QColor(0,255,0,150)

            elif(index.column()==self.fieldIndex('shift_state') and super().data(index, Qt.DisplayRole) == 'Inactive'):
                return QtGui.QColor(255,0,0,150)
            
            elif(index.column()==self.fieldIndex('shift_state') and super().data(index, Qt.DisplayRole) == 'Finished'):
                return QtGui.QColor(0,0,255,150)

        
        return super().data(index, role)

    def flags(self, index: QtCore.QModelIndex):
        if(self._ADD_FLAG):
            return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsEnabled|Qt.ItemIsSelectable|Qt.ItemIsEditable)
        
        else:
            return Qt.ItemFlags(QAbstractTableModel.flags(self, index) | Qt.ItemIsSelectable | Qt.ItemIsEnabled)

class  ShiftsSortModel(QtCore.QSortFilterProxyModel):
    """ Daily customers sorting model"""
    def __init__(self, source_model, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._date_pattern = QRegularExpression()

        # Set source model
        self.setSourceModel(source_model)

    def setDateFilter(self, date):
        """Set regex pattern for date type""" 
        if(date == ''):
            self._date_pattern.setPattern('')
            
        else:
            date = QLocale(QLocale.English, QLocale.UnitedStates).toString(date, "yyyy-MM-dd")
            self._date_pattern.setPattern(date)

        self.invalidateFilter()
    
    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex):
        
        date_index = self.sourceModel().index(row_num, self.sourceModel().fieldIndex('shift_date'),  source_parent)

        date = self.sourceModel().data(date_index, Qt.DisplayRole)

        return self._date_pattern.match(date).hasMatch()

    
######################
# Shifts-Supervisors #
######################
class HierarcicalShiftsSupervisorsModel(QtGui.QStandardItemModel):

    def __init__(self, db, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)
        self.db = db
        self.showShiftsSupervisors()

    def showShiftsSupervisors(self):
        
        ret = retrieveShiftsSupervisors(db = self.db)
        dates = list(map(lambda x : QtGui.QStandardItem(x), ret.keys()))

        for date in dates:
            shift_ids = list(map(lambda x : QtGui.QStandardItem(x), ret[date.text()]))

            for shift_id in shift_ids:
                supervisors_names = list(map(lambda x : QtGui.QStandardItem(x), ret[date.text()][shift_id.text()]))

                shift_id.appendRows(supervisors_names)

                date.appendRow(shift_id)

            
            self.appendRow(date)



###########
# Reports #
###########
class ReportsModel(QSqlQueryModel):
    """ Reports model for controlling all transctions"""
    
    def __init__(self, db: QSqlDatabase, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)
        self.db = db
        self.showReports()
    
    def showReports(self, filter = ''):
        
        STATEMENT = None
        headers = None

        if(filter == ''):
            return

        elif(filter == 'يومي'):
            # headers = ('اليوم','زبون يومي','اشتراكات يومية','مشترك شهري','اشتراكات شهرية','إيراد المشروب','إيراد الطعام','الاجمالي')
            headers = ('Day','#Daily customers','Daily fees','#Monthly customers','Monthly fees','Beverage revenue','Food revenue','Total')
          
            STATEMENT = \
                """
                    SELECT date, numbers_of_daily_customers, daily_subscribtion_income, numbers_of_monthly_customers, monthly_subscribtion_income, drinks_total_income, food_total_income, total_income FROM Reports WHERE 1
                """

        elif (filter == 'شهري'):
            # headers = ('الشهر','زبون يومي','اشتراكات يومية','مشترك شهري','اشتراكات شهرية','إيراد المشروب','إيراد الطعام','الاجمالي')
            headers = ('Month','#Daily customers','Daily fees','#Monthly customers','Monthly fees','Beverage revenue','Food revenue','Total')
    
            STATEMENT = \
                """
                
                SELECT strftime('%m', Reports.date) AS month, sum(numbers_of_daily_customers), sum(daily_subscribtion_income), 
                    sum(numbers_of_monthly_customers), sum(monthly_subscribtion_income),
                    sum(drinks_total_income), sum(food_total_income), sum(total_income)
                
                FROM Reports GROUP BY strftime('%m', Reports.date)


                """
        
        elif (filter == 'سنوي'):
            # headers = ('السنة','زبون يومي','اشتراكات يومية','مشترك شهري','اشتراكات شهرية','إيراد المشروب','إيراد الطعام','الاجمالي')
            headers = ('Year','#Daily customers','Daily fees','#Monthly customers','Monthly fees','Beverage revenue','Food revenue','Total')

            STATEMENT = \
                """
                
                SELECT strftime('%Y', Reports.date) AS year, sum(numbers_of_daily_customers), sum(daily_subscribtion_income), 
                    sum(numbers_of_monthly_customers), sum(monthly_subscribtion_income),
                    sum(drinks_total_income), sum(food_total_income), sum(total_income)
                FROM Reports


                GROUP BY strftime('%Y', Reports.date)

                """

        elif (filter == 'معدل الزبائن'):
            # headers = ('الشهر','زبون يومي','زبون شهري','عدد الزبائن الكلي','مشترك شهري','معدل الزبائن اليوميين')
            headers = ('Month','#Daily customers','#Monthly customers','#All customers','Monthly subscribers','Average daily customers')

            STATEMENT = \
                """
                
                
                SELECT strftime('%m', Reports.date) AS month, 
                sum(numbers_of_daily_customers),
                sum(numbers_of_dailyMonthly_customers), 
                sum(numbers_of_total_customers), 
                sum(numbers_of_monthly_customers), 
                average_numbers_of_daily_customers
                     
                FROM Reports GROUP BY strftime('%m', Reports.date)

                """
        
        self.setQuery(STATEMENT, self.db)
        
        for ind, header in enumerate(headers):
            self.setHeaderData(ind, Qt.Horizontal,header)
                
    def removeReport(self, date):
        if(date is not None):
            deleted_date = ''
            # Daily regex
            if(QRegularExpression("(\\d{4})-(\\d{2})-(\\d{2})").match(date).hasMatch()):
                deleted_date = date
            
            # Monthly regex
            elif(QRegularExpression("^[0|1]?\\d{1}$").match(date).hasMatch()):
                deleted_date = f'%-{date}-%'

            # Yearly regex
            elif(QRegularExpression("^\\d{4}$").match(date).hasMatch()):
                deleted_date = f'{date}-%'

            STATEMENT = \
                f"""
                    DELETE FROM Reports WHERE date LIKE '{deleted_date}'
                """
            query = QSqlQuery(self.db)
            query.exec(STATEMENT)

    def data(self, index: QtCore.QModelIndex, role: int):
        if(role == Qt.TextAlignmentRole):
            return Qt.AlignHCenter

        return super().data(index, role=role)

class ReportsSortModel(QtCore.QSortFilterProxyModel):
    """ Reports sorting model"""
    def __init__(self, source_model, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)

        # Create private regex for filtering
        self._date_pattern = QRegularExpression()
        
        # Set source model
        self.setSourceModel(source_model)
    
    def setDateFilter(self, string):
        """Set regex pattern for subscription type"""
        self._date_pattern.setPattern(string)
            
        self.invalidateFilter()

    def filterAcceptsRow(self, row_num: int, source_parent: QtCore.QModelIndex) -> bool:
        
        date_index = self.sourceModel().index(row_num, 0,  source_parent)

        date = self.sourceModel().data(date_index, Qt.DisplayRole)

        tests =  [
            self._date_pattern.match(date).hasMatch()
        ]
        
        return (not False in tests)

class HierarcicalDateModel(QtGui.QStandardItemModel):

    def __init__(self, db, table, field, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent=parent)
        self.db = db
        self.table = table
        self.field = field
        self.showYMDs()


    def showYMDs(self):
        
        # Get available years for the selected table
        years = retrieveArchiveYears(db = self.db, table = self.table, field = self.field)
        years = list(map(lambda x : QtGui.QStandardItem(x), years))

        for y_item in years:
            
            # Get available months for the selected table and append them to the specific year
            months = retrieveArchiveMonths(year = y_item.text(), db = self.db, table = self.table, field = self.field)
            months = list(map(lambda x : QtGui.QStandardItem(x), months))
            
            for m_item in months:
    
                # Get available days for the selected table and append them to the specific month
                days = retrieveArchiveDays(month = m_item.text(), db = self.db,  table = self.table, field = self.field)
                days = list(map(lambda x : QtGui.QStandardItem(x), days))
            
                m_item.appendRows(days)

                y_item.appendRow(m_item)

            
            self.appendRow(y_item)


