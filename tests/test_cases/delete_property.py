#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class DeletePropertyTest (RecombeeTest ):

    def create_request(self,property_name):
        pass

    def test_delete_property(self):

        # it 'does not fail with existing property'
        req = self.create_request('int_property')
        resp = self.client.send(req)
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)
        # it 'fails with invalid property'
        req = self.create_request('not_valid_id-*.?!')
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)
        # it 'fails with non-existing property'
        req = self.create_request('not_existing')
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)

