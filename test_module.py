'''
Assignment 2
Daniel Parris
CETM73
'''

#This is the testing module

import loan_module
import pytest

#class to test the user class
#The below link helped me name my test classes and methods correctly:
#https://stackoverflow.com/questions/37353960/pytest-exits-with-no-error-but-with-collected-0-items
class TestUser:

    def test_user(self):
        
        first_user = loan_module.user_module.Users("CillitBang", "Barry", "Scott", "6a", "Brook Street", "bn26 6bg", "my@email.com", 19830319)
    
        assert first_user.ReturnFirstName() == "Barry"
        
        assert first_user.ReturnSurname() == "Scott"
        
        assert first_user.ReturnPostcode() == "bn26 6bg"

class TestUserList:

    def test_user_list(self):

        first_user_list = loan_module.user_module.UserList()

        first_user = loan_module.user_module.Users("CillitBang", "Barry", "Scott", "6a", "Brook Street", "bn26 6bg", "my@email.com", 19830319)

        second_user = loan_module.user_module.Users("DeontayWiilder", "Deontay", "Wilder", "57", "Sleepy Street", "po25 7jf", "deontay@wilder.com", 19851029)

        first_user_list.AddUser(first_user)

        first_user_list.AddUser(second_user)

        assert first_user_list.collection_of_users[0].ReturnFirstName() == "Barry"

        assert first_user_list.collection_of_users[1].ReturnFirstName() == "Deontay"

        

class TestBook:

    def test_book(self):

        first_book = loan_module.book_module.Books("Data Analytics For Absolute Beginners", "Oliver Theobald", 2019, "Independent", 56, 20192107)

        assert first_book.ReturnTitle() == "Data Analytics For Absolute Beginners"

        assert first_book.ReturnYear() == 2019

        assert first_book.ReturnPubDate() == 20192107

class TestBookList:

    def test_book_list(self):

        first_book = loan_module.book_module.Books("Data Analytics For Absolute Beginners", "Oliver Theobald", 2019, "Independent", 56, 20192107)

        first_book_list = loan_module.book_module.BookList()

        first_book_list.AddBook(first_book)

        assert first_book_list.collection_of_books[0].ReturnTitle() == "Data Analytics For Absolute Beginners"
        


#I researched how to pre-empt inputs using pytest but wasn't able to get it working sadly so this test class is incomplete
#reference - https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
        #https://stackoverflow.com/questions/59986625/how-to-simulate-two-consecutive-console-inputs-with-pytest-monkeypatch?noredirect=1&lq=1
'''
class TestLoans:

    first_book = loan_module.book_module.Books("Data Analytics For Absolute Beginners", "Oliver Theobald", 2019, "Independent", 56, 20192107)

    first_book_list = loan_module.book_module.BookList()

    first_user = loan_module.user_module.Users("CillitBang", "Barry", "Scott", "6a", "Brook Street", "bn26 6bg", "my@email.com", 19830319)

    first_loan_list = loan_module.Loans()
    

    responses = iter(['CillitBang', 'Data Analytics For Absolute Beginners'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
'''
    

    

