import os
import pandas as pd
from xgboost import XGBRegressor
# from sklearn.metrics import roc_auc_score
# from sklearn.model_selection import cross_val_predict


def create_xgboost_model(test_data):
    # Read data
    data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'datasets', 'data.csv')
    data = pd.read_csv(data_file_path)

    # Set model features and prediction target
    features = ['age', 'male', 'female', 'symptom_onset_hospitalization', 'mortality_rate', 'pop_density', 'high_risk_travel']
    x = data[features]
    y = data.death

    # Train model
    model = XGBRegressor(n_estimators=100, learning_rate=0.05)
    model.fit(x, y)

    # Perform 10-fold cross validation and find AUC (area under curve) value of model's ROC curve 
    # predictions = cross_val_predict(model, x, y, cv=10)
    # auc = roc_auc_score(y, predictions)
    # print(auc)

    return model.predict(test_data)

