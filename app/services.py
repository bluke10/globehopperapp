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


def createCountry(data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryId = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']
    #execute SQL
    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s,%s,%s,%s);"
    values = (countryId, name, population, continent)
    mycursor.execute(mysql, values)

    #close connection
    mycursor.close()
    conn.myconn.close()