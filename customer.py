from database import db_query, con

class Customer:

    def __init__(self, username, password, name, age, city, account_number):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__city = city
        self.__account_number = account_number

    def createuser(self):
        query = "INSERT INTO customers VALUES (?, ?, ?, ?, ?, 0, ?, 1)"
        parameters = (self.__username, self.__password, self.__name, self.__age, self.__city, self.__account_number)
        db_query(query, parameters)
        con.commit()
