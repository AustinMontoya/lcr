import json

result = {}

def create(request, id):
	if request is None:
		result['success'] = False
		result['error'] = "request data was not found"
	else:
		result['success'] = True

	# handle multi and inline parameters in request

	result['id'] = "id of the newly created resource"

	return json.dumps(result)

def retrieve(request, id):
	if request is None:
		result['success'] = False
		result['error'] = "request data was not found"
	else:
		result['success'] = True

	# handle metadata parameter

	result['document'] = json.dumps({'filename':'value','description':'value2'})

	return json.dumps(result)

def update(request, id):
	if request is None:
		result['success'] = False
		result['error'] = "request data was not found"
	else:
		result['success'] = True

	return json.dumps(result)

def delete(request, id):
	if request is None:
		result['success'] = False
		result['error'] = "request data was not found"
	else:
		result['success'] = True

	return json.dumps(result)