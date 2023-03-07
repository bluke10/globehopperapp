#Connect to mySQL Database 
#python -m pip install mysql-connector-python

import mysql.connector

myconn = mysql.connector.connect(
    host="localhost",
    user="ally",
    password="allyfinancial123",
    database="globehopperapp"
)
