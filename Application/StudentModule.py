from random import randint
import datetime
import pymysql
import cgi



def getConnection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='w0rkb3nch',
                           db='BookFetch')

def newStudent():
    fName = input("First Name:\t ")
    lName = input("Last Name:\t ")
    email = input("Email:\t ")
    telephone = input("Telephone [##########]:\t ")
    street = input("Street:\t ")
    city = input("City:\t ")
    state = input("State:\t ")
    country = input("Country:\t ")
    major = input("Major:\t ")
    status = input("Undergrad/Graduate:\t ")
    year = input("Year [#]:\t ")
    print("-----University is a foreign key constraint!-----")
    university = input("University:\t ")
    dob = input("DOB:\t ")

    id = fName[:2] + lName[:2] + "St" + str(randint(100, 999))
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

            sql = ("insert into Students values (\"" + id + "\", \"" + major + "\", " + year + ", \""
                   + university + "\", \"" + dob + "\", \"" + status + "\");")
            cursor.execute(sql)

    finally:
        connection.close()


def newCart():
    now = datetime.datetime.now()
    currentDate = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    print("-----If the already has a cart created then it will be an error.-----")
    firstName = input("Enter student's first name: ")
    lastName = input("Enter student's last name: ")
    bookTitle = input("Enter the book title: ")
    rentBuy = input("Enter purchase type (rent/buy): ")
    quantity = input("Enter quantity: ")
    wishlist = input("Wishlist (y/n): ")



    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into Cart values(("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\"),"
                   + "(select ISBN from BookDetails where Title = \"" + bookTitle + "\"), \"" + rentBuy + "\", " + quantity
                   + ", \"" + wishlist + "\");")
            cursor.execute(sql)
            sql = ("insert into CartDateCreated values(("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\"), \""
                   + currentDate + "\");"
                   )
            cursor.execute(sql)
            sql = ("insert into CartDateUpdated values(("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\"), \""
                   + currentDate + "\");"
                   )
            cursor.execute(sql)
    except:
        print(cursor)
    finally:
        connection.close()


def newOrder():
    now = datetime.datetime.now()
    currentDate = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    print("-----Enter the name of the user whose cart will be turned into order.-----")
    firstName = input("Enter student's first name: ")
    lastName = input("Enter student's last name: ")
    sType = input("Shipping type: ")
    ccNumber = input("Credit card number: ")
    ccExpiration = input("Credit card expiration: ")
    ccName = input("Credit card name: ")
    ccType = input("Credit card type: ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("select * from Cart where Cart.StudentID = ("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\");")
            cursor.execute(sql)
            commands = []

            for i in cursor:
                if (i[4] == "n"):
                    sql = ("insert into Orders values(\"" + i[0] + "\", "
                           + str(i[1]) + ", \"" + i[2] + "\", " + str(i[3])
                           + ", \"" + currentDate + "\", \"\", \""
                           + sType + "\", \"" + ccNumber + "\", \""
                           + ccExpiration + "\", \"" + ccName + "\", \"" + ccType
                           + "\", \"" + "new\");")
                    commands.append(sql)
                    sql = ("delete from cart where StudentID = \""
                           + i[0] + "\" and ISBN = " + str(i[1]) + ";")
                    commands.append(sql)
                    sql = ("update CartDateUpdated set DUpdated = \"" + currentDate
                           + "\" where StudentID"
                           + " = \"" + i[0] + "\";"
                           )
                    commands.append(sql)


            for i in commands:
                cursor.execute(i)
    finally:
        connection.close()

def newRating():
    print("-----Enter the name of the user who will rate a book.-----")
    firstName = input("Enter student's first name: ")
    lastName = input("Enter student's last name: ")
    bookTitle = input("Enter book title: ")
    bookRating = input("Your rating [0-5]: ")
    ratingTitle = input("Rating title: ")
    ratingDescription = input("Rating description: ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into BReviewed values(("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\"), \""
                   + ratingTitle + "\", " + bookRating
                   + ", (select ISBN from BookDetails where Title = \"" + bookTitle + "\"), \""
                   + ratingDescription + "\");")
            cursor.execute(sql)


    finally:
        connection.close()

def updateCart():

    print("-----Enter the name of the user who's cart you will modify.-----")
    firstName = input("Enter student's first name: ")
    lastName = input("Enter student's last name: ")
    cartOptions = (
    """Here are your options:
    1) Add to cart
    2) Delete from cart
    Enter [1-2]: """)
    userInput = input(cartOptions)
    if (userInput == 1):
        addToCart(firstName, lastName)
    elif (userInput == 2):
        deleteFromCart(firstName, lastName)


def addToCart(firstName, lastName):
    now = datetime.datetime.now()
    currentDate = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    bookTitle = input("Enter the book title: ")
    rentBuy = input("Enter purchase type (rent/buy): ")
    quantity = input("Enter quantity: ")
    wishlist = input("Wishlist (y/n): ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into Cart values(("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\"),"
                   + "(select ISBN from BookDetails where Title = \"" + bookTitle + "\"), \"" + rentBuy + "\", " + quantity
                   + ", \"" + wishlist + "\");")
            cursor.execute(sql)

            sql = ("insert into CartDateUpdated values(("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\"), \""
                   + currentDate + "\");"
                   )
            cursor.execute(sql)

    finally:
        connection.close()


def deleteFromCart(firstName, lastName):
    now = datetime.datetime.now()
    currentDate = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("select * from Cart where StudentID = ("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\");")
            cursor.execute(sql)

            print("\nHere is the cart of " + firstName + " " + lastName)
            counter = 0
            commands = []
            for i in cursor:
                print(str(counter) + ") " + i[0] + " " + str(i[1]) + " " + i[2] + " " + str(i[3]) + " " + i[4])
                sql = ("delete from Cart where StudentID = \"" + i[0] + "\" and ISBN = " + str(i[1]) + ";")
                commands.append(sql)
                counter = counter + 1

            deleteItem = input("Enter the number of item that you want to delete [0-"
                               + str(counter - 1) + "]: ")

            cursor.execute(commands[int(deleteItem)])

            sql = ("insert into CartDateUpdated values(("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\"), \""
                   + currentDate + "\");"
                   )
            cursor.execute(sql)

    finally:
        connection.close()

def cancelOrder():
    print("-----Enter the name of the user who's order you will modify.-----")
    firstName = input("Enter student's first name: ")
    lastName = input("Enter student's last name: ")
    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("select * from Orders where StudentID = ("
                   + "select ID from Users where FirstName = \""
                   + firstName + "\" and " + "LastName = \"" + lastName + "\");")
            cursor.execute(sql)

            print("\nHere are the orders of " + firstName + " " + lastName)
            counter = 0
            commands = []
            for i in cursor:
                print(str(counter) + ") " + i[0] + " " + str(i[1]) + " " + i[2] + " " + str(i[3]) + " " + i[4])
                sql = ("delete from Orders where StudentID = \"" + i[0] + "\" and BookISBN = " + str(i[1])
                       + " and RentBuy = \"" + i[2] + "\" and DateCreated = \"" + i[4] + "\";")
                commands.append(sql)
                counter = counter + 1
            deleteItem = input("Enter the number of item that you want to delete [0-"
                               + str(counter - 1) + "]: ")

            cursor.execute(commands[int(deleteItem)])


    finally:
        connection.close()


def studentModuleMain():
    welcomeMsg = ("---------------------\nStudent Module\n---------------------")

    mainOptionsMsg = (
    """Here are your options:
    1) Create a new student
    2) Create a cart for a user
    3) Create a new order based on a cart
    4) Create a new book rating
    5) Update a cart
    6) Cancel an order
    7) Return
    8) Quit
    Enter [1-8]: """)

    invalidInputMsg = "Invalid input, please enter a valid input."
    print(welcomeMsg)
    userInput = int(input(mainOptionsMsg))
    print("\n")

    while(userInput < 1 or userInput > 8):
        print(invalidInputMsg)
        userInput = int(input(mainOptionsMsg))
        print("\n")

    if (userInput == 1):
        newStudent()
    elif (userInput == 2):
        newCart()
    elif (userInput == 3):
        newOrder()
    elif (userInput == 4):
        newRating()
    elif (userInput == 5):
        updateCart()
    elif (userInput == 6):
        cancelOrder()
    elif (userInput == 7):
        return
    elif (userInput == 8):
        quit()

    studentModuleMain()
