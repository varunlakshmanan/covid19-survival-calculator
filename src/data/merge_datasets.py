#!/usr/bin/python3

import pandas as pd


# Mortality rate
df = pd.read_csv('datasets/data.csv')
df2 = pd.read_csv('datasets/mortality_rates.csv')

series = []
for i in df.index:
    if df['country'][i] in df2['country'].values:
        series.append(df2.loc[df2['country'] == df['country'][i]].iloc[0]['mortality_rate'])
        for j in df2.loc[df2['country'] == df['country'][i]].index:
            if not type(df2['state'][j]) == float and df2['state'][j] in df['location'][i]:
                series[-1] = df2['mortality_rate'][j]
                break
    else:
        series.append(0.034) # Worldwide mortality rate
series = pd.Series(series)
df['mortality_rate'] = series


# Population density
df2 = pd.read_csv('datasets/population_density.csv')

series = []
for i in df.index:
    if df['country'][i] in df2['country'].values:
        series.append(df2.loc[df2['country'] == df['country'][i]].iloc[0]['pop_density'])
    else:
        series.append(25)
series = pd.Series(series)
df['pop_density'] = series
df.to_csv('datasets/data.csv', index=False)
