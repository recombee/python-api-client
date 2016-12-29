#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class InsertToSeriesTest (RecombeeTest ):

    def create_request(self,series_id,item_type,item_id,time,cascade_create=None):
        pass

    def test_insert_to_series(self):

        # it 'does not fail when inserting existing item into existing set'
        req = AddItem('new_item')
        resp = self.client.send(req)
        req = self.create_request('entity_id','item','new_item',3)
        resp = self.client.send(req)
        # it 'does not fail when cascadeCreate is used'
        req = self.create_request('new_set','item','new_item2',1,cascade_create=True)
        resp = self.client.send(req)
        # it 'really inserts item to the set'
        req = AddItem('new_item3')
        resp = self.client.send(req)
        req = self.create_request('entity_id','item','new_item3',2)
        resp = self.client.send(req)
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 409)

