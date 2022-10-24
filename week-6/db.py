import mysql.connector
from mysql.connector import errorcode
from __future__ import print_function
from datetime import date, datetime, timedelta



# Connect to our DB
# REMEMBER DO NOT leave your PW on github
# try:
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="5074Av.ril",
#         database="website",
#         charset="utf8",
#     )
# Ｈandle connection errors, use the try statement and catch all errors using the errors.Error exception:
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with your user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#   mydb.close()
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5074Av.ril",
    database="website",
    charset="utf8",
)

cursor = mydb.cursor()

# Insert data into member table
add_member = ("INSERT INTO member "
               "(name, username, password, follower_count, time) "
               " VALUES (%s, %s, %s, 0, current_timestamp())")

cursor.execute(add_member)
mem_no = cursor.lastrowid


# Make sure data is committed to the database
mydb.commit()

