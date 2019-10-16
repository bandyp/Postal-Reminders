{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import os\nfrom flask import Flask, render_template, redirect, request, url_for, session\nfrom flask_pymongo import PyMongo\nfrom bson.objectid import ObjectId\n\napp = Flask(__name__)\n\napp.config.from_object(__name__)\napp.config[\"MONGO_DBNAME\"] = 'route_reminders'\napp.config[\"MONGO_URI\"] = 'mongodb+srv://bandyp:Ema1LandreW@myfirstcluster-ehsli.mongodb.net/route_reminders?retryWrites=true&w=majority'\n\nmongo = PyMongo(app)\n\n@app.route('/')\n@app.route('/reminders')\ndef reminders():\n    return render_template(\"login.html\")\n\n@app.route('/insert_login', methods=['POST'])\ndef insert_login():\n    # login form called and results posted to mongo\n    logins = mongo.db.logins\n    logins.insert_one(request.form.to_dict())\n    # go to main page\n    return redirect(url_for('get_incidents'))\n\n@app.route('/get_incidents')\ndef get_incidents():\n    # find incidents and put onto incident template\n    return render_template(\"incidents.html\", incidents=mongo.db.incidents.find())\n\n@app.route('/insert_hazard', methods=['POST'])\ndef insert_hazard():\n    # insert new hazard onto incident page\n    incidents = mongo.db.incidents\n    incidents.insert_one(request.form.to_dict())\n    return redirect(url_for('get_incidents'))\n    \n@app.route('/searches', methods=['POST'])\ndef searches():\n    # post the street name from the search form. \n    if request.method == 'POST':\n        search_result = request.form.get('search')\n        results = mongo.db.incidents.find({\"street_name\":search_result})\n        # print results of the search to the searched template\n        print(results)\n        return render_template(\"searched.html\", results=results) \n    else:\n        return redirect(url_for('get_incidents'))\n\n@app.route('/goto_home')\ndef goto_home():\n    # function to return to incident page\n    return render_template(\"incidents.html\", incidents=mongo.db.incidents.find(), logins=mongo.db.logins.find())    \n\n@app.route('/add_hazard')\ndef add_hazard():\n    # goto add hazard html template\n    return render_template(\"addhazard.html\", walk_340=mongo.db.walk_340.find())\n    \n@app.route('/add_access')\ndef add_access():\n    # goto add access issue html template\n    return render_template(\"addaccess.html\", walk_340=mongo.db.walk_340.find())\n    \n@app.route('/add_request')\ndef add_request():\n    # goto add request html template\n    return render_template(\"addrequest.html\", walk_340=mongo.db.walk_340.find())\n\n@app.route('/edit_incident/<incident_id>')\ndef edit_incident(incident_id):\n    # edit incident page\n    the_incident =  mongo.db.incidents.find_one({\"_id\": ObjectId(incident_id)})\n    return render_template('editincident.html', incident=the_incident, walk_340=mongo.db.walk_340.find())\n\n@app.route('/update_incident/<incident_id>', methods=[\"POST\"])\ndef update_incident(incident_id):\n    incidents = mongo.db.incidents\n    # update incident after editing\n    incidents.update( {'_id': ObjectId(incident_id)},\n    {\n        'number':request.form.get('number'),\n        'street_name':request.form.get('street_name'),\n        'incident_description': request.form.get('incident_description'),\n        'comments': request.form.get('comments'),\n        'date_reported': request.form.get('date_reported'),\n        'management_aware':request.form.get('management_aware')\n    })\n    return redirect(url_for('get_incidents'))\n\n@app.route('/delete_incident/<incident_id>')\ndef delete_incident(incident_id):\n    # delete incidents from mongodb\n    mongo.db.incidents.remove({'_id': ObjectId(incident_id)})\n    return redirect(url_for('see_route'))\n    \n@app.route('/see_route')\ndef see_route():\n    # function to view expanded table\n    return render_template(\"route.html\", incidents=mongo.db.incidents.find(), logins=mongo.db.logins.find())\n\nif __name__ == '__main__':\n    app.run(host=os.environ.get('IP'),\n            port=int(os.environ.get('PORT')),\n            debug=True)\n            \n            ","undoManager":{"mark":60,"position":100,"stack":[[{"start":{"row":43,"column":10},"end":{"row":43,"column":11},"action":"insert","lines":[" "],"id":1608}],[{"start":{"row":43,"column":11},"end":{"row":43,"column":12},"action":"insert","lines":["r"],"id":1609},{"start":{"row":43,"column":12},"end":{"row":43,"column":13},"action":"insert","lines":["e"]},{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"insert","lines":["s"]},{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":["u"]},{"start":{"row":43,"column":15},"end":{"row":43,"column":16},"action":"insert","lines":["l"]},{"start":{"row":43,"column":16},"end":{"row":43,"column":17},"action":"insert","lines":["t"]},{"start":{"row":43,"column":17},"end":{"row":43,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"insert","lines":[" "],"id":1610},{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["="]}],[{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":[" "],"id":1611}],[{"start":{"row":43,"column":21},"end":{"row":43,"column":23},"action":"insert","lines":["\"\""],"id":1612}],[{"start":{"row":43,"column":23},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":1613},{"start":{"row":44,"column":0},"end":{"row":44,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":44,"column":8},"end":{"row":44,"column":12},"action":"insert","lines":["    "],"id":1614}],[{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["p"],"id":1615},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["r"]},{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["i"]},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["n"]},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":44,"column":17},"end":{"row":44,"column":19},"action":"insert","lines":["()"],"id":1616}],[{"start":{"row":44,"column":18},"end":{"row":44,"column":19},"action":"insert","lines":["N"],"id":1617},{"start":{"row":44,"column":19},"end":{"row":44,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":[" "],"id":1618},{"start":{"row":44,"column":21},"end":{"row":44,"column":22},"action":"insert","lines":["r"]},{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"insert","lines":["e"]},{"start":{"row":44,"column":23},"end":{"row":44,"column":24},"action":"insert","lines":["m"]},{"start":{"row":44,"column":24},"end":{"row":44,"column":25},"action":"insert","lines":["i"]},{"start":{"row":44,"column":25},"end":{"row":44,"column":26},"action":"insert","lines":["n"]},{"start":{"row":44,"column":26},"end":{"row":44,"column":27},"action":"insert","lines":["d"]},{"start":{"row":44,"column":27},"end":{"row":44,"column":28},"action":"insert","lines":["e"]},{"start":{"row":44,"column":28},"end":{"row":44,"column":29},"action":"insert","lines":["r"]},{"start":{"row":44,"column":29},"end":{"row":44,"column":30},"action":"insert","lines":["s"]}],[{"start":{"row":44,"column":30},"end":{"row":44,"column":31},"action":"insert","lines":[" "],"id":1619},{"start":{"row":44,"column":31},"end":{"row":44,"column":32},"action":"insert","lines":["a"]},{"start":{"row":44,"column":32},"end":{"row":44,"column":33},"action":"insert","lines":["v"]},{"start":{"row":44,"column":33},"end":{"row":44,"column":34},"action":"insert","lines":["a"]},{"start":{"row":44,"column":34},"end":{"row":44,"column":35},"action":"insert","lines":["i"]},{"start":{"row":44,"column":35},"end":{"row":44,"column":36},"action":"insert","lines":["l"]},{"start":{"row":44,"column":36},"end":{"row":44,"column":37},"action":"insert","lines":["a"]},{"start":{"row":44,"column":37},"end":{"row":44,"column":38},"action":"insert","lines":["b"]},{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"insert","lines":["l"]}],[{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"insert","lines":["e"],"id":1620},{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"insert","lines":["."]}],[{"start":{"row":44,"column":41},"end":{"row":44,"column":42},"action":"insert","lines":[" "],"id":1621}],[{"start":{"row":44,"column":42},"end":{"row":44,"column":43},"action":"insert","lines":["P"],"id":1622},{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"insert","lines":["l"]},{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"insert","lines":["e"]},{"start":{"row":44,"column":45},"end":{"row":44,"column":46},"action":"insert","lines":["a"]},{"start":{"row":44,"column":46},"end":{"row":44,"column":47},"action":"insert","lines":["s"]},{"start":{"row":44,"column":47},"end":{"row":44,"column":48},"action":"insert","lines":["e"]}],[{"start":{"row":44,"column":48},"end":{"row":44,"column":49},"action":"insert","lines":[" "],"id":1623},{"start":{"row":44,"column":49},"end":{"row":44,"column":50},"action":"insert","lines":["c"]},{"start":{"row":44,"column":50},"end":{"row":44,"column":51},"action":"insert","lines":["h"]},{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"insert","lines":["e"]},{"start":{"row":44,"column":52},"end":{"row":44,"column":53},"action":"insert","lines":["c"]},{"start":{"row":44,"column":53},"end":{"row":44,"column":54},"action":"insert","lines":["k"]}],[{"start":{"row":44,"column":54},"end":{"row":44,"column":55},"action":"insert","lines":[" "],"id":1624},{"start":{"row":44,"column":55},"end":{"row":44,"column":56},"action":"insert","lines":["s"]},{"start":{"row":44,"column":56},"end":{"row":44,"column":57},"action":"insert","lines":["p"]},{"start":{"row":44,"column":57},"end":{"row":44,"column":58},"action":"insert","lines":["e"]},{"start":{"row":44,"column":58},"end":{"row":44,"column":59},"action":"insert","lines":["l"]},{"start":{"row":44,"column":59},"end":{"row":44,"column":60},"action":"insert","lines":["l"]},{"start":{"row":44,"column":60},"end":{"row":44,"column":61},"action":"insert","lines":["i"]},{"start":{"row":44,"column":61},"end":{"row":44,"column":62},"action":"insert","lines":["n"]},{"start":{"row":44,"column":62},"end":{"row":44,"column":63},"action":"insert","lines":["g"]}],[{"start":{"row":44,"column":63},"end":{"row":44,"column":64},"action":"insert","lines":["."],"id":1625}],[{"start":{"row":44,"column":65},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":1626},{"start":{"row":45,"column":0},"end":{"row":45,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"insert","lines":["e"],"id":1627},{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"insert","lines":[";"]},{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"insert","lines":["s"]},{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"remove","lines":["e"],"id":1628},{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"remove","lines":["s"]},{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"remove","lines":[";"]}],[{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"insert","lines":["l"],"id":1629},{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"insert","lines":["s"]},{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":45,"column":12},"end":{"row":45,"column":13},"action":"insert","lines":[":"],"id":1630}],[{"start":{"row":46,"column":8},"end":{"row":46,"column":12},"action":"insert","lines":["    "],"id":1631}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":12},"action":"insert","lines":["    "],"id":1632}],[{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["="],"id":1633}],[{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["("],"id":1634}],[{"start":{"row":43,"column":25},"end":{"row":43,"column":26},"action":"insert","lines":[")"],"id":1635}],[{"start":{"row":42,"column":72},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":1636},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"insert","lines":["        "]},{"start":{"row":43,"column":8},"end":{"row":43,"column":9},"action":"insert","lines":["c"]},{"start":{"row":43,"column":9},"end":{"row":43,"column":10},"action":"insert","lines":["o"]},{"start":{"row":43,"column":10},"end":{"row":43,"column":11},"action":"insert","lines":["u"]},{"start":{"row":43,"column":11},"end":{"row":43,"column":12},"action":"insert","lines":["n"]},{"start":{"row":43,"column":12},"end":{"row":43,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"insert","lines":[" "],"id":1637},{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":43,"column":15},"end":{"row":43,"column":16},"action":"insert","lines":[" "],"id":1638}],[{"start":{"row":43,"column":16},"end":{"row":43,"column":17},"action":"insert","lines":["m"],"id":1639},{"start":{"row":43,"column":17},"end":{"row":43,"column":18},"action":"insert","lines":["o"]},{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"insert","lines":["n"]},{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["g"]},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["o"]},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["."]}],[{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["d"],"id":1640},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["b"]}],[{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"insert","lines":["."],"id":1641}],[{"start":{"row":43,"column":13},"end":{"row":43,"column":14},"action":"insert","lines":["e"],"id":1642},{"start":{"row":43,"column":14},"end":{"row":43,"column":15},"action":"insert","lines":["d"]}],[{"start":{"row":43,"column":26},"end":{"row":43,"column":27},"action":"remove","lines":["."],"id":1643},{"start":{"row":43,"column":25},"end":{"row":43,"column":26},"action":"remove","lines":["b"]},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"remove","lines":["d"]},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"remove","lines":["."]},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"remove","lines":["o"]},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"remove","lines":["g"]},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"remove","lines":["n"]},{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"remove","lines":["o"]},{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"remove","lines":["m"]}],[{"start":{"row":43,"column":18},"end":{"row":43,"column":19},"action":"insert","lines":["r"],"id":1644},{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["e"]},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["s"]},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["u"]},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["l"]},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["t"]},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"insert","lines":["s"]}],[{"start":{"row":43,"column":25},"end":{"row":43,"column":26},"action":"insert","lines":["."],"id":1645},{"start":{"row":43,"column":26},"end":{"row":43,"column":27},"action":"insert","lines":["c"]},{"start":{"row":43,"column":27},"end":{"row":43,"column":28},"action":"insert","lines":["o"]},{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"insert","lines":["u"]},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["n"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["t"]}],[{"start":{"row":43,"column":31},"end":{"row":43,"column":33},"action":"insert","lines":["()"],"id":1646}],[{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"remove","lines":["s"],"id":1647},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"remove","lines":["t"]},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"remove","lines":["l"]},{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"remove","lines":["u"]},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"remove","lines":["s"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"remove","lines":["e"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"remove","lines":["r"]}],[{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["c"],"id":1648},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["o"]},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["u"]},{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["n"]},{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":["t"]},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["e"]},{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"insert","lines":["d"]}],[{"start":{"row":44,"column":25},"end":{"row":44,"column":26},"action":"remove","lines":[")"],"id":1649},{"start":{"row":44,"column":24},"end":{"row":44,"column":25},"action":"remove","lines":["\""]},{"start":{"row":44,"column":23},"end":{"row":44,"column":24},"action":"remove","lines":["\""]},{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"remove","lines":["("]}],[{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"insert","lines":["0"],"id":1650}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"remove","lines":["="],"id":1651}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":["="],"id":1652}],[{"start":{"row":44,"column":23},"end":{"row":44,"column":24},"action":"insert","lines":[";"],"id":1653}],[{"start":{"row":44,"column":23},"end":{"row":44,"column":24},"action":"remove","lines":[";"],"id":1654}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"remove","lines":["="],"id":1655}],[{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":["="],"id":1656}],[{"start":{"row":44,"column":21},"end":{"row":44,"column":22},"action":"insert","lines":[">"],"id":1657}],[{"start":{"row":44,"column":21},"end":{"row":44,"column":22},"action":"remove","lines":[">"],"id":1658}],[{"start":{"row":45,"column":18},"end":{"row":45,"column":19},"action":"insert","lines":["\""],"id":1659}],[{"start":{"row":45,"column":65},"end":{"row":45,"column":66},"action":"insert","lines":["\""],"id":1660}],[{"start":{"row":44,"column":23},"end":{"row":44,"column":24},"action":"insert","lines":[":"],"id":1661}],[{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"remove","lines":["0"],"id":1662}],[{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"insert","lines":["1"],"id":1663}],[{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"remove","lines":["1"],"id":1664}],[{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"insert","lines":["0"],"id":1665}],[{"start":{"row":43,"column":0},"end":{"row":46,"column":14},"action":"remove","lines":["        counted = results.count()","        if counted == 0:","            print(\"No reminders available. Please check spelling.\")","        else: "],"id":1666},{"start":{"row":42,"column":72},"end":{"row":43,"column":3},"action":"remove","lines":["","   "]}],[{"start":{"row":43,"column":8},"end":{"row":43,"column":12},"action":"remove","lines":["    "],"id":1716}],[{"start":{"row":44,"column":8},"end":{"row":44,"column":12},"action":"remove","lines":["    "],"id":1717}],[{"start":{"row":76,"column":34},"end":{"row":77,"column":0},"action":"insert","lines":["",""],"id":1718},{"start":{"row":77,"column":0},"end":{"row":77,"column":4},"action":"insert","lines":["    "]},{"start":{"row":77,"column":4},"end":{"row":77,"column":5},"action":"insert","lines":["#"]}],[{"start":{"row":77,"column":5},"end":{"row":77,"column":6},"action":"insert","lines":[" "],"id":1719},{"start":{"row":77,"column":6},"end":{"row":77,"column":7},"action":"insert","lines":["u"]},{"start":{"row":77,"column":7},"end":{"row":77,"column":8},"action":"insert","lines":["p"]},{"start":{"row":77,"column":8},"end":{"row":77,"column":9},"action":"insert","lines":["d"]},{"start":{"row":77,"column":9},"end":{"row":77,"column":10},"action":"insert","lines":["a"]},{"start":{"row":77,"column":10},"end":{"row":77,"column":11},"action":"insert","lines":["t"]},{"start":{"row":77,"column":11},"end":{"row":77,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":77,"column":12},"end":{"row":77,"column":13},"action":"insert","lines":[" "],"id":1720}],[{"start":{"row":77,"column":13},"end":{"row":77,"column":14},"action":"insert","lines":["i"],"id":1721},{"start":{"row":77,"column":14},"end":{"row":77,"column":15},"action":"insert","lines":["n"]},{"start":{"row":77,"column":15},"end":{"row":77,"column":16},"action":"insert","lines":["c"]},{"start":{"row":77,"column":16},"end":{"row":77,"column":17},"action":"insert","lines":["i"]},{"start":{"row":77,"column":17},"end":{"row":77,"column":18},"action":"insert","lines":["d"]},{"start":{"row":77,"column":18},"end":{"row":77,"column":19},"action":"insert","lines":["e"]},{"start":{"row":77,"column":19},"end":{"row":77,"column":20},"action":"insert","lines":["n"]},{"start":{"row":77,"column":20},"end":{"row":77,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":77,"column":21},"end":{"row":77,"column":22},"action":"insert","lines":[" "],"id":1722},{"start":{"row":77,"column":22},"end":{"row":77,"column":23},"action":"insert","lines":["a"]},{"start":{"row":77,"column":23},"end":{"row":77,"column":24},"action":"insert","lines":["f"]},{"start":{"row":77,"column":24},"end":{"row":77,"column":25},"action":"insert","lines":["t"]},{"start":{"row":77,"column":25},"end":{"row":77,"column":26},"action":"insert","lines":["e"]},{"start":{"row":77,"column":26},"end":{"row":77,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":77,"column":27},"end":{"row":77,"column":28},"action":"insert","lines":[" "],"id":1723},{"start":{"row":77,"column":28},"end":{"row":77,"column":29},"action":"insert","lines":["e"]},{"start":{"row":77,"column":29},"end":{"row":77,"column":30},"action":"insert","lines":["d"]},{"start":{"row":77,"column":30},"end":{"row":77,"column":31},"action":"insert","lines":["i"]},{"start":{"row":77,"column":31},"end":{"row":77,"column":32},"action":"insert","lines":["t"]},{"start":{"row":77,"column":32},"end":{"row":77,"column":33},"action":"insert","lines":["i"]},{"start":{"row":77,"column":33},"end":{"row":77,"column":34},"action":"insert","lines":["n"]},{"start":{"row":77,"column":34},"end":{"row":77,"column":35},"action":"insert","lines":["g"]}],[{"start":{"row":39,"column":15},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":1724},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"insert","lines":["#"]}],[{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":[" "],"id":1725}],[{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["p"],"id":1726},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["o"]},{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["s"]},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":[" "],"id":1727}],[{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["t"],"id":1728},{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"insert","lines":["h"]},{"start":{"row":40,"column":13},"end":{"row":40,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":40,"column":14},"end":{"row":40,"column":15},"action":"insert","lines":[" "],"id":1729},{"start":{"row":40,"column":15},"end":{"row":40,"column":16},"action":"insert","lines":["s"]},{"start":{"row":40,"column":16},"end":{"row":40,"column":17},"action":"insert","lines":["t"]},{"start":{"row":40,"column":17},"end":{"row":40,"column":18},"action":"insert","lines":["r"]},{"start":{"row":40,"column":18},"end":{"row":40,"column":19},"action":"insert","lines":["e"]},{"start":{"row":40,"column":19},"end":{"row":40,"column":20},"action":"insert","lines":["e"]},{"start":{"row":40,"column":20},"end":{"row":40,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":40,"column":21},"end":{"row":40,"column":22},"action":"insert","lines":[" "],"id":1730},{"start":{"row":40,"column":22},"end":{"row":40,"column":23},"action":"insert","lines":["n"]},{"start":{"row":40,"column":23},"end":{"row":40,"column":24},"action":"insert","lines":["a"]},{"start":{"row":40,"column":24},"end":{"row":40,"column":25},"action":"insert","lines":["m"]},{"start":{"row":40,"column":25},"end":{"row":40,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":40,"column":26},"end":{"row":40,"column":27},"action":"insert","lines":[" "],"id":1731},{"start":{"row":40,"column":27},"end":{"row":40,"column":28},"action":"insert","lines":["f"]},{"start":{"row":40,"column":28},"end":{"row":40,"column":29},"action":"insert","lines":["r"]},{"start":{"row":40,"column":29},"end":{"row":40,"column":30},"action":"insert","lines":["o"]},{"start":{"row":40,"column":30},"end":{"row":40,"column":31},"action":"insert","lines":["m"]}],[{"start":{"row":40,"column":31},"end":{"row":40,"column":32},"action":"insert","lines":[" "],"id":1732},{"start":{"row":40,"column":32},"end":{"row":40,"column":33},"action":"insert","lines":["t"]},{"start":{"row":40,"column":33},"end":{"row":40,"column":34},"action":"insert","lines":["h"]},{"start":{"row":40,"column":34},"end":{"row":40,"column":35},"action":"insert","lines":["e"]}],[{"start":{"row":40,"column":35},"end":{"row":40,"column":36},"action":"insert","lines":[" "],"id":1733},{"start":{"row":40,"column":36},"end":{"row":40,"column":37},"action":"insert","lines":["s"]},{"start":{"row":40,"column":37},"end":{"row":40,"column":38},"action":"insert","lines":["e"]},{"start":{"row":40,"column":38},"end":{"row":40,"column":39},"action":"insert","lines":["a"]},{"start":{"row":40,"column":39},"end":{"row":40,"column":40},"action":"insert","lines":["r"]},{"start":{"row":40,"column":40},"end":{"row":40,"column":41},"action":"insert","lines":["c"]},{"start":{"row":40,"column":41},"end":{"row":40,"column":42},"action":"insert","lines":["h"]}],[{"start":{"row":40,"column":42},"end":{"row":40,"column":43},"action":"insert","lines":[" "],"id":1734},{"start":{"row":40,"column":43},"end":{"row":40,"column":44},"action":"insert","lines":["f"]},{"start":{"row":40,"column":44},"end":{"row":40,"column":45},"action":"insert","lines":["o"]},{"start":{"row":40,"column":45},"end":{"row":40,"column":46},"action":"insert","lines":["r"]},{"start":{"row":40,"column":46},"end":{"row":40,"column":47},"action":"insert","lines":["m"]}],[{"start":{"row":40,"column":47},"end":{"row":40,"column":48},"action":"insert","lines":["."],"id":1735}],[{"start":{"row":40,"column":48},"end":{"row":40,"column":49},"action":"insert","lines":[" "],"id":1736}],[{"start":{"row":43,"column":72},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":1737},{"start":{"row":44,"column":0},"end":{"row":44,"column":8},"action":"insert","lines":["        "]},{"start":{"row":44,"column":8},"end":{"row":44,"column":9},"action":"insert","lines":["#"]}],[{"start":{"row":44,"column":9},"end":{"row":44,"column":10},"action":"insert","lines":[" "],"id":1738},{"start":{"row":44,"column":10},"end":{"row":44,"column":11},"action":"insert","lines":["p"]},{"start":{"row":44,"column":11},"end":{"row":44,"column":12},"action":"insert","lines":["r"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["t"]},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["i"]},{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["n"]}],[{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"remove","lines":["n"],"id":1739},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"remove","lines":["i"]},{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"remove","lines":["t"]}],[{"start":{"row":44,"column":12},"end":{"row":44,"column":13},"action":"insert","lines":["i"],"id":1740},{"start":{"row":44,"column":13},"end":{"row":44,"column":14},"action":"insert","lines":["n"]},{"start":{"row":44,"column":14},"end":{"row":44,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":44,"column":15},"end":{"row":44,"column":16},"action":"insert","lines":[" "],"id":1741},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["r"]},{"start":{"row":44,"column":17},"end":{"row":44,"column":18},"action":"insert","lines":["e"]},{"start":{"row":44,"column":18},"end":{"row":44,"column":19},"action":"insert","lines":["s"]},{"start":{"row":44,"column":19},"end":{"row":44,"column":20},"action":"insert","lines":["u"]},{"start":{"row":44,"column":20},"end":{"row":44,"column":21},"action":"insert","lines":["l"]},{"start":{"row":44,"column":21},"end":{"row":44,"column":22},"action":"insert","lines":["t"]},{"start":{"row":44,"column":22},"end":{"row":44,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":44,"column":23},"end":{"row":44,"column":24},"action":"insert","lines":[" "],"id":1742},{"start":{"row":44,"column":24},"end":{"row":44,"column":25},"action":"insert","lines":["o"]},{"start":{"row":44,"column":25},"end":{"row":44,"column":26},"action":"insert","lines":["f"]}],[{"start":{"row":44,"column":26},"end":{"row":44,"column":27},"action":"insert","lines":[" "],"id":1743},{"start":{"row":44,"column":27},"end":{"row":44,"column":28},"action":"insert","lines":["t"]},{"start":{"row":44,"column":28},"end":{"row":44,"column":29},"action":"insert","lines":["h"]},{"start":{"row":44,"column":29},"end":{"row":44,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":44,"column":30},"end":{"row":44,"column":31},"action":"insert","lines":[" "],"id":1744},{"start":{"row":44,"column":31},"end":{"row":44,"column":32},"action":"insert","lines":["s"]},{"start":{"row":44,"column":32},"end":{"row":44,"column":33},"action":"insert","lines":["e"]},{"start":{"row":44,"column":33},"end":{"row":44,"column":34},"action":"insert","lines":["a"]},{"start":{"row":44,"column":34},"end":{"row":44,"column":35},"action":"insert","lines":["r"]},{"start":{"row":44,"column":35},"end":{"row":44,"column":36},"action":"insert","lines":["c"]},{"start":{"row":44,"column":36},"end":{"row":44,"column":37},"action":"insert","lines":["h"]}],[{"start":{"row":44,"column":37},"end":{"row":44,"column":38},"action":"insert","lines":[" "],"id":1745}],[{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"insert","lines":["i"],"id":1746},{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"insert","lines":["n"]}],[{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"insert","lines":[" "],"id":1747}],[{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"remove","lines":[" "],"id":1748},{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"remove","lines":["n"]},{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"remove","lines":["i"]}],[{"start":{"row":44,"column":38},"end":{"row":44,"column":39},"action":"insert","lines":["t"],"id":1749},{"start":{"row":44,"column":39},"end":{"row":44,"column":40},"action":"insert","lines":["o"]}],[{"start":{"row":44,"column":40},"end":{"row":44,"column":41},"action":"insert","lines":[" "],"id":1750},{"start":{"row":44,"column":41},"end":{"row":44,"column":42},"action":"insert","lines":["t"]},{"start":{"row":44,"column":42},"end":{"row":44,"column":43},"action":"insert","lines":["e"]},{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"insert","lines":["h"]}],[{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"insert","lines":[" "],"id":1751}],[{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"remove","lines":[" "],"id":1752},{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"remove","lines":["h"]},{"start":{"row":44,"column":42},"end":{"row":44,"column":43},"action":"remove","lines":["e"]}],[{"start":{"row":44,"column":42},"end":{"row":44,"column":43},"action":"insert","lines":["h"],"id":1753},{"start":{"row":44,"column":43},"end":{"row":44,"column":44},"action":"insert","lines":["e"]}],[{"start":{"row":44,"column":44},"end":{"row":44,"column":45},"action":"insert","lines":[" "],"id":1754},{"start":{"row":44,"column":45},"end":{"row":44,"column":46},"action":"insert","lines":["s"]},{"start":{"row":44,"column":46},"end":{"row":44,"column":47},"action":"insert","lines":["e"]},{"start":{"row":44,"column":47},"end":{"row":44,"column":48},"action":"insert","lines":["a"]}],[{"start":{"row":44,"column":48},"end":{"row":44,"column":49},"action":"insert","lines":["r"],"id":1755},{"start":{"row":44,"column":49},"end":{"row":44,"column":50},"action":"insert","lines":["c"]},{"start":{"row":44,"column":50},"end":{"row":44,"column":51},"action":"insert","lines":["h"]},{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"insert","lines":["e"]},{"start":{"row":44,"column":52},"end":{"row":44,"column":53},"action":"insert","lines":["d"]}],[{"start":{"row":44,"column":53},"end":{"row":44,"column":54},"action":"insert","lines":[" "],"id":1756},{"start":{"row":44,"column":54},"end":{"row":44,"column":55},"action":"insert","lines":["t"]},{"start":{"row":44,"column":55},"end":{"row":44,"column":56},"action":"insert","lines":["e"]},{"start":{"row":44,"column":56},"end":{"row":44,"column":57},"action":"insert","lines":["m"]},{"start":{"row":44,"column":57},"end":{"row":44,"column":58},"action":"insert","lines":["p"]},{"start":{"row":44,"column":58},"end":{"row":44,"column":59},"action":"insert","lines":["l"]},{"start":{"row":44,"column":59},"end":{"row":44,"column":60},"action":"insert","lines":["a"]}],[{"start":{"row":44,"column":60},"end":{"row":44,"column":61},"action":"insert","lines":["t"],"id":1757},{"start":{"row":44,"column":61},"end":{"row":44,"column":62},"action":"insert","lines":["e"]}]]},"ace":{"folds":[],"scrolltop":480,"scrollleft":0,"selection":{"start":{"row":44,"column":62},"end":{"row":44,"column":62},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":23,"state":"start","mode":"ace/mode/python"}},"timestamp":1571179703983}