# web_dashboard/app.py

from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        devices = pd.read_csv("data/baseline.csv").to_dict(orient="records")
    except:
        devices = []

    try:
        usage = pd.read_csv("data/usage_logs.csv").to_dict(orient="records")
    except:
        usage = []

    try:
        alerts = pd.read_csv("data/spoof_alerts.csv").to_dict(orient="records")
    except:
        alerts = []

    return render_template("index.html", devices=devices, usage=usage, alerts=alerts)

if __name__ == '__main__':
    app.run(debug=True)
