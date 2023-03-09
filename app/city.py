

from flask import Flask, request, jsonify
import services

#function to get all citiess
def getcities():
    results = services.allcities()

    data = []
    for row in results:
        data.append({
            "CityId" : row[0],
            "Name" : row[1],
            "CountryId" : row[2],
            "Capital" : row[3],
            "FirstLandmark" : row[4],
            "SecondLandmark" : row[5],
            "ThirdLandmark" : row[6],
        })


    return jsonify(data)

def getcitybycountry(countryid):
    result = services.getcitybycountryid(countryid)
    return jsonify(result)

def createcity(data):
    services.createcity(data)
    return jsonify({'message' : 'city created successfully'})


def deletecity(cityid):
    services.deletecity(cityid)
    return jsonify({'message' : 'city deleted successfully'})



def updatecity(cityid, data):
    services.updatecity(cityid, data)
    return jsonify({'message' : 'city updated successfully'})