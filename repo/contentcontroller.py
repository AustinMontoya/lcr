import json
import util
import creation


result = {}

def create(request):
	success = True
	error = ''

	if request is None:
		success = False
		error = "request data was not found"

	# handle multi and inline parameters in request
	multi = util.str2bool(request.args.get('multi'))

	if multi is True:
		if request.headers['content-type'] != 'application/json':
			print "request content-type was not application/json"

		if type(request.json) is not list:
			# check to see if it is a single document (i.e., dict)
			pass

	inline = util.str2bool(request.args.get('inline'))

	try:
		result['id'] = creation.create_content(request.json)					
		result['success'] = True
	except Exception as e:
		result['success'] = False
		result['error'] = str(e)

	#if multi is True:
	#	if len(request.json) > 1:
	#		for doc in request.json:
	#			print doc['title']

	if inline is True:
		# parse out resource
		pass

	# create the document in mongo and return the id
	#print request.json

	#for item in request.form:
	#	print 'key: ' + item + ', value: ' + request.form[item]
	#print request.files[1]
	#creation.create_content()

	if success is True:
		result['success'] = True
	else:
		result['success'] = False
		result['error'] = error

	return json.dumps(result)

def retrieve(request, id):
	if request is None:
		result['success'] = False
		result['error'] = "request data was not found"
	else:
		result['success'] = True

	# get the document out of mongo matching the given id
	result['document'] = {'title':'value','description':'value2'}

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