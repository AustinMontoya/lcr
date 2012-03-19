import json
import util

result = {}

def create(request, id):
	success = True
	error = ''

	if request is None:
		success = False
		error = "Request data was not found."

	# handle multi and inline parameters in request

	result['id'] = "id of the newly created resource"

	if success is True:
		result['success'] = True
	else:
		result['success'] = False
		result['error'] = error

	return json.dumps(result)

def retrieve(request, id):
	success = True
	error = ''

	if request is None:
		success = False
		error = "Request data was not found."

	# handle metadata parameter

	result['document'] = json.dumps({'filename':'value','description':'value2'})

	if success is True:
		result['success'] = True
	else:
		result['success'] = False
		result['error'] = error

	return json.dumps(result)

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

	if request is None:
		success = False
		error = "Request data was not found."

	if success is True:
		result['success'] = True
	else:
		result['success'] = False
		result['error'] = error

	return json.dumps(result)