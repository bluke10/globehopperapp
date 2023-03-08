

from flask import Flask, request, jsonify
import services

#function to get all countries
def getcountries():
    results = services.allcountries()

    data = []
    for row in results:
        data.append({
            "CountryId" : row[0],
            "Name" : row[1],
            "Population"  : row[2],
            "Continent" : row[3]
        })


    return jsonify(data)


def createcountry(data):
    services.createcountry(data)
    return jsonify({'message' : 'data inserted successfully'})


def deletecountry(countryid):
    services.deletecountry(countryid)
    return jsonify({'message' : 'country deleted'})



def updatecountry(countryid):
    services.updatecountry(countryid)
    return jsonify({'message' : 'country updated'})