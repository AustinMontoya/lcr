from flask import make_response
from repo import mongo
from repo.models import Package, WebResource, FileResource
from datetime import datetime
import json
from types import NoneType
from bson.objectid import ObjectId, InvalidId
import jinja2

def createJsonResponse(doc, status_code):
    response = make_response(json.dumps(doc), status_code)
    response.headers['content-type'] = "application/json"
    return response

def createErrorResponse(error, status_code):
    result = {}
    result['error'] = error
    response = createJsonResponse(result, status_code)
    return response

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
    package = {}
    if id is not None:
        existing_package = retrieve_package(id).to_python()
        for k in metadata:
            try:
                existing_package[k] = metadata[k]
            except:
                continue
        package = Package(**existing_package)
    else:
        package = Package(**metadata)

    # parse the metadata
    try:        
        package.validate()
    except:
        raise HelperException("The metadata used to create the package object was not in the expected form.", 400)

    # create the package object
    try:
        return _save_from_model(package)
    except Exception as e:
        raise HelperException("The learning package could not be saved. " + str(e), 500)

def create_package(metadata):
    id = save_package(metadata)
    return str(id)

def create_url_resource(package_id, metadata, resource_name):

    resource_id = None

    # get the package
    package = retrieve_package(package_id)

    # create the resource
    resource = WebResource(**metadata)
    resource.last_updated = datetime.now()
    resource.name = resource_name

    try:
        resource.validate()
    except Exception as e:
        raise HelperException("The metadata used to create the resource was not in the expected form. " + str(e), 400)

    # add the resource to the package
    try:
        package.urls.append(resource)
        _save_from_model(package)
    except Exception as e:
        raise HelperException("The resource could not be added to the package." + str(e), 500)

def retrieve_json_package(id):
    pkg = retrieve_package(id).to_python_public()
    return json.dumps(pkg)

def retrieve_package(id):
    obj_id = None

    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HelperException("'%s' is not a valid id." % id, 400)
    
    try:
        document = Package(**mongo.db.packages.find_one({ "_id" : obj_id}))
    except:
        raise HelperException("No package item was found with an id of " + id + ".", 404)

    return document

def update_package(id, metadata):
    save_package(metadata, id)

def delete_package(id):
    try:
        mongo.db.packages.remove(ObjectId(id))
    except Exception as e:
        raise HelperException("The object could not be removed from the database. " + str(e), 500)

# saves it directly from a model to mongodb.
# takes care of the id mapping problem in dictshield
def _save_from_model(model):

    # Escapes any html markup using Jinja2.
    # We don't want to send potential xss attacks
    # to API consumers.
    def sanitize(obj):
        if isinstance(obj, dict):
            for key in obj:
                obj[key] = sanitize(obj[key])
        elif isinstance(obj, list) and len(obj) > 0:
            obj = map(lambda x : sanitize(x), obj)
        else:
            types_to_escape = [str, unicode]
            if type(obj) in types_to_escape:
                obj = jinja2.Markup.escape(obj)
        return obj
            
    package_dict = sanitize(model.to_python())

    if 'id' in package_dict:
        id = ObjectId(package_dict['id'])
        del package_dict['id']
        package_dict['_id'] = ObjectId(id)

    return mongo.db.packages.save(package_dict)
    
