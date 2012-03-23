import json
from test_app import BaseAppTestCase

class Delete_Package_Tests(BaseAppTestCase):
    
    def test_package_delete_success(self):
        print '\n8: '
        response_post = self.app.post(self.CreatePackageURL, 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_delete_post = self.app.post(self.DeletePackageURL + str(vals_post['id']), 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_delete_post.data)) + ' ' + str(response_delete_post.status_code)
        self.assertEqual(response_delete_post.status_code, 200)

    def test_package_delete_fail(self):
        print '\n9: '
        response_post = self.app.post(self.CreatePackageURL, 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 400)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_delete_post = self.app.post(self.DeletePackageURL + self.IdNotInDB, 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_delete_post.data)) + ' ' + str(response_delete_post.status_code)
        self.assertGreaterEqual(response_delete_post.status_code, 400)
        vals = json.loads(response_delete_post.data)
        self.assertIn('error', vals)
