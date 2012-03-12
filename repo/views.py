from repo import app, db, fs
from flask import request, url_for, render_template
import models
import forms

COMING_SOON_MSG = "Coming Soon!"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create')
def create():
	return render_template("create.html")

@app.route('/show')
def show():
	return render_template("show.html")

@app.route('/object/<id>/<action>', methods=["POST"]):
def object():
	return LearningObjectController.handleAction(action, id)