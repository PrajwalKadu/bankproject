import sqlite3
from pathlib import Path

# Create database file if it doesn't exist
db_file = 'bank.db'
Path(db_file).touch()

# Connect to the database
con = sqlite3.connect(db_file)
cursor = con.cursor()

def db_query(query, parameters=None):
    if parameters:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    return cursor.fetchall()

def createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers
                (username VARCHAR(20) PRIMARY KEY,
                password VARCHAR(20) NOT NULL,
                name VARCHAR(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                status INTEGER NOT NULL)
    ''')

    con.commit()

if __name__ == "__main__":
    createcustomertable()
