#Define all services for Country and City


from flask import Flask, request, jsonify
import conn



#Gets all records from Country table using SQL
def allCountries():
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #execute SQL
    mycursor.execute("SELECT * FROM Country")
    results = mycursor.fetchall()

    #close connection
    mycursor.close()
    conn.myconn.close()
    return results