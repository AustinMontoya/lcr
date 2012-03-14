"""
    SCORM-Repo Tests
    ~~~~~~~~~~~~

    Tests the SCORM-Repo application.

"""
import unittest
from flask import Flask
from werkzeug.exceptions import NotFound
from flaskext import mongoalchemy
from helpers import _make_LCR_Object, _make_LCR_Resource
from nose.tools import assert_equals
from repo import LearningObject


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        self.setup()

    def tearDown(self):
        super(BaseTestCase, self).tearDown()
        self.teardown()

    def setup(self):
        pass

    def teardown(self):
        pass

class BaseAppTestCase(BaseTestCase):

    def setup(self):
        self.app = Flask(__name__)
        self.app.config['MONGOALCHEMY_DATABASE'] = 'testing'
        self.app.config['TESTING'] = True
        self.db = mongoalchemy.MongoAlchemy(self.app)
        self.LCR_Object = LearningObject(self.db)

    def teardown(self):
        for lcr in self.LCR_Object.query.all():
            lcr.remove()

    def test_should_use_localhost_for_server_and_27017_for_port_when_only_the_database_name_was_specified(self):
        from flaskext.mongoalchemy import _get_mongo_uri
        assert_equals(_get_mongo_uri(self.app), 'mongodb://localhost:27017/')
        print 'success'

    def test_should_return_None_when_querying_for_a_non_existing_document_on_database(self):
        "\"get()\" method should return None when querying for a non-existing document"
        searched_LCR_Object = self.LCR_Object.query.get('47cc67093475061e3d95369d')
        assert searched_LCR_Object is None

#    def test_should_provide_a_get_method_on_query_object(self):
#        "Should provide a \"get()\" method on Query object"
#        lcr_obj = self.LCR_Object(id='4e038a23e4206650da0000db', title=u'test object', description=u'Start something very new', tags=['key1','key2'], files=[{id='47cc67093475061e3d95369d', name=u'test_item', type='file'}])
#        lcr_obj.save()
#        searched_lcr_obj = self.LCR_Object.query.get(str(lcr_obj.mongo_id))
#        assert_equals(lcr_obj, searched_lcr_obj)

if __name__ == '__main__':
    unittest.main()        
