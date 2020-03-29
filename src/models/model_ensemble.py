def predict(test_data):
    from xgb_model import create_xgboost_model
    xgb_prob = create_xgboost_model(test_data)

    from lgbm_model import create_light_gradient_boosting_model
    lgbm_prob = create_light_gradient_boosting_model(test_data)

    prob_avg = xgb_prob * 0.51 + lgbm_prob * 0.49
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
