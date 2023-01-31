'''
Assignment 2
Daniel Parris
CETM73
'''
#This module contains the Loans class

import user_module

import book_module

class Loans:

    #dictionary in which to store the loans with the users as the key and the books as the value(s)
    loans = {}

    def BorrowBook(self):

        username_flag = 0

        book_flag = 0

        print ("Borrow Book")

        #checks if the borrower name is available and if not returns an error message
        borrower_search = input("Please type in the username of the borrower: ")

        for i in user_module.ulist.collection_of_users:

            if borrower_search == i.username:

                borrower = i

                username_flag = 1

        if username_flag == 0:

            print ("Username not found!")

        #once the user object is found asks user to type in a book to borrow and again
        #checks to see if the book exists or not
        borrowed_book_search = input("Please type in the title of the book to borrow: ")

        for i in book_module.blist.collection_of_books:

            if borrowed_book_search == i.title:

                borrowed_book = i

                book_flag = 1
                
        if book_flag == 0:

            print ("Book not found!")

        #if username and book have been found
        if username_flag == 1 and book_flag == 1:

            #code to deduct one from the number of copies a book has using the Book methods
            borrowed_book.ChangeCopies(borrowed_book.ReturnCopies() - 1 )

            #if/else to either write up a new key/value pairing in the dictionary or if the user already
            #exists append the book object to it
            if borrower in self.loans:

                self.loans[borrower].append(borrowed_book)

            else:

                self.loans[borrower] = [borrowed_book]

    #method to return a book
    def ReturnBook(self):

        print ("Return Book")

        username_flag = 0

        borrowed_book_list = []

        still_on_loan = []

        returnee_search = input("Please type in the username of the borrower: ")

        #simple for loop to iterate through the loans list to see if the username exists
        for user in self.loans:

            if user.username == returnee_search:

                borrowed_book_list = self.loans[user]

                username_flag = 1

        if username_flag == 0:

            print ("Sorry username not found!")

            return

        #pre-emptively printing out all the books that user has on loan in order to make the user
        #experience better
        print ("Here are the books that", returnee_search, "has out on loan:")

        for book in borrowed_book_list:

            book.PrintInfo()

            book_question = ""

            #simple while to keep the user inputting until they type y or n
            while book_question != "y" and book_question != "n":

                book_question = input("Do you want to return this book? Please type y for yes or n for no: ")

                if book_question != "y" and book_question != "n":

                    print ("Sorry, please try again!")

                elif book_question == "n":
                    
                    #append the book object to the still_on_loan list
                    #I found it easier to append to a list and then overwrite the user values at the end
                    #as opposed to deleting the book object within this loop - when I tried this way the
                    #for loop was finishing prematurely
                    still_on_loan.append(book)

                elif book_question == "y":

                    book.ChangeCopies(book.ReturnCopies() + 1 )

        #code to delete the user from the loan list if they have no books left
        if len(still_on_loan) == 0:

            for user in self.loans:

                if user.username == returnee_search:

                    remove_user = user

            #this is best placed outside of the for loop above
            self.loans.pop(remove_user)

        #code to overwrite the user loans with the still_on_loan list
        else:

            for user in self.loans:

                if user.username == returnee_search:

                    self.loans[user] = still_on_loan

    #method to return all loans of a particular user
    def ReturnAllUserLoans(self):

        print ("Return All Loans of a User")
        
        username_flag = 0

        #standard code to find the user object that matches what the user inputs
        borrower_search = input("Please type in the username of the borrower: ")

        for user in self.loans:

            if user.username == borrower_search:

                #access the value of the appropriate key in the loans dictionary and store it 
                borrowed_book_list = self.loans[user]

                username_flag = 1

        if username_flag == 0:

            print ("Sorry username not found!")

            return

        #display how many books out on loan
        print (borrower_search, "has", len(borrowed_book_list), "books out on loan.")

        #then print the details for each book individually
        print ("Here are the books that", borrower_search, "has out on loan:")

        for book in borrowed_book_list:

            print("\n")

            book.PrintInfo()

        #returning the list of books just to be on the safe side as am unsure what is being requested
        #in the specification
        return borrowed_book_list

    #method to return all books out on loan
    #I was completely unsure what the spec was asking for with this so I wrote the method to return all books that
    #are currently being borrowed. At no point in the spec are we asked to write methods or attributes to deal with
    #loan lengths so without such attributes or methods no books can be overdue
    def ReturnOverdueBooks(self):

        print ("Return Overdue Books")

        overdue_books = []

        count = 0
        
        #simple for loop to get the user name and the first name of users that have borrowed books
        for borrower in self.loans:

            overdue_books.append([])

            overdue_books[count].append(borrower.ReturnUsername())

            overdue_books[count].append(borrower.ReturnFirstName())
            
            #simple for loop to get the title of all the books the current user has borrowed
            for book in self.loans[borrower]:

                overdue_books[count].append(book.ReturnTitle())

            count += 1

        #printing and returning the overdue_books list as unclear if it needed to be returned or displayed
        print (overdue_books)

        return overdue_books

    #method to return the borrower details of a specific book
    def ReturnBorrowerDetails(self):

        print ("Return Borrower Details")

        book_flag = 0
        
        borrowed_book_search = input("Please type in the title of the book to see the borrower information for: ")

        borrowers = []
        
        #simple code to find the book by iterating first through the users and then all the books a user has
        #out on loan
        for user in self.loans:

            for book in self.loans[user]:

                if borrowed_book_search == book.title:
                    
                    #if book is found then firstname surname and email are appended to the borrowers list using
                    #the appropriate built in methods
                    borrowers.append([user.ReturnFirstName(), user.ReturnSurname(), user.ReturnEmail()])

                

                book_flag = 1
                
        if book_flag == 0:

            print ("Book not found!")

        else:

            print ("Here are the details of the users borrowing this book: ")

            #nested for loops to print the details neatly
            for element in borrowers:

                for item in element:

                    print (item)

        #returning the borrowers list just to be on the safe side and make sure I meet the specification
        return borrowers

        
    

    
#initialise a Loans() object
loanlist = Loans()


#references
#https://stackoverflow.com/questions/2349991/how-to-import-other-python-files#:~:text=the%20best%20way%20to%20import%20.py%20files%20is,for%20making%2C%20importing%2C%20and%20setting%20up%20python%20packages.
