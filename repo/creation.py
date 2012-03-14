from models import LearningObject
import json

result = {}

def create_content(metadata):
	# create a new content object in mongo
	# return an id
	
	#print metadata
	new_object = LearningObject(title='test', description='test description', tags=['tag1', 'tag2'])
	new_object.save()

	return str(new_object.mongo_id)

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