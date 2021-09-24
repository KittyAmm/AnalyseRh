from flask import Flask, render_template, request
import pandas as pd
import json
import plotly

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

app.run(debug = True)