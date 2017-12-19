import os
from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from bson import BSON
from bson import json_util
import json
from datetime import date

app = Flask(__name__)
print(os.environ)
client = MongoClient('backend_db_1', 27017)

db = client.tododb

@app.route('/')
def index():
  """Home route"""
  db.counter.update({ '_id' : 'a'}, {'$inc' : { 'val' : 1 } })
  count = db.counter.find_one( { '_id' : 'a' })['val']
  return render_template("index.html", count=count)

@app.route('/api/hits')
def hits():
  """Test API Route"""
  db.counter.update({ '_id' : 'a'}, {'$inc' : { 'val' : 1 } })
  count = db.counter.find_one( { '_id' : 'a' })['val']
  return jsonify({'hits': count})

@app.route('/api/contacts', methods=['Get'])
def contacts():
  """API for Contacts"""
  contacts = db.contacts
  _contacts = contacts.find()
  contact_fields = {'firstname', 'lastname', 'dob', 'address', 'phone', 'email'}
  contact_list = [contact for contact in _contacts]
  return json.dumps(contact_list, indent=4, default=json_util.default)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
