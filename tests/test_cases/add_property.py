#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class AddPropertyTest (RecombeeTest ):

    def create_request(self,property_name,type):
        pass

    def test_add_property(self):

        # it 'does not fail with valid name and type'
        req = self.create_request('number','int')
        resp = self.client.send(req)
        req = self.create_request('str','string')
        resp = self.client.send(req)
        # it 'fails with invalid type'
        req = self.create_request('prop','integer')
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)
        # it 'really stores property to the system'
        req = self.create_request('number2','int')
        resp = self.client.send(req)
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 409)

