from repo import models
import json
from types import NoneType
from models import LearningObject

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

def create_content(metadata):
    id = ''
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
        except:
            raise HelperException("The metadata used to create the content object was not in the expected form.", 400)

        # create the content object
        try:
            new_object = LearningObject(title=incoming_title, 
                                        description=incoming_description, 
                                        tags=incoming_tags)
            new_object.save()
            
            id = str(new_object.mongo_id)
        except Exception as e:
            raise HelperException("The object could not be created in the database. " + str(e), 500)
    else:
        raise HelperException("The metadata was not of the expected type.  The type found was " + str(type(metadata)) + ", whereas the type expected was dict.", 400)

    return id

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
