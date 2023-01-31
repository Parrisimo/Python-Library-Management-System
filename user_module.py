'''
Assignment 2
Daniel Parris
CETM73
'''

#In this module are the Users and UserList classes

class Users:

    #initialising an instance
    def __init__(self, username, first_name, surname, house_no, street_name, postcode, email, DOB):

        self.username = username

        self.first_name = first_name

        self.surname = surname

        self.house_no = house_no

        self.street_name = street_name

        self.postcode = postcode

        self.email = email

        self.DOB = DOB

        #adds instance to the ulist instance of UserList class
        ulist.AddUser(self)

    #simple method to print information about the user
    def PrintInfo(self):
        
        print ("Username:     ", self.username)
        
        print ("First Name:   ", self.first_name)
        
        print ("Surname:      ", self.surname)
        
        print ("House Number: ", self.house_no)
        
        print ("Street Name:  ", self.street_name)
        
        print ("Postcode:     ", self.postcode)
        
        print ("Email:        ", self.email)
        
        print ("DOB:           {}/{}/{}".format (str(self.DOB)[4:6],str(self.DOB)[6:],str(self.DOB)[:4]))

    #methods to return various pieces of information as requested
    def ReturnUsername(self):

        return self.username

    def ReturnFirstName(self):

        return self.first_name

    def ReturnSurname(self):

        return self.surname

    def ReturnHouseNo(self):

        return self.house_no

    def ReturnStreetName(self):

        return self.street_name

    def ReturnPostcode(self):

        return self.postcode

    def ReturnEmail(self):

        return self.email

    def ReturnDOB(self):

        return self.DOB

    #methods to edit the user details as requested
    def EditFirstName(self):

        temp_first = ""

        #simple while loop to prevent the user entering nothing
        while temp_first == "":

            temp_first = input("Please type in the new first name: ")
                
            if temp_first == "":
                
                print ("Please type something!")

        #writes the new name over the one stored in the instance
        self.first_name = temp_first

    #very similar to previous method    
    def EditSurname(self):

        temp_surname = ""
        
        while temp_surname == "":
                
            temp_surname = input("Please type in the new surname: ")
                
            if temp_surname == "":
                
                print ("Please type something!")

        self.surname = temp_surname

    def EditEmail(self):

        temp_email = ""

        #validation to make sure the user is typing in a valid email - it has to have
        #the @ symbol in it to be valid
        while temp_email == "" or "@" not in temp_email:

            
                
            temp_email = input("Please type in the new email: ")

            #appropriate error messages dependent on what the user put in    
            if temp_email == "":
                
                print ("Please type something!")

            elif "@" not in temp_email:

                print ("Please type in a valid email address!")

        self.email = temp_email


    def EditDOB(self):

        temp_year = 0

        temp_DOB = ""
        
        #code to make sure the user puts in a realistic year of birth
        while temp_year < 1900 or temp_year > 2021:

            #try/except to handle the user not typing in a number
            try:

                temp_year = int(input("Please type in your year of birth: "))

            except:

                print("Please type in numbers only!")

        #converted to a string because it's easier to check/handle for dates especially
        #when they might have leading zeros (see below)
        temp_DOB += str(temp_year)

        temp_month = 0

        #making sure the user can only type between 1-12 inclusive
        while temp_month < 1 or temp_month > 12:

            try:

                temp_month = int(input("Please type in your month of birth (1-12): "))

            except:

                print("Please type in numbers only!")

            if temp_month <1 or temp_month>12:

                print ("Please type in a valid number for the month!")
        
        if temp_month <10:

            #adds a leading 0 before months 1-9, as this allows the DOB to follow the
            #format YYYYMMDD
            temp_DOB += "0" + str(temp_month)

        else:

            temp_DOB += str(temp_month)

        temp_day = 0

        #makes sure the user puts a valid day for the majority of the months
        #I thought about doing proper validation to make sure that the user couldn't, for example
        #type in 31 days in June but there were more important things to code.
        while temp_day < 1 or temp_day > 31:

            try:

                temp_day = int(input("Please type in your day of birth: "))

            except:

                print("Please type in numbers only!")

            if temp_day <1 or temp_day>31:

                print ("Please type in a valid number for the day!")

        #adding a leading zero to days < 10 for reasons outlined above
        if temp_day <10:

            temp_DOB += "0" + str(temp_day)

        else:

            temp_DOB += str(temp_day)

        #converting it back into an integer and overwriting the stored value
        self.DOB = int(temp_DOB)

    
    #here are some retrospectively written methods to help with the GUI task
    #on reflection this is how I should have made all the methods but it is too late to change the previous methods now
    def ChangeUsername(self, username):

        self.username = username

    def ChangeHouseNo(self, house_no):

        self.house_no = house_no

    def ChangeStreet(self, street):

        self.street_name = street

    def ChangePostcode(self, postcode):

        self.postcode = postcode
        

######################################################################################################################################################
                
class UserList:

    #empty list where instances of Users() will be stored
    collection_of_users = []

    #simple method to add instances to collection_of_users
    def AddUser(self, user):

        self.collection_of_users.append(user)

    #method to remove a user
    def RemoveUser (self):

        found_flag = 0

        temp_names = []

        temp_usernames = []

        print ("Remove User")

        remove_user = input("Please type in the first name of the account you want to remove: ")
        #iterates through the list of user objects and checks the first name of them all for a match
        for user in self.collection_of_users:

            #checks if first name matches user input
            if user.first_name == remove_user:

                #appends the object to the temp_names list
                #this is because there might be multiple users with the same first name so the user
                #will have the option to pick which account to remove
                temp_names.append(user)

                found_flag = 1

                print ("User removed")

        

        if found_flag == 0:

            print ("User not found!")

        #handles instances where there are more than one result
        elif len(temp_names)>1:

            print("Search returned more than one account!")

            #prints out the information for the found accounts
            for item in temp_names:

                item.PrintInfo()

                #appends the username to a list for validation
                temp_usernames.append(item.user_name)

            remove_username = ""

            #while loop that keeps going until user types something in the list
            while remove_username not in temp_usernames:

                remove_username = input("Please type in the username of the account you want to remove: ")

                if remove_username not in temp_usernames:

                    print ("Username not found! Please try again")
                    
            #removes the object from the collection of users
            for i in self.collection_of_users:

                if i.user_name == remove_username:

                    self.collection_of_users.remove(i)

        else:

            self.collection_of_users.remove(temp_names[0])


            

            

            
    #simple method to display and return the number of users
    def CountUsers (self):

        print("The total number of users registered on the system is:", len(self.collection_of_users))

        return len(self.collection_of_users)
    
    #another simple method to display the details of a specified user using the extra PrintInfo() method
    def DisplayUserDetails(self):

        found_flag = 0

        print ("Display User Details")

        user_details = input("Please type in the username you want to see the details of: ")

        for i in self.collection_of_users:

            if i.username == user_details:

                i.PrintInfo()

                found_flag = 1

        if found_flag == 0:

            print ("User not found!")

    
#setting up an instance of UserList()
ulist = UserList()

#sample users to populate the system
a = Users("CillitBang", "Barry", "Scott", "6a", "Brook Street", "bn26 6bg", "my@email.com", 19830319)

b = Users("DeontayWiilder", "Deontay", "Wilder", "57", "Sleepy Street", "po25 7jf", "deontay@wilder.com", 19851029)

c = Users("TheCount", "Ted", "Hankey", "180", "The Count Street", "bn7 2xn", "ted@hankey.com", 19652206)



