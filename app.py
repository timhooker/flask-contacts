import os
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from bson import json_util
from helpers import filter_contacts, filter_contact
import json
from datetime import date
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

client = MongoClient('www_db_1', 27017)
db = client.tododb

@app.route('/')
def index():
  """Home route"""
  count = db.counter.find_one_and_update({ '_id' : 'a'}, {'$inc' : { 'val' : 1 } })['val']
  return render_template("index.html", count=count)

@app.route('/api/hits')
def hits():
  """Test API Route"""
  count =   count = db.counter.find_one_and_update({ '_id' : 'a'}, {'$inc' : { 'val' : 1 } })['val']
  return jsonify({'hits': count})

@app.route('/api/contacts', methods=['Get'])
def contacts():
  """API for Contacts"""
  contacts = db.contacts
  _contacts = contacts.find()
  """Using helper method to ensure we only return desired information"""
  contact_list = filter_contacts([contact for contact in _contacts])
  return json.dumps(contact_list, indent=4, default=json_util.default)

@app.route('/api/contacts', methods=['POST'])
def new_contact():
  """API for Contacts"""
  contacts = db.contacts
  data = json.loads(request.data)
  """Using helper method to ensure we only save desired information"""
  contact = filter_contact(data)
  if("email" in contact and contact["email"] is not ""):
    contacts.replace_one({"email":data["email"]}, contact, True)
    new_contact = contacts.find_one({"email": contact["email"]})
    return jsonify(filter_contact(new_contact))
  else:
    return jsonify({"msg": "Email is a required key for user data"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=80)
