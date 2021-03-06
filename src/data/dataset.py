#!/usr/bin/python3

import os
import json
import requests
import pandas as pd
from subprocess import Popen, PIPE


def download_us_states_mortality_rates_dataset():
    process = Popen([os.path.join(os.path.dirname(os.path.abspath(__file__)), 'worldometers_webscraper.rb')], stdout=PIPE, stderr=PIPE)
    mortality_rate_data = json.loads(process.communicate()[0].decode().strip())
    df = pd.DataFrame(mortality_rate_data)
    df['mortality_rate'] = pd.Series([df['deaths'][i] / df['cases'][i] if df['cases'][i] > 0 else 0 for i in df.index])
    df['state'] = df['state'].map(lambda x: x.lower() if type(x) == str else x)
    df.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'us_states_mortality_rates.csv'), index=False)


def download_country_mortality_rates_dataset():
    response = requests.get('https://datahub.io/core/covid-19/r/time-series-19-covid-combined.csv')
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'country_mortality_rates.csv'), 'wb') as file:
        file.write(response.content)
    df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'country_mortality_rates.csv'))
    df = df.loc[df['Date'] == df['Date'].max()]
    df = df.drop(['Date', 'Lat', 'Long', 'Recovered'], axis=1)
    df = df.rename(columns={'Deaths': 'deaths', 'Confirmed': 'cases', 'Country/Region': 'country', 'Province/State': 'state'})
    df = df.reset_index(drop=True)
    df['mortality_rate'] = pd.Series([df['deaths'][i] / df['cases'][i] if df['cases'][i] > 0 else 0 for i in df.index])
    df['country'] = df['country'].map(lambda x: x.lower() if type(x) == str else x)
    df['state'] = df['state'].map(lambda x: x.lower() if type(x) == str else x)
    df.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'country_mortality_rates.csv'), index=False)


def merge_mortality_rates_datasets():
    df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'country_mortality_rates.csv'))
    df2 = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'us_states_mortality_rates.csv'))
    df = df.drop(df.loc[df['country'] == 'us'].index)
    df = df.reset_index(drop=True)
    for i in df2.index:
        df = df.append(pd.Series(['us', df2['state'][i], df2['cases'][i], df2['deaths'][i], df2['mortality_rate'][i]], index=['country', 'state', 'cases', 'deaths', 'mortality_rate']), ignore_index=True)
    df = df.sort_values(['country', 'state'])
    df.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'mortality_rates.csv'), index=False)


def merge_into_original_dataset():
    # Mortality rate
    df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'data.csv'))
    df2 = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'mortality_rates.csv'))

    df['mortality_rate'] = pd.Series([get_mortality_rate(df['country'][i], df['region'][i], df=df2) for i in df.index])

    # Population density
    df2 = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'population_density.csv'))

    df['pop_density'] = pd.Series([get_pop_density(df['country'][i], df=df2) for i in df.index])
    df.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'data.csv'), index=False)


def get_mortality_rate(country, region, df=pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'mortality_rates.csv'))):
    if country in df['country'].values:
        mortality_rate = df.loc[df['country'] == country].iloc[0]['mortality_rate']
        for i in df.loc[df['country'] == country].index:
            if not type(df['state'][i]) == float and df['state'][i] in region:
                mortality_rate = df['mortality_rate'][i]
                break
    else:
        mortality_rate = 0.034  # Worldwide mortality rate
    return mortality_rate


def get_pop_density(country, df=pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'datasets', 'population_density.csv'))):
    if country in df['country'].values:
        pop_density = df.loc[df['country'] == country].iloc[0]['pop_density']
    else:
        pop_density = 25  # Worldwide population density
    return pop_density
