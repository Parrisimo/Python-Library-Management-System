'''
Assignment 2
Daniel Parris
CETM73
'''

#This is the book module - I have written the Books and BookList classes here as I found it much neater to write
#the whole system over several modules rather than all in one unwieldy module

#importing the random module to generate the random book ID
import random

class Books:
    
    #list to store the collection IDs
    collection_IDs=[0]

    #initialising the object
    def __init__ (self, title, author, year, publisher, number_of_copies, publication_date):
        
        ID = 0

        #simple while loop to ensure that the book ID is unique to that book
        while ID in self.collection_IDs:
            
            ID = random.randint (1,999999)
            
        self.collection_IDs.append(ID)
        
        self.ID = ID
        
        self.title = title
        
        self.author = author
        
        self.year = year
        
        self.publisher = publisher
        
        self.number_of_copies = number_of_copies
        
        self.publication_date = publication_date

        #adds an instance of self to booklist using the appropriate method
        blist.AddBook(self)
        
        
    #methods to change various items as requested
    def ChangeTitle(self, title):
        self.title = title

    def ChangeAuthor(self, author):
        self.author = author

    def ChangeYear(self, year):
        self.year = year

    def ChangePublisher(self, publisher):
        self.publisher = publisher

    def ChangeCopies(self, number_of_copies):
        self.number_of_copies = number_of_copies

    def ChangePubDate(self, publication_date):
        self.publication_date = publication_date

    #methods to edit various items as requested
    def ReturnTitle(self):
        return self.title

    def ReturnAuthor(self):
        return self.author

    def ReturnYear(self):
        return self.year

    def ReturnPublisher(self):
        return self.publisher

    def ReturnCopies(self):
        return self.number_of_copies

    def ReturnPubDate(self):
        return self.publication_date

    #a simple method to print information relating to the object
    def PrintInfo(self):
        
        print ("Title:            ", self.title)
        
        print ("Author:           ", self.author)
        
        print ("Publisher:        ", self.publisher)
        
        print ("Number of copies: ", self.number_of_copies)
        
        print ("Publication date:  {}/{}/{}".format (str(self.publication_date)[4:6],str(self.publication_date)[6:],str(self.publication_date)[:4]))

        print ("Book ID:          ", self.ID)


##########################################################################################################      

class BookList:

    #list which will hold all the instances of the Book class
    collection_of_books =[]

    #method that adds books to the collection_of_books list
    def AddBook(self, Book):
        self.collection_of_books.append(Book)

    
        
       
    #searching the collection method
    #I chose to do this (and the other methods) without arguments as I thought it was neater to have the code
    #requesting user input within this method
    def SearchCollection(self):
        
        userinput = 0

        found_flag = 0

        #code will keep running until userinput is between 1 and 4 inclusive
        while userinput < 1 or userinput > 4:

            #try/except pair used to handle users typing in non integers
            try:

                print ("What do you want to search for?\n1.Title\n2.Author\n3.Publisher\n4.Publication Date")

                userinput = int(input())

                if userinput < 1 or userinput > 4:

                    print ("Input out of range! Please type in a number between 1 and 4")

            except:

                print ("Invalid input, please type in a number between 1 and 4!")

            #if statements to handle the different options a user could have chosen
            #I don't think this was the most efficient way to do this - perhaps sub-routines would have been
            #better and more efficient, but at least here it's easy to read the code
            if userinput == 1:
                
                print ("Search by Title")

                search_title = input("Please type in the title of the book you are looking for: ")
                
                #iterate through the collection of books list
                for book in self.collection_of_books:

                    if book.title == search_title:

                        print ("Search result:")

                        #using the PrintInfo() method to display all the information about the book
                        book.PrintInfo()

                        found_flag = 1

                #handles cases when the user's book couldn't be found
                if found_flag == 0:

                    print ("Sorry, couldn't find it!")
                    
            #these next 3 sections are pretty much identical to the previous section except we're looking for author not the
            #title of the book
            elif userinput == 2:

                print ("Search by Author")

                search_author = input("Please type in the author of the book you are looking for :")

                for book in self.collection_of_books:

                    if book.author == search_author:

                        print ("Search result:")

                        book.PrintInfo()

                        found_flag = 1

                if found_flag == 0:

                    print ("Sorry, couldn't find it!")

            elif userinput == 3:

                print ("Search by Publisher")

                search_publisher = input("Please type in the publisher of the book you are looking for :")

                for book in self.collection_of_books:

                    if book.publisher == search_publisher:

                        print ("Search result:")

                        book.PrintInfo()

                        found_flag = 1

                if found_flag == 0:

                    print ("Sorry, couldn't find it!")

            elif userinput == 4:

                print ("Search by Publication Date")

                search_pub_date = str(input("Please type in the publication date of the book you are looking for :"))

                for book in self.collection_of_books:
                    
                    if str(book.publication_date) == search_pub_date:

                        print ("Search result:")

                        book.PrintInfo()

                        found_flag = 1

                if found_flag == 0:

                    print ("Sorry, couldn't find it!")
            

            
    #method to remove book as requested
    def RemoveBook(self):

        found_flag = 0

        print ("Remove Book")

        remove_title = input("Please type in the title of the book you want to remove: ")

        #iterates through the collection of books list
        for book in self.collection_of_books:

            #checks whether the user input matches the title attribute of the current book object
            if book.title == remove_title:
                
                #removes the whole instance from the list
                self.collection_of_books.remove(book)

                print ("Book removed")

                found_flag = 1

        if found_flag == 0:

            print ("Book not found!")


    #method to return total number of books in the collection
    def ReturnTotal(self):

        book_total = 0

        #iterate through collection of books
        for book in self.collection_of_books:

            #update a running total of the number of total books
            book_total += book.number_of_copies

        print("The total number of books in this collection is:", book_total)

########################################################################################################



#title, author, year, publisher, number_of_copies, publication_date

#creates an instance of the BookList() class - this made it much easier to store the collection of instances
#of Books()
blist = BookList()



#a collection of book objects to populate the system
a = Books("Data Analytics For Absolute Beginners", "Oliver Theobald", 2019, "Independent", 56, 20192107)

b = Books("Machine Learning for Absolute Beginners", "Oliver Theobald", 2020, "Independent", 37, 20203112)

c = Books("Kick the drink... Easily!", "Jason Vale", 2011, "Crown House Publishing", 24, 20110103)

d = Books("Super System 2", "Doyle Brunson", 2004, "Cardoza Publishing", 72, 20043110)

e = Books("Curious George at the Aquarium", "H.A. Rey", 2007, "HMH Books", 54, 20070309)

f = Books("Juice And Blend: 7-day Reset", "Jason Vale", 2021, "Juice Master Publications", 29, 20210106)


#for the video






    




'''
References
https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/
https://vegibit.com/python-class-examples/#:~:text=You%20can%20store%20an%20instance%20of%20a%20class,together%20to%20model%20complex%20situations.%20A%20Battery%20class
https://pythonhowtoprogram.com/how-to-split-and-organise-your-source-code-into-multiple-files-in-python-3/#:~:text=Yes%2C%20we%20can%20split%20our%20source%20code%20into,i.e.%20a%20single%20module%20is%20a%20single.py%20file.
'''
