"""This module provides a database Daily and Archive connection."""

from itertools import groupby
from operator import itemgetter
from typing import Any
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createCustomersTables(db_1, db_2, database1_path):
    """Create database tables if they don't exist"""

    # Updated DateBase
    CHECK_VERSION_STATEMENT = \
        """
        SELECT value FROM Meta WHERE key = 'current version'  
        """
    UPDATE_STATEMNET = \
        """
        DROP TRIGGER update_finish_shift;
        DROP TRIGGER update_start_shift;
        DROP TRIGGER update_shift_income;
        UPDATE Meta SET value='0.1.3' WHERE key = 'current version';
        UPDATE Meta SET value='0.1.2' WHERE key = 'last version';

        """

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
                                                                                                                ON UPDATE CASCADE,
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
                                                                                                                ON UPDATE CASCADE,
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
                                                            ON UPDATE CASCADE,
            item_id  INTEGER (10) REFERENCES Warehouse (item_id) ON DELETE SET NULL
                                                                ON UPDATE CASCADE,
            offer_id INTEGER (10) REFERENCES Offers (offer_id) ON DELETE SET NULL
                                                            ON UPDATE CASCADE,
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
            subsription_type    VARCHAR (255) NOT NULL
            );
    
        """

    EMPLOYEES_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Employees (
            employee_id   INTEGER       PRIMARY KEY AUTOINCREMENT
                                        UNIQUE
                                        NOT NULL,
            employee_name VARCHAR (255) NOT NULL,
            gender        VARCHAR (255),
            job_type      VARCHAR (255) NOT NULL
                                        CHECK (job_type IN ('Manager', 'Employee') ),
            username      VARCHAR (255) NOT NULL
                                        UNIQUE,
            password      VARCHAR (255) NOT NULL
                                        UNIQUE,
            num_workdays  INTEGER (10)  DEFAULT (0) 
                                        NOT NULL
        );

                
        """

    SHIFTS_EMPLOYEES_TABEL_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Shifts_employees (
            shift_id    INTEGER (10) REFERENCES Shifts (shift_id) ON DELETE CASCADE
                                                          ON UPDATE CASCADE,
            employee_id INTEGER      REFERENCES Employees (employee_id) ON DELETE CASCADE
                                                                        ON UPDATE CASCADE,
            date        DATE         DEFAULT (date('now') ) 
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
            offers_total_income                REAL (10)    NOT NULL
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
      
        """
    
    FEES_TABLE_STATEMENT = \
        """
        CREATE TABLE IF NOT EXISTS Fees (
            fee_id    INTEGER       PRIMARY KEY
                                    UNIQUE
                                    NOT NULL,
            fee_name  VARCHAR (255) NOT NULL
                                    UNIQUE,
            fee_value INTEGER (10)  NOT NULL
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
            shift_income   INTEGER       NOT NULL
                                        DEFAULT (0) 
                                        CHECK (shift_income >= 0),
            shift_state    VARCHAR (255) NOT NULL
                                        DEFAULT Inactive
                                        CHECK (shift_state IN ('Active', 'Inactive', 'Finished') ),
            shift_date     DATE          NOT NULL
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
                                                                    ON UPDATE CASCADE,
            item_id       INTEGER (10) REFERENCES Warehouse (item_id) ON DELETE CASCADE
                                                                    ON UPDATE CASCADE,
            quantity      INTEGER      NOT NULL
                                    DEFAULT (1),
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
                        SELECT fee_value
                            FROM Fees
                            WHERE fee_name = 'Daily fee'
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
    
    
    # Daily_customers update monthly id after update of daily_name trigger
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
            SET price = CASE WHEN (
                                        SELECT order_type
                                        FROM Orders
                                        WHERE order_id = new.order_id
                                    )
        =              'عام' THEN CASE WHEN new.offer_id NOTNULL THEN 0 ELSE new.quantity * (
                                                                                                SELECT item_price
                                                                                                FROM Warehouse
                                                                                                WHERE item_id = new.item_id
                                                                                            )
                    END WHEN (
                                    SELECT order_type
                                    FROM Orders
                                    WHERE order_id = new.order_id
                                )
        =              'ضيافة' THEN 0 END
            WHERE id = new.id;
        END;

        """
    
    # Orders_items update price after update quantity trigger
    TRIGGER2_ORDERS_ITEMS_STATEMENT = \
        """
        CREATE TRIGGER update_price2
                AFTER UPDATE OF item_id,
                                quantity
                    ON Orders_items
        BEGIN
            UPDATE Orders_items
            SET price = CASE WHEN (
                                        SELECT order_type
                                        FROM Orders
                                        WHERE order_id = new.order_id
                                    )
        =              'عام' THEN CASE WHEN new.offer_id NOTNULL THEN 0 ELSE new.quantity * (
                                                                                                SELECT item_price
                                                                                                FROM Warehouse
                                                                                                WHERE item_id = new.item_id
                                                                                            )
                    END WHEN (
                                    SELECT order_type
                                    FROM Orders
                                    WHERE order_id = new.order_id
                                )
        =              'ضيافة' THEN 0 END
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
    
    # Monthly_customers update date after update subscription_state
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
    
    # Monthly_customers update monthly_tickect_cost after insert trigger
    TRIGGER2_MONTHLY_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_monthly_tickect_cost
                       AFTER INSERT
                    ON Monthly_customers
        BEGIN
            UPDATE Monthly_customers
            SET ticket_monthly_cost = CASE new.subsription_type WHEN 'University fee' THEN (
                                                SELECT fee_value
                                                    FROM Fees
                                                WHERE fee_name = 'University fee'
                                            )
                WHEN                       'School fee' THEN (
                                                SELECT fee_value
                                                    FROM Fees
                                                WHERE fee_name = 'School fee'
                                            )
                WHEN                       'VIP' THEN 0 END
            WHERE monthly_id = new.monthly_id;
        END;


        """


    # Reports update total_income after update of any income
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
            SET total_income = daily_subscribtion_income + monthly_subscribtion_income + food_total_income + drinks_total_income + offers_total_income
            WHERE Reports.date = date('now');
        END;


        """
    
    # Reports update average_numbers_of_customers after update of numbers of customers
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
    

    # Shifts update finish_shift after update of shift_state trigger
    TRIGGER1_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_finish_shift
                AFTER UPDATE OF shift_state
                    ON Shifts
        BEGIN
            UPDATE Shifts
            SET finish_shift = time('now', 'localtime'),
                shift_duration = round(CAST((strftime('%s', finish_shift) - strftime('%s', start_shift)) AS REAL) / 60 / 60, 3) 
            WHERE shift_id = old.shift_id AND 
                shift_date = date('now') AND 
                shift_state = 'Finished';
        END;

        """
    
    # Shifts update shift_duration after update of finish_shift trigger
    TRIGGER2_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_shift_duration
                AFTER UPDATE OF finish_shift
                    ON Shifts
        BEGIN
            UPDATE Shifts
            SET shift_duration = round(CAST((strftime('%s', finish_shift) - strftime('%s', start_shift) ) AS REAL) / 60 / 60, 3) 
            WHERE shift_id = old.shift_id AND 
                shift_date = date('now') AND 
                shift_state = 'Finished';
        END;


        """

    # Shifts update start_shift after update of shift_state trigger
    TRIGGER3_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_start_shift
                AFTER UPDATE OF shift_state
                    ON Shifts
        BEGIN
            UPDATE Shifts
            SET start_shift = time('now', 'localtime') 
            WHERE shift_state = 'Active' AND 
                shift_id = new.shift_id AND 
                shift_date = date('now');
        END;


        """

    # Shifts update shift_name after insert trigger
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
    
    # Shifts update num_workdays after update of shift_state trigger
    TRIGGER5_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_employee_dayworks
                AFTER UPDATE OF shift_state
                    ON Shifts
                WHEN new.shift_state = 'Finished'
        BEGIN
            UPDATE Employees
            SET num_workdays = num_workdays + 1
            WHERE employee_id IN (
                SELECT employee_id
                FROM Shifts_employees
                WHERE shift_id = new.shift_id
            );
        END;

        """

    # Shifts update shift_income after update of shift_state trigger
    TRIGGER6_SHIFTS_STATEMENT = \
        """
        CREATE TRIGGER IF NOT EXISTS update_shift_income
                AFTER UPDATE OF shift_state
                    ON Shifts
                WHEN new.shift_state = 'Finished'
        BEGIN
            UPDATE Shifts
            SET shift_income = abs( (CASE WHEN (
                                            SELECT total_income
                                                FROM Reports
                                                WHERE date = date('now') 
                                        )
                                        ISNULL THEN 0 ELSE (
                                            SELECT total_income
                                                FROM Reports
                                                WHERE date = date('now') 
                                        )
                                    END) - (CASE WHEN (
                                                    SELECT sum(shift_income) 
                                                        FROM Shifts
                                                    WHERE shift_date = date('now') 
                                                )
                                                ISNULL THEN 0 ELSE (
                                                    SELECT sum(shift_income) 
                                                        FROM Shifts
                                                    WHERE shift_date = date('now') 
                                                )
                                            END) ) 
            WHERE shift_id = old.shift_id;
        END;

        """

    INSERT1_FEE_STATEMENT = \
        """
        INSERT OR IGNORE INTO Fees (fee_name, fee_value) VALUES ('Daily fee','0');
        """
    
    INSERT2_FEE_STATEMENT = \
        """
        INSERT OR IGNORE INTO Fees (fee_name, fee_value) VALUES ('University fee','0');
        """

    INSERT3_FEE_STATEMENT = \
        """
        INSERT OR IGNORE INTO Fees (fee_name, fee_value) VALUES ('School fee','0');
        """
    
    INSERT1_EMPLOYEES_STATEMENT = \
        """
        INSERT INTO Employees (employee_name, job_type, username ,password) SELECT 'admin','Manager','admin','admin' WHERE 
                NOT EXISTS (SELECT 1 FROM Meta WHERE key = 'setting admin' AND value = 1)
        """
    
    INSERT1_META_STATEMENT = \
        """
        INSERT OR IGNORE INTO Meta (key, value) VALUES ('current version', '0.1.3')

        """
    
    INSERT2_META_STATEMENT = \
        """
        INSERT OR IGNORE INTO Meta (key, value) VALUES ('last version', '0.1.2')
        """
        
    INSERT3_META_STATEMENT = \
        """
        INSERT OR IGNORE INTO Meta (key, value) VALUES ('setting admin', '0')
        """
    
    UPDATE3_META_STATEMENT = \
        """
        UPDATE Meta SET value = 1 WHERE key = 'setting admin'
        """
    
   
    # Run update statements
    query = QSqlQuery(db_1)
    ret = query.exec(CHECK_VERSION_STATEMENT)
    while query.next():
        ret = query.value(query.record().indexOf('value'))
    
    if(ret and ret < '0.1.3'):
        updateDB(database1_path)
    
    

    # Daily DataBase Tables
    sql_statements = (
        DAILYCUSTOMERS_TABLE_STATEMENT,
        ORDERS_TABLE_STATEMENT,
        ORDER_ITEMS_STATEMENT,
        MONTHLYCUSTOMERS_TABLE_STATEMENT,
        EMPLOYEES_TABLE_STATEMENT,
        SHIFTS_EMPLOYEES_TABEL_STATEMENT,
        WAREHOUSE_TABLE_STATEMENT,
        REPORTS_TABLE_STATEMENT,
        FEES_TABLE_STATEMENT,
        SHIFTS_STATEMENT,
        OFFERS_STATEMENT,
        OFFERS_ITEMS_STATEMENT,
        META_TABLE_STATEMENT,

        TRIGGER1_DAILYCUSTOMERS_STATEMENT,
        TRIGGER2_DAILYCUSTOMERS_STATEMENT,
        TRIGGER3_DAILYCUSTOMERS_STATEMENT,
        TRIGGER4_DAILYCUSTOMERS_STATEMENT,
        TRIGGER5_DAILYCUSTOMERS_STATEMENT,

        TRIGGER1_MONTHLY_STATEMENT,
        TRIGGER2_MONTHLY_STATEMENT,

        TRIGGER1_ORDERS_ITEMS_STATEMENT,
        TRIGGER2_ORDERS_ITEMS_STATEMENT,
        TRIGGER3_ORDERS_ITEMS_STATEMENT,
        TRIGGER4_ORDERS_ITEMS_STATEMENT,
        TRIGGER5_ORDERS_ITEMS_STATEMENT,

        TRIGGER1_REPORTS_STATEMENT,
        TRIGGER2_REPORTS_STATEMENT,


        TRIGGER1_SHIFTS_STATEMENT,
        TRIGGER2_SHIFTS_STATEMENT,
        TRIGGER3_SHIFTS_STATEMENT,
        TRIGGER4_SHIFTS_STATEMENT,
        TRIGGER5_SHIFTS_STATEMENT,
        TRIGGER6_SHIFTS_STATEMENT,


        INSERT1_FEE_STATEMENT,
        INSERT2_FEE_STATEMENT,
        INSERT3_FEE_STATEMENT,


        INSERT1_META_STATEMENT,
        INSERT2_META_STATEMENT,
        INSERT3_META_STATEMENT,

        INSERT1_EMPLOYEES_STATEMENT,

        UPDATE3_META_STATEMENT,

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

def createConnection(database1_path, database2_path) -> bool:
    """Connect to SQLite database"""

    daily_connection = QSqlDatabase.addDatabase("QSQLITE", 'daily_connection')
    daily_connection.setDatabaseName(database1_path)
    
    archive_connection = QSqlDatabase.addDatabase("QSQLITE", 'archive_connection')
    archive_connection.setDatabaseName(database2_path)
    
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
    _createCustomersTables(daily_connection, archive_connection, database1_path)
    
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
        SELECT DISTINCT subsription_type from Monthly_customers
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    subs_types = []
    while query.next():
        subs_types.append(query.value(query.record().indexOf('subsription_type')))

    return subs_types   

def retrieveMonthlySubsState(db = None):
    STATEMENT = f"""
        SELECT DISTINCT subscription_state from Monthly_customers
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

def retrieveOrderType(db = None) -> list:
    types = []
    
    STATEMENT = f"""
        SELECT DISTINCT(order_type) as order_type FROM Orders
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        type = str(query.value(query.record().indexOf('order_type'))).strip()
        types.append(type)
       
    return types

def linkOrderItems(order_id, item_name, quantity, offer_id = None, db = None) -> None:

    item_id = retrieveItemId(item_name, db=db)

    if(offer_id == None):
        STATEMENT = \
            f"""
            INSERT INTO Orders_items (order_id, item_id, quantity) VALUES ({order_id}, {item_id}, {quantity})
            """
    elif(offer_id != None):
        STATEMENT = \
            f"""
            INSERT INTO Orders_items (order_id, item_id, offer_id, quantity) VALUES ({order_id}, {item_id}, {offer_id}, {quantity})
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

def updateCurrentItemsQuantities(db = None) -> None:
    CALCULATE_OFFERS_TOTAL_PRICE_STATEMENT = f"""
        UPDATE Warehouse SET item_current_quantity = item_current_quantity - item_consumed_quantity;
    """
    STATEMENT2 = f"""
        UPDATE Warehouse SET item_consumed_quantity = 0;
    """
    query = QSqlQuery(db = db)
    query.exec(CALCULATE_OFFERS_TOTAL_PRICE_STATEMENT)
    query.exec(STATEMENT2)

    return query

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
# Fees #
#######################
def retrieveSubsCost(subs_type, db = None) -> int:
    STATEMENT = f"""
        SELECT fee_value FROM Fees WHERE fee_name = '{subs_type}'
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        cost = query.value(query.record().indexOf('fee_value'))
        return cost
    
    return ''

def changeSubsCost(subs_cost, subs_type, db = None):
    STATEMENT = f"""
        UPDATE Fees SET fee_value = {subs_cost} WHERE fee_name = '{subs_type}'
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    return query


###############
# Employees #
###############
def retrieveEmployeesId(employee_name, db = None) -> int:
    id = None
    
    STATEMENT = f"""
        SELECT employee_id FROM Employees where employee_name = '{employee_name}'
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        id = query.value(query.record().indexOf('employee_id'))
        
    return id

def retrieveEmployeesIds(db = None) -> list:
    
    ids = []
    STATEMENT = f"""
        SELECT employee_id FROM Employees
    """

    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        id = str(query.value(query.record().indexOf('employee_id'))).strip()
        ids.append(id)

    return ids

def retrieveEmployeesNames(id = None, db = None) -> list:
    
    names = []

    if(id == None):
        STATEMENT = f"""
            SELECT employee_name FROM Employees WHERE employee_id NOT IN (SELECT employee_id FROM Shifts_employees WHERE date = date('now'))
        """

    elif(id != None):
        STATEMENT = f"""
            SELECT employee_name FROM Employees WHERE employee_id = {id}
        """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        name = str(query.value(query.record().indexOf('employee_name'))).strip()
        names.append(name)

    return names

def retrieveEmployeesJobType(db = None) -> list:
    result = []
    
    STATEMENT = f"""
        SELECT DISTINCT job_type FROM Employees
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        name = str(query.value(query.record().indexOf('job_type'))).strip()
        result.append(name)
    
    return result

def linkShiftEmployees(shift_id, employee_name, db = None) -> None:

    employee_id = retrieveEmployeesId(employee_name, db=db)
    STATEMENT = \
        f"""
        INSERT INTO Shifts_employees (shift_id, employee_id) VALUES ({shift_id}, {employee_id})
        """
    
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)
    return query

##########
# Offers #
##########
def linkOfferItems(offer_id, item_name, quantity, db = None) -> None:

    item_id = retrieveItemId(item_name, db=db)
    STATEMENT = \
        f"""
        INSERT INTO Offers_items (offer_id, item_id, quantity) VALUES ({offer_id}, {item_id}, {quantity})
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

def retrieveOffersItems(with_date = True, with_quantity = True, with_names = False, db = None):
    
    indices_tree = []

    if(with_date ==True and with_quantity == True and with_names == True):

        # Get available dates
        STATEMENT = \
            """
            SELECT date, offer_id, item_id, quantity FROM Offers_items
            """

        query = QSqlQuery(db)
        query.exec(STATEMENT)

        while(query.next()):
            date = str(query.value(query.record().indexOf('date'))).strip()
            offer_id = int(str(query.value(query.record().indexOf('offer_id'))).strip())
            item_id = int(str(query.value(query.record().indexOf('item_id'))).strip())
            quantity = int(str(query.value(query.record().indexOf('quantity'))).strip())
            offer_name = retrieveOfferNames(offer_id, db=db)[0]
            item_name = retrieveItemNames(item_id, db=db)[0]
            
            indices_tree.append([date, offer_name, item_name, quantity])

        
        dic = {key: {key2 : {key3: [val for _,_,_,val in values3 ][0] for key3,values3 in groupby(values2, itemgetter(2))} for key2, values2 in groupby(values, itemgetter(1))} for key, values in groupby(indices_tree, itemgetter(0))}

    elif(with_date == False and with_quantity == False and with_names == False):

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

    elif(with_date == False and with_quantity == True and with_names == False):
        # Get available dates
        STATEMENT = \
            """
            SELECT offer_id, item_id, quantity FROM Offers_items
            """

        query = QSqlQuery(db)
        query.exec(STATEMENT)

        while(query.next()):
            offer_id = int(str(query.value(query.record().indexOf('offer_id'))).strip())
            item_id = int(str(query.value(query.record().indexOf('item_id'))).strip())
            quantity = int(str(query.value(query.record().indexOf('quantity'))).strip())
            indices_tree.append([offer_id, item_id, quantity])

        
        dic = {key: {key2 : [val for _,_,val in values2][0] for key2, values2 in groupby(values, itemgetter(1))} for key, values in groupby(indices_tree, itemgetter(0))}
    
    elif(with_date == False and with_quantity == True and with_names == True):
        # Get available dates
        STATEMENT = \
            """
            SELECT offer_id, item_id, quantity FROM Offers_items
            """

        query = QSqlQuery(db)
        query.exec(STATEMENT)

        while(query.next()):
            offer_id = int(str(query.value(query.record().indexOf('offer_id'))).strip())
            item_id = int(str(query.value(query.record().indexOf('item_id'))).strip())
            offer_name = retrieveOfferNames(offer_id, db=db)[0]
            item_name = retrieveItemNames(item_id, db=db)[0]
            quantity = int(str(query.value(query.record().indexOf('quantity'))).strip())
            indices_tree.append([offer_name, item_name, quantity])

        
        dic = {key: {key2 : [val for _,_,val in values2][0] for key2, values2 in groupby(values, itemgetter(1))} for key, values in groupby(indices_tree, itemgetter(0))}


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

def retrieveOfferPrice(offer_id, db = None):

    offer_price = None

    STATEMENT = \
        f"""
        SELECT offer_price FROM Offers WHERE offer_id = {offer_id}
        """
    
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while(query.next()):
        offer_price = query.value(query.record().indexOf('offer_price'))
        
    return offer_price


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

def retrieveShiftsEmployees(db = None):

    indices_tree = []

    # Get available dates
    STATEMENT = \
        """
        SELECT date, shift_id, employee_id FROM Shifts_employees WHERE shift_id NOTNULL
        """

    query = QSqlQuery(db)
    query.exec(STATEMENT)

    while(query.next()):
        date = str(query.value(query.record().indexOf('date'))).strip()
        shift_id = int(str(query.value(query.record().indexOf('shift_id'))).strip())
        employee_id = int(str(query.value(query.record().indexOf('employee_id'))).strip())
        shift_name = retrieveShiftNames(shift_id, db=db)[0]
        employee_name = retrieveEmployeesNames(employee_id, db=db)[0]
        indices_tree.append([date, shift_name, employee_name])

   
    dic = {key: {key2 : [val for _,_,val in values2] for key2, values2 in groupby(values, itemgetter(1))} for key, values in groupby(indices_tree, itemgetter(0))}
    return dic

def startShift(id, db = None):
    CALCULATE_OFFERS_TOTAL_PRICE_STATEMENT = \
        """
        UPDATE Shifts SET shift_state = 'Finished' WHERE shift_state = 'Active' AND shift_date = date('now');
        """

    STATEMENT2 = \
        f"""
        UPDATE Shifts SET shift_state = 'Active' WHERE shift_id = {id} AND shift_date = date('now') AND shift_state = 'Inactive';

        """

    query = QSqlQuery(db)
    for statement in [CALCULATE_OFFERS_TOTAL_PRICE_STATEMENT, STATEMENT2]:
        query.exec(statement)

    return query

def finishShift(id, db = None):


    STATEMENT = \
        f"""
        UPDATE Shifts SET shift_state = 'Finished' WHERE shift_id = {id} AND shift_state = 'Active';

        """

    query = QSqlQuery(db)
    query.exec(STATEMENT)

    return query

def checkShiftActive(db = None):

    count = 0

    STATEMENT = f"""
        SELECT count(*) as count FROM Shifts WHERE shift_state = 'Active' AND shift_date = date('now')
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        count = int(query.value(query.record().indexOf('count')))

    return count


###########
# Reports #
###########
def updateReports(db = None):
    
    CALCULATE_OFFERS_TOTAL_PRICE_STATEMENT = \
        """
            DROP TABLE IF EXISTS "temp".TEMP_TABLE1;

            CREATE TEMPORARY TABLE TEMP_TABLE1 AS SELECT * FROM Offers INNER JOIN Orders_items ON Orders_items.offer_id = Offers.offer_id 
            GROUP BY Orders_items.order_id HAVING Orders_items.date = date('now');

        """

    query = QSqlQuery(db = db)
    for state in CALCULATE_OFFERS_TOTAL_PRICE_STATEMENT.split(';'):
        query.exec(state)


    STATEMENT= \
        """
        UPDATE Reports SET 
        
        daily_subscribtion_income = CASE WHEN(SELECT sum(daily_ticket_cost) FROM Daily_customers WHERE monthly_id ISNULL AND subscription_state = 'Not Subscribed' AND daily_date = date('now')) NOTNULL THEN (SELECT sum(daily_ticket_cost) FROM Daily_customers WHERE monthly_id ISNULL AND subscription_state = 'Not Subscribed' AND daily_date = date('now')) ELSE 0 END,

        monthly_subscribtion_income = CASE WHEN (SELECT sum(ticket_monthly_cost) FROM Monthly_customers WHERE start_date = date('now')) NOTNULL THEN (SELECT sum(ticket_monthly_cost) FROM Monthly_customers WHERE start_date = date('now')) ELSE 0 END,

        drinks_total_income = CASE 
        WHEN (SELECT sum(Orders_items.price) FROM Orders_items INNER JOIN Warehouse ON Warehouse.item_id = Orders_items.item_id AND Orders_items.offer_id ISNULL AND item_type = 'Drink' AND date = date('now')) NOTNULL 
        THEN (SELECT sum(Orders_items.price) FROM Orders_items INNER JOIN Warehouse ON Warehouse.item_id = Orders_items.item_id AND Orders_items.offer_id ISNULL AND item_type = 'Drink' AND date = date('now')) 
        ELSE 0 
        END, 

        food_total_income = CASE 
        WHEN (SELECT sum(Orders_items.price) FROM Orders_items INNER JOIN Warehouse ON Warehouse.item_id = Orders_items.item_id AND Orders_items.offer_id ISNULL AND item_type = 'Food' AND date = date('now')) NOTNULL 
        THEN (SELECT sum(Orders_items.price) FROM Orders_items INNER JOIN Warehouse ON Warehouse.item_id = Orders_items.item_id AND Orders_items.offer_id ISNULL AND item_type = 'Food' AND date = date('now')) 
        ELSE 0 
        END,

        offers_total_income = CASE 
        WHEN (SELECT sum(offer_price) FROM "temp".TEMP_TABLE1) NOTNULL 
        THEN (SELECT sum(offer_price) FROM "temp".TEMP_TABLE1) 
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




######################
# Subscriptions fees #
######################
def checkFeesValue(db = None):

    count = 0

    STATEMENT = f"""
        SELECT count(fee_value) as count FROM Fees WHERE fee_value = 0
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        count = int(query.value(query.record().indexOf('count')))

    return count


#########
# Login #
#########
def checkLoging(username, password, db = None):
    USERNAME_STATEMENT = \
        f"""
            SELECT count(*) from Employees where username='{username}'
        """
    PASSWORD_STATEMENT = \
        f"""
            SELECT count(*) from Employees where  password='{password}' AND username='{username}'
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
        SELECT job_type FROM Employees WHERE username='{username}'
    """
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)

    while query.next():
        job_type = query.value(query.record().indexOf('job_type'))
        
        return job_type
    
    return None


    

##############################################################
# Retrieve Available Years, Months, and days  for any tables #
##############################################################
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

def retrieveArchiveDates(table, field, db = None):
    """Get the days from daily customers table in Archive DataBase"""
    
    STATEMENT_DAYS = \
        f"""            
            SELECT (strftime('%Y', {field})) AS years, (strftime('%m',{field})) AS months, (strftime('%d', {field})) AS days FROM {table};
        """

    
    dates = []

    query = QSqlQuery(db = db)
    query.exec(STATEMENT_DAYS)
    while (query.next()):
        year = str(query.value(query.record().indexOf('years'))).strip()
        month = str(query.value(query.record().indexOf('months'))).strip()
        day = str(query.value(query.record().indexOf('days'))).strip()
        dates.append([year, month, day])

    dic = {key: {key2 : [val for _,_,val in values2] for key2, values2 in groupby(values, itemgetter(1))} for key, values in groupby(dates, itemgetter(0))}

    return dic



#####################
# Supportin methods #
#####################
def retrieveAvailableId(id_column: str, date_column: str, table_name: str, db = None) -> int:

    # Get Available ids for inserting
    table_ids = []

    # The data is given
    if(isinstance(date_column, str)):
        STATEMENT = f"""
            SELECT {id_column} FROM {table_name} WHERE {date_column} = date('now')
        """
    # The data is not given
    else:
        STATEMENT = f"""
            SELECT {id_column} FROM {table_name}
        """

    # Get available ids 
    query = QSqlQuery(db = db)
    query.exec(STATEMENT)
    while (query.next()):
        table_ids.append(query.value(0))
    

    # If the list length is 1 then return 1
    if(len(table_ids) == 1):
        if(table_ids[0] > 1):
            return 1

    # If the list length is greater or equal 2 then
    elif(len(table_ids) >= 2):
        table_ids = set(table_ids) # elemenate repeated ids
        ids = set(list(range(min(table_ids),max(table_ids)+1))) # get range from min to max ids

        # Take the difference between two sets to get available ids to use
        available_ids = list(ids.difference(table_ids))

        
        if(len(available_ids) > 0):
            return str(available_ids[0])
    
    return None

def isRecordFound(value: Any, name_column: str, date_column: str, table_name: str, db = None):

    result = None

    if(isinstance(date_column, str)):
        STATEMENT = f"""
            SELECT count(*) FROM {table_name} WHERE {name_column} = '{value}' AND {date_column} = date('now')
        """
    else:
        STATEMENT = f"""
            SELECT count(*) FROM {table_name} WHERE {name_column} = '{value}'
        """

    query = QSqlQuery(db= db)
    query.exec(STATEMENT)
    
    # Take the last recorde
    if(query.first() == True):
        result = query.value(0)
    
    return result


#############
# Backup DB #
#############
def backUpDB(database1_path, database2_path):
    """Make a backup from entire main DataBase to another one"""
    import sqlite3
    def progress(status, remaining, total):
        print(f'Copied {total-remaining} of {total} pages...')

    conn = sqlite3.connect(database1_path)
    # back = sqlite3.connect(f'{database1_path[:-3]}-backup.db')
    back = sqlite3.connect(database2_path)

    conn.backup(back, pages=0)
    # print('Backup performed successfully.')
    # print('Saved as customers-backup.sql')
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
    
def updateDB(database1_path):
    import sqlite3
    con = sqlite3.connect(database1_path)
    cur = con.cursor()

    script = \
        """
        PRAGMA writable_schema = 1;
        delete from sqlite_master where type in ('table', 'index', 'trigger');
        PRAGMA writable_schema = 0;
        VACUUM;
        PRAGMA INTEGRITY_CHECK;

        """

    cur.executescript(script) 
    con.close()




###################
# General methods #
###################
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
    