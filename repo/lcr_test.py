import os
import runserver
import unittest
import tempfile


class LCRTestCase(unittest.TestCase):

    def setUp(self):
        """Before each test, set up a blank database"""
        #self.db_fd = tempfile.mkstemp()
        self.dbname = 'test-repo'
        
        runserver.fs = runserver.GridFsFileStore(self.dbname, '127.0.0.1', 27017)
	runserver.app.config['TESTING'] = True
        
        self.app = runserver.app.test_client()

    def tearDown(self):
        """Get rid of the database again after each test."""
        #os.close(self.db_fd)
        #os.unlink(self.dbname)

    # testing functions

    def test_create_content(self):
        rv = self.app.get('/api/content/5')
        assert 'true' in rv.data
        print rv.data


if __name__ == '__main__':
    unittest.main()