from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from subprocess import Popen, PIPE
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from data import dataset


def index(request):
    return HttpResponse('Hello world!')


def geolocate(request, ip):
    response = requests.get('http://ip-api.com/json/' + ip)
    if not response.status_code == 200:
        return HttpResponse('HTTP 500 Error')
    json_object = json.loads(response.text)
    return HttpResponse(str(json_object))


def get_mortality_rate(request, ip):
    response = requests.get('http://ip-api.com/json/' + ip)
    if not response.status_code == 200:
        return HttpResponse('HTTP 500 Error')
    ip_data = json.loads(response.text)
    if ip_data['country'] == 'United States':
        process = Popen(['../data/worldometers_webscraper.rb'], stdout=PIPE, stderr=PIPE)
        mortality_rate_data = json.loads(process.communicate()[0].decode().strip())
        if ip_data['regionName'] in mortality_rate_data['states']:
            state_index = mortality_rate_data['states'].index(ip_data['regionName'])
            mortality_rate = mortality_rate_data['deaths'][state_index] / mortality_rate_data['cases'][state_index]
            return HttpResponse('Mortality rate in ' + ip_data['regionName'] + ': ' + str(round(mortality_rate * 100, 2)) + "%")
        else:
            pass
            # Get location from all of US
    return HttpResponse('Fix this!')


def update_databases(request, **kwargs):
    dataset.download_us_states_mortality_rates_dataset()
    dataset.download_country_mortality_rates_dataset()
    dataset.merge_mortality_rates_datasets()
    dataset.merge_into_original_dataset()
    return HttpResponse('Test')
