from pymongo import MongoClient
from datetime import date

print('Seeding contacts')
client = MongoClient('www_db_1', 27017)

db = client.tododb

"""setting up hits counter to run"""
db.counter.insert({'_id': 'a', 'val': 1})

contacts = db.contacts

contact_list = [{
      "firstname": "Jim",
      "lastname": "Hopper",
      "dob": date(1940,6,6).isoformat(),
      "address": "555 somewhere ln",
      "phone": "555-555-5555",
      "email": "jim@example.com"
    }, 
    {
      "firstname": "Joyce",
      "lastname": "Byers",
      "dob": date(1940,4,23).isoformat(),
      "address": "444 Creepy Rd",
      "phone": "444-444-4444",
      "email": "joyce@example.com"
    }
  ]

contacts.insert_many(contact_list)
