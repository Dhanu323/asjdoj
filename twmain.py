from testover import Account
"""
BANK ATM Management Application Script
Authors:
    Dhanush Rao H S
"""
Bank_ledger = {}
''' 
Variables
   
   
    ledger (dict) : { Account number : Appointment object}
                            holds All the account holders account number and all there details in the object
    ''' 
print("Welcome to Speckbit Bank")
#Application loop
while True:

     # Print the options in a table and  Taking the user's choice from options as (int)
    print("-"*30)
    ch = int(input("What would u like to do: \n\
        1. Create account\n\
        2. Withdraw\n \
        3. Deposit\n \
        4. Balance\n \
        5. Get Account Deatail\n-->\n"))

    if ch == 1:
        '''
            If user choice is 1 (int) : Creation an object of Account class and passing the attributes
            '''
            # get the  details to create an account
        name = input("Name: ")
        phno = input("Phone: ")
        acc_no = input("Create Account No: ")
        bal = float(input("Enter Initial Bal: "))
# Use the current person's account number an Bank account is created slot save the object
        account =Account(name, phno, acc_no, bal)
       
        Bank_ledger[acc_no] = account

    elif ch == 2:
        #If user choice is 2 (int) - perform withdraw of money
            
        acc_no = input("Enter Account No: ")# get the accountnum
        amount = float(input("Enter Amount: "))# get the amount

        account = Bank_ledger[acc_no]
        account.withdraw(amount)
        account.get_balance()
    elif ch == 3:
        #If user choice is 3 (int) - perform Deposit of money
        acc_no = input("Enter Account No: ")
        amount = float(input("Enter Amount: "))
        account = Bank_ledger[acc_no]
        account.deposit(amount)
        account.get_balance()
    elif ch == 4:
        #If user choice is 4 (int) - Displays Balance amount
        acc_no = input("Enter Account No: ")
        account = Bank_ledger[acc_no]
        account.get_balance()
    elif ch == 5:
        #If user choice is 2 (int) - Displays the account holders details
        acc_no = input("Enter Account No: ")
        account = Bank_ledger[acc_no]
        account.get_account_details()
        
    else:
          # Exit the loop if input is invalid
        break