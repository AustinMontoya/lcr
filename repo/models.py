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
	_public_fields = ['name', 'last_updated', 'url']
	name = StringField(min_length=1, max_length=50, required=True)
	last_updated = DateTimeField(required=True)
	url = URLField(required=True)

class FileResource(Resource):
	_private_fields = ['fileId']
	_public_fields = ['name', 'last_updated', 'mimeType']
	name = StringField(min_length=1, max_length=50, required=True)
	last_updated = DateTimeField(required=True)
	fileId = ObjectIdField(required=True)
	mimeType = StringField(max_length=50)

##
# Containers
##

class Package(Document):
	'''Holds general information about a collection of loosely organized
	resources related to a given topic.'''
	_public_fields=['id', 'title', 'description', 'tags', 'resources', 'last_updated', 'files', 'urls']
	title = StringField(min_length=1, max_length=50, required=True)
	description = StringField(max_length=140)
	tags = ListField(StringField(max_length=30))
	urls = ListField(EmbeddedDocumentField(WebResource))
	files = ListField(EmbeddedDocumentField(FileResource))
	last_updated = DateTimeField(required=True)

	class Meta:
		id_field = ObjectIdField