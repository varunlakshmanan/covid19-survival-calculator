from django.shortcuts import render
from django.http import HttpResponse
import os
import sys
import json
import math
import numpy as np
import requests
import pandas as pd
from subprocess import Popen, PIPE
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from data import dataset
from django.views.decorators.csrf import csrf_exempt
from calculator.models import Person


def index(request):
    return HttpResponse('Hello world!')


def home(request):
    return render(request, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'home.html'), {'title': 'COVID-19 Recovery Calculator'})


# Need a POST request for this API endpoint
# Must be: /predict/IP_ADDRESS_HERE/
# Needs the following POST form data:
#   ip: string representing user's public IP address
#   age: integer representing user age
#   gender: string of either 'male' or 'female'
#   symptom_onset_hospitalization: integer representing the number of days between symptom onset and hospitalization
#   high_risk_travel: string of either 'yes' or 'no'
#   medical_conditions: string representing prior medical conditions (see Google Doc for possible choices)
@csrf_exempt
def predict(request):
    ip = request.POST.get('ip')
    response = requests.get('http://ip-api.com/json/' + ip)
    if not response.status_code == 200:
        return HttpResponse('HTTP 500 Error')
    ip_data = json.loads(response.text)
    region = ip_data['regionName'].lower()
    country = 'us' if ip_data['country'] == 'United States' else ip_data['country'].lower()
    data = {
        'region': region,
        'country': country,
        'age': int(request.POST.get('age')),
        'death': 0,
        'male': 1 - int(request.POST.get('gender').lower() in ['female', 'f']),
        'female': int(request.POST.get('gender').lower() in ['female', 'f']),
        'symptom_onset_hospitalization': int(request.POST.get('symptom_onset_hospitalization')),
        'mortality_rate': dataset.get_mortality_rate(country, region),
        'pop_density': dataset.get_pop_density(country),
        'high_risk_travel': int(request.POST.get('high_risk_travel').lower() in ['yes', 'y'])
    }

    df = pd.DataFrame({k: [v] for k, v in data.items()})

    medical_condition_death_rates = {
        'cardiovascular disease': 0.105,
        'diabetes': 0.073,
        'chronic respiratory disease': 0.063,
        'hypertension': 0.06,
        'cancer': 0.056,
        'none': 0.009
    }

    medical_condition_factor = np.prod([medical_condition_death_rates[x] / medical_condition_death_rates['none'] for x in request.POST.getlist('medical_conditions')])

    medical_condition_factor = 200 / (1 + math.exp(-medical_condition_factor / 100)) - 100 if medical_condition_factor > 1 else 1.0  # Modified sigmoid function

    print(medical_condition_factor)

    p = Person(**data)
    #p.save()

    return HttpResponse(str(list(df.values[0])))


def update_databases(request):
    dataset.download_us_states_mortality_rates_dataset()
    dataset.download_country_mortality_rates_dataset()
    dataset.merge_mortality_rates_datasets()
    dataset.merge_into_original_dataset()
    return HttpResponse('Test')
