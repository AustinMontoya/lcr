from repo import app, db, fs
from flask import request, url_for, render_template
import models
import forms

COMING_SOON_MSG = "Coming Soon!"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
	'''POST -- Creates a Learning Object and stores any associated files.
	   GET -- Returns the view for creating a Learning Object and uploading any associated files.'''
	if request.method == 'POST':
		# to be called via ajax only.
		# Steps:
		# 1. create the Learning Object from the POST information
		# 2. store any files and associate them with the newly created object
		# 3. return some json containing at least the id for the Learning Object so that 
		#	 a client-side redirect can be performed to the new view.
		return COMING_SOON_MSG
	else:
		return render_template("create.html", form=forms.CreateForm())

@app.route('/show/<learningObjId>/<fieldName>', methods=['GET', 'POST'])
def show(learningObjId, fieldName=None):
	'''POST /show/learningObjId/ -- Returns all of the associated metadata for a Learning Object as json.
	   POST /show/learningObjId/fieldName -- Returns the data for a particular field.
	   GET /show/learningObjId -- Returns the view for a learning object and its associated metadata.'''
	if request.method == 'POST':
		return COMING_SOON_MSG