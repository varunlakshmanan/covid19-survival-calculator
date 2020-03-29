def predict(test_data):
    from xgb_model import create_xgboost_model
    xgb_prob = create_xgboost_model(test_data)

    from lgbm_model import create_light_gradient_boosting_model
    lgbm_prob = create_light_gradient_boosting_model(test_data)

    prob_avg = (xgb_prob * 0.51 + lgbm_prob * 0.49) / 2
    return prob_avg

    '''
    condition_weights = {
        'cardiovascular disease': 0.015,
        'diabetes': 0.073,
        'chronic respiratory disease': 0.063,
        'hypertension': 0.06,
        'cancer': 0.056,
        'none': 0.009
    }

    factor = condition_weights[condition] / condition_weights['none']
    adjusted_prob_avg = prob_avg * factor
    if adjusted_prob_avg > 100:
        return 100
    elif adjusted_prob_avg < 0:
        return 0
    return adjusted_prob_avg
    '''

import pandas as pd
import os
import sys

# Random
#df = pd.DataFrame({
#    'age': [17],
#    'male': [1],
#    'female': [0],
#    'symptom_onset_hospitalization': [5],
#    'mortality_rate': [0.013868],
#    'pop_density': [35.766089],
#    'high_risk_travel': [0]
#})

# Dead person: hubei ,china,36,1,1,0,3,0.0468577159628914,148.348833270666,0
#df = pd.DataFrame({
#    'age': [36],
#    'male': [1],
#    'female': [0],
#    'symptom_onset_hospitalization': [3],
#    'mortality_rate': [0.0468577159],
#    'pop_density': [148.3488332],
#    'high_risk_travel': [0]
#})

# Alive person: district of columbia,us,55,0,1,0,8,0.014619883040935672,35.766088580168,0
df = pd.DataFrame({
    'age': [55],
    'male': [1],
    'female': [0],
    'symptom_onset_hospitalization': [8],
    'mortality_rate': [0.01461988],
    'pop_density': [35.7660885],
    'high_risk_travel': [0]
})
print(predict(df))
