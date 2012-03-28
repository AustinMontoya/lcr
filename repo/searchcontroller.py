from models import Package
from repo import mongo
from crud_helpers import createJsonResponse, createErrorResponse
import bson

# Parses out the actual request and performs the desired query
def get_from_query(request):
	pass

# Simple exact match from list of tags
def get_by_tags(tagList):
	query = { '$or' : map(lambda x: { 'tags' : x }, tagList) }
	results = mongo.db.packages.find(query)
	return createJsonResponse(
		map(lambda pkg: Package(**pkg).to_python_public(), results), 200)