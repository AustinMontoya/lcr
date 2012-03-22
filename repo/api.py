from flask import Blueprint, current_app, request, make_response, url_for, render_template
import resourcecontroller
import packagecontroller
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
@api.route('/package/<id>/resource/<int:resource_number>', methods=['GET'])
def RetrieveResource(id, resource_number):
	return resourcecontroller.retrieve(request, id, resource_number) 

# Update (supports metadata parameter)
@api.route('/update/package/<id>/resource/<int:resource_number>', methods=['POST'])
def UpdateResource(id):
	return resourcecontroller.update(request, id, resource_number) 

# Delete
@api.route('/delete/package/<id>/resource/<int:resource_number>', methods=['POST'])
def DeleteResource(id):
	return resourcecontroller.content(request, id, resource_number)