"""This module provides a database Daily and Archive connection."""

from itertools import groupby
from operator import itemgetter
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createCustomersTables(db_1, db_2):
    """Create database tables if they don't exist"""

    # Daily DateBase Tables and Triggers
    DAILYCUSTOMERS_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Daily_customers (
            daily_id           INTEGER       UNIQUE
                                     PRIMARY KEY ASC ON CONFLICT ABORT AUTOINCREMENT
                                     NOT NULL,
            daily_name         VARCHAR (255) NOT NULL,
            daily_ticket_cost  REAL (10),
            subscription_state VARCHAR,
            monthly_id         INTEGER       CONSTRAINT fk_monthly_id REFERENCES Monthly_customers (monthly_id) ON DELETE SET NULL
                                                                                                                ON UPDATE NO ACTION,
            daily_date         DATE          NOT NULL
                                            DEFAULT (date('now') )
        );

        """

    ORDERS_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Orders (
            order_id          INTEGER      PRIMARY KEY ASC ON CONFLICT ABORT AUTOINCREMENT
                                   UNIQUE
                                   NOT NULL,
            daily_customer_id INTEGER (10) CONSTRAINT fk_daily_customer_id REFERENCES Daily_customers (daily_id) ON DELETE CASCADE
                                                                                                                ON UPDATE NO ACTION,
            order_price       REAL (10)    NOT NULL
                                        CHECK (order_price >= 0) 
                                        DEFAULT (0),
            order_type        VARCHAR      NOT NULL
                                        DEFAULT عام,
            order_date        DATE         NOT NULL
                                        DEFAULT (date('now') )  
        );

        """

    ORDER_ITEMS_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Orders_items (
            id       INTEGER      PRIMARY KEY
                                NOT NULL
                                UNIQUE,
            order_id INTEGER (10) REFERENCES Orders (order_id) ON DELETE CASCADE
                                                            ON UPDATE NO ACTION,
            item_id  INTEGER (10) REFERENCES Warehouse (item_id) ON DELETE SET NULL
                                                                ON UPDATE NO ACTION,
            offer_id INTEGER (10) REFERENCES Offers (offer_id) ON DELETE SET NULL
                                                            ON UPDATE NO ACTION,
            quantity INTEGER (10) NOT NULL,
            price    REAL (10),
            date     DATE         NOT NULL
                                DEFAULT (date('now') )
        );

        """

    MONTHLYCUSTOMERS_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Monthly_customers (
            monthly_id          INTEGER       PRIMARY KEY ASC ON CONFLICT ABORT AUTOINCREMENT
                                            UNIQUE
                                            NOT NULL,
            monthly_name        VARCHAR (255) NOT NULL,
            ticket_monthly_cost REAL (10),
            start_date          DATE          NOT NULL
                                            DEFAULT (DATE('now') ),
            end_date            DATE          NOT NULL
                                            DEFAULT (DATE('now', '+30 day') ),
            subscription_state  VARCHAR       NOT NULL
                                            DEFAULT Subscribed
                                            CHECK (subscription_state IN ('Not Subscribed', 'Subscribed', 'Expired') ),
            subsription_type    VARCHAR (255)   NOT NULL
            );
    
        """

    EMPLOYEES_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Supervisors (
            supervisor_id   INTEGER       PRIMARY KEY AUTOINCREMENT
                                  UNIQUE
                                  NOT NULL,
            supervisor_name VARCHAR (255) NOT NULL,
            username        VARCHAR (255) NOT NULL
                                        UNIQUE,
            password        VARCHAR (255) NOT NULL
                                        UNIQUE,
            job_type        VARCHAR (255) NOT NULL
                                        CHECK (job_type IN ('Manager', 'Employee') ),
            num_workdays    INTEGER (10)  NOT NULL
                                        DEFAULT (0) 
                
        """

    SHIFTS_EMPLOYEES_TABEL_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Shifts_Supervisors (
            shift_id      INTEGER (10) REFERENCES Shifts (shift_id) ON DELETE CASCADE
                                                                    ON UPDATE NO ACTION,
            supervisor_id INTEGER      REFERENCES Supervisors (supervisor_id) ON DELETE CASCADE
                                                                            ON UPDATE NO ACTION,
            date          DATE         DEFAULT (date('now') ) 
                                    NOT NULL
        );

        """
    
    WAREHOUSE_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Warehouse (
            item_id                INTEGER       PRIMARY KEY AUTOINCREMENT
                                                UNIQUE
                                                NOT NULL,
            item_name              VARCHAR (255) NOT NULL,
            item_price             REAL (10)     NOT NULL,
            item_type              VARCHAR (255) CHECK (item_type IN ('Drink', 'Food') ) 
                                                NOT NULL,
            item_current_quantity  INTEGER (10)  CHECK (item_current_quantity >= 0) 
                                                NOT NULL,
            item_consumed_quantity INTEGER (10)  CHECK (item_consumed_quantity >= 0) 
                                                NOT NULL
                                                DEFAULT (0)
        );
        """

    REPORTS_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Reports (
            id                                 INTEGER       PRIMARY KEY AUTOINCREMENT
                                                     UNIQUE
                                                     NOT NULL,
            date                               DATE          DEFAULT (DATE('now') ) 
                                                            NOT NULL
                                                            UNIQUE,
            daily_subscribtion_income          REAL (10)     NOT NULL
                                                            DEFAULT (0),
            monthly_subscribtion_income        REAL (10)     DEFAULT (0) 
                                                            NOT NULL,
            drinks_total_income                REAL (10)     NOT NULL
                                                            DEFAULT (0),
            food_total_income                  REAL (10)     NOT NULL
                                                            DEFAULT (0),
            total_income                       REAL (10)     NOT NULL
                                                            DEFAULT (0),
            numbers_of_daily_customers         INTEGER (10)  DEFAULT (0) 
                                                            NOT NULL,
            numbers_of_dailyMonthly_customers  INTEGER (10) NOT NULL
                                                            DEFAULT (0),
            numbers_of_total_customers         INTEGER (10) NOT NULL
                                                            DEFAULT (0),
            numbers_of_monthly_customers       INTEGER (10)  NOT NULL
                                                            DEFAULT (0),
            average_numbers_of_daily_customers INTEGER (10) NOT NULL
                                                            DEFAULT (0)  
        );
      
        """
    
    SUBSCRIPTION_PRICES_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Subscription_prices (
            subs_id    INTEGER       PRIMARY KEY
                                    UNIQUE
                                    NOT NULL,
            subs_name  VARCHAR (255) NOT NULL
                                    UNIQUE,
            subs_price INTEGER (10)  NOT NULL
        );

        """

    SHIFTS_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Shifts (
            shift_id       INTEGER       PRIMARY KEY
                                    UNIQUE
                                    NOT NULL,
            shift_name     VARCHAR (255),
            start_shift    TIME,
            finish_shift   TIME,
            shift_duration TIME,
            total_income   INTEGER,
            shift_state    VARCHAR (255) NOT NULL
                                        DEFAULT Inactive
                                        CHECK (shift_state IN ('Active', 'Inactive', 'Finished') ),
            shift_date           DATE          NOT NULL
                                        DEFAULT (date('now') ) 
        );

        """

    OFFERS_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Offers (
            offer_id    INTEGER      NOT NULL
                                    PRIMARY KEY AUTOINCREMENT
                                    UNIQUE,
            offer_name  VARCHAR      NOT NULL
                                    UNIQUE,
            offer_price INTEGER (10) NOT NULL,
            offer_date  DATE         DEFAULT (date('now') ) 
                                    NOT NULL
        );

        """

    OFFERS_ITEMS_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Offers_items (
            item_offer_id INTEGER      PRIMARY KEY
                                    UNIQUE
                                    NOT NULL,
            offer_id      INTEGER      REFERENCES Offers (offer_id) ON DELETE CASCADE
                                                                    ON UPDATE NO ACTION,
            item_id       INTEGER (10) REFERENCES Warehouse (item_id) ON DELETE CASCADE
                                                                    ON UPDATE NO ACTION,
            date          DATE         NOT NULL
                                    DEFAULT (date('now') ) 
        );
    
        """
        
    META_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Meta (
            key VARCHAR (255) NOT NULL
                        UNIQUE
                        PRIMARY KEY,
            value VARCHAR (255) NOT NULL
        );

        """
        

    # Daily_customers after insert trigger
    # update subscription_state
    TRIGGER1_DAILYCUSTOMERS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_daily_subs_state1
                        AFTER INSERT
                    ON Daily_customers
        BEGIN
            UPDATE Daily_customers
            SET subscription_state = CASE WHEN new.monthly_id ISNULL THEN CASE WHEN new.subscription_state = '' THEN 'Not Subscribed' WHEN new.subscription_state NOTNULL THEN 'Subscribed to another center' END WHEN new.monthly_id NOTNULL THEN (
                        SELECT Monthly_customers.subscription_state
                            FROM Monthly_customers
                            WHERE Monthly_customers.monthly_id = NEW.monthly_id
                    )
                END
            WHERE Daily_customers.daily_id = NEW.daily_id;
        END;


        """

    # Daily_customers after insert trigger
    # update subscription_state
    TRIGGER2_DAILYCUSTOMERS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_daily_subs_state2
                AFTER UPDATE OF monthly_id
                    ON Daily_customers
        BEGIN
            UPDATE Daily_customers
            SET subscription_state = CASE WHEN new.monthly_id ISNULL THEN 'Not Subscribed' ELSE (
                        SELECT Monthly_customers.subscription_state
                            FROM Monthly_customers
                            WHERE Monthly_customers.monthly_id = NEW.monthly_id
                    )
                END
            WHERE Daily_customers.daily_id = NEW.daily_id;
        END;
        """
    
    # Daily_customers after update subscription_state trigger
    # update daily_ticket_cost
    TRIGGER3_DAILYCUSTOMERS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_daily_ticket_cost
                AFTER UPDATE OF subscription_state
                    ON Daily_customers
        BEGIN
            UPDATE Daily_customers
            SET daily_ticket_cost = CASE WHEN new.subscription_state IN ('Not Subscribed', 'Expired') THEN (
                        SELECT subs_price
                            FROM Subscription_prices
                            WHERE subs_name = 'Daily fee'
                    )
                WHEN new.subscription_state IN ('Subscribed', 'Subscribed to another center') THEN 0 END
            WHERE Daily_customers.daily_id = NEW.daily_id;
        END;


        """
    
    # Daily_customers after insert trigger
    # insert new record to Reports
    TRIGGER4_DAILYCUSTOMERS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS insert_new_report
                AFTER INSERT
                    ON Daily_customers
        BEGIN
            INSERT OR IGNORE INTO Reports (
                                            date
                                        )
                                        VALUES (
                                            date('now') 
                                        );
        END;
            

        """
    
    
    # Daily_customers after update daily_name trigger
    # update monthly id
    TRIGGER5_DAILYCUSTOMERS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_monthly_id
                AFTER UPDATE OF daily_name
                    ON Daily_customers
        BEGIN
            UPDATE Daily_customers
            SET monthly_id = (
                    SELECT monthly_id
                        FROM Monthly_customers
                        WHERE monthly_name = daily_name
                );
        END;

        """
    
    
    # Orders_items update price after insert trigger
    TRIGGER1_ORDERS_ITEMS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_price1
                AFTER INSERT
                    ON Orders_items
        BEGIN
            UPDATE Orders_items
            SET price = new.quantity * (
                                            SELECT item_price
                                                FROM Warehouse
                                            WHERE item_id = NEW.item_id
                                        )
            WHERE id = new.id;
        END;

        """
    

    # Orders_items update price after update quantity trigger
    TRIGGER2_ORDERS_ITEMS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_price2
                AFTER UPDATE OF item_id,
                                quantity
                    ON Orders_items
        BEGIN
            UPDATE Orders_items
            SET price = new.quantity * (
                                            SELECT item_price
                                                FROM Warehouse
                                            WHERE item_id = new.item_id
                                        )
            WHERE id = new.id;
        END;


        """

    # Orders_items update item_consumed_quantity after insert trigger
    TRIGGER3_ORDERS_ITEMS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_item_consumed_quantity1
                AFTER INSERT
                    ON Orders_items
        BEGIN
            UPDATE Warehouse
            SET item_consumed_quantity = CASE WHEN new.quantity <= (
                                                                        SELECT item_current_quantity - item_consumed_quantity
                                                                            FROM Warehouse
                                                                        WHERE item_id = new.item_id
                                                                    )
                THEN item_consumed_quantity + new.quantity ELSE RAISE(ABORT, "The item is out of warehouse") END
            WHERE Warehouse.item_id = new.item_id;
        END;

        """
    
    # Orders_items update item_consumed_quantity after update of quantity trigger
    TRIGGER4_ORDERS_ITEMS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_item_consumed_quantity2
                AFTER UPDATE OF quantity
                    ON Orders_items
        BEGIN
            UPDATE Warehouse
            SET item_consumed_quantity = CASE WHEN abs(new.quantity - old.quantity) > (
                                                                                            SELECT item_current_quantity - item_consumed_quantity
                                                                                            FROM Warehouse
                                                                                            WHERE item_id = old.item_id
                                                                                        )
                THEN RAISE(ABORT, "The item is out of warehouse") WHEN (new.quantity < old.quantity) THEN item_consumed_quantity - abs(new.quantity - old.quantity) WHEN (new.quantity > old.quantity) THEN item_consumed_quantity + abs(new.quantity - old.quantity) END
            WHERE Warehouse.item_id = new.item_id;
        END;

        """

    # Orders_items update item_consumed_quantity after delete trigger
    TRIGGER5_ORDERS_ITEMS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_item_consumed_quantity3
                AFTER DELETE
                    ON Orders_items
        BEGIN
            UPDATE Warehouse
            SET item_consumed_quantity = CASE WHEN item_consumed_quantity >= old.quantity THEN Warehouse.item_consumed_quantity - old.quantity END
            WHERE item_id = old.item_id;
        END;

        """
    
    # Monthly_customers after insert trigger
    # update monthly_subscribtion_income in Inventroy
    TRIGGER1_MONTHLY_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_date
                AFTER UPDATE OF subscription_state
                    ON Monthly_customers
                WHEN NEW.subscription_state = 'Subscribed'
        BEGIN
            UPDATE Monthly_customers
            SET start_date = DATE('now'),
                end_date = DATE('now', '+30 day') 
            WHERE Monthly_customers.monthly_id = NEW.monthly_id;
        END;

        """
    
    
    # Monthly_customers after insert trigger
    # update monthly_tickect_cost
    TRIGGER2_MONTHLY_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_monthly_tickect_cost
                       AFTER INSERT
                    ON Monthly_customers
        BEGIN
            UPDATE Monthly_customers
            SET ticket_monthly_cost = CASE new.subsription_type WHEN 'University fee' THEN (
                                                SELECT subs_price
                                                    FROM Subscription_prices
                                                WHERE subs_name = 'University fee'
                                            )
                WHEN                       'School fee' THEN (
                                                SELECT subs_price
                                                    FROM Subscription_prices
                                                WHERE subs_name = 'School fee'
                                            )
                WHEN                       'VIP' THEN 0 END
            WHERE monthly_id = new.monthly_id;
        END;


        """

    # Reports after update of any income
    # update total_income
    TRIGGER1_REPORTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_total_income
                AFTER UPDATE OF daily_subscribtion_income,
                                monthly_subscribtion_income,
                                drinks_total_income,
                                food_total_income
                    ON Reports
        BEGIN
            UPDATE Reports
            SET total_income = daily_subscribtion_income + monthly_subscribtion_income + food_total_income + drinks_total_income
            WHERE Reports.date = date('now');
        END;

        """
    
    # Reports after update of numbers of customers
    # update average_numbers_of_customers
    TRIGGER2_REPORTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_avg_number_of_customers
                AFTER UPDATE OF numbers_of_daily_customers
                    ON Reports
        BEGIN
            UPDATE Reports
            SET average_numbers_of_daily_customers = (
                    SELECT sum(numbers_of_daily_customers) / count(Reports.date) 
                        FROM Reports
                        WHERE strftime('%m', Reports.date) = strftime('%m', new.date) 
                )
            WHERE strftime('%m', Reports.date) = strftime('%m', new.date);
        END;
        """
    
    TRIGGER1_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_finish_shift
                AFTER UPDATE OF shift_state
                    ON Shifts
        BEGIN
            UPDATE Shifts
            SET finish_shift = time('now'),
                shift_duration = round(CAST ( (strftime('%s', finish_shift) - strftime('%s', start_shift) ) AS REAL) / 60 / 60, 3) 
            WHERE shift_id = old.shift_id AND 
                shift_date = date('now') AND 
                shift_state = 'Finished';
        END;

        """
    
    TRIGGER2_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_shift_duration
                AFTER UPDATE OF finish_shift
                    ON Shifts
        BEGIN
            UPDATE Shifts
            SET shift_duration = round(CAST ( (strftime('%s', finish_shift) - strftime('%s', start_shift) ) AS REAL) / 60 / 60, 3) 
            WHERE shift_id = old.shift_id AND 
                shift_date = date('now') AND 
                shift_state = 'Finished';
        END;


        """

    TRIGGER3_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_start_shift
                AFTER UPDATE OF shift_state
                    ON Shifts
        BEGIN
            UPDATE Shifts
            SET start_shift = time('now') 
            WHERE shift_state = 'Active' AND 
                shift_id = new.shift_id AND 
                shift_date = date('now');
        END;


        """

    TRIGGER4_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_shift_name
                    AFTER INSERT
                        ON Shifts
            BEGIN
                UPDATE Shifts
                SET shift_name = (
                        SELECT printf('%s%s', 'shift' || ' ' || (
                                                                    SELECT count(shift_id) 
                                                                        FROM Shifts
                                                                        WHERE shift_date = date('now') 
                                                                )
                                ) 
                    )
                WHERE shift_id = new.shift_id;
            END;

        """
    
    TRIGGER5_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER update_employee_dayworks
                AFTER UPDATE OF shift_state
                    ON Shifts
                WHEN new.shift_state = 'Finished'
        BEGIN
            UPDATE Supervisors
            SET num_workdays = num_workdays + 1
            WHERE supervisor_id IN (
                SELECT supervisor_id
                FROM Shifts_Supervisors
                WHERE shift_id = new.shift_id
            );
        END;
"""

    INSERT1_SUBSCRIPTION_STATEMENT = \
        """
        INSERT OR IGNORE INTO Subscription_prices (subs_name, subs_price) VALUES ('Daily fee','0');
        """
    
    INSERT2_SUBSCRIPTION_STATEMENT = \
        """
        INSERT OR IGNORE INTO Subscription_prices (subs_name, subs_price) VALUES ('University fee','0');
        """

    INSERT3_SUBSCRIPTION_STATEMENT = \
        """
        INSERT OR IGNORE INTO Subscription_prices (subs_name, subs_price) VALUES ('School fee','0');
        """
    
    INSERT1_EMPLOYEES_STATEMENT = \
        """
        INSERT OR IGNORE INTO Supervisors (supervisor_name, job_type, username ,password) VALUES ('admin','Manager','admin','admin')
        """
    
    INSERT1_META_STATEMENT = \
        """
        INSERT OR IGNORE INTO Meta (key, value) VALUES ('version', '0.1.1')

        """
    INSERT2_META_STATEMENT = \
        """
        INSERT OR IGNORE INTO Meta (key, value) VALUES ('last version', '0.1.0')
        """
        
    
    sql_statements = (
        DAILYCUSTOMERS_TABLE_STATEMENT,
        ORDERS_TABLE_STATEMENT,
        ORDER_ITEMS_STATEMENT,
        MONTHLYCUSTOMERS_TABLE_STATEMENT,
        EMPLOYEES_TABLE_STATEMENT,
        SHIFTS_EMPLOYEES_TABEL_STATEMENT,
        WAREHOUSE_TABLE_STATEMENT,
        REPORTS_TABLE_STATEMENT,
        SUBSCRIPTION_PRICES_TABLE_STATEMENT,
        SHIFTS_STATEMENT,
        OFFERS_STATEMENT,
        OFFERS_ITEMS_STATEMENT,
        META_TABLE_STATEMENT,

        TRIGGER1_DAILYCUSTOMERS_STATEMENT,
        TRIGGER2_DAILYCUSTOMERS_STATEMENT,
        TRIGGER3_DAILYCUSTOMERS_STATEMENT,
        TRIGGER4_DAILYCUSTOMERS_STATEMENT,
        TRIGGER5_DAILYCUSTOMERS_STATEMENT,

        TRIGGER1_ORDERS_ITEMS_STATEMENT,
        TRIGGER2_ORDERS_ITEMS_STATEMENT,
        TRIGGER3_ORDERS_ITEMS_STATEMENT,
        TRIGGER4_ORDERS_ITEMS_STATEMENT,
        TRIGGER5_ORDERS_ITEMS_STATEMENT,

        TRIGGER1_REPORTS_STATEMENT,
        TRIGGER2_REPORTS_STATEMENT,

        TRIGGER1_MONTHLY_STATEMENT,
        TRIGGER2_MONTHLY_STATEMENT,

        TRIGGER1_SHIFTS_STATEMENT,
        TRIGGER2_SHIFTS_STATEMENT,
        TRIGGER3_SHIFTS_STATEMENT,
        TRIGGER4_SHIFTS_STATEMENT,
        TRIGGER5_SHIFTS_STATEMENT,

        INSERT1_SUBSCRIPTION_STATEMENT,
        INSERT2_SUBSCRIPTION_STATEMENT,
        INSERT3_SUBSCRIPTION_STATEMENT,

        INSERT1_EMPLOYEES_STATEMENT,

        INSERT1_META_STATEMENT,
        INSERT2_META_STATEMENT 
    )

    query = QSqlQuery(db_1)
    for statement in sql_statements:
        query.exec(statement)
    

    # Archive DataBase Tables
    sql_statements = (
        DAILYCUSTOMERS_TABLE_STATEMENT,
        MONTHLYCUSTOMERS_TABLE_STATEMENT,
        ORDERS_TABLE_STATEMENT,
        WAREHOUSE_TABLE_STATEMENT,
   )

    query = QSqlQuery(db_2)
    for statement in sql_statements:
        query.exec(statement)

    return query

def createConnection(databaseName1, databaseName2) -> bool:
    """Connect to SQLite database"""

    daily_connection = QSqlDatabase.addDatabase("QSQLITE", 'daily_connection')
    daily_connection.setDatabaseName(databaseName1)
    
    archive_connection = QSqlDatabase.addDatabase("QSQLITE", 'archive_connection')
    archive_connection.setDatabaseName(databaseName2)
    
    if not (daily_connection.open() and archive_connection.open()):
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Daily Database Error: {daily_connection.lastError().text()}\n\
            Archive Database Error: {archive_connection.lastError().text()}",
        )
        return False
    
    
    # Enable foreign key to ensure delete child when parent will be deleted.
    query = QSqlQuery(daily_connection)
    query.exec("PRAGMA foreign_keys = ON;")
    
    query = QSqlQuery(archive_connection)
    query.exec("PRAGMA foreign_keys = ON;")

    # Create DB tables
    _createCustomersTables(daily_connection, archive_connection)
    
    return (daily_connection, archive_connection)


#####################
# Monthly customers #
#####################
# Return monthly_customers names
def retrieveMonthlyNames(id = None, db = None):

    result = []

    if(id is None):
        STATEMENT = """
            SELECT trim(monthly_name) AS monthly_name from "Monthly_customers"
        """
    else:
        STATEMENT = f"""
            SELECT trim(monthly_name) AS monthly_name from "Monthly_customers" WHERE monthly_id = '{id}'
        """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        result.append(query.value(query.record().indexOf('monthly_name')))
    
    return result

# Return monthly_customers id
def retrieveMonthlyid(name = None, db = None) -> int:
  
    id = None

    STATEMENT = f"""
        SELECT monthly_id from "Monthly_customers" WHERE monthly_name = '{name}'
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        id = query.value(query.record().indexOf('monthly_id'))
    
    return id   
    
def retrieveMonthlySubsType(db = None):
    STATEMENT = f"""
        SELECT DISTINCT subsription_type from "Monthly_customers"
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    subs_types = []
    while query.next():
        subs_types.append(query.value(query.record().indexOf('subsription_type')))

    return subs_types   

def retrieveMonthlySubsState(db = None):
    STATEMENT = f"""
        SELECT DISTINCT subscription_state from "Monthly_customers"
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    subs_states = []
    while query.next():
        subs_states.append(query.value(query.record().indexOf('subscription_state')))

    return subs_states  

def updateSubsState(id=None, db = None):
    """
    Update monthly subscribtion state every day or by monthly id
    """
    if(id is not None):
        STATEMENT = f"""
        UPDATE Monthly_customers SET subscription_state = 'Subscribed' WHERE monthly_id = {id} AND subsription_type <> 'VIP'
        """
    else:
        STATEMENT = """
            UPDATE Monthly_customers SET subscription_state = 'Expired' WHERE end_date < date('now')
        """ 
    query = QSqlQuery(db= db)
    query.exec(STATEMENT)

    return query


###################
# Daily customers #
###################
# Return monthly_customers names
def retrieveDailyNames(id = None, db = None) -> list or str:
    result = []

    if(id != None):
        STATEMENT = f"""
            SELECT trim(daily_name) AS daily_name from "Daily_customers" WHERE monthly_id = '{id}'
        """
    else:
        STATEMENT = """
            SELECT trim(daily_name) AS daily_name from "Daily_customers"
        """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        result.append(query.value(query.record().indexOf('daily_name')))
    
    return result

# Return monthly_customers id
def retrieveDailyId(name, db = None) -> int:

        
    id = None

    STATEMENT = f"""
        SELECT daily_id from "Daily_customers" WHERE daily_name = trim('{name}')
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        id = query.value(query.record().indexOf('daily_id'))
    
    return id   

def retrieveDailySubsState(db = None):
    STATEMENT = f"""
        SELECT DISTINCT subscription_state from "Daily_customers"
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    subs_states = []
    while query.next():
        subs_states.append(query.value(query.record().indexOf('subscription_state')))

    return subs_states  

##########
# Orders #
##########
def retrieveItemId(item_name, db = None) -> int:
    id = None
    
    STATEMENT = f"""
        SELECT item_id FROM Warehouse where item_name = '{item_name}'
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        id = query.value(query.record().indexOf('item_id'))
        
    return id

def linkOrderItems(order_id, item_name, quantity, db = None) -> None:

    item_id = retrieveItemId(item_name, db=db)
    STATEMENT = \
        f"""
        INSERT INTO Orders_items (order_id, item_id, quantity) VALUES ({order_id}, {item_id}, {quantity})
        """
    
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)
    return query

def retrieveOrdersItems(db = None):

    indices_tree = []

    # Get available dates
    STATEMENT = \
        """
        SELECT date, order_id, item_id FROM Orders_items
        """

    query = QSqlQuery(db)
    query.exec(STATEMENT)

    while(query.next()):
        date = str(query.value(query.record().indexOf('date'))).strip()
        order_id = int(str(query.value(query.record().indexOf('order_id'))).strip())
        item_id = int(str(query.value(query.record().indexOf('item_id'))).strip())
        item_name = retrieveItemNames(item_id, db=db)[0]
        indices_tree.append([date, order_id, item_name])

   
    dic = {key: {key2 : [val for _,_,val in values2] for key2, values2 in groupby(values, itemgetter(1))} for key, values in groupby(indices_tree, itemgetter(0))}
    return dic

def retrieveOrderItems(order_id = None, db = None):

    items = []

    # Get available dates
    STATEMENT = \
        f"""
        SELECT item_id, quantity FROM Orders_items WHERE order_id = {order_id} AND date = date('now')
        """
    query = QSqlQuery(db)
    query.exec(STATEMENT)

    while(query.next()):
        item_id = query.value(query.record().indexOf('item_id'))
        quantity = query.value(query.record().indexOf('quantity'))
        items.append([item_id, quantity])

    return items


#############
# Warehouse #
#############
def retrieveItemNames(id = None, name_filter : tuple = None, db = None) -> list:
    result = []
    
    if(id == None):
        if(name_filter != None):
            STATEMENT = f"""
            SELECT item_name FROM Warehouse WHERE item_current_quantity > 0 AND item_name NOT IN {name_filter}
            """
        elif(name_filter == None):
            STATEMENT = f"""
            SELECT item_name FROM Warehouse WHERE item_current_quantity > 0
            """

    elif(id != None):
        STATEMENT = f"""
        SELECT item_name FROM Warehouse WHERE item_current_quantity > 0 AND item_id = {id}
        """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        name = str(query.value(query.record().indexOf('item_name'))).strip()
        result.append(name)
       
    return result

def retrieveItemPrice(item_name, db = None) -> int:
    STATEMENT = f"""
        SELECT item_price FROM Warehouse WHERE item_name = '{item_name}'
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        price = query.value(query.record().indexOf('item_price'))
        
        return int(price)
    
    return None

def retrieveItemId(item_name, db) -> int:

    STATEMENT = f"""
        SELECT item_id FROM Warehouse WHERE item_name = '{item_name}'
    """
    id = None
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        id = query.value(query.record().indexOf('item_id'))
        
        
    return id

def retrieveItemAvailabelQuantity(item_id, db = None):
    STATEMENT = f"""
        SELECT item_current_quantity - item_consumed_quantity AS available FROM Warehouse WHERE item_id = '{item_id}'
    """
    result = None
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    # Take the last recorde
    if(query.next()):
        result = query.value(0)

    return int(result)

def retrieveItemType(db = None) -> list:
    result = []
    
    STATEMENT = f"""
        SELECT DISTINCT(item_type) FROM Warehouse
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        name = str(query.value(query.record().indexOf('item_type'))).strip()
        result.append(name)
       
    return result

def resetCounting(table = None, column = None, db1 = None , db2 = None):

    daily_query = None
    archive_query = None
    
    if(db1 is not None):
        daily_query = QSqlQuery(db1)
    if(db2 is not None):
        archive_query = QSqlQuery(db2)

    if(archive_query is not None):
        # Check if all data in Archive is removed
        # Then reset counting in Daily tables
        RESET_AUTOINCREMENT_STATEMENTS = \
            """
            UPDATE sqlite_sequence SET seq = 0 WHERE name = 'Daily_customers';
            UPDATE sqlite_sequence SET seq = 0 WHERE name = 'Orders';        

            """
        archive_query.exec(
            """
            SELECT count(*) FROM Daily_customers
            """
        )
        if(archive_query.first()):
            ret = archive_query.value(0)
            if(ret==0):
                for statement in RESET_AUTOINCREMENT_STATEMENTS.split(';'):
                    daily_query.exec(statement)


    if(table is not None and column is not None):
        daily_query.exec(
            f"""
            UPDATE sqlite_sequence SET seq = (SELECT MAX({column}) FROM {table}) WHERE name="{table}"

            """
        )
    
#######################
# Subscription_prices #
#######################
def retrieveSubsCost(subs_type, db = None) -> int:
    STATEMENT = f"""
        SELECT subs_price FROM Subscription_prices WHERE subs_name = '{subs_type}'
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        cost = query.value(query.record().indexOf('subs_price'))
        return cost
    
    return ''

def changeSubsCost(subs_cost, subs_type, db = None):
    STATEMENT = f"""
        UPDATE Subscription_prices SET subs_price = {subs_cost} WHERE subs_name = '{subs_type}'
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    return query


###############
# Supervisors #
###############
def retrieveSupervisorsId(supervisor_name, db = None) -> int:
    id = None
    
    STATEMENT = f"""
        SELECT supervisor_id FROM Supervisors where supervisor_name = '{supervisor_name}'
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        id = query.value(query.record().indexOf('supervisor_id'))
        
    return id

def retrieveSupervisorsIds(db = None) -> list:
    
    ids = []
    STATEMENT = f"""
        SELECT supervisor_id FROM Supervisors
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        id = str(query.value(query.record().indexOf('supervisor_id'))).strip()
        ids.append(id)

    return ids

def retrieveSupervisorsNames(id = None, db = None) -> list:
    
    names = []

    if(id == None):
        STATEMENT = f"""
            SELECT supervisor_name FROM Supervisors WHERE supervisor_id NOT IN (SELECT supervisor_id FROM Shifts_Supervisors WHERE date = date('now'))
        """

    elif(id != None):
        STATEMENT = f"""
            SELECT supervisor_name FROM Supervisors WHERE supervisor_id = {id}
        """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        name = str(query.value(query.record().indexOf('supervisor_name'))).strip()
        names.append(name)

    return names

def retrieveSuperviosrsJobType(db = None) -> list:
    result = []
    
    STATEMENT = f"""
        SELECT DISTINCT job_type FROM Supervisors
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        name = str(query.value(query.record().indexOf('job_type'))).strip()
        result.append(name)
    
    return result

def linkShiftSupervisor(shift_id, supervisor_name, db = None) -> None:

    supervisor_id = retrieveSupervisorsId(supervisor_name, db=db)
    STATEMENT = \
        f"""
        INSERT INTO Shifts_Supervisors (shift_id, supervisor_id) VALUES ({shift_id}, {supervisor_id})
        """
    
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)
    return query

##########
# Offers #
##########
def linkOfferItems(offer_id, item_name, db = None) -> None:

    item_id = retrieveItemId(item_name, db=db)
    STATEMENT = \
        f"""
        INSERT INTO Offers_items (offer_id, item_id) VALUES ({offer_id}, {item_id})
        """
    
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)
    return query

def retrieveOfferNames(id, db = None):
    names = []

    if(id == None):
        STATEMENT = f"""
            SELECT offer_name FROM Offers WHERE offer_id NOT IN (SELECT offer_id FROM Offers_items WHERE date = date('now'))
        """

    elif(id != None):
        STATEMENT = f"""
            SELECT offer_name FROM Offers WHERE offer_id = {id}
        """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        name = str(query.value(query.record().indexOf('offer_name'))).strip()
        names.append(name)

    return names

def retrieveOffersItems(with_date = True, db = None):
    
    indices_tree = []

    if(with_date):

        # Get available dates
        STATEMENT = \
            """
            SELECT date, offer_id, item_id FROM Offers_items
            """

        query = QSqlQuery(db)
        query.exec(STATEMENT)

        while(query.next()):
            date = str(query.value(query.record().indexOf('date'))).strip()
            offer_id = int(str(query.value(query.record().indexOf('offer_id'))).strip())
            item_id = int(str(query.value(query.record().indexOf('item_id'))).strip())
            offer_name = retrieveOfferNames(offer_id, db=db)[0]
            item_name = retrieveItemNames(item_id, db=db)[0]
            indices_tree.append([date, offer_name, item_name])

        
        dic = {key: {key2 : [val for _,_,val in values2] for key2, values2 in groupby(values, itemgetter(1))} for key, values in groupby(indices_tree, itemgetter(0))}

    elif(with_date == False):

        # Get available dates
        STATEMENT = \
            """
            SELECT offer_id, item_id FROM Offers_items
            """

        query = QSqlQuery(db)
        query.exec(STATEMENT)

        while(query.next()):
            offer_id = int(str(query.value(query.record().indexOf('offer_id'))).strip())
            item_id = int(str(query.value(query.record().indexOf('item_id'))).strip())
            offer_name = retrieveOfferNames(offer_id, db=db)[0]
            indices_tree.append([offer_name, item_id])

        
        dic = {key: [val for _,val in values]  for key, values in groupby(indices_tree, itemgetter(0))}

    return dic

def retrieveItemsOfferId(items : tuple = None, db = None):

    offer_id = None

    # Get available dates
    STATEMENT = \
        f"""
        SELECT offer_id FROM Offers_items WHERE item_id IN {items}
        """

    print(STATEMENT)
    query = QSqlQuery(db)
    query.exec(STATEMENT)

    while(query.next()):
        offer_id = query.value(query.record().indexOf('offer_id'))

    return offer_id

##########
# Shifts #
##########
def retrieveShiftNames(id = None, db =None):
    names = []

    if(id == None):
        STATEMENT = f"""
            SELECT shift_name FROM Shifts
        """

    elif(id != None):
        STATEMENT = f"""
            SELECT shift_name FROM Shifts WHERE shift_id = {id}
        """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        name = str(query.value(query.record().indexOf('shift_name'))).strip()
        names.append(name)

    return names

def retrieveShiftsSupervisors(db = None):

    indices_tree = []

    # Get available dates
    STATEMENT = \
        """
        SELECT date, shift_id, supervisor_id FROM Shifts_Supervisors WHERE shift_id NOTNULL
        """

    query = QSqlQuery(db)
    query.exec(STATEMENT)

    while(query.next()):
        date = str(query.value(query.record().indexOf('date'))).strip()
        shift_id = int(str(query.value(query.record().indexOf('shift_id'))).strip())
        supervisor_id = int(str(query.value(query.record().indexOf('supervisor_id'))).strip())
        shift_name = retrieveShiftNames(shift_id, db=db)[0]
        supervisor_name = retrieveSupervisorsNames(supervisor_id, db=db)[0]
        indices_tree.append([date, shift_name, supervisor_name])

   
    dic = {key: {key2 : [val for _,_,val in values2] for key2, values2 in groupby(values, itemgetter(1))} for key, values in groupby(indices_tree, itemgetter(0))}
    return dic

def startShift(id, db = None):
    STATEMENT1 = \
        """
        UPDATE Shifts SET shift_state = 'Finished' WHERE shift_state = 'Active' AND shift_date = date('now');
        """

    STATEMENT2 = \
        f"""
        UPDATE Shifts SET shift_state = 'Active' WHERE shift_id = {id} AND shift_date = date('now') AND shift_state = 'Inactive';

        """

    query = QSqlQuery(db)
    for statement in [STATEMENT1, STATEMENT2]:
        query.exec(statement)

    return query

def finishShift(id, db = None):


    STATEMENT = \
        f"""
        UPDATE Shifts SET shift_state = 'Finished' WHERE shift_id = {id} AND shift_date = date('now') AND shift_state = 'Active';

        """

    query = QSqlQuery(db)
    query.exec(STATEMENT)

    return query

###########
# Reports #
###########
def updateReports(db = None):
    
    STATEMENT= \
        """
        UPDATE Reports SET 
        
        daily_subscribtion_income = CASE WHEN(SELECT sum(daily_ticket_cost) FROM Daily_customers WHERE monthly_id ISNULL AND subscription_state = 'Not Subscribed' AND daily_date = date('now')) NOTNULL THEN (SELECT sum(daily_ticket_cost) FROM Daily_customers WHERE monthly_id ISNULL AND subscription_state = 'Not Subscribed' AND daily_date = date('now')) ELSE 0 END,

        monthly_subscribtion_income = CASE WHEN (SELECT sum(ticket_monthly_cost) FROM Monthly_customers WHERE start_date = date('now')) NOTNULL THEN (SELECT sum(ticket_monthly_cost) FROM Monthly_customers WHERE start_date = date('now')) ELSE 0 END,

        drinks_total_income = CASE 
        WHEN (SELECT sum(total_price) FROM Warehouse INNER JOIN Orders ON Warehouse.item_id = Orders.warehouse_item_id AND item_type = 'Drink' AND order_date = date('now')) NOTNULL 
        THEN (SELECT sum(total_price) FROM Warehouse INNER JOIN Orders ON Warehouse.item_id = Orders.warehouse_item_id AND item_type = 'Drink' AND order_date = date('now')) 
        ELSE 0 
        END, 

        food_total_income = CASE 
        WHEN (SELECT sum(total_price) FROM Warehouse INNER JOIN Orders ON Warehouse.item_id = Orders.warehouse_item_id AND item_type = 'Food' AND order_date = date('now')) NOTNULL 
        THEN (SELECT sum(total_price) FROM Warehouse INNER JOIN Orders ON Warehouse.item_id = Orders.warehouse_item_id AND item_type = 'Food' AND order_date = date('now')) 
        ELSE 0 
        END,

        numbers_of_daily_customers = CASE WHEN (SELECT count(daily_id) FROM Daily_customers WHERE daily_ticket_cost <> 0 AND daily_date = date('now')) NOTNULL THEN (SELECT count(daily_id) FROM Daily_customers WHERE daily_ticket_cost <> 0 AND daily_date = date('now')) ELSE 0 END, 
        numbers_of_dailyMonthly_customers = CASE WHEN (SELECT count(daily_id) FROM Daily_customers WHERE daily_ticket_cost = 0 AND daily_date = date('now')) NOTNULL THEN (SELECT count(daily_id) FROM Daily_customers WHERE daily_ticket_cost = 0 AND daily_date = date('now')) ELSE 0 END, 
        numbers_of_total_customers = CASE WHEN (SELECT count(daily_id) FROM Daily_customers WHERE daily_date = date('now')) NOTNULL THEN (SELECT count(daily_id) FROM Daily_customers WHERE daily_date = date('now')) ELSE 0 END,
        numbers_of_monthly_customers = CASE WHEN (SELECT count(monthly_id) FROM Monthly_customers WHERE start_date = date('now')) NOTNULL THEN (SELECT count(monthly_id) FROM Monthly_customers WHERE start_date = date('now')) ELSE 0 END
        

        WHERE Reports.date = date('now')

        """
    
    
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    return query


#########
# Login #
#########
def checkLoging(username, password, db = None):
    USERNAME_STATEMENT = \
        f"""
            SELECT count(*) from Supervisors where username='{username}'
        """
    PASSWORD_STATEMENT = \
        f"""
            SELECT count(*) from Supervisors where  password='{password}' AND username='{username}'
        """
    
    query = QSqlQuery(db = db)

    ret1 = None
    ret2 = None

    query.exec(USERNAME_STATEMENT)
    while query.next():
        ret1 = query.value(0)
    
    
    if(ret1==1):
        query.exec(PASSWORD_STATEMENT)
        while query.next():
            ret2 = query.value(0)
        if(ret2==1):
            return True
        else:
            return 'password is not true'
    else:
        return 'username is not true'
        
def retrieveJobType(username, db = None):
    STATEMENT = f"""
        SELECT job_type FROM Supervisors WHERE username='{username}'
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        job_type = query.value(query.record().indexOf('job_type'))
        
        return job_type
    
    return None

#############
# Backup DB #
#############
def backUpDB(backup_DBname):
    """Make a backup from entire main DataBase to another one"""
    import sqlite3
    def progress(status, remaining, total):
        print(f'Copied {total-remaining} of {total} pages...')

    conn = sqlite3.connect('Daily.db')
    back = sqlite3.connect(f'{backup_DBname}.db')

    conn.backup(back, pages=0, progress=progress)
    print('Backup performed successfully.')
    print('Saved as customers-backup.sql')
    back.close()
    conn.close()

def copyData(src_db_1, dest_db_2):
    """Copy daily customers, monthly customers, and orders data to Archive DataBase"""

    COPY_STATEMETNS = \
        f"""
        ATTACH DATABASE '{src_db_1.databaseName()}' AS daily;
        INSERT INTO Monthly_customers SELECT * FROM daily.Monthly_customers;
        INSERT OR IGNORE INTO Warehouse SELECT * FROM daily.Warehouse;
        INSERT INTO Daily_customers SELECT * FROM daily.Daily_customers;
        INSERT INTO Orders SELECT * FROM daily.Orders;
        """
    

    UPDATE_WAREHOUSE = \
        """
        UPDATE Warehouse SET item_current_quantity = item_current_quantity - item_consumed_quantity;                     
        """
    
    DELETE_STATEMENTS = \
        """
        DELETE FROM Daily_customers WHERE 1;
        DELETE FROM Orders WHERE 1;
        """

    

    archive_query = QSqlQuery(dest_db_2)
    for statement in COPY_STATEMETNS.splitlines():
        if(statement != ''):
            archive_query.exec(statement)


    daily_query = QSqlQuery(src_db_1)
    for statement in UPDATE_WAREHOUSE.split(';'):
        daily_query.exec(statement)

    for statement in DELETE_STATEMENTS.split(';'):
        daily_query.exec(statement)
    
    
    

#####################################
# Available Years, Months, and days #
#####################################
def retrieveArchiveYears(db, table, field):

    """Get the years from daily customers table in Archive DataBase"""
    STATEMENT_YEARS= \
        f"""
            SELECT DISTINCT(strftime('%Y', {field})) AS years FROM {table} ORDER BY years
        """

    
    years= []

    query = QSqlQuery(db = db)
    query.exec(STATEMENT_YEARS)
    while (query.next()):
        years.append(query.value(0))

    return years

def retrieveArchiveMonths(year, db, table, field):
       
    """Get the months from daily customers table in Archive DataBase"""
    STATEMENT_MONTHS = \
        f"""
            SELECT DISTINCT(strftime('%m', {field})) AS months FROM {table} WHERE strftime('%Y', {field}) = '{year}' ORDER BY months
        """

    
    months = []

    query = QSqlQuery(db = db)
    query.exec(STATEMENT_MONTHS)
    while (query.next()):
        months.append(query.value(0))
        
    return months

def retrieveArchiveDays(month, db, table, field):
    """Get the days from daily customers table in Archive DataBase"""
    
    STATEMENT_DAYS = \
        f"""
            SELECT DISTINCT(strftime('%d', {field})) AS days FROM {table} WHERE strftime('%m', {field}) = '{month}' ORDER BY days
        """

    
    days = []

    query = QSqlQuery(db = db)
    query.exec(STATEMENT_DAYS)
    while (query.next()):
        days.append(query.value(0))
        
    return days



def updateDB():
    import sqlite3
    con = sqlite3.connect('./Database/Daily.db')
    cur = con.cursor()

    script1 = \
        """
        PRAGMA foreign_keys = 0;

        CREATE TABLE sqlitestudio_temp_table AS SELECT *
                                                FROM Daily_customers;

        DROP TABLE Daily_customers;

        CREATE TABLE Daily_customers (
            daily_id           INTEGER       UNIQUE
                                            PRIMARY KEY ASC ON CONFLICT ABORT AUTOINCREMENT
                                            NOT NULL,
            daily_name         VARCHAR (255) NOT NULL,
            daily_ticket_cost  REAL (10),
            subscription_state VARCHAR,
            monthly_id         INTEGER       CONSTRAINT fk_monthly_id REFERENCES Monthly_customers (monthly_id) ON DELETE SET NULL
                                                                                                                ON UPDATE NO ACTION,
            daily_date         DATE          NOT NULL
                                            DEFAULT (date('now') ) 
        );

        INSERT INTO Daily_customers SELECT * FROM sqlitestudio_temp_table;

        DROP TABLE sqlitestudio_temp_table;

        CREATE TRIGGER update_daily_subs_state1
                AFTER INSERT
                    ON Daily_customers
        BEGIN
            UPDATE Daily_customers
            SET subscription_state = CASE WHEN new.monthly_id ISNULL THEN CASE WHEN new.subscription_state = '' THEN 'Not Subscribed' WHEN new.subscription_state NOTNULL THEN 'Subscribed to another center' END WHEN new.monthly_id NOTNULL THEN (
                        SELECT Monthly_customers.subscription_state
                            FROM Monthly_customers
                            WHERE Monthly_customers.monthly_id = NEW.monthly_id
                    )
                END
            WHERE Daily_customers.daily_id = NEW.daily_id;
        END;

        CREATE TRIGGER update_daily_subs_state2
                AFTER UPDATE OF monthly_id
                    ON Daily_customers
        BEGIN
            UPDATE Daily_customers
            SET subscription_state = CASE WHEN new.monthly_id ISNULL THEN 'Not Subscribed' ELSE (
                        SELECT Monthly_customers.subscription_state
                            FROM Monthly_customers
                            WHERE Monthly_customers.monthly_id = NEW.monthly_id
                    )
                END
            WHERE Daily_customers.daily_id = NEW.daily_id;
        END;

        CREATE TRIGGER update_daily_ticket_cost
                AFTER UPDATE OF subscription_state
                    ON Daily_customers
        BEGIN
            UPDATE Daily_customers
            SET daily_ticket_cost = CASE WHEN new.subscription_state IN ('Not Subscribed', 'Expired') THEN (
                        SELECT subs_price
                            FROM Subscription_prices
                            WHERE subs_name = 'Daily fee'
                    )
                WHEN new.subscription_state IN ('Subscribed', 'Subscribed to another center') THEN 0 END
            WHERE Daily_customers.daily_id = NEW.daily_id;
        END;

        CREATE TRIGGER insert_new_report
                AFTER INSERT
                    ON Daily_customers
        BEGIN
            INSERT OR IGNORE INTO Reports (
                                            date
                                        )
                                        VALUES (
                                            date('now') 
                                        );
        END;

        CREATE TRIGGER update_monthly_id
                AFTER UPDATE OF daily_name
                    ON Daily_customers
        BEGIN
            UPDATE Daily_customers
            SET monthly_id = (
                    SELECT monthly_id
                        FROM Monthly_customers
                        WHERE monthly_name = daily_name
                );
        END;

        PRAGMA foreign_keys = 1;

        """

    script2 = \
        """
        PRAGMA foreign_keys = 0;

        CREATE TABLE sqlitestudio_temp_table AS SELECT *
                                                FROM Reports;

        DROP TABLE Reports;

        CREATE TABLE Reports (
            id                                 INTEGER      PRIMARY KEY AUTOINCREMENT
                                                            UNIQUE
                                                            NOT NULL,
            date                               DATE         DEFAULT (DATE('now') ) 
                                                            NOT NULL
                                                            UNIQUE,
            daily_subscribtion_income          REAL (10)    NOT NULL
                                                            DEFAULT (0),
            monthly_subscribtion_income        REAL (10)    DEFAULT (0) 
                                                            NOT NULL,
            drinks_total_income                REAL (10)    NOT NULL
                                                            DEFAULT (0),
            food_total_income                  REAL (10)    NOT NULL
                                                            DEFAULT (0),
            total_income                       REAL (10)    NOT NULL
                                                            DEFAULT (0),
            numbers_of_daily_customers         INTEGER (10) DEFAULT (0) 
                                                            NOT NULL,
            numbers_of_dailyMonthly_customers  INTEGER (10) NOT NULL
                                                            DEFAULT (0),
            numbers_of_total_customers         INTEGER (10) NOT NULL
                                                            DEFAULT (0),
            numbers_of_monthly_customers       INTEGER (10) NOT NULL
                                                            DEFAULT (0),
            average_numbers_of_daily_customers INTEGER (10) NOT NULL
                                                            DEFAULT (0) 
        );

        INSERT INTO Reports (
                                id,
                                date,
                                daily_subscribtion_income,
                                monthly_subscribtion_income,
                                drinks_total_income,
                                food_total_income,
                                total_income,
                                numbers_of_daily_customers,
                                numbers_of_total_customers,
                                numbers_of_monthly_customers,
                                average_numbers_of_daily_customers
                            )
                            SELECT id,
                                date,
                                daily_subscribtion_income,
                                monthly_subscribtion_income,
                                drinks_total_income,
                                food_total_income,
                                total_income,
                                numbers_of_daily_customers,
                                numbers_of_total_customers,
                                numbers_of_monthly_customers,
                                average_numbers_of_daily_customers
                            FROM sqlitestudio_temp_table;

        DROP TABLE sqlitestudio_temp_table;

        CREATE TRIGGER update_total_income
                AFTER UPDATE OF daily_subscribtion_income,
                                monthly_subscribtion_income,
                                drinks_total_income,
                                food_total_income
                    ON Reports
        BEGIN
            UPDATE Reports
            SET total_income = daily_subscribtion_income + monthly_subscribtion_income + food_total_income + drinks_total_income
            WHERE Reports.date = date('now');
        END;

        CREATE TRIGGER update_avg_number_of_customers
                AFTER UPDATE OF numbers_of_daily_customers
                    ON Reports
        BEGIN
            UPDATE Reports
            SET average_numbers_of_daily_customers = (
                    SELECT sum(numbers_of_daily_customers) / count(Reports.date) 
                        FROM Reports
                        WHERE strftime('%m', Reports.date) = strftime('%m', new.date) 
                )
            WHERE strftime('%m', Reports.date) = strftime('%m', new.date);
        END;

        PRAGMA foreign_keys = 1;


        """

    cur.executescript(script1) 
    cur.executescript(script2) 
    con.close()



