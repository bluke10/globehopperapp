

from flask import Flask, request, jsonify
import services

#function to get all countries
def getCountries():
    results = services.allCountries()

    data = []
    for row in results:
        data.append({
            "CountryId" : row[0],
            "Name" : row[1],
            "Population"  : row[2],
            "Continent" : row[3]
        })


    return jsonify(data)


def createCountry(data):
    services.createCountry(data)
    return jsonify({'message' : 'data inserted successfully'})