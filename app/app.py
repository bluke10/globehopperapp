#Starting point of our WebApp - main
#pip install Flask 

from flask import Flask, request, jsonify
import country

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
    return country.updatecountry(countryid)


#Execute on the terminal
if __name__ == '__main__':
    app.run()