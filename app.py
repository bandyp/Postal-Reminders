import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps, loads


app = Flask(__name__)

app.config.from_object(__name__)
app.config["MONGO_DBNAME"] = 'route_reminders'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

#direct to the initial login page
@app.route('/')
@app.route('/reminders')
def reminders():
    return render_template("login.html")

# login form posted to mongo
@app.route('/insert_login', methods=['POST'])
def insert_login():
    logins = mongo.db.logins
    logins.insert_one(request.form.to_dict())
    # go to main page
    return redirect(url_for('get_incidents'))

# find incidents and put onto incident template
@app.route('/get_incidents')
def get_incidents():
    return render_template("incidents.html", incidents=mongo.db.incidents.find())

# insert new hazard onto incident page
@app.route('/insert_hazard', methods=['POST'])
def insert_hazard():
    incidents = mongo.db.incidents
    incidents.insert_one(request.form.to_dict())
    return redirect(url_for('get_incidents'))

# post the street name from the search form.   
@app.route('/searches', methods=['POST'])
def searches():
    if request.method == 'POST':
        search_result = request.form.get('search')
        results = mongo.db.incidents.find({"street_name":search_result})
        # print results of the search to the searched template
        return render_template("searched.html", results=loads(dumps(results))) 
    else:
        return redirect(url_for('get_incidents'))

# function to return to incident page
@app.route('/goto_home')
def goto_home():
    return render_template("incidents.html", incidents=mongo.db.incidents.find(), logins=mongo.db.logins.find())    

# goto add_hazard html template
@app.route('/add_hazard')
def add_hazard():
    return render_template("addhazard.html", walk_340=mongo.db.walk_340.find())

# goto add access issue html template  
@app.route('/add_access')
def add_access():
    return render_template("addaccess.html", walk_340=mongo.db.walk_340.find())

# goto add request html template    
@app.route('/add_request')
def add_request():
    return render_template("addrequest.html", walk_340=mongo.db.walk_340.find())

# edit incident page
@app.route('/edit_incident/<incident_id>')
def edit_incident(incident_id):
    the_incident =  mongo.db.incidents.find_one({"_id": ObjectId(incident_id)})
    return render_template('editincident.html', incident=the_incident, walk_340=mongo.db.walk_340.find())

# update incident after editing
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

# delete incidents from mongodb
@app.route('/delete_incident/<incident_id>')
def delete_incident(incident_id):
    mongo.db.incidents.remove({'_id': ObjectId(incident_id)})
    return redirect(url_for('see_route'))
    
@app.route('/see_route')
def see_route():
    # function to view expanded table
    return render_template("route.html", incidents=mongo.db.incidents.find(), logins=mongo.db.logins.find())

# function to return to login page
@app.route('/see_login')
def see_login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)