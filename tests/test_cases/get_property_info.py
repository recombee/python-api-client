#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class GetPropertyInfoTest (RecombeeTest ):

    def create_request(self,property_name):
        pass

    def test_get_property_info(self):

        # it 'does not fail with existing properties'
        req = self.create_request('int_property')
        resp = self.client.send(req)
        self.assertEqual(resp['type'], 'int')
        req = self.create_request('str_property')
        resp = self.client.send(req)
        self.assertEqual(resp['type'], 'string')

