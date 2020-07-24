from datetime import date
from datetime import datetime
class Account:

    """
    General Account Class
    """
    
    def __init__(self, name, phone, acc_no, bal):
        """
        Constructor function for the Account Class
        Executed by interpreter to create an instance of this class.
        Attributes:
            self.name -- name of the Account holder (str)
            self.phno -- phone number of the Account holder (int) 
            self.acc_no -- Account number(int)
            self.bal -- Account balance (float)
             
        """
        self.name = name
        self.phno = phone
        self.acc_no = acc_no
        self.bal = bal
        

    def deposit(self, amt):
        '''
            Gets the amount and withdraws from the total balance
        '''
        self.bal += amt


    def withdraw(self, amt):   
        '''
            Gets the amount and deposita from the total balance
        ''' 
        self.bal -= amt

    def get_balance(self):
        '''
            Displays the balance amount
        '''
        today = date.today()
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print("Date:", today,"    Time:",time)
        print("Current Balance:", self.bal)

    def get_account_details(self):
        '''
        displays the Accunt holder details
        '''
        today = date.today()
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print("Date:", today,"    Time:",time) 
        print("Account Holders name: ",self.name, "\nphone number: ",self.phno, "\nAccount number :",self.acc_no, "\nBalance: ",self.bal)











'''class SavingsAccount(Account):
    """Child Class"""

    # overriding
    def withdraw(self, amt):
        if self.bal - amt <= 5000:
            print("Unable to withdraw, Insufficient Balance!")
        else:
            self.bal -= amt'''