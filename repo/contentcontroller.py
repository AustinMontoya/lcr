from flask import make_response
from flask import render_template
import json
import util
import crud_helpers

def create(request):
	success = True
	result = {}

	if request is None:
		success = False
		make_response(render_template('not_found.html'), 400)

	# handle multi and inline parameters in request
	multi = util.str2bool(request.args.get('multi'))
	inline = util.str2bool(request.args.get('inline'))

	# handle multiple documents
	if multi is True:
		# TODO

		if type(request.json) is not list:
			# check to see if it is a single document (i.e., dict)
			#if multi is True:
			#	if len(request.json) > 1:
			#		for doc in request.json:
			#			print doc['title']
			pass

	print request.headers['content-type']

	if 'application/json' in request.headers['content-type']:
		# create the content object
		try:
			result['id'] = crud_helpers.create_content(request.json)
		except Exception as e:
			success = False
			error = str(e)
	else:
		success = False
		error = "The content-type was not of the expected type.  The content-type found was " + request.headers["content-type"] + ", whereas the content-type expected was application/json."		

	# handle inline parameter in request
	if inline is True:
		# parse out resource
		pass
		# TODO

	if success is True:
		response = createJsonResponse(result, 200)
	else:
		result['error'] = error
		response = createJsonResponse(result, 400)
	
	return response

def retrieve(request, id):
	# use HTTP status codes
	response = ''

	if request is None:
		response = make_response(render_template('bad_request.html'), 400)

	if id is None:
		response = make_response(render_template('bad_request.html'), 400)
	
	try:
		result = crud_helpers.retrieve_content(id)
		response = createJsonResponse(result, 200)
	except:
		response =  make_response(render_template('not_found.html'), 404)

	return response

def update(request, id):
	success = True
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

def delete(request, id):
	success = True
	error = ''

	if success is True:
		result['success'] = True
	else:
		result['success'] = False
		result['error'] = error

	return json.dumps(result)

def createJsonResponse(doc, status_code):
	response = make_response(json.dumps(doc), status_code)
	response.headers['content-type'] = "application/json"
	return response