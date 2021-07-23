from bs4 import BeautifulSoup
from datetime import datetime, timedelta

import requests
import json
import math
import csv
import re
import numpy as np

class DataParser:
    BASE_URL = 'https://www.worldometers.info/coronavirus'

    @staticmethod
    def save_data_to_file(filename, data):
        data_to_save = []

        for i in range(0, len(data)):
            data_to_save.append([i, data[i]])

        with open('datasets/' + filename, 'w', newline='') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerows(data_to_save)

    @staticmethod
    def get_dataset_file_name(dataset_prefix, dataset_date=''):
        filename = dataset_prefix + '_dataset_'
        if dataset_date == '':
            filename += datetime.today().strftime('%Y-%m-%d')
        else:
            filename += dataset_date

        filename += '.csv'

        return filename

    @staticmethod
    def create_date_axis_forward(dataset):

        january = datetime(2020, 1, 23)
        date_list = [int(datetime.timestamp(january + timedelta(days=x)) * 1000) for x in range(len(dataset))]

        return list(date_list)

    @staticmethod
    def create_date_axis(dataset):

        yesterday = datetime.now() - timedelta(days=1)
        date_list = [int(datetime.timestamp(yesterday - timedelta(days=x)) * 1000) for x in range(len(dataset))]

        return date_list[::-1]

    def scrape_table(self):
        pass
        # rewrite method





class UpdatesDataParser(DataParser):

    def __init__(self):
        super()

    @staticmethod
    def get_updates():
        url = DataParser.BASE_URL
        r = requests.get(url)
        content = r.content

        soup = BeautifulSoup(content, 'html.parser')

        allData = soup.find_all('tr', class_="total_row_world")

        test = soup.find_all('tr', style_="")

        
        testData = []
        index = 0

        for item in test:
            index += 1
            
            # print("-------------")

            if(index>231):
                break
            
            elif(index>9):
                num = 0
                for tag in item:
                    num += 1
                    if(num == 26):
                        # print(tag.text)
                        testData.append((tag.text.replace(",","")))
            
        

        newTestData = []
        totalTest = 0
        for i in range(len(testData)):
            if testData[i]!= "":
                newTestData.append(int(testData[i]))
                totalTest += int(testData[i])
            else:
                newTestData.append(None)

        for data in allData:
            try:
                data.nobr.getText()==""
                    
            except:
                worldData = data
                break

        number = 0
        for item in worldData:
        
            
            if(number == 5):
                totalCase = item
            elif(number == 7):
                newCases = item
            elif(number == 9):
                totalDeaths = item
            elif(number == 11):
                newDeaths = item
            elif(number == 13):
                totalRecover = item
            elif(number == 15):
                newRecover = item
            elif(number == 17):
                activeCases = item
            elif(number == 19):
                criticalCases = item
            

            number +=1


        numTotalcase=totalCase.text.replace(",","")
        numnewCases = newCases.text[1:].replace(",","")
        numtotalDeaths = totalDeaths.text.replace(",","")
        numnewDeaths = newDeaths.text[1:].replace(",","")
        totalRecover = totalRecover.text.replace(",","")
        numnewRecover = newRecover.text[1:].replace(",","")
        numactiveCases = activeCases.text.replace(",","")
        criticalCases = criticalCases.text.replace(",","")

        return {"totalTest": totalTest,
                "totalCases":numTotalcase,
                "newCases":numnewCases,
                "totalDeaths":numtotalDeaths,
                "newDeaths":numnewDeaths,
                "totalRecovered":totalRecover,
                "newRecovered":numnewRecover,
                "activeCases":numactiveCases,
                "criticalCases":criticalCases
                }
                

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
def get_nytimes_news():
    news_url="https://rss.nytimes.com/services/xml/rss/nyt/Health.xml"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")
    news_titles = []
    news_descriptions = []
    news_link = []
    news_image = []
    news_date = []
    news_creator = []
    news_folder = "The New York Times"
    # Print news title, url and publish date
    num = 0
    for news in news_list:
        if(("covid" in news.title.text) 
        or ("coronavirus" in news.title.text) 
        or ("Coronavirus" in news.title.text) 
        or ("COVID" in news.title.text)
            or ("Covid" in news.title.text)
        or ("coronavirus" in news.description.text) 
        or ("Coronavirus" in news.description.text) 
        or ("covid" in news.description.text)
        or ("COVID" in news.description.text)
            or ("Covid" in news.description.text)):
            if(news.find("media:content")!=None):
                print(news.title.text)
                news_titles.append(news.title.text)
                print(news.link.text)
                news_link.append(news.link.text)
                print(news.pubDate.text)
                news_date.append(news.pubDate.text[0:16])
                print(news.description.text)
                news_descriptions.append(news.description.text)
                print(news.find("media:content"))
                print(news.find("media:content").get("url"))
                news_image.append(news.find("media:content").get("url"))
                print(news.find("dc:creator").text)
                news_creator.append(news.find("dc:creator").text)
                print("-"*60)
                num +=1

    return {"newsTitle": news_titles,
                    "newsLink":news_link,
                    "newsImage":news_image,
                    "newsDescription":news_descriptions,
                    "newsDate":news_date,
                    "newsCreator":news_creator,
                    "folder": news_folder
                    }


    