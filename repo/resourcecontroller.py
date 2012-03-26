from flask import make_response
import json
import util
import crud_helpers
from crud_helpers import HelperException
from crud_helpers import createJsonResponse
from crud_helpers import createErrorResponse

def create(request, id):
	success = True
	result = {}
	error = ''
	status_code = 200

	if request is None:
		success = False
		error = "Bad request.  Somehow the request wasn't found."
		status_code = 400

	if id is None:
		success = False
		error = "Bad request.  Somehow the id wasn't found."
		status_code = 400

	# handle type, name, and multi parameters in request
	resource_type = request.args.get('type')
	resource_name = request.args.get('name')
	multi = util.str2bool(request.args.get('multi'))

	# handle multiple resources
	if multi is True:
		# TODO
		pass

	if resource_type == "url":
		# create a url type resource

		if 'application/json' in request.headers['content-type']:
			# create the content object

			json_data = ''

			try:
				json_data = request.json
			except Exception as e:
				success = False
				error = str(e)
				status_code = 400

			try:
				crud_helpers.create_url_resource(id, json_data, resource_name)
				
			except HelperException as e:
				success = False
				error = e.error
				status_code = e.status_code
		else:
			success = False
			error = "The content-type was not of the expected type.  The content-type found was " + request.headers["content-type"] + ", whereas the content-type expected was application/json."
			status_code = 400

	else:
		success = False
		error = "The resource type was not understood.  The specified value for resource type was " + str(resource_type) + "."
		status_code = 400		

	if success is True:
		response = createJsonResponse(result, status_code)
	else:
		result['error'] = error
		response = createJsonResponse(result, status_code)
	
	return response

def retrieve(request, id, resource_name):
    result = {}
    error = ''

    if request is None:
        return crud_helpers.createErrorResponse("Request data was not found.", 400)

    # retrieve the package
    try:
        package_str = crud_helpers.retrieve_json_package(id)
        package = json.loads(package_str)
    except Exception as e:
        return crud_helpers.createErrorResponse(e.error, e.status_code)

    # get the resource
    try:
        for item in package['resources']:
            if item['name'] == resource_name:
                resource = item
                break
    except Exception as e:
        return crud_helpers.createErrorResponse("An error occured while attempting to get the specified resource. " + str(e), 500)

	# determine the resource type
    if resource['type'] == 'url':
        # make the response and set content type
        result['url'] = resource['url']
        try:
            response = make_response(json.dumps(result), 200)
        except Exception as e:
            return crud_helpers.createErrorResponse("An error occured while attempting to get the URL of the resource. " + str(e), 500)

    	response.headers['content-type'] = "application/json"
    	return response


def update(request, id, resource_number):
	success = True
	result = {}
	error = ''

	if request is None:
		success = False
		error = "Request data was not found."

	if success is True:
		result['success'] = True
	else:
		result['success'] = False
		result['error'] = error

	return json.dumps(result)

def delete(request, id, resource_number):
	success = True
	result = {}
	error = ''

	if request is None:
		success = False
		error = "Request data was not found."

	if success is True:
		result['success'] = True
	else:
		result['success'] = False
		result['error'] = error

	return json.dumps(result)