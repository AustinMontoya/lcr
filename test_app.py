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
from repo import create_app, models
from settings import TestConfig
from flaskext.mongoalchemy import MongoAlchemy

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
        self.testContent = {
            'title' : 'testTitle',
            'description' : 'Test description',
            'tags' : ['tag1', 'tag2']
        }

    def teardown(self):
        for lcr in models.LearningObject.query.all():
            lcr.remove()

    def test_content_create_success(self):
        print 'test_content_create(self) Test Document: ' + str(json.dumps(self.testContent))
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        print 'test_content_create(self) status code: ' + str(response.status_code)
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


    def test_content_retrieve(self):
        rv = self.app.get('/api/content/5')
        assert 'true' in rv.data
       # print rv.data


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
