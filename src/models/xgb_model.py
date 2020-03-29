def create_xgboost_model(test_data):
    import os
    import pandas as pd

    data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'datasets', 'data.csv')
    #data_file_path = 'D:/Documents/Leetcode + Foobar + Kaggle/COVIDCalculator/updated_data.csv'
    data = pd.read_csv(data_file_path)

    features = ['age', 'male', 'female', 'symptom_onset_hospitalization', 'mortality_rate', 'pop_density', 'high_risk_travel']
    X = data[features]
    y = data.death

    from xgboost import XGBRegressor
    model = XGBRegressor(n_estimators=100, learning_rate=0.05)
    model.fit(X, y)

    from sklearn.model_selection import cross_val_predict
    from sklearn.metrics import roc_auc_score

    predictions = cross_val_predict(model, X, y, cv=10)
    auc = roc_auc_score(y, predictions)
    #print(auc)

    return model.predict(test_data)

