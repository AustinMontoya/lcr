import json
from test_app import BaseAppTestCase

class Create_Package_Tests(BaseAppTestCase):
    
    def test_package_create_multi_f_inline_f_success(self):
        response = self.app.post(self.CreatePackageURLFF, 
                        content_type='application/json',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 200)
        vals = json.loads(response.data)
        self.assertIn('id', vals)

    def test_package_create_multi_f_inline_t_success(self):
        #response = self.app.post(self.CreatePackageURLFT, 
        #                content_type='application/json',
        #                data=json.dumps(self.testContent),
        #                follow_redirects=True)
        #print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        #self.assertEqual(response.status_code, 200)
        #vals = json.loads(response.data)
        #self.assertIn('id', vals)
        raise NotImplementedError("TODO")

    def test_package_create_multi_t_inline_f_success(self):
        #response = self.app.post(self.CreatePackageURLTF, 
        #                content_type='application/json',
        #                data=json.dumps(self.testContent),
        #                follow_redirects=True)
        #print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        #self.assertEqual(response.status_code, 200)
        #vals = json.loads(response.data)
        #self.assertIn('id', vals)
        raise NotImplementedError("TODO")

    def test_package_create_multi_t_inline_t_success(self):
        #response = self.app.post(self.CreatePackageURLTT, 
        #                content_type='application/json',
        #                data=json.dumps(self.testContent),
        #                follow_redirects=True)
        #print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        #self.assertEqual(response.status_code, 200)
        #vals = json.loads(response.data)
        #self.assertIn('id', vals)
        raise NotImplementedError("TODO")

    def test_package_create_invaild_type_fail(self):
        bad_content = self.testContent
        bad_content['title'] = True
        response = self.app.post(self.CreatePackageURLFF, 
                        content_type='application/json',
                        data=json.dumps(bad_content),
                        follow_redirects=True)
        print '\n' + str(json.dumps(response.data)) + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 400)
        vals = json.loads(response.data)
        self.assertIn('error', vals)
        self.assertIn("The metadata used to create the package object was not in the expected form.", vals["error"])

    def test_package_create_invalid_json_fail(self):
        response = self.app.post(self.CreatePackageURLFF, 
                        content_type='application/json',
                        data=json.dumps(self.testContent) + '1',
                        follow_redirects=True)
        print '\n' + response.data + ' ' + str(response.status_code)
        self.assertEqual(response.status_code, 400)
        self.assertIn("The browser (or proxy) sent a request that this server could not understand.", response.data)

    def test_package_create_missing_metadata_fail(self):
        raise NotImplementedError("TODO")

    def test_package_create_invalid_content_type_fail(self):
        response = self.app.post(self.CreatePackageURLFF, 
                        content_type='text/html',
                        data=json.dumps(self.testContent),
                        follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        vals = json.loads(response.data)
        self.assertIn('error', vals)
        self.assertIn("The content-type was not of the expected type.", vals["error"])
