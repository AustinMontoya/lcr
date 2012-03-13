def handleAction(action, request, id):
	if request is None:
		return "{ Error: 'request data was not found' }" 
	
	if action is None:
		return "{ Error: 'requested action was not specified' }"

	if action == 'object':	
		if request.method == 'POST':
			if request.json is None:
				return "{ Error: 'JSON metadata was not found' }"
			# parse the JSON
			# Input: 
			# {
			#	title: <string>,
			#   description: <string>|null
			#	tags: <string>|null
			# }			
			# if resource locator or URL included in JSON, then treat it as a webResource 
			# create a mongo object
			# return id
			return "{ id: 'id of mongo object'}"
		else:
			if id is None:
				return "{ Error: 'ID for the requested object not specified' }"
			try:
				testint = int(id) + 1
				# get the JSON document matching ID out of mongo
				return "{ result_data: 'JSON data matching id' }"
			except ValueError:
				return "{ Error: 'ID was expected to be an integer, but something else was found' }"
			except TypeError:
				return "{ Error: 'ID was expected to be an integer, but something else was found' }"
	elif action == "files":
		if request.method == 'POST':
			# if input is file, then store the file and return id of the file
			return "{ id: 'ID of stored file' }"
		else:
			if id is None:
				# if input is none, return ids				
				return "{ ids: 'list of IDs for the object's files }"
			# if input is id, return the file
			return "file contents"
		return "files " + id
	else:
		return "{ Error: 'Unexpected action encountered' }"