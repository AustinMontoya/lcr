def create(request, id):
	if request is None:
		return "{ Error: 'request data was not found' }" 

	if id is None:
		return "{ Error: 'content id was not found' }" 

	# handle multi parameter in request

	return "{ id: 'id of the newly created resource' }"

def retreive(request, id):
	if request is None:
		return "{ Error: 'request data was not found' }" 

	# handle metadata parameter in request

	return "{ name: 'value', name2, 'value2' }"

def update(request, id):
	if request is None:
		return "{ Error: 'request data was not found' }" 

	return "{ success: 'revision of the object?' }"

def delete(request, id):
	if request is None:
		return "{ Error: 'request data was not found' }" 

	return "{ success: 'transaction id?' }"