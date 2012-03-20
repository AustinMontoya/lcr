"""
    SCORM-Repo Tests
    ~~~~~~~~~~~~

    Tests the SCORM-Repo application.

"""
import unittest
import json
from flask import Flask
from werkzeug.exceptions import NotFound
from unittest import TestCase
from repo import create_app, mongo
from settings import TestConfig
import pymongo

class BaseTestCase(TestCase):

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
        self.app = create_app(TestConfig).test_client()
        
        self.IdNotInDB = '4c271729e13823182f000000'

        self.testContent = {
            'title' : 'testTitle',
            'description' : 'Test description',
            'tags' : ['tag1', 'tag2']
        }
        
        self.testContentwID = {
            'id' : 'test_id_1',
            'title' : 'testTitle_1',
            'description' : 'Test description_1',
            'tags' : ['tag1_1', 'tag2_2']
        }

    def teardown(self):
        conn = pymongo.Connection(TestConfig.MONGO_HOST,TestConfig.MONGO_PORT)
        conn[TestConfig.MONGO_DBNAME].drop_collection("learningObjects")

    def test_content_create_success(self):
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertEqual(vals['success'],True)
        self.assertIn('id', vals)

    def test_content_create_fail(self): 
        bad_content = self.testContent
        bad_content['title'] = True
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(bad_content),
                        follow_redirects=True)
        self.assertGreaterEqual(response.status_code, 400)
        vals = json.loads(response.data)
        self.assertIn('error', vals)

    def test_content_retrieve_success(self):
        response_post = self.app.post('/api/create/content', 
                content_type='application/json',
                data=json.dumps(self.testContentwID),
                follow_redirects=True)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertEqual(vals_post['success'],True)

        response_get = self.app.get('/api/content/' + str(vals_post['id']))
        vals_get = json.loads(response_get.data)
        self.assertIn('id', vals_get)
        self.assertEqual(vals_get['id'], vals_post['id'])

    def test_content_retrieve_fail(self):
        response_get = self.app.get('/api/content/' + self.IdNotInDB)
        vals_get = json.loads(response_get.data)
        print str(json.dumps(vals_get))
        self.assertIn('id', vals_get)
        self.assertNotEqual(vals_get['id'], self.IdNotInDB)

    def test_content_update(self):
        raise NotImplementedError("TODO")

    def test_content_delete(self):
        raise NotImplementedError("TODO")

    def test_resource_create(self):
        raise NotImplementedError("TODO")

    def test_resource_retrieve(self):
        raise NotImplementedError("TODO")

    def test_resource_update(self):
        raise NotImplementedError("TODO")

    def test_resource_delete(self):
        raise NotImplementedError("TODO")

if __name__ == '__main__':
    unittest.main()        
