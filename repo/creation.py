from models import LearningObject
import json

result = {}

def create_content(metadata):
	# create a new content object in mongo
	# return an id

	id = ''

	if type(metadata) is dict:

		incoming_title = ''
		incoming_description = ''
		incoming_tags = ''

		try:
			incoming_title = metadata['title']
			incoming_description = metadata['description']
			incoming_tags = metadata['tags']
		except:
			raise Exception("metadata invalid")

		try:
			new_object = LearningObject(title=incoming_title, 
										description=incoming_description, 
										tags=incoming_tags)
			new_object.save()
			
			id = str(new_object.mongo_id)
		except:
			raise Exception("error saving object to database")
	else:
		raise Exception("invalid JSON")

	return id

def create_resource_link(url):
	# create a new content object in mongo
	# return an id
	result['id'] = 10

	return result

def create_resource_file(file):
	# create a new content object in mongo
	# return an id
	result['id'] = 15

	return result