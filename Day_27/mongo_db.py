# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo


app = Flask(__name__)

load_dotenv(override=True)
database_url = os.getenv("DATABASE_URL")
client = MongoClient(database_url)


db = client['thirty_days_of_python'] # accessing the database
students = db.students.find().sort('name')
for student in students:
print(student)

students = db.students.find().sort('name',-1)
for student in students:
print(student)
students = db.students.find().sort('age')
for student in students:
print(student)
students = db.students.find().sort('age',-1)
for student in students:
print(student)
app = Flask(__name__)
if __name__ == '__main__':

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)