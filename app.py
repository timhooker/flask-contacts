import os
from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from bson import BSON
from bson import json_util
import json
from datetime import date

app = Flask(__name__)
print(os.environ)
client = MongoClient(
    'docker_db_1',
    27017)

db = client.tododb
count = 0

@app.route('/')
def index():
  """Home route"""
  count = 1
  return render_template("index.html", count=count)

@app.route('/api/hits')
def hits():
  """Test API Route"""
  count = 1
  return jsonify({'hits': count})

@app.route('/api/contacts', methods=['Get'])
def contacts():
  """API for Contacts"""
  contacts = db.contacts
  _contacts = contacts.find()
  contact_list = [contact for contact in _contacts]
  return json.dumps(contact_list, indent=4, default=json_util.default)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
