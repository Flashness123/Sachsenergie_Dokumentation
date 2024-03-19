from flask import Flask, jsonify, abort, request
import models
from model import forecast_n_days, forecast_one_day, forecast_validate_date
from prophet import Prophet
app = Flask(__name__)

@app.route('/')
def introduction():
    return 'Home Path of the Prophet API'


@app.route("/forecast-one-day", methods=["POST"])
def get_forecast_one_day():
   
    predictions = forecast_one_day()

    if not predictions:
        abort(400, "Model not found from get_forecast_one_day")

    return jsonify({"forecast": predictions})


@app.route("/forecast-n-days", methods=["POST"])
def get_forecast_n_days():
    if not request.json or not 'days' in request.json:
        predictions = forecast_n_days()
    else:
        predictions = forecast_n_days(request.json['days'])

    if not predictions:
        abort(400, "Model not found.")

    return jsonify({"forecast": predictions})

@app.route("/forecast_validate_date", methods=["POST"])
def get_forecast_validate_date():
    if not request.json or not 'date' in request.json or not 'value' in request.json:
        abort(400, "No date provided or not .json")

    predictions, percentage = forecast_validate_date(request.json['date'], request.json['value'])
    
    return jsonify({"forecast": predictions, "percentage": percentage})

@app.route("/retrain_model", methods=["POST"])
def retrain_model():
    my_model = Prophet(changepoint_prior_scale =  0.4, holidays_prior_scale = 0.5, n_changepoints = 150, seasonality_mode = 'multiplicative')
    # going to the database and getting newest dates
    # test if runable in docker
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000, debug=True)