

from flask import Flask, request, jsonify
import services

#function to get all countries
def getCountries():
    results = services.allCountries()
    return jsonify(results)