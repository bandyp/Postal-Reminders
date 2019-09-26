import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config.from_object(__name__)
app.config["MONGO_DBNAME"] = 'route_reminders'
app.config["MONGO_URI"] = 'mongodb+srv://bandyp:Ema1LandreW@myfirstcluster-ehsli.mongodb.net/route_reminders?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/reminders')
def reminders():
    return render_template("login.html")

@app.route('/insert_login', methods=['POST'])
def insert_login():
    # login form called and results posted to mongo
    logins = mongo.db.logins
    logins.insert_one(request.form.to_dict())
    # go to main page
    return redirect(url_for('get_incidents'))

@app.route('/get_incidents')
def get_incidents():
    # find incidents and put onto incident template
    return render_template("incidents.html", incidents=mongo.db.incidents.find(), logins=mongo.db.logins.find())

@app.route('/insert_hazard', methods=['POST'])
def insert_hazard():
    # insert new hazard onto incident page
    incidents = mongo.db.incidents
    incidents.insert_one(request.form.to_dict())
    return redirect(url_for('get_incidents'))
    
@app.route('/searches', methods=['POST'])
def searches():
    if request.method == 'POST':
        THE_STRING = request.form.get('search')
        results = mongo.db.find({"street_name":THE_STRING})
        return render_template("route.html", print(results)) 
    else:
        return redirect(url_for('get_incidents'))

@app.route('/goto_home')
def goto_home():
    # function to return to incident page
    return render_template("incidents.html", incidents=mongo.db.incidents.find(), logins=mongo.db.logins.find())    

@app.route('/add_hazard/<logins_id>')
def add_hazard(logins_id):
    new_login = mongo.db.logins.find_one({"_id": ObjectId()})
    all_logins = mongo.db.logins.find()
    # goto add hazard html template
    return render_template("addhazard.html", walk_340=mongo.db.walk_340.find(), login=new_login, logins=all_logins)
    
@app.route('/add_access')
def add_access():
    # goto add access issue html template
    return render_template("addaccess.html", walk_340=mongo.db.walk_340.find())
    
@app.route('/add_request')
def add_request():
    # goto add request html template
    return render_template("addrequest.html", walk_340=mongo.db.walk_340.find())

@app.route('/edit_incident/<incident_id>')
def edit_incident(incident_id):
    # edit incident page
    the_incident =  mongo.db.incidents.find_one({"_id": ObjectId(incident_id)})
    return render_template('editincident.html', incident=the_incident, walk_340=mongo.db.walk_340.find())

@app.route('/update_incident/<incident_id>', methods=["POST"])
def update_incident(incident_id):
    incidents = mongo.db.incidents
    incidents.update( {'_id': ObjectId(incident_id)},
    {
        'number':request.form.get('number'),
        'street_name':request.form.get('street_name'),
        'incident_description': request.form.get('incident_description'),
        'comments': request.form.get('comments'),
        'date_reported': request.form.get('date_reported'),
        'management_aware':request.form.get('management_aware')
    })
    return redirect(url_for('get_incidents'))

@app.route('/delete_incident/<incident_id>')
def delete_incident(incident_id):
    # delete incidents from mongodb
    mongo.db.incidents.remove({'_id': ObjectId(incident_id)})
    return redirect(url_for('see_route'))
    
@app.route('/see_route')
def see_route():
    # function to view expanded table
    return render_template("route.html", incidents=mongo.db.incidents.find(), logins=mongo.db.logins.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            