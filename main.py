from flask import Flask
import json
# from flask_login import login_required, current_user
from flask import render_template, request, Blueprint, jsonify, send_file, current_app

import requests
import os

from requests.models import Response

from templates import*
from countryInfo import dataParser
# from api.data_parser.csse_parser import *

def getUpdateData():
    updates = dataParser.UpdatesDataParser()
    updates_data = updates.get_updates()
    # with open('static/landing/allData.txt', 'w') as outfile:
    #     json.dump(updates_data, outfile)
    return updates_data

def getNews():
    news = dataParser.get_nytimes_news()
    print(news)
    return news


app = Flask('__name__', template_folder='templates')

@app.route('/') 
@app.route("/home", methods=['GET', 'POST'])
def home():
    

    return render_template('/landing/index.html',allData = getUpdateData(),news=getNews())
    
@app.route("/live", methods=['GET', 'POST'])
def monitor():
    # url = 'https://media-cdn.factba.se/rss/json/coronavirus.json'

    # r = requests.get(url=url)
    # data = r.json()

    # metrics = data['world']
    # countries = sorted(data['countries'], key=lambda item: (data['countries'][item]['cases']), reverse=True)
    # countries = [data['countries'][item] for item in countries if data['countries'][item]['iso3166-2']]

    # cases = CasesDataParser()
    # cases_data = cases.get_cases()
    return "monitor"
    # return render_template('dashboard/coronavirus/monitor.html')

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    
    return "dashboard"
    # return render_template('dashboard/coronavirus/dashboard.html')

@app.route("/news", methods=['GET', 'POST'])
def news():
    return "Hello News!"

@app.route("/countries", methods=['GET', 'POST'])
def countries():
    countries = CountriesAdvDataParser()
    countries_data = countries.get_countries()

    # return render_template('dashboard/coronavirus/countries.html', countries=countries_data)


@app.route("/countries/<string:country>", methods=['GET', 'POST'])
def single_country():
    population_data = {
        "China": { 'population': '1,439,323,776', 'density': 153, 'land': '9,388,211' },
        "South Korea": { 'population': '51,269,185', 'density': 527, 'land': '97,230' },
        "United States": { 'population': '331,002,651', 'density': 36, 'land': '9,147,420' },
        "United Kingdom": { 'population': '67,886,011', 'density': 281, 'land': '241,930' },
        "Iran": { 'population': '83,992,949', 'density': 52, 'land': '1,628,550' },
        "Italy": { 'population': '60,461,826', 'density': 206, 'land': '294,140' },
        "France": { 'population': '65,273,511', 'density': 119, 'land': '547,557' },
        "Spain": { 'population': '46,754,778', 'density': 94, 'land': '498,800' },
        "Germany": { 'population': '83,783,942', 'density': 153, 'land': '348,560' },
        "Canada": { 'population': '37,742,154', 'density': 4, 'land': '9,093,510' },
        "Australia": { 'population': '25,499,884', 'density': 3, 'land': '7,682,300' },
        "Switzerland": { 'population': '8,654,622', 'density': 219, 'land': '39,516' },

    }

    return "Hello China"

@app.route('/history')
def history():
    return render_template('dashboard/coronavirus/history.html')


@app.route("/predictions", methods=['GET', 'POST'])
def predictions():

    return "Hello Prediction"


@app.route("/documentation", methods=['GET', 'POST'])
def docs():
    return "Hello Documentations"


@app.route('/download_report')
def download_report():

    return "Hello Reports"

@app.route("/api/cases", methods=['GET', 'POST'])
def api_cases():
    cases = CasesDataParser()
    return jsonify(cases.get_cases())