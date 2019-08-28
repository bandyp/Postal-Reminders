import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'route_reminders'
app.config["MONGO_URI"] = 'mongodb+srv://bandyp:Ema1LandreW@myfirstcluster-ehsli.mongodb.net/route_reminders?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_incidents')
def get_incidents():
    return render_template("incidents.html")

@app.route('/add_incident')
def add_incident():
    return render_template("addincident.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            