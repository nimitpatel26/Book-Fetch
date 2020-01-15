
from random import randint
import datetime
import pymysql
import cgi

def getConnection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='w0rkb3nch',
                           db='BookFetch')

def addCSE():

    saFName = input("Enter the first name of super admin: ")
    saLName = input("Enter the last name of super admin: ")
    print("Enter the information about the new employee: ")

    fName = input("First Name:\t ")
    lName = input("Last Name:\t ")
    email = input("Email:\t ")
    telephone = input("Telephone [##########]:\t ")
    street = input("Street:\t ")
    city = input("City:\t ")
    state = input("State:\t ")
    country = input("Country:\t ")

    gender = input("Gender:\t ")
    salary = input("Salary:\t ")
    ssn = input("SSN:\t ")

    id = fName[:2] + lName[:2] + "Ep" + str(randint(100, 999))
    id = id.upper()

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into Users values (\"" + id + "\", \"" + fName
                  + "\", \"" + lName + "\", \"" + email + "\", \"" + street + "\", \"" + city
                  + "\", \"" + state + "\", \"" + country + "\");")

            cursor.execute(sql)

            sql = ("insert into PhoneNumbers values (\"" + id + "\", " + telephone + ");")
            cursor.execute(sql)

            sql = ("insert into Employees values (\"" + id + "\", \"" + gender + "\", " + salary + ", \""
                   + ssn + "\");")
            cursor.execute(sql)


            sql = ("insert into CustomerSupport values(\"" + id
                   + "\", (select ID from Users where FirstName = \""
                   + saFName + "\" and " + "LastName = \"" + saLName + "\"));")
            cursor.execute(sql)
    finally:
        connection.close()

def deactivateAdmin():
    print("")
    # List of admins
    now = datetime.datetime.now()
    currentDate = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("select Admin.EmployeeID, Users.FirstName, Users.LastName from Admin, Users where Users.ID = Admin.EmployeeID;")
            cursor.execute(sql)

            print("\nHere is the list of admins")
            print("#) EmployeeID FirstName LastName")
            counter = 0
            commands = []
            commands2 = []
            commands3 = []
            for i in cursor:
                print(str(counter) + ") " + i[0] + " " + i[1] + " " + i[2])
                sql = ("delete from Admin where EmployeeID = \"" + i[0] + "\";")
                commands.append(sql)
                sql = ("delete from Employees where EmployeeID = \"" + i[0] + "\";")
                commands2.append(sql)
                sql = ("delete from Users where ID = \"" + i[0] + "\";")
                commands3.append(sql)
                counter = counter + 1

            deleteItem = input("Enter the number of item that you want to delete [0-"
                               + str(counter - 1) + "]: ")

            cursor.execute(commands[int(deleteItem)])
            cursor.execute(commands2[int(deleteItem)])
            cursor.execute(commands3[int(deleteItem)])

    finally:
        connection.close()

def sAdminModuleMain():

    welcomeMsg = ("---------------------\nSuper Admin Module\n---------------------")

    mainOptionsMsg = (
    """Here are your options:
    1) Create a new customer service employee
    2) Deactivate an administrator
    3) Return
    4) Quit
    Enter [1-4]: """)

    invalidInputMsg = "Invalid input, please enter a valid input."
    print(welcomeMsg)
    userInput = int(input(mainOptionsMsg))
    print("\n")

    while(userInput < 1 or userInput > 4):
        print(invalidInputMsg)
        userInput = int(input(mainOptionsMsg))
        print("\n")

    if (userInput == 1):
        addCSE()
    elif (userInput == 2):
        deactivateAdmin()
    elif (userInput == 3):
        return
    elif (userInput == 4):
        quit()


    sAdminModuleMain()