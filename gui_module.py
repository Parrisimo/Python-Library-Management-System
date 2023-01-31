'''
Assignment 2
Daniel Parris
CETM73
'''

#This is the GUI module
#I didn't have time to learn ktinker so a basic text based interface is all I can manage

import loan_module


def MainTitle():

    user_input = 0

    print ("Welcome to CETM Library Management Suite!\n")

    print ("Please choose an option\n")

    print ("1. Modify book data\n")

    print ("2. Modify user data\n")

    while user_input != 1 and user_input != 2:

        try:

            user_input = int(input("Please type 1 or 2: "))

        except:

            pass

    if user_input == 1:

        BooksGUI()

    elif user_input == 2:

        UserGUI()

def BooksGUI():

    book_object_list = []

    book_title_list = []

    user_book_search = ""

    print("\nModify book data selected")

    print()

    print("Here is a list of the books currently stored on the system: ")

    for book in loan_module.book_module.blist.collection_of_books:

        print()

        print (book.title)

        book_object_list.append(book)

        book_title_list.append(book.title)

    while user_book_search not in book_title_list:

        user_book_search = input("\nPlease type in the title of the book for which you wish to modify the data: ")

        if user_book_search not in book_title_list:

            print("Book not found, please try again!")

    print ("You have selected:", user_book_search)

    book_object_list[book_title_list.index(user_book_search)].PrintInfo()    

    user_input = 0

    print("What do you wish to modify?\n")

    print("1. Title\n")

    print("2. Author \n")

    print("3. Year \n")

    print("4. Publisher \n")

    print ("5. Number of Copies \n")

    while user_input < 1 or user_input > 5:

        try:

            user_input = int(input("Please choose: "))

        except:

            print("\nPlease type in a number!")

        if user_input <1 or user_input > 5:

            print ("\nPlease choose a value between 1 and 5!\n")

    book = book_object_list[book_title_list.index(user_book_search)]

    BookGUIFunctions = [ModifyTitle, ModifyAuthor, ModifyYear, ModifyPublisher, ModifyCopies]

    print (user_input + 1)

    BookGUIFunctions[user_input - 1](book)

def ModifyTitle(book):

    print ("Current Title: ", book.ReturnTitle())

    user_input = input("Please type in the new title: ")

    book.ChangeTitle(user_input)

    print ("New Title: ", book.ReturnTitle())

def ModifyAuthor(book):

    print ("Current Author: ", book.ReturnAuthor())

    user_input = input("Please type in the new author: ")

    book.ChangeAuthor(user_input)

    print ("New Author: ", book.ReturnAuthor())

def ModifyYear(book):

    print ("Current Year: ", book.ReturnYear())

    user_input = ""

    while user_input == "":

        try:

            user_input = int(input("Please type in the new year: "))

        except:

            print("Please type in an integer value!")

    book.ChangeYear(user_input)

    print ("New Year: ", book.ReturnYear())

def ModifyPublisher(book):

    print ("Current Publisher: ", book.ReturnPublisher())

    user_input = input("Please type in the new publisher: ")

    book.ChangePublisher(user_input)

    print ("New Publisher: ", book.ReturnPublisher())

def ModifyCopies(book):

    print ("Current Number of Copies: ", book.ReturnCopies())

    user_input = ""

    while user_input == "":

        try:

            user_input = int(input("Please type in the new number of copies: "))

        except:

            print("Please type in an integer value!")

    book.ChangeCopies(user_input)

    print ("New Copies: ", book.ReturnCopies())


    


def UserGUI():

    user_object_list = []

    user_name_list = []

    user_name_search = ""

    print("\nModify user data selected")

    print()

    print("Here is a list of the users currently stored on the system: ")

    for user in loan_module.user_module.ulist.collection_of_users:

        print()

        print (user.username)

        user_object_list.append(user)

        user_name_list.append(user.username)

    while user_name_search not in user_name_list:

        user_name_search = input("\nPlease type in the username of the user for which you wish to modify the data: ")

        if user_name_search not in user_name_list:

            print("User not found, please try again!")

    print ("You have selected:", user_name_search)

    user_object_list[user_name_list.index(user_name_search)].PrintInfo()    

    user_input = 0

    print("What do you wish to modify?\n")

    print("1. Username\n")

    print("2. First Name \n")

    print("3. Surname \n")

    print("4. House Number \n")

    print("5. Street Name \n")

    print("6. Postcode \n")

    while user_input < 1 or user_input > 6:

        try:

            user_input = int(input("Please choose: "))

            if user_input <1 or user_input > 6:

                print ("\nPlease choose a value between 1 and 6!\n")

        except:

            print("\nPlease type in a number!\n")
    
    user = user_object_list[user_name_list.index(user_name_search)]

    UserGUIFunctions = [ModifyUsername, ModifyFirstName, ModifySurname, ModifyHouseNumber, ModifyStreet, ModifyPostcode]

    UserGUIFunctions[user_input - 1](user)

def ModifyUsername(user):

    print ("Current Username: ", user.ReturnUsername())

    user_input = input("Please type in the new username: ")

    user.ChangeUsername(user_input)

    print ("New Username: ", user.ReturnUsername())

def ModifyFirstName(user):
    
    print ("Current First Name: ", user.ReturnFirstName())

    user.EditFirstName()

    print ("New First Name: ", user.ReturnFirstName())

def ModifySurname(user):

    print ("Current Surname: ", user.ReturnSurname())

    user.EditSurname()

    print ("New Surname: ", user.ReturnSurname())

def ModifyHouseNumber(user):

    print ("Current House Number: ", user.ReturnHouseNo())

    user_input = input("Please type in the new house number: ")

    user.ChangeHouseNo(user_input)

    print ("New House Number: ", user.ReturnHouseNo())

def ModifyStreet(user):

    print ("Current Street: ", user.ReturnStreetName())

    user_input = input("Please type in the new street: ")

    user.ChangeStreet(user_input)

    print ("New Street: ", user.ReturnStreetName())

def ModifyPostcode(user):

    print ("Current Postcode: ", user.ReturnPostcode())

    user_input = input("Please type in the new postcode: ")

    user.ChangePostcode(user_input)

    print ("New Postcode: ", user.ReturnPostcode())


user_input = "y"

while user_input == "y":

    MainTitle()

    user_input = ""

    while user_input != "y" and user_input != "n":

        print("Do you want to modify more data?\n")

        user_input=input("Please type 'y' or 'n': \n")

        if user_input != "y" and user_input != "n":

            print ("Invalid input!")

        elif user_input == "n":

            print ("Thank you for using CETM Library Management Suite\n")

            print ("Have a nice day!")

            break

        

            
