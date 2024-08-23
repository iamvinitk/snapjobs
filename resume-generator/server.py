import os

from flask import Flask, request, send_from_directory

from enums import Section
from main import generate_resume

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/resume", methods=["POST", "GET"])
def resume():
    if request.method == "GET":
        return "Please use POST method to generate resume."
    data = request.get_json()
    file_name = generate_resume(data, {
        Section.EDUCATION: 2,
        Section.EXPERIENCE: 1,
        Section.PROJECTS: 3,
        Section.SKILLS: 4
    })
    return send_from_directory("tmp", file_name, as_attachment=True)
