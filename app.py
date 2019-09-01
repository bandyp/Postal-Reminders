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
    return render_template("incidents.html", incidents=mongo.db.incidents.find())

@app.route('/add_hazard')
def add_hazard():
    return render_template("addhazard.html")
    
@app.route('/add_access')
def add_access():
    return render_template("addaccess.html")
    
@app.route('/add_request')
def add_request():
    return render_template("addrequest.html")

@app.route('/insert_hazard', methods=['POST'])
def insert_hazard():
    incidents=mongo.db.incidents
    incidents.insert_one(request.form.to.dict())
    return redirect(url_for('get_incidents'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            