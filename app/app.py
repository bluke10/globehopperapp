#Starting point of our WebApp - main
#pip install Flask 

from flask import Flask, request, jsonify
import country

#Using Flask framework
app = Flask(__name__)

#Read all countries
@app.route('/countries')
def getAllCountries():
    return country.getCountries()

#create a country
@app.route('/countries', methods=['POST'])
def createNewCountry():
    data = request.json
    return country.createCountry(data)

#Execute on the terminal
if __name__ == '__main__':
    app.run()