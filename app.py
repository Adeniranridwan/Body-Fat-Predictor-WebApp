import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

#load the model
model = pickle.load(open("./lr_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    weight = float(request.form['weight'])
    neck = float(request.form['neck'])
    chest = float(request.form['chest'])
    abdomen = float(request.form['abdomen'])
    hip = float(request.form['hip'])
    thigh = float(request.form['thigh'])
    knee = float(request.form['knee'])
    biceps = float(request.form['biceps'])

    # Use the model to make a prediction
    input_features = [weight, neck, chest, abdomen, hip, thigh, knee, biceps]
    prediction = model.predict([input_features])

    output = float(prediction[0])

    return render_template(
        "index.html", prediction_text="The Body Fat percentage(%)  is :{}".format(output))


if __name__ == "__main__":
    app.run(debug=True)