import datetime
from dictshield.document import Document, EmbeddedDocument, diff_id_field
from dictshield.fields import StringField, IntField, DateTimeField, URLField
from dictshield.fields.compound import ListField, EmbeddedDocumentField
from dictshield.fields.mongo import ObjectIdField

from bson.objectid import ObjectId

##
# Resources
##

class Resource(EmbeddedDocument):
	'''A general resource representing an piece of content that is
	valuable for learning the topic of the containing content package'''

	name = StringField(min_length=1, max_length=50, required=True)
	last_updated = DateTimeField(required=True)

class WebResource(Resource):
	url = URLField(required=True)

class FileResource(Resource):
	_private_fields = ['fileId']
	fileId = ObjectIdField(required=True)
	mimeType = StringField(max_length=50)

##
# Containers
##

@diff_id_field(ObjectIdField, ['id'])
class Package(Document):
	'''Holds general information about a collection of loosely organized
	resources related to a given topic.'''
	_public_fields=['id', 'title', 'description', 'tags', 'resources', 'last_updated']
	title = StringField(min_length=1, max_length=50, required=True)
	description = StringField(max_length=140)
	tags = ListField(StringField(max_length=30))
	resources = ListField(EmbeddedDocumentField(Resource))
	last_updated = DateTimeField(required=True)