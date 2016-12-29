#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class RemoveFromSeriesTest (RecombeeTest ):

    def create_request(self,series_id,item_type,item_id,time):
        pass

    def test_remove_from_series(self):

        # it 'fails when removing item which have different time'
        req = self.create_request('entity_id','item','entity_id',0)
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)
        # it 'does not fail when removing item that is contained in the set'
        req = self.create_request('entity_id','item','entity_id',1)
        resp = self.client.send(req)
        # it 'fails when removing item that is not contained in the set'
        req = self.create_request('entity_id','item','not_contained',1)
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)

