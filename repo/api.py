from flask import Blueprint, current_app, request, make_response, url_for, render_template
import resourcecontroller, packagecontroller, searchcontroller
api = Blueprint('api', __name__, url_prefix='/api')
# Content CRUD routes ---------------------------------
# Create (supports optional inline and multi parameters)
@api.route('/create/package', methods=['POST'])
def CreatePackage():
	return packagecontroller.create(request) 

# Retrieve
@api.route('/package/<id>', methods=['GET'])
def RetrievePackage(id):
	return packagecontroller.retrieve(request, id) 

# Update
@api.route('/update/package/<id>', methods=['POST'])
def UpdatePackage(id):
	return packagecontroller.update(request, id) 

# Delete
@api.route('/delete/package/<id>', methods=['POST'])
def DeletePackage(id):
	return packagecontroller.delete(request, id) 

# Resource CRUD routes ---------------------------------
# Create (supports optional multi parameters)
@api.route('/create/package/<id>/resource', methods=['POST'])
def CreateResource(id):
	return resourcecontroller.create(request, id) 

# Retrieve
@api.route('/package/<id>/resource/<resource_name>', methods=['GET'])
def RetrieveResource(id, resource_name):
	return resourcecontroller.retrieve(request, id, resource_name) 

# Update (supports metadata parameter)
@api.route('/update/package/<id>/resource/<resource_name>', methods=['POST'])
def UpdateResource(id, resource_name):
	return resourcecontroller.update(request, id, resource_name) 

# Delete
@api.route('/delete/package/<id>/resource/<resource_name>', methods=['POST'])
def DeleteResource(id, resource_name):
	return resourcecontroller.content(request, id, resource_name)

# Browsing CRUD routes ---------------------------------

# Lists all the items of a particular tag
@api.route('/tags/<tag>', methods=['GET'])
def GetDocumentsByTag(tag):
	return searchcontroller.get_by_tags([tag])
