from flask import g
from repo import mongo
from repo.models import Package, WebResource, FileResource
from datetime import datetime
import json
from types import NoneType


class HelperException(Exception):
    """Internal class to manage error messages and status codes"""
    status_code = ''
    error = ''

    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

    def setError(self, error):
        self.error = error

    def setStatusCode(self, status_code):
        self.status_code = status_code

def save_package(metadata, id=None):
    metadata['last_updated'] = datetime.now()

    if id is not None:
        metadata['_id'] = id

    package = Package(**metadata)

    # parse the metadata
    try:        
        package.validate()
    except:
        raise HelperException("The metadata used to create the package object was not in the expected form.", 400)

    # create the package object
    try:
        return mongo.db.packages.save(package.to_python())
    except Exception as e:
        raise HelperException("The learning package could not be saved. " + str(e), 500)

def create_package(metadata):
    id = save_package(metadata)
    return str(id)

def retrieve_package(id):
    str_id = str(id)
    print str_id

    document = mongo.db.packages.find_one({ "_id" : str_id})

    if isinstance(document, NoneType):
        raise HelperException("No package item was found with an id of " + str_id + ".", 404)

    del document['_id']
    document['id'] = str_id

    return document

def update_package(id, metadata):
    save_package(metadata, id)

def delete_package(id):
    try:
        mongo.db.packages.remove(id)
    except Exception as e:
        raise HelperException("The object could not be removed from the database. " + str(e), 500)
