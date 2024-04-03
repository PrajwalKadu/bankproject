from register import SignUp, SignIn
from bank import Bank
from database import createcustomertable, db_query

# Create the customers table if it doesn't exist
createcustomertable()

status = False
user = None  # Initialize user variable to None
print("Welcome to Mohit Banking Project")
while True:
    try:
        register = int(input("1. SignUp\n"
                             "2. SignIn\n"
                             "Choose an option: "))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
                user = SignIn()
                if user:
                    status = True
                    break
        else:
            print("Please Enter Valid Input From Options")

    except ValueError:
        print("Invalid Input. Try Again with Numbers")

# Once signed in, retrieve the account number of the user from the database
if status:
    account_number_query = f"SELECT account_number FROM customers WHERE username = '{user}';"
    account_number_result = db_query(account_number_query)
    if account_number_result:
        account_number = account_number_result[0][0]
        bobj = Bank(user, account_number)  # Initialize Bank object with username and account number
        bobj.create_transaction_table()
    else:
        print("Error: Account number not found in database.")
        status = False

# Now you can proceed with banking functionalities
if status:
    while True:
        print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
        try:
            facility = int(input("1. Balance Enquiry\n"
                                 "2. Cash Deposit\n"
                                 "3. Cash Withdraw\n"
                                 "4. Fund Transfer\n"
                                 "5. Logout\n"
                                 "Choose an option: "))
            if 1 <= facility <= 5:
                if facility == 1:
                    bobj.balanceequiry()
                elif facility == 2:
                    amount = int(input("Enter Amount to Deposit: "))
                    bobj.deposit(amount)
                elif facility == 3:
                    amount = int(input("Enter Amount to Withdraw: "))
                    bobj.withdraw(amount)
                elif facility == 4:
                    receive = input("Enter Receiver Username: ")
                    amount = int(input("Enter Money to Transfer: "))
                    bobj.fundtransfer(receive, amount)
                elif facility == 5:
                    print("Logout successful.")
                    break
            else:
                print("Please Enter Valid Input From Options")

        except ValueError:
            print("Invalid Input. Try Again with Numbers")
else:
    print("Login failed. Exiting...")
