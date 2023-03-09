#Define all services for Country and City


from flask import Flask, request, jsonify
import conn



#Gets all records from Country table using SQL
def allcountries():
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

def countrybycontinent(continent):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()


    #execute SQL
    values = [continent]
    mysql = "SELECT * FROM Country WHERE Continent = %s;"
    mycursor.execute(mysql,values)
    results = mycursor.fetchall()

    #close connection
    mycursor.close()
    conn.myconn.close()
    return results 

def getcitybycountryid(countryid):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #execute SQL
    values = [countryid]
    mysql = "SELECT * FROM City WHERE CountryId = %s AND Capital = 1;"
    mycursor.execute(mysql, values)
    results = mycursor.fetchall()
    
    #close connection
    mycursor.close()
    conn.myconn.close()
    return results 

#Gets all records from City table using SQL
def allcities():
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #execute SQL
    mycursor.execute("SELECT * FROM City")
    results = mycursor.fetchall()

    #close connection
    mycursor.close()
    conn.myconn.close()
    return results


def createcountry(data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']
    #execute SQL
    mysql = "INSERT INTO Country (CountryId, Name, Population, Continent) VALUES (%s,%s,%s,%s);"
    values = (countryid, name, population, continent)
    mycursor.execute(mysql, values)

    #close connection
    mycursor.close()
    conn.myconn.close()


def createcity(data):
    #open connection
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    cityid = data['CityId']
    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    firstlandmark = data['FirstLandmark']
    secondlandmark = data['SecondLandmark']
    thirdlandmark = data['ThirdLandmark']
    
    #execute SQL
    mysql = "INSERT INTO City (CityId, Name, CountryId, Capital, FirstLandmark, SecondLandmark, ThirdLandmark) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    values = (cityid, name, countryid, capital, firstlandmark, secondlandmark, thirdlandmark)
    mycursor.execute(mysql, values)

    #close connection
    mycursor.close()
    conn.myconn.close()

def updatecountry(country_id, data):
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    countryid = data['CountryId']
    name = data['Name']
    population = data['Population']
    continent = data['Continent']
    values = (countryid, name, population, continent, country_id)
    #execute sql
    mysql = "UPDATE Country SET CountryId = %s, Name = %s, Population = %s, Continent = %s WHERE CountryId = %s;"
    mycursor.execute(mysql, values)

    mycursor.close()
    conn.myconn.close()

def updatecity(city_id, data):
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    cityid = data['CityId']
    name = data['Name']
    countryid = data['CountryId']
    capital = data['Capital']
    firstlandmark = data['FirstLandmark']
    secondlandmark = data['SecondLandmark']
    thirdlandmark = data['ThirdLandmark']
    values = (cityid, name, countryid, capital, firstlandmark, secondlandmark, thirdlandmark, city_id)
    #execute sql
    mysql = "UPDATE City SET CityId = %s, Name = %s, CountryId = %s, Capital = %s, FirstLandmark = %s, SecondLandmark = %s, ThirdLandmark = %s WHERE CityId = %s;"
    mycursor.execute(mysql, values)

    mycursor.close()
    conn.myconn.close()


def deletecountry(countryid):
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #execute sql
    mysql = "DELETE FROM Country WHERE CountryId = %s;"
    mycursor.execute(mysql, [countryid])

    mycursor.close()
    conn.myconn.close()

def deletecity(cityid):
    conn.myconn._open_connection()
    mycursor = conn.myconn.cursor()

    #execute sql
    mysql = "DELETE FROM City WHERE CityId = %s;"
    mycursor.execute(mysql, [cityid])
    mycursor.close()
    conn.myconn.close()

