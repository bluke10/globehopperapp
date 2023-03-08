#Starting point of our WebApp - main
#pip install Flask 

from flask import Flask, request, jsonify
import country
import city

#Using Flask framework

app = Flask(__name__)

#Read all countries
@app.route('/countries')
def getallcountries():
    return country.getcountries()

#create a country
@app.route('/countries', methods=['POST'])
def createnewcountry():
    data = request.json
    return country.createcountry(data)

#delete
@app.route('/countries/<int:countryid>', methods=['DELETE'])
def deletecountrybyid(countryid):
    return country.deletecountry(countryid)

#UPDATE country
@app.route('/countries/<int:countryid>', methods=['PUT'])
def updatecountrybyid(countryid):
    data = request.json
    return country.updatecountry(countryid,data)


#Read all cities
@app.route('/cities')
def getallcities():
    return city.getcities()

#create a city
@app.route('/cities', methods=['POST'])
def createnewcity():
    data = request.json
    return city.createcity(data)


#Execute on the terminal
if __name__ == '__main__':
    app.run()