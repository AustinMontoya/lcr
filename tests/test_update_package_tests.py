import json
from test_app import BaseAppTestCase

class Update_Package_Tests(BaseAppTestCase):

    def test_package_update_success(self):
        print '\n6: '
        response_post = self.app.post(self.CreatePackageURL, 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_update_post = self.app.post(self.UpdatePackageURL + str(vals_post['id']), 
                content_type='application/json',
                data=json.dumps(self.testContentUpdate),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_update_post.data)) + ' ' + str(response_update_post.status_code)
        self.assertEqual(response_update_post.status_code, 200)

    def test_package_update_fail(self):
        print '\n7: '
        response_post = self.app.post(self.CreatePackageURL, 
                content_type='application/json',
                data=json.dumps(self.testContent),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_post.data)) + ' ' + str(response_post.status_code)
        self.assertEqual(response_post.status_code, 200)
        vals_post = json.loads(response_post.data)
        self.assertIn('id', vals_post)

        response_update_post = self.app.post(self.UpdatePackageURL + self.IdNotInDB, 
                content_type='application/json',
                data=json.dumps(self.testContentUpdate),
                follow_redirects=True)
        print '\n post: ' + str(json.dumps(response_update_post.data)) + ' ' + str(response_update_post.status_code)
        self.assertGreaterEqual(response_update_post.status_code, 400)
        vals = json.loads(response_update_post.data)
        self.assertIn('error', vals)
