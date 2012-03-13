import json
import util
import creation

from werkzeug import secure_filename

result = {}

def create(request):
	if request is None:
		result['success'] = False
		result['error'] = "request data was not found"
	else:
		result['success'] = True

	# handle multi and inline parameters in request
	multi = util.str2bool(request.args.get('multi'))
	inline = util.str2bool(request.args.get('inline'))

	if multi is True:
		if len(request.json) > 1:
			for doc in request.json:
				print doc['title']

	if inline is True:
		# parse out resource

	# create the document in mongo and return the id
	#print request.json

	#for item in request.form:
	#	print 'key: ' + item + ', value: ' + request.form[item]
	#print request.files[1]
	#creation.create_content()
	result['id'] = "id of the newly created content"

	return json.dumps(result)

def retrieve(request, id):
	if request is None:
		result['success'] = False
		result['error'] = "request data was not found"
	else:
		result['success'] = True

	# get the document out of mongo matching the given id
	result['document'] = json.dumps({'title':'value','description':'value2'})

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