import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# For classroom testing, set CORS_ORIGINS to a comma-separated list of
# trusted frontend origins. "*" is convenient for a fictional-data demo,
# but should not be used for a production student information system.
allowed_origins = os.getenv("CORS_ORIGINS", "*")
origins = [origin.strip() for origin in allowed_origins.split(",") if origin.strip()]
CORS(app, resources={r"/api/*": {"origins": origins}})

COURSES = [
    {
        "id": 1,
        "code": "ITAS 3228",
        "name": "Web and Mobile Development",
        "description": "Introduction to web and mobile application development."
    },
    {
        "id": 2,
        "code": "SIA 3101",
        "name": "System Integration and Architecture",
        "description": "Fundamentals of connecting applications and services."
    },
    {
        "id": 3,
        "code": "IT 2102",
        "name": "Database Management Systems",
        "description": "Introduction to organizing and managing structured data."
    },
    {
        "id": 4,
        "code": "IT 2204",
        "name": "Networking Fundamentals",
        "description": "Basic concepts of computer networks and communication."
    },
    {
        "id": 5,
        "code": "IT 2305",
        "name": "Human-Computer Interaction",
        "description": "Principles for designing usable digital interfaces."
    }
]


@app.get("/")
def home():
    return jsonify({
        "message": "Welcome to the Student Course API",
        "documentation": "See README.md for available endpoints."
    }), 200


@app.get("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Student Course API is running"
    }), 200


@app.get("/api/courses")
def get_courses():
    return jsonify(COURSES), 200


@app.get("/api/courses/<int:course_id>")
def get_course(course_id):
    course = next((item for item in COURSES if item["id"] == course_id), None)
    if course is None:
        return jsonify({
            "status": "error",
            "message": f"Course with ID {course_id} was not found."
        }), 404
    return jsonify(course), 200


@app.errorhandler(404)
def not_found(_error):
    return jsonify({
        "status": "error",
        "message": "The requested endpoint or resource was not found."
    }), 404


@app.errorhandler(500)
def internal_error(_error):
    return jsonify({
        "status": "error",
        "message": "An unexpected server error occurred."
    }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
