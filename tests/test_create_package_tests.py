import json
from test_app import BaseAppTestCase

class Create_Package_Tests(BaseAppTestCase):
    
    def test_package_create_success(self):
        print '\n1: '
        response = self.app.post(self.CreatePackageURL, 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

    def test_package_create_fail_bad_type(self):
        print '\n2: ' 
        bad_content = self.testContent
        bad_content['title'] = True
        response = self.app.post(self.CreatePackageURL, 
                        content_type='application/json',
                        data=json.dumps(bad_content),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 400)
        vals = json.loads(response.data)
        self.assertIn('error', vals)
        self.assertIn("The metadata used to create the package object was not in the expected form.", vals["error"])

    def test_package_create_fail_invalid_json(self):
        raise NotImplementedError("TODO")

    def test_package_create_fail_missing_metadata(self):
        raise NotImplementedError("TODO")

    def test_package_create_fail_invalid_package_type(self):
        raise NotImplementedError("TODO")
