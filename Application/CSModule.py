from random import randint
import datetime
import pymysql
import cgi

def getConnection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='w0rkb3nch',
                           db='BookFetch')

def createTicket():
    #Ask for CS Name
    #TicketNumber
    #TicketCategory
    #insert into TroubleTickets values(TicketNumber, TicketCategory, Title, Description, Solution, HandledBy, AssignedTo);
    #insert into TicketStatusHistory values();

    now = datetime.datetime.now()
    currentDate = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    print("-----Enter the name of the cs employee who will create a ticket-----")
    cseName = input("Enter employee's name: ")
    ticketNumber = input("Enter ticket number: ")
    ticketCategory = input("Enter ticket category: ")
    ticketTitle = input("Enter ticket title: ")

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("insert into TroubleTickets values(\"" + ticketNumber + "\", \"" + ticketCategory + "\", \"" + ticketTitle
                   + "\", \"\", \"\", \"" + cseName + "\", \"\");")
            cursor.execute(sql)
            sql = ("insert into TicketStatusHistory values(\"%s\", \"%s\", \"%s\");"
                   % (ticketNumber, "new", currentDate))
            cursor.execute(sql)


    finally:
        connection.close()

def updateTicket():
    now = datetime.datetime.now()
    currentDate = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    connection = getConnection()
    connection.autocommit(True)
    try:
        with connection.cursor() as cursor:
            sql = ("select * from TroubleTickets;")
            cursor.execute(sql)

            print("\nHere is the list of trouble tickets:")
            counter = 0

            tickets = []
            print("#) TicketNumber | Title | Description | AssignedTo")
            for i in cursor:
                print(str(counter) + ") " + i[0] + "\t | " + i[2] + "\t | " + i[3] + "\t | " + i[6])
                tickets.append(i[0])
                counter = counter + 1

            ticketOptions = ("\nHere are your options:\n1) Add a description\n2) Assign the ticket to an Admin\nEnter [1-2]: ")
            userInput = int(input(ticketOptions))
            if (userInput == 1):
                userInput = int(input("Enter the number of item that you want to modify the description of [0-" + str(counter - 1) + "]: "))
                description = input("Enter the new description: ")
                sql = ("update TroubleTickets set Description = \"" + description
                       + "\" where TicketNumber = \"" + tickets[userInput] + "\";")

                cursor.execute(sql)

            elif (userInput == 2):
                userInput = int(input("Enter the number of item that you want to assign [0-" + str(counter - 1) + "]: "))
                assignedTo = input("Enter the person you want to assign it to: ")
                sql = ("update TroubleTickets set AssignedTo = \"" + assignedTo
                       + "\" where TicketNumber = \"" + tickets[userInput] + "\";")
                cursor.execute(sql)
                sql = ("insert into TicketStatusHistory values(\"" + tickets[userInput] +"\", \"assigned\", \"" + currentDate + "\");")
                cursor.execute(sql)

    finally:
        connection.close()

def csModuleMain():
    welcomeMsg = ("---------------------\nCustomer Support Module\n---------------------")

    mainOptionsMsg = (
    """Here are your options:
    1) Create a new trouble ticket
    2) Update a trouble ticket
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
        createTicket()
    elif (userInput == 2):
        updateTicket()
    elif (userInput == 3):
        return
    elif (userInput == 4):
        quit()

    csModuleMain()