from django.shortcuts import render
from django.http import HttpResponse
import os
import sys
import json
import requests
from subprocess import Popen, PIPE
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


def update_databases(request, **kwargs):
    dataset.download_us_states_mortality_rates_dataset()
    dataset.download_country_mortality_rates_dataset()
    dataset.merge_mortality_rates_datasets()
    dataset.merge_into_original_dataset()
    return HttpResponse('Test')
