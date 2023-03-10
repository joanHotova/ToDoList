import mysql
import mysql.connector
from mysql.connector import Error
def attributesFunction(category):  # ,deadline,amount,timecap,cals,budget
    match category:
        case 'Bills':
            deadline = input("Deadline (m/d/y): ")
            amount = input("Amount: ")
            return deadline, amount
        case 'Work':
            deadline = input("Deadline (m/d/y): ")
            return deadline
        case 'Gym':
            timecap = input("Time Cap (mins): ")
            cals = input("Calories goal: ")
            return timecap, cals
        case 'Shopping':
            budget = input("Budget limit: ")
            return budget

def DBconnectionInsert(insertQuery):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='ToDoDB',
                                             user='root',
                                             password='mysqlrootpass123!@#')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            #print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            #print("You're connected to database: ", record)

            cursor.execute(insertQuery)
            connection.commit()
            # cursor.execute('SELECT * FROM WorkCategory')
            # for i in cursor:
            #     print(i)

    except Error as e:
        if e.errno==1050: #table exists
            cursor.execute(insertQuery)
            connection.commit()
            # cursor.execute('SELECT * FROM WorkCategory')
            # for i in cursor:
            #     print(i)
        else: #other errors
            print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")

def DBconnectionQueriesExec(deleteQuery):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='ToDoDB',
                                             user='root',
                                             password='mysqlrootpass123!@#')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            # print("You're connected to database: ", record)

            cursor.execute(deleteQuery)
            connection.commit()
            # cursor.execute('SELECT * FROM WorkCategory')
            # for i in cursor:
            #     print(i)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")

def DBconnectionSelect(selectQuery):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='ToDoDB',
                                             user='root',
                                             password='mysqlrootpass123!@#')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            # print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor(buffered=True)
            cursor.execute("select database();")
            record = cursor.fetchone()
            # print("You're connected to database: ", record)

            cursor.execute(selectQuery)
            connection.commit()
            return cursor.fetchone()
            # cursor.execute('SELECT * FROM WorkCategory')
            # for i in cursor:
            #     print(i)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")



class ToDoListClass:
    def __init__(self, title, category, todolist, owner, last_edit_date):
        self.title = title
        self.category = category
        self.todolist = todolist
        self.owner = owner
        self.last_edit_date = last_edit_date


    def AddOnList(self, selectedlist, last_edit_date, category):
        addedItem=input("Write: ")
        selectedlist.append(addedItem)
        match category:
            case 'Bills':
                deadline, amount=attributesFunction(str(category))
                insertQuery = "INSERT INTO BillsCategory(name, deadline,amount) VALUES ('" + addedItem + "','" + deadline + "','"+ amount +"')"
                DBconnectionInsert(insertQuery)
            case 'Work':
                deadline=attributesFunction(str(category))
                insertQuery = "INSERT INTO WorkCategory(name, deadline) VALUES ('" + addedItem + "','" + deadline + "')"
                DBconnectionInsert(insertQuery)
            case 'Gym':
                timecap, cals=attributesFunction(str(category))
                insertQuery = "INSERT INTO GymCategory(name,timecap, cals) VALUES ('" + addedItem + "','" + timecap + "','" + cals + "')"
                DBconnectionInsert(insertQuery)
            case 'Shopping':
                budget=attributesFunction(str(category))
                insertQuery = "INSERT INTO ShoppingCategory(name, budget) VALUES ('"+addedItem+"','"+budget+"')"
                DBconnectionInsert(insertQuery)
            case _:
                tableName = str(category + "Category")
                insertQuery = "INSERT INTO "+tableName+"(name) VALUES ('"+addedItem+"')"
                DBconnectionInsert(insertQuery)

        print("\nAdded on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
        print(selectedlist)
        return selectedlist

    def EditOnList(self, selectedlist, last_edit_date,category):
        print(selectedlist)
        editedItem = input("Which item you wish to edit (type number): ")
        t1=str(selectedlist[int(editedItem) - 1])
        selectedlist.remove(t1)
        t2=input("What you wish to rewrite: ")
        selectedlist.append(t2)
        match category:
            case 'Bills':
                selectQuery = "select deadline from BillsCategory where name='" + t1 + "'"
                selectedDeadline = DBconnectionSelect(selectQuery)
                selectQuery = "select amount from BillsCategory where name='" + t1 + "'"
                selectedAmount = DBconnectionSelect(selectQuery)
                updateQuery = "UPDATE BillsCategory SET Name='" + t2 + "' WHERE deadline = '" + selectedDeadline[0] + "' and name='" + t1 + "' and amount='" + str(selectedAmount[0]) + "'"
                DBconnectionQueriesExec(updateQuery)
            case 'Work':
                selectQuery = "select deadline from WorkCategory where name='" + t1 + "'"
                selectedDeadline = DBconnectionSelect(selectQuery)
                updateQuery = "UPDATE WorkCategory SET Name='" + t2 + "' WHERE deadline = '" + selectedDeadline[0] + "' and name='" + t1 + "'"
                DBconnectionQueriesExec(updateQuery)
            case 'Gym':
                selectQuery = "select timecap from GymCategory where name='" + t1 + "'"
                selectedTimeCap = DBconnectionSelect(selectQuery)
                selectQuery = "select cals from GymCategory where name='" + t1 + "'"
                selectedCals = DBconnectionSelect(selectQuery)
                updateQuery = "UPDATE GymCategory SET Name='" + t2 + "' WHERE timecap = '" + str(selectedTimeCap[0]) + "' and name='" + t1 + "' and cals='" + str(selectedCals[0]) + "'"
                DBconnectionQueriesExec(updateQuery)
            case 'Shopping':
                selectQuery = "select budget from ShoppingCategory where name='" + t1 + "'"
                selectedBudget = DBconnectionSelect(selectQuery)
                updateQuery = "UPDATE ShoppingCategory SET Name='" + t2 + "' WHERE budget = '" + str(selectedBudget[0]) + "' and name='"+t1+"'"
                DBconnectionQueriesExec(updateQuery)
            case _:
                tableName = str(category + "Category")
                updateQuery = "UPDATE " + tableName + " SET Name='" + t2 + "' WHERE name='" + t1 + "'"
                DBconnectionQueriesExec(updateQuery)
        print("\nEdited on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
        print(selectedlist)
        return selectedlist

    def DeleteOnList(self, selectedlist, last_edit_date, category):
        deletedItem = input("Which item you wish to delete (type number): ")
        t1=str(selectedlist[int(deletedItem) - 1])
        selectedlist.remove(t1)

        match category:
            case 'Work':
                selectQuery = "select deadline from WorkCategory where name='"+t1+"'"
                selectedDeadline = DBconnectionSelect(selectQuery)
                deleteQuery = "DELETE FROM WorkCategory WHERE deadline = '"+selectedDeadline[0]+"' and name='"+t1+"'"
                DBconnectionQueriesExec(deleteQuery)
            case 'Bills':
                selectQuery = "select deadline from BillsCategory where name='" + t1 + "'"
                selectedDeadline = DBconnectionSelect(selectQuery)
                selectQuery = "select amount from BillsCategory where name='" + t1 + "'"
                selectedAmount = DBconnectionSelect(selectQuery)
                deleteQuery = "DELETE FROM BillsCategory WHERE deadline = '" + selectedDeadline[0] + "' and name='" + t1 + "' and amount='"+str(selectedAmount[0])+"'"
                DBconnectionQueriesExec(deleteQuery)
            case 'Gym':
                selectQuery = "select timecap from GymCategory where name='" + t1 + "'"
                selectedTimeCap = DBconnectionSelect(selectQuery)
                selectQuery = "select cals from GymCategory where name='" + t1 + "'"
                selectedCals = DBconnectionSelect(selectQuery)
                deleteQuery = "DELETE FROM GymCategory WHERE timecap = '" + str(selectedTimeCap[0]) + "' and name='" + t1 + "' and cals='" + str(selectedCals[0]) + "'"
                DBconnectionQueriesExec(deleteQuery)
            case 'Shopping':
                selectQuery = "select budget from ShoppingCategory where name='" + t1 + "'"
                selectedBudget = DBconnectionSelect(selectQuery)
                deleteQuery = "DELETE FROM ShoppingCategory WHERE budget = '" + str(selectedBudget[0]) + "' and name='"+t1+"'"
                DBconnectionQueriesExec(deleteQuery)
            case _:
                tableName = str(category + "Category")
                deleteQuery = "DELETE FROM " + tableName + " WHERE  name='" + t1 + "'"
                DBconnectionQueriesExec(deleteQuery)

        print("\nDeleted on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
        return selectedlist

    def CleanList(self, selectedObj, all_lists, last_edit_date, category):
        all_lists.remove(selectedObj)
        tableName=str(category+"Category")
        clearQuery = "drop table "+tableName
        DBconnectionQueriesExec(clearQuery)
        print("Completed on " + str(last_edit_date.strftime("%x") + " " + last_edit_date.strftime("%X")))
        return all_lists


    # GETTERS N SETTERS
    def get_title(self):
        return self.title

    def get_category(self):
        return self.category

    def get_list(self):
        return self.todolist

    def get_owner(self):
        return self.owner

    def get_last_edit_date(self):
        return self.last_edit_date

    def set_title(self, title):
        self.title = title

    def set_category(self, category):
        self.category = category

    def set_list(self, todolist):
        self.todolist = todolist

    def set_owner(self, owner):
        self.owner = owner

    def set_last_edit_date(self, last_edit_date):
        self.last_edit_date = last_edit_date
