
import StudentModule
import CSModule
import AdminModule
import SAdminModule


def main():
    welcomeMsg =("---------------------\nWelcome to Book Fetch\n---------------------")

    mainOptionsMsg = (
    """Here are your options:
    1) Student Module
    2) Customer Support Module
    3) Admin Module
    4) Super Admin Module
    5) Quit
    Enter [1-5]: """)

    invalidInputMsg = "Invalid input, please enter a valid input."

    print(welcomeMsg)
    userInput = int(input(mainOptionsMsg))
    print("\n")

    while(userInput < 1 or userInput > 5):
        print(invalidInputMsg)
        userInput = int(input(mainOptionsMsg))
        print("\n")

    repeat = 0

    if (userInput == 1):
        repeat = StudentModule.studentModuleMain()

    elif (userInput == 2):
        repeat = CSModule.csModuleMain()

    elif (userInput == 3):
        repeat = AdminModule.adminModuleMain()

    elif (userInput == 4):
        repeat = SAdminModule.sAdminModuleMain()

    elif (userInput == 5):
        repeat = quit()


    main()

main()
