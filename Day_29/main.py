from flask import Flask, Response, request, jsonify
import json
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGODB_URI")
client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]


@app.route("/api/v1.0/students", methods=["GET"])
def get_students():
    students = db.students.find()
    return Response(dumps(students), mimetype="application/json")


@app.route("/api/v1.0/students/<id>", methods=["GET"])
def get_single_student(id):
    student = db.students.find_one({"_id": ObjectId(id)})
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return Response(dumps(student), mimetype="application/json")


@app.route("/api/v1.0/students", methods=["POST"])
def create_student():
    try:
        name = request.form["name"]
        country = request.form["country"]
        city = request.form["city"]
        skills = request.form["skills"].split(", ")
        bio = request.form["bio"]
        birthyear = request.form["birthyear"]
        created_at = datetime.now()

        student = {
            "name": name,
            "country": country,
            "city": city,
            "birthyear": birthyear,
            "skills": skills,
            "bio": bio,
            "created_at": created_at,
        }

        result = db.students.insert_one(student)
        return jsonify({"message": "Student created", "id": str(result.inserted_id)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/v1.0/students/<id>", methods=["PUT"])
def update_student(id):
    try:
        query = {"_id": ObjectId(id)}
        if not db.students.find_one(query):
            return jsonify({"error": "Student not found"}), 404

        name = request.form["name"]
        country = request.form["country"]
        city = request.form["city"]
        skills = request.form["skills"].split(", ")
        bio = request.form["bio"]
        birthyear = request.form["birthyear"]
        updated_at = datetime.now()

        new_data = {
            "$set": {
                "name": name,
                "country": country,
                "city": city,
                "birthyear": birthyear,
                "skills": skills,
                "bio": bio,
                "updated_at": updated_at,
            }
        }

        db.students.update_one(query, new_data)
        return jsonify({"message": "Student updated successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/v1.0/students/<id>", methods=["DELETE"])
def delete_student(id):
    result = db.students.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"message": "Student deleted successfully"})



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
