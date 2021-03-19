#!/usr/bin/env python3
from flask import Flask, request, render_template, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA3_256, MD5
import json
import jwt
import uuid
import requests
import base64
import os
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/webapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = './admin/files/'
db = SQLAlchemy(app)
hasher = SHA3_256.new()


#
#       Place for models
#
class User(db.Model):
    Id = db.Column(db.Integer(), primary_key=True)
    uuid = db.Column(db.String(36), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    admin_cap = db.Column(db.Boolean(), default=False, nullable=False)

    def check_password(self, password):
        return self.password == password


class Notes(db.Model):
    Id = db.Column(db.Integer(), primary_key=True)
    owner_uuid = db.Column(db.String(36), nullable=False)
    title = db.Column(db.String(), nullable=False)
    note = db.Column(db.String(), nullable=False, unique=True)


#
#       Place for utility functions
#

def secureFilename(fileData):
    return fileData


def checkSession(authCookie):
    default = False, False, None
    if authCookie is None:
        return default
    else:
        try:
            payload = jwt.decode(authCookie, key="secret_key", algorithms='HS256')
        except Exception as e:
            print(e)
            return default
        username = payload['username']
        admin_cap = payload['admin_cap']
        user = User.query.filter_by(username=username).first()
        if user is None:
            return default
        else:
            if admin_cap:
                return True, True, user
            else:
                return True, False, user


def signUpValidate(username, email):
    userExists = False
    emailExists = False
    user = User.query.filter_by(username=username).first()
    email = User.query.filter_by(email=email).first()
    if user is not None:
        userExists = True
    if email is not None:
        emailExists = True
    return userExists, emailExists


def loggedIn(username, email, admin_cap=0):
    return jwt.encode({'username': username, 'email': email, 'admin_cap': admin_cap}, "secret_key", algorithm="HS256")


#
#       Place for routes
#

@app.route('/')
def home():
    signedIn, isAdmin, user = checkSession(request.cookies.get('auth'))
    user_uuid = request.cookies.get('uuid')
    return render_template("index.html", signedIn=signedIn, isAdmin=isAdmin, user=user)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", reason=None)
    elif request.method == "POST":
        username = request.form.get('username')
        password = SHA3_256.new(request.form.get('password').encode()).hexdigest()
        email = request.form.get('email')
        userExists, emailExists = signUpValidate(username, email)
        if not userExists and not emailExists:
            new_user = User(username=username, password=password, uuid=str(uuid.uuid4()), email=email)
            db.session.add(new_user)
            db.session.commit()
            response = make_response(redirect("/"))
            response.set_cookie("auth", loggedIn(username=username, email=email))
            response.set_cookie("uuid", new_user.uuid)
            return response, 302
        else:
            return render_template("register.html", reason=(userExists, emailExists))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", reason=None)
    elif request.method == "POST":
        username = request.form.get('username')
        password = SHA3_256.new(request.form.get('password').encode()).hexdigest()
        user = User.query.filter_by(username=username).first()
        if user is None:
            return render_template("login.html", reason="User doesn't exist.")
        elif not user.check_password(password):
            return render_template("login.html", reason="Incorrect Password")
        else:
            response = make_response(redirect("/"))
            response.set_cookie("auth", loggedIn(username, user.email, user.admin_cap))
            response.set_cookie("uuid", user.uuid)
        return response, 302


@app.route('/logout')
def logout():
    response = make_response(redirect("/"))
    response.set_cookie("auth", "", max_age=0)
    response.set_cookie("uuid", "", max_age=0)
    return response, 302


@app.route('/<user_id>/notes')
def notes(user_id):
    
    signedIn, isAdmin, user = checkSession(request.cookies.get('auth'))
    listOfNotes = Notes.query.filter_by(owner_uuid=user_id).all()
    return (render_template("notes.html", signedIn=signedIn, isAdmin=isAdmin, user=user, uuid=user_id,
                            listOfNotes=listOfNotes))


@app.route('/admin')
def admin():
    isSignedIn, isAdmin, user = checkSession(request.cookies.get('auth'))
    if isSignedIn and isAdmin:
        return render_template("admin.html", signedIn=isSignedIn, isAdmin=isAdmin, user=user)
    else:
        return "Forbidden", 403


@app.route('/admin/viewnotes')
def adminViewNotes():
    isSignedIn, isAdmin, user = checkSession(request.cookies.get('auth'))
    if isSignedIn and isAdmin:
        return (render_template("notes.html", signedIn=isSignedIn, isAdmin=isAdmin, listOfNotes=Notes.query.all(),
                                user=user))
    else:
        return "Forbidden", 403



@app.route('/admin/console',methods=["GET", "POST"])
def adminConsole():
    isSignedIn, isAdmin, user = checkSession(request.cookies.get('auth'))
    if isSignedIn and isAdmin:
        if request.method == "GET":
            return (render_template("console.html", signedIn=isSignedIn, isAdmin=isAdmin, listOfNotes=Notes.query.all(),
                                user=user))
        elif request.method == "POST":
            command = request.form.get('command')
            #result = exec(print(command))
            #result = (subprocess.check_output(command, shell=True)).decode('UTF-8')
            #result = os.system(command)
            if ("python" in command) or ("bash" in command):
                print(command)
                result = "For security, bash and python scripts are blocked"
                return render_template('console.html', result=result)
            else:
                result = subprocess.Popen([command], stdout=subprocess.PIPE,shell=True)
                result = (result.stdout.read()).decode('UTF-8')
                return render_template('console.html', result=result)
    else:
        return "Forbidden", 403



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug = True) 

