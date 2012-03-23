import json
from test_app import BaseAppTestCase

class Retrieve_Package_Tests(BaseAppTestCase):

    def test_package_retrieve_success(self):
        print '\n3: '
        response_post = self.app.post(self.CreatePackageURL, 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_get = self.app.get(self.RetrievePackageURL + str(vals_post['id']))
        print '\n get: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertEqual(response_get.status_code, 200)

    def test_package_retrieve_metadata_success(self):
        print '\n4: '      
        response_post = self.app.post(self.CreatePackageURL, 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)

        response_get = self.app.get(self.RetrievePackageURL + str(vals_post['id']) + '?metadata=true')
        print '\n post: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertEqual(response_get.status_code, 200)

    def test_package_retrieve_fail(self):
        print '\n5: '
        response_get = self.app.get(self.RetrievePackageURL + self.IdNotInDB)
        print '\n get: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertGreaterEqual(response_get.status_code, 400)
        vals = json.loads(response_get.data)
        self.assertIn('error', vals)
