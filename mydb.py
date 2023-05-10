# Install Mysql on your computer
# pip install mysql on virtual environment
# pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'M@14032012%l',
)

"""
# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE pi1_univesp")

print("All Done!")
"""