import os
import json
import datetime
import pandas as pd
from prophet.serialize import model_from_json

def get_percentage(forecast, actual_value):
    predicted_value = forecast[['yhat']].tail(1).values[0][0]
    print(predicted_value)
    return float(actual_value)/predicted_value*100

def forecast_n_days(days = 7):
    #model_file = "api/Flaskapp/models/prophet_serialized_model.json"
    model_file = "Flaskapp/models/prophet_serialized_model.json"

    if not os.path.exists(model_file):
        print("Model file could not be found")
        return False

    with open(model_file, 'r') as fin:
        model = model_from_json(json.load(fin))

    #generate future dates

    dates = pd.date_range(start=datetime.datetime.now().date(), end=datetime.datetime.now().date() + datetime.timedelta(days=days), freq='D')
    future = pd.DataFrame({"ds": dates})
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(days).to_dict("records")

def forecast_one_day():
    print("Accessed forecast_one_day")
    #model_file = "api/Flaskapp/models/prophet_serialized_model.json"
    model_file = "Flaskapp/models/prophet_serialized_model.json"

    if not os.path.exists(model_file):
        print("Model file could not be found from forecast_one_day()")
        return False
    
    with open(model_file, 'r') as fin:
        model = model_from_json(json.load(fin)) 

    dates = pd.date_range(start=datetime.datetime.now().date(), end=datetime.datetime.now().date() + datetime.timedelta(days=1), freq='D')
    future = pd.DataFrame({"ds": dates})  
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(1).to_dict("records")

def forecast_validate_date(posted_date, value):
    model_file = "Flaskapp/models/prophet_serialized_model.json"
    if not os.path.exists(model_file):
        print("Model file could not be found")
        return False

    with open(model_file, 'r') as fin:
        model = model_from_json(json.load(fin))
    
    print("Model found and loaded")
    print("Date is: " + posted_date)
    print("Value is: " + value)
    date = pd.to_datetime(posted_date)
    future = pd.DataFrame({"ds": [date]})
    forecast = model.predict(future)
    percentage = get_percentage(forecast, value)
    print(percentage)

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(1).to_dict("records"), percentage