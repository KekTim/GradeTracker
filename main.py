# to create database if it deletet 
import database

from flask import Flask, redirect, request, render_template
import sqlite3
import uuid
import datetime
import bcrypt
import os

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test():
    return render_template("test.html")

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

#--------------------

@app.route("/api/users/", methods=["GET", "PUT", "DELETE"])
def users():
    pass

@app.route("/api/users/password", methods=["PUT"])
def users_password():
    pass

@app.route("/api/users/signup", methods=["POST"])
def users_signup():
    pass

@app.route("/api/users/login", methods=["POST"])
def users_login():
    pass

@app.route("/api/users/image", methods=["POST"])
def users_image():
    pass

@app.route("/api/users/image/<image_id>", methods=["GET"])
def users_image_imageID(image_id):
    pass

#--------------------

@app.route("/api/users/friends", methods=["GET"])
def users_friends():
    pass

@app.route("/api/users/friends/<user_id>", methods=["GET", "POST", "PUT", "DELETE"])
def users_friends(user_id):
    pass

@app.route("/api/users/<user_id>/subjects", methods=["GET"])
def users_userID_subjects(user_id):
    pass

@app.route("/api/users/<user_id>/exams", methods=["GET"])
def users_userID_exams(user_id):
    pass

@app.route("/api/users/<user_id>/image/<image_id>", methods=["GET"])
def users_userID_image_imageID(image_id):
    pass

#--------------------

@app.route("/api/users/subjects", methods=["GET", "POST"])
def users_subjects():
    pass

@app.route("/api/users/subjects/<subject_id>", methods=["PUT", "DELETE"])
def users_subjects_subjectID(subject_id):
    pass

#--------------------

@app.route("/api/users/exams", methods=["GET", "POST"])
def users_subjects():
    pass

@app.route("/api/users/exams/<exam_id>", methods=["PUT", "DELETE"])
def users_subjects(exam_id):
    pass

#--------------------

if __name__ == '__main__':
    app.run(debug=True) 