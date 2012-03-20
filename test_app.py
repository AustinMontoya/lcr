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
        
        self.IdNotInDB = '4c271729e13823182f000000'

        self.testContent = {
            'title' : 'testTitle',
            'description' : 'Test description',
            'tags' : ['tag1', 'tag2']
        }

        self.testContentUpdate = {
            'title' : 'testUpdateTitle',
            'description' : 'Test update description',
            'tags' : ['tag1', 'tag2', 'tag3']
        }
        
        self.testResourceURL = {
            'id' : '',
            'type' : 'url',
            'name' : 'http://www.adlnet.gov',
            'multi' : 'false'
        }

    def teardown(self):
        for lcr in models.LearningObject.query.all():
            lcr.remove()

    def test_content_create_success(self):
        print '\n1: '
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

    def test_content_create_fail_bad_type(self):
        print '\n2: ' 
        bad_content = self.testContent
        bad_content['title'] = True
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(bad_content),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 400)
        vals = json.loads(response.data)
        self.assertIn('error', vals)
        self.assertIn("The object could not be created in the database. ", vals["error"])

    def test_content_create_fail_invalid_json(self):
        raise NotImplementedError()

    def test_content_create_fail_missing_metadata(self):
        raise NotImplementedError()

    def test_content_create_fail_invalid_content_type(self):
        raise NotImplementedError()

    def test_content_retrieve_success(self):
        print '\n3: '
        response_post = self.app.post('/api/create/content', 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_get = self.app.get('/api/content/' + str(vals_post['id']))
        print '\n get: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertEqual(response_get.status_code, 200)

    def test_content_retrieve_success(self):
        print '\n4: '      
        response_post = self.app.post('/api/create/content', 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)

        response_get = self.app.get('/api/content/' + str(vals_post['id']) + '?metadata=true')
        print '\n post: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertEqual(response_get.status_code, 200)

    def test_content_retrieve_fail(self):
        print '\n5: '
        response_get = self.app.get('/api/content/' + self.IdNotInDB)
        print '\n get: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertGreaterEqual(response_get.status_code, 400)
        vals = json.loads(response_get.data)
        self.assertIn('error', vals)

    def test_content_update_success(self):
        print '\n6: '
        response_post = self.app.post('/api/create/content', 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_update_post = self.app.post('/api/update/content/' + str(vals_post['id']), 
                content_type='application/json',
                data=json.dumps(self.testContentUpdate),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_update_post.data)) + ' ' + str(response_update_post.status_code)
        self.assertEqual(response_update_post.status_code, 200)

    def test_content_update_fail(self):
        print '\n7: '
        response_post = self.app.post('/api/create/content', 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_update_post = self.app.post('/api/update/content/' + self.IdNotInDB, 
                content_type='application/json',
                data=json.dumps(self.testContentUpdate),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_update_post.data)) + ' ' + str(response_update_post.status_code)
        self.assertGreaterEqual(response_update_post.status_code, 400)
        vals = json.loads(response_update_post.data)
        self.assertIn('error', vals)

    def test_content_delete_success(self):
        print '\n8: '
        response_post = self.app.post('/api/create/content', 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_delete_post = self.app.post('/api/delete/content/' + str(vals_post['id']), 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_delete_post.data)) + ' ' + str(response_delete_post.status_code)
        self.assertEqual(response_delete_post.status_code, 200)

    def test_content_delete_fail(self):
        print '\n9: '
        response_post = self.app.post('/api/create/content', 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_delete_post = self.app.post('/api/delete/content/' + self.IdNotInDB, 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_delete_post.data)) + ' ' + str(response_delete_post.status_code)
        self.assertGreaterEqual(response_delete_post.status_code, 400)
        vals = json.loads(response_delete_post.data)
        self.assertIn('error', vals)

    def test_resource_url_create_success(self):
        print '\n10: '
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

        new_resource = self.testResourceURL
        new_resource['id'] = vals['id']

        response_resource = self.app.post('/api/create/resource/' + str(vals['id']) + '?type=' + str(new_resource['type']) + '&name=' + str(new_resource['name']), 
                        content_type='application/json',
                        data=json.dumps(new_resource),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response_resource.data)) + ' ' + str(response_resource.status_code)
        self.assertEqual(response_resource.status_code, 200)
        vals = json.loads(response_resource.data)
        self.assertIn('id', vals)

    def test_resource_url_create_fail(self):
        print '\n11: '
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

        new_resource = self.testResourceURL
        new_resource['id'] = self.IdNotInDB

        response_resource = self.app.post('/api/create/resource/' + str(vals['id']) + '?type=' + str(new_resource['type']) + '&name=' + str(new_resource['name']), 
                        content_type='application/json',
                        data=json.dumps(new_resource),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response_resource.data)) + ' ' + str(response_resource.status_code)
        self.assertGreaterEqual(response_resource.status_code, 400)
        vals = json.loads(response_resource.data)
        self.assertIn('error', vals)

    def test_resource_url_retrieve_success(self):
        print '\n12: '
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

        new_resource = self.testResourceURL
        new_resource['id'] = vals['id']

        response_resource = self.app.post('/api/create/resource/' + str(vals['id']) + '?type=' + str(new_resource['type']) + '&name=' + str(new_resource['name']), 
                        content_type='application/json',
                        data=json.dumps(new_resource),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response_resource.data)) + ' ' + str(response_resource.status_code)
        self.assertEqual(response_resource.status_code, 200)
        vals = json.loads(response_resource.data)
        self.assertIn('id', vals)

        response_get = self.app.get('/api/resource/' + str(vals['id']) + '?metadata=false')
        print '\n get: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertEqual(response_get.status_code, 200)

    def test_resource_url_retrieve_failure(self):
        print '\n13: '
        response = self.app.post('/api/create/content', 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

        new_resource = self.testResourceURL
        new_resource['id'] = vals['id']

        response_resource = self.app.post('/api/create/resource/' + str(vals['id']) + '?type=' + str(new_resource['type']) + '&name=' + str(new_resource['name']), 
                        content_type='application/json',
                        data=json.dumps(new_resource),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response_resource.data)) + ' ' + str(response_resource.status_code)
        self.assertEqual(response_resource.status_code, 200)
        vals = json.loads(response_resource.data)
        self.assertIn('id', vals)

        response_get = self.app.get('/api/resource/' + self.IdNotInDB + '?metadata=false')
        print '\n get: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertGreaterEqual(response_get.status_code, 400)
        vals = json.loads(response_get.data)
        self.assertIn('error', vals)

    def test_resource_url_update_success(self):
        print '\n14: '
        raise NotImplementedError("TODO")

    def test_resource_url_update_fail(self):
        print '\n15: '
        raise NotImplementedError("TODO")

    def test_resource_url_delete_success(self):
        print '\n16: '
        raise NotImplementedError("TODO")

    def test_resource_url_delete_fail(self):
        print '\n17: '
        raise NotImplementedError("TODO")

if __name__ == '__main__':
    unittest.main()        
