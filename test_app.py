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
from repo import create_app, mongo
from settings import TestConfig
import pymongo

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

        self.CreatePackageURLFF = '/api/create/package?multi=false&inline=false'
        self.CreatePackageURLFT = '/api/create/package?multi=false&inline=true'
        self.CreatePackageURLTF = '/api/create/package?multi=true&inline=false'
        self.CreatePackageURLTT = '/api/create/package?multi=true&inline=true'
        self.CreatePackageResourceURL = '/api/create/package/'
        self.RetrievePackageURL = '/api/package/'
        self.UpdatePackageURL = '/api/update/package/'
        self.DeletePackageURL = '/api/delete/package/'

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
        conn = pymongo.Connection(TestConfig.MONGO_HOST,TestConfig.MONGO_PORT)
        conn[TestConfig.MONGO_DBNAME].drop_collection("learningObjects")
