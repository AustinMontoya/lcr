from repo import app, db, fs
from flask import request, make_response, url_for, render_template
import models
import resourcecontroller
import contentcontroller

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

# Content CRUD routes ---------------------------------
# Create (supports optional inline and multi parameters)
@app.route('/api/create/content/', methods=['POST'])
def CreateContent():
	return contentcontroller.create(request) 

# Retrieve
@app.route('/api/content/<id>', methods=['GET'])
def RetrieveContent(id):
	return contentcontroller.retrieve(request, id) 

# Update
@app.route('/api/update/content/<id>', methods=['POST'])
def UpdateContent(id):
	return contentcontroller.update(request, id) 

# Delete
@app.route('/api/delete/content/<id>', methods=['POST'])
def DeleteContent(id):
	return contentcontroller.delete(request, id) 

# Resource CRUD routes ---------------------------------
# Create (supports optional multi parameters)
@app.route('/api/create/resource/<id>', methods=['POST'])
def CreateResource(id):
	return resourcecontroller.create(request, id) 

# Retrieve
@app.route('/api/resource/<id>', methods=['GET'])
def RetrieveResource(id):
	return resourcecontroller.retrieve(request, id) 

# Update (supports metadata parameter)
@app.route('/api/update/resource/<id>', methods=['POST'])
def UpdateResource(id):
	return resourcecontroller.update(request, id) 

# Delete
@app.route('/api/delete/resource/<id>', methods=['POST'])
def DeleteResource(id):
	return resourcecontroller.content(request, id)