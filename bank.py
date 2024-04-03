from database import db_query, con
import datetime

class Bank:
    def __init__(self, username, account_number=None):
        self.__username = username
        self.__account_number = account_number

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")
        con.commit()

    def balanceequiry(self):
        if self.__account_number is not None:
            temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
            print(f"{self.__username} Balance is {temp[0][0]}")
        else:
            print("Error: Account number not available.")

    def deposit(self, amount):
        if self.__account_number is not None:
            temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
            test = amount + temp[0][0]
            db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
            con.commit()
            self.balanceequiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Amount Deposit',"
                     f"'{amount}'"
                     f")")
            print(f"{self.__username} Amount is Sucessfully Depositted into Your Account {self.__account_number}")
        else:
            print("Error: Account number not available.")

    def withdraw(self, amount):
        if self.__account_number is not None:
            temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
            if amount > temp[0][0]:
                print("Insufficient Balance Please Deposit Money")
            else:
                test = temp[0][0] - amount
                db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
                con.commit()
                self.balanceequiry()
                db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Amount Withdraw',"
                         f"'{amount}'"
                         f")")
                print(f"{self.__username} Amount is Sucessfully Withdraw from Your Account {self.__account_number}")
        else:
            print("Error: Account number not available.")

    def fundtransfer(self, receive, amount):
        if self.__account_number is not None:
            temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
            if amount > temp[0][0]:
                print("Insufficient Balance Please Deposit Money")
            else:
                temp2 = db_query(f"SELECT balance FROM customers WHERE username = '{receive}';")
                if temp2:
                    test1 = temp[0][0] - amount
                    test2 = amount + temp2[0][0]
                    db_query(f"UPDATE customers SET balance = '{test1}' WHERE username = '{self.__username}'; ")
                    db_query(f"UPDATE customers SET balance = '{test2}' WHERE username = '{receive}'; ")
                    con.commit()
                    self.balanceequiry()
                    db_query(f"INSERT INTO {receive}_transaction VALUES ("
                             f"'{datetime.datetime.now()}',"
                             f"'{self.__account_number}',"
                             f"'Fund Transfer From {self.__account_number}',"
                             f"'{amount}'"
                             f")")
                    db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                             f"'{datetime.datetime.now()}',"
                             f"'{self.__account_number}',"
                             f"'Fund Transfer -> {receive}',"
                             f"'{amount}'"
                             f")")
                    print(f"{self.__username} Amount is Successfully Transferred from Your Account {self.__account_number} to {receive}'s account.")
                else:
                    print("Error: Receiver's account not found.")
        else:
            print("Error: Account number not available.")
