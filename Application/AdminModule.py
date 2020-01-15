from random import randint
import datetime
import pymysql
import cgi

def getConnection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='w0rkb3nch',
                           db='BookFetch')

def newBook():
    Title = input("Enter the title of the new book: ")
    ISBN = input("Enter the isbn of the new book: ")
    ISBN13 = input ("Enter the isbn 13: ")
    DPublished = input("Enter date published: ")
    Quantity = input("Enter quantity: ")
    Publisher = input("Enter publisher: ")
    Edition = input("Edition: ")
    Language = input("Language: ")
    Category = input("Category: ")
    Author = input("Author: ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into BookDetails values (\"" + Title + "\", " + ISBN
                   + ", " + ISBN13 + ", \"" + DPublished + "\", " + Quantity
                   + ", \"" + Publisher + "\", " + Edition + ", \"" + Language
                   + "\", \"" + Category + "\", \"" + Author + "\");")
            cursor.execute(sql)

    finally:
        connection.close()

def newUniversity():
    Name = input("Enter the name of the university: ")
    RFName = input("First name of the representative: ")
    RLName = input("Last name of the representative: ")
    Street = input("Street: ")
    City = input("City: ")
    State = input("State: ")
    Country = input("Country: ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into Universities values(\"" + Name
                   + "\", \"" + RFName + "\", \"" + RLName + "\", \""
                   + Street + "\", \"" + City + "\", \"" + State
                   + "\", \"" + Country + "\");")
            cursor.execute(sql)

    finally:
        connection.close()

def newDepartment():
    UniversityName = input("Enter the name of the university: ")
    DeptName = input("Enter the name of the department: ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into Departments values(\"" + UniversityName
                   + "\", \"" + DeptName + "\");")
            cursor.execute(sql)

    finally:
        connection.close()

def newCourses():
    CourseName = input("Enter the name of the course: ")
    UniversityName = input("Enter the name of the university: ")
    DeptName = input("Enter the name of the department: ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into Courses values(\"" + CourseName
                   + "\", \"" + UniversityName + "\", \"" + DeptName + "\");")
            cursor.execute(sql)

    finally:
        connection.close()


def newBAssociation():
    print("All of these are foreign key constraints: ")
    CourseName = input("Enter the name of the course: ")
    UniversityName = input("Enter the name of the university: ")
    ISBN = input("Enter the isbn of the book: ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into CourseReq values(" + ISBN
                   + ", \"" + CourseName + "\", \"" + UniversityName + "\");")
            cursor.execute(sql)

    finally:
        connection.close()


def adminModuleMain():
    welcomeMsg = ("---------------------\nAdmin Module\n---------------------")

    mainOptionsMsg = (
    """Here are your options:
    1) Create a new book with inventory
    2) Create a new university
    3) Create a new department
    4) Create a new courses
    5) Create a new book associations
    6) Return
    7) Quit
    Enter [1-7]: """)

    invalidInputMsg = "Invalid input, please enter a valid input."
    print(welcomeMsg)
    userInput = int(input(mainOptionsMsg))
    print("\n")

    while(userInput < 1 or userInput > 7):
        print(invalidInputMsg)
        userInput = int(input(mainOptionsMsg))
        print("\n")

    if (userInput == 1):
        newBook()
    elif (userInput == 2):
        newUniversity()
    elif (userInput == 3):
        newDepartment()
    elif (userInput == 4):
        newCourses()
    elif (userInput == 5):
        newBAssociation()
    elif (userInput == 6):
        return
    elif (userInput == 7):
        quit()

    adminModuleMain()