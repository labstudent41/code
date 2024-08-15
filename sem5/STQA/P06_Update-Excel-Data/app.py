import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    df = pd.read_excel("student-records.xlsx")
    data = df.to_dict('records')
    return render_template("index.html", data=data)

app.run()
