import numpy as np
import pandas as pd
from numpy import genfromtxt
import csv
from datetime import datetime

trainable_data = []
days = np.array([])
format_str = '%m/%d/%Y'
domestic_count = 0
traveler_count = 0
count = 0
male = 0
female = 0

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        data_in_row = row
        if (line_count != 0):
            if (row[6] != '') and (row[7] != ''):
                if (row[8] != '' and row[10] != ''):
                    if (data_in_row[11] == ''):
                        data_in_row[11] = 0
                    if (data_in_row[12] == ''):
                        data_in_row[12] = 0
                    if (data_in_row[16] == ''):
                        data_in_row[16] = 0
                    if (data_in_row[17] == ''):
                        data_in_row[17] = 0
                    if (data_in_row[18] == ''):
                        data_in_row[18] = 0
                    elif (data_in_row[18] != '0' and data_in_row[18] != '1'):
                        data_in_row[18] = 1
                    if (data_in_row[19] == ''):
                        data_in_row[19] = 0
                    elif (data_in_row[19] != '0' and data_in_row[19] != '1'):
                        data_in_row[19] = 1
                    first_datetime = datetime.strptime(row[8], format_str)
                    last_datetime = datetime.strptime(row[10], format_str)
                    num_of_days = (last_datetime-first_datetime).days
                    if (num_of_days < 0):
                        num_of_days = 0
                    days = np.append(days, num_of_days)
                    if (data_in_row[6] == 'male'):
                        male = 1
                        female = 0
                    else:
                        male = 0
                        female = 1
                    data_in_row.pop(22)
                    data_in_row.pop(21)
                    data_in_row.pop(20)
                    data_in_row.pop(15)
                    data_in_row.pop(14)
                    data_in_row.pop(13)
                    data_in_row.pop(10)
                    data_in_row.pop(9)
                    data_in_row.pop(8)
                    data_in_row.pop(6)
                    data_in_row.pop(3)
                    data_in_row.pop(2)
                    data_in_row.pop(1)
                    data_in_row.pop(0)
                    data_in_row.append(male)
                    data_in_row.append(female)
                    data_in_row.append(num_of_days)
                    array = np.array(data_in_row)
                    trainable_data.extend(array)
        else:
            data_in_row.pop(22)
            data_in_row.pop(21)
            data_in_row.pop(20)
            data_in_row.pop(15)
            data_in_row.pop(14)
            data_in_row.pop(13)
            data_in_row.pop(10)
            data_in_row.pop(9)
            data_in_row.pop(8)
            data_in_row.pop(6)
            data_in_row.pop(3)
            data_in_row.pop(2)
            data_in_row.pop(1)
            data_in_row.pop(0)
            data_in_row.append('male')
            data_in_row.append('female')
            data_in_row.append('number of days between symptom onset and hospitalization')
            array = np.array(data_in_row)
            trainable_data.extend(array)
        line_count += 1
trainable_data = np.array(trainable_data)
num_of_cols = 12
num_of_rows = int(trainable_data.size/num_of_cols)
trainable_data = np.reshape(trainable_data, (num_of_rows, num_of_cols))
pd.DataFrame(trainable_data).to_csv('processed_data.csv', index=False, header=False)
