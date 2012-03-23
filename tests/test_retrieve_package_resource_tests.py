import json
from test_app import BaseAppTestCase

class Retrieve_Package_Resource_Tests(BaseAppTestCase):

    def test_resource_url_retrieve_success(self):
        print '\n12: '
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

        response_get = self.app.get(self.RetrievePackageURL + str(vals['id']) + '?metadata=false')
        print '\n get: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertEqual(response_get.status_code, 200)

    def test_resource_url_retrieve_failure(self):
        print '\n13: '
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

        response_get = self.app.get(self.RetrievePackageURL + self.IdNotInDB + '?metadata=false')
        print '\n get: ' + str(json.dumps(response_get.data)) + ' ' + str(response_get.status_code)
        self.assertGreaterEqual(response_get.status_code, 400)
        vals = json.loads(response_get.data)
        self.assertIn('error', vals)
