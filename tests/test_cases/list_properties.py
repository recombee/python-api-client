#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class ListPropertiesTest (RecombeeTest ):

    def create_request(self):
        pass

    def test_list_properties(self):

        # it 'lists properties'
        req = self.create_request()
        resp = self.client.send(req)
        self.assertEqual(len(resp), 2)

