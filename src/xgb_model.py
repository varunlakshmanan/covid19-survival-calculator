import pandas as pd

data_file_path = 'D:/Documents/Leetcode + Foobar + Kaggle/COVIDCalculator/data.csv'
data = pd.read_csv(data_file_path)

features = ['age', 'international_traveler', 'domestic_traveler', 'male', 'female', 'number of days between symptom onset and hospitalization', 'mortality_rate', 'pop_density']
X = data[features]
y = data.death

from xgboost import XGBRegressor
model = XGBRegressor()
model.fit(X, y)

from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_auc_score

predictions = cross_val_predict(model, X, y, cv=10)
auc = roc_auc_score(y, predictions)
print(auc)

# Scoring for mean absolute error
#from sklearn.model_selection import cross_val_score
#scores = -cross_val_score(model, X, y, scoring='neg_mean_absolute_error', cv=10)
#print(scores.mean())


