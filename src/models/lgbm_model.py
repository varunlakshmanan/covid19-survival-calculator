import os
import pandas as pd

def create_light_gradient_boosting_model(test_data):
    data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'datasets', 'data.csv')
    data = pd.read_csv(data_file_path)

    features = ['age', 'male', 'female', 'symptom_onset_hospitalization', 'mortality_rate', 'pop_density', 'high_risk_travel']
    X = data[features]
    y = data.death

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state=0)

    import lightgbm as lgb
    train_dataset = lgb.Dataset(X_train, label=y_train)
    param = {'num_leaves': 64,
             'objective': 'binary',
             'learning_rate': 0.005,
             'boosting_type': 'dart',
             'max_depth': 8,
             'num_iterations': 500,
             'min_data_in_leaf': 55,
             'metric': 'auc',
             'verbose': -1}
    bst = lgb.train(param, train_dataset, 100, verbose_eval=False)

    from sklearn.metrics import roc_auc_score
    predictions = bst.predict(X_test, num_iteration=bst.best_iteration)
    auc = roc_auc_score(y_test, predictions)
    #print(auc)

    return bst.predict(test_data, num_iteration=bst.best_iteration)
