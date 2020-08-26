from routes import urls
from os import path
import requests
import json
import datetime
import time


class SpaceXData(object):
    def __init__(self):
        self.todays_date = datetime.date.today()
    def check_data(self):
        # check json data, if data is old then download latest and replace with current
        list = []
        for url in urls:
            request_url = url
            filename = url.replace('https://api.spacexdata.com/v4/', '')
            filename = filename.replace('/','')
            filename = 'data/'+filename+'_'+str(self.todays_date)+'.json'
            if path.exists(filename):
                print(f"File({filename}) already exists")
            else:
                list.append(request_url)
                for x in list:
                    self.fetch_data(x)

    def fetch_data(self, url):
        # download json data from api
        response = requests.get(url).json()
        url = url.replace('https://api.spacexdata.com/v4/', '')
        url = url.replace('/','')
        filename = url+'_'+str(self.todays_date)+'.json'
        with open('data/'+filename, 'w') as f:
            json.dump(response, f)


def menu():
    spacexdata = SpaceXData()
    spacexdata.check_data()

menu()