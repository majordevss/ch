import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://test-clone-3ead3-default-rtdb.firebaseio.com/"})
ref = db.reference("apps").child("complusxmessengerandroid")

# Write the data to the database

import json

# Step 1: Read JSON data from file
with open('config.json', 'r') as json_file:
    json_data = json_file.read()

# Step 2: Parse JSON data
try:
    parsed_data = json.loads(json_data)
    print(parsed_data)
    ref.update(parsed_data)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)

