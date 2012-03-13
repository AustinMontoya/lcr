from repo import app, db, fs
from flask import request, url_for, render_template
import models
import forms
import LearningObjectController

COMING_SOON_MSG = "Coming Soon!"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create')
def create(jsonString):
	obj = json.loads(jsonString)
	obj["propName"]
	return render_template("create.html")

@app.route('/show')
def show():
	return render_template("show.html")

@app.route('/object/<id>', methods=['GET','POST'])
def object(id):
	return LearningObjectController.handleAction("object", request, id) 

@app.route('/files/', defaults={'id':None}, methods=['GET'])
@app.route('/files/<id>', methods=['GET', 'POST'])
def files(id):
	return LearningObjectController.handleAction("files", request, id)