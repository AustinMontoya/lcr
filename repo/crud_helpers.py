from repo import db, models
import json
from types import NoneType
from models import LearningObject

def create_content(metadata):
    # create a new content object in mongo
    # return an id

    id = ''

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
            raise Exception("The metadata used to create the content object was not in the expected form.")

        # create the content object
        try:
            new_object = LearningObject(title=incoming_title, 
                                        description=incoming_description, 
                                        tags=incoming_tags)
            new_object.save()
            
            id = str(new_object.mongo_id)
        except:
            raise Exception("The object could not be created in the database.")
    else:
        raise Exception("The metadata was not of the expected type.  The type found was " + str(type(metadata)) + ", whereas the type expected was dict.")

    return id

def create_resource_link(url):
    # create a new content object in mongo
    # return an id
    result['id'] = 10

    return result

def create_resource_file(file):
    # create a new resource object in mongo
    # return an id

    id = ''

    if type(file) is dict:

        incoming_title = ''
        incoming_description = ''
        incoming_tags = ''

        # parse the metadata
        try:
            incoming_title = metadata['title']
            incoming_description = metadata['description']
            incoming_tags = metadata['tags']
        except:
            raise Exception("The metadata used to create the content object was not in the expected form.")

        # create the content object
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
    result['id'] = 15

    return result

def retrieve_content(id):

    document = ''

    str_id = str(id)

    document = models.LearningObject.query.get(str_id)

    if isinstance(document, NoneType):
        raise Exception("The requested id was not found")
        return

    # convert mongo document to a python dictionary
    result = document.wrap()

    del result['_id']

    return result

