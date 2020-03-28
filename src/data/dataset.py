#!/usr/bin/python3

import pandas as pd
import numpy as np
import json
import requests
from subprocess import Popen, PIPE


def download_us_states_mortality_rate_dataset():
    process = Popen(['./worldometers_webscraper.rb'], stdout=PIPE, stderr=PIPE)
    mortality_rate_data = json.loads(process.communicate()[0].decode().strip())
    data_frame = pd.DataFrame(mortality_rate_data)
    data_frame['mortality_rate'] = pd.Series([data_frame['deaths'][i] / data_frame['cases'][i] for i in data_frame.index])
    data_frame.to_csv('datasets/us_states_mortality_rates.csv', index=False)


def download_country_mortality_rate_dataset():
    response = requests.get('https://datahub.io/core/covid-19/r/time-series-19-covid-combined.csv')
    with open('datasets/country_mortality_rates.csv', 'wb') as file:
        file.write(response.content)
    data_frame = pd.read_csv('datasets/country_mortality_rates.csv')
    data_frame['mortality_rate'] = pd.Series([data_frame['Deaths'][i] / data_frame['Confirmed'][i] if data_frame['Confirmed'][i] > 0 else 0 for i in data_frame.index])
    data_frame.to_csv('datasets/country_mortality_rates.csv', index=False)


def merge_datasets():


download_country_mortality_rate_dataset()