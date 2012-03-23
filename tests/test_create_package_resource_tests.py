import json
from test_app import BaseAppTestCase

class Create_Package_Resource_Tests(BaseAppTestCase):

    def test_resource_url_create_success(self):
        print '\n10: '
        response = self.app.post(self.CreatePackageURL, 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

        new_resource = self.testResourceURL
        new_resource['id'] = vals['id']

        response_resource = self.app.post(self.CreatePackageResourceURL + str(vals['id']) + '?type=' + str(new_resource['type']) + '&name=' + str(new_resource['name']), 
                        content_type='application/json',
                        data=json.dumps(new_resource),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response_resource.data)) + ' ' + str(response_resource.status_code)
        self.assertEqual(response_resource.status_code, 200)
        vals = json.loads(response_resource.data)
        self.assertIn('id', vals)

    def test_resource_url_create_fail(self):
        print '\n11: '
        response = self.app.post(self.CreatePackageURL, 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

        new_resource = self.testResourceURL
        new_resource['id'] = self.IdNotInDB

        response_resource = self.app.post(self.CreatePackageResourceURL + str(vals['id']) + '?type=' + str(new_resource['type']) + '&name=' + str(new_resource['name']), 
                        content_type='application/json',
                        data=json.dumps(new_resource),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response_resource.data)) + ' ' + str(response_resource.status_code)
        self.assertGreaterEqual(response_resource.status_code, 400)
        vals = json.loads(response_resource.data)
        self.assertIn('error', vals)
