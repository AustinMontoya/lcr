from flask import make_response
from repo import models
import json
from types import NoneType
from models import LearningObject, Resource, WebResource

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

def createJsonResponse(doc, status_code):
    response = make_response(json.dumps(doc), status_code)
    response.headers['content-type'] = "application/json"
    return response

def create_content(metadata):
    id = ''
    result = ''

    incoming_title = ''
    incoming_description = ''
    incoming_tags = ''

    # parse the metadata
    try:
        incoming_title = metadata['title']
        incoming_description = metadata['description']
        incoming_tags = metadata['tags']
    except:
        raise HelperException("The metadata used to create the content object was not in the expected form.", 400)

    # create the content object
    try:
        new_object = LearningObject(title=incoming_title, 
                                    description=incoming_description, 
                                    tags=incoming_tags,
                                    resources=[])
        new_object.save()
        
        id = str(new_object.mongo_id)
    except Exception as e:
        raise HelperException("The object could not be created in the database. " + str(e), 500)

    return id

def create_url_resource(content_id, json_data, resource_name):
    id = ''
    result = ''
    new_url_resource = ''

    # get the content object
    str_content_id = str(content_id)

    document = models.LearningObject.query.get(str_content_id)

    if isinstance(document, NoneType):
        raise HelperException("No content item was found with an id of " + str_content_id + ".", 404)
        return    

    # parse the url and create the url resource
    if type(json_data) is dict:

        incoming_url = ''

        # parse the metadata
        try:
            incoming_url = json_data['url']
        except Exception as e:
            raise HelperException("A url key was not found in the json data.", 400)

        if resource_name is None:
            resource_name = incoming_url

        new_url_resource = WebResource(url=incoming_url, name=resource_name)

        new_url_resource.save()
    else:
        raise HelperException("The request body was not of the expected type.  The type found was " + str(type(json_data)) + ", whereas the type expected was dict.", 400)

    # add the url resource to the content object
    try:
        document.resources.append(new_url_resource)
        document.save()
    except Exception as e:
        raise HelperException("The resource could not be appended to the content object in the database. " + str(e), 500)
    
    return

def retrieve_content(id):
    document = ''
    result = ''

    str_id = str(id)

    document = models.LearningObject.query.get(str_id)

    if isinstance(document, NoneType):
        raise HelperException("No content item was found with an id of " + str_id + ".", 404)
        return

    # convert mongo document to a python dictionary
    result = document.wrap()

#    print result
#    for resource in result['resources']:
#        print resource

    del result['_id']

    return result

def update_content(id, metadata):
    document = ''
    result = '' 

    if type(metadata) is dict:

        incoming_title = ''
        incoming_description = ''
        incoming_tags = ''

        # parse the metadata
        try:
            incoming_title = metadata['title']
            incoming_description = metadata['description']
            incoming_tags = metadata['tags']
        except Exception as e:
            raise HelperException("The metadata provided was not in the expected form. "  + str(e), 400)

        # get the object by id
        str_id = str(id)  
        
        document = models.LearningObject.query.get(str_id)

        if isinstance(document, NoneType):
            raise HelperException("No content item was found with an id of " + str_id + ".", 404)
            return

        # create the content object
        try:
            document.title = incoming_title 
            document.description = incoming_description
            document.tags = incoming_tags
            
            document.save()
        except Exception as e:
            raise HelperException("The object could not be updated in the database. " + str(e), 500)
    else:
        raise HelperException("The metadata was not of the expected type.  The type found was " + str(type(metadata)) + ", whereas the type expected was dict.", 400)

    return

def delete_content(id):

    document = ''

    # get the object by id
    str_id = str(id)  
    
    document = models.LearningObject.query.get(str_id)

    if isinstance(document, NoneType):
        raise HelperException("No content item was found with an id of " + str_id + ".", 404)
        return

    try:
        document.remove()
    except Exception as e:
        raise HelperException("The object could not be removed from the database. " + str(e), 500)

    return    
