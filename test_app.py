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

    testContent = {
        'title' : 'testTitle',
        'description' : 'Test description',
        'tags' : ['tag1', 'tag2']
    }

    def setup(self):
        self.app = create_app(TestConfig).test_client()
    def teardown(self):
        for lcr in models.LearningObject.query.all():
            lcr.remove()

    def test_content_create(self):
        print json.dumps(self.testContent)
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        vals = json.loads(response.data)
        self.assertEqual(vals['success'],True)
        self.assertIn('id', vals)

    def test_content_retrieve(self):
        rv = self.app.get('/api/content/5')
        assert 'true' in rv.data
       # print rv.data

if __name__ == '__main__':
    unittest.main()        
