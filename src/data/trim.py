import numpy as np
import pandas as pd
import csv

processed_data = []

with open('data1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        high_risk = 0
        if line_count == 0:
            data_in_row = row
            data_in_row.append('High risk travel')
            data_in_row.pop(6)
            data_in_row.pop(5)
            data_in_row.pop(4)
            data_in_row.pop(3)
            processed_data.extend(data_in_row)
            print(data_in_row)
        else:
            if (row[5]=='1' or row[6]=='1'):
                high_risk = 1
            elif(row[3] == '1'):
                high_risk = 1
            data_in_row = row
            data_in_row.append(high_risk)
            data_in_row.pop(6)
            data_in_row.pop(5)
            data_in_row.pop(4)
            data_in_row.pop(3)
            processed_data.extend(data_in_row)
            print(data_in_row)
        line_count+=1
processed_data = np.array(processed_data)
num_of_cols = 10
num_of_rows = int(processed_data.size/num_of_cols)
processed_data = np.reshape(processed_data, (num_of_rows, num_of_cols))
dataframe = pd.DataFrame(processed_data).to_csv('updated_data.csv', index=False, header=False)