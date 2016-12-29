#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class ListSetItemsTest (RecombeeTest ):

    def create_request(self,series_id):
        pass

    def test_list_set_items(self):

        # it 'lists set items'
        req = self.create_request('entity_id')
        resp = self.client.send(req)
        self.assertEqual(len(resp), 1)
        self.assertEqual(resp[0]['itemId'], 'entity_id')
        self.assertEqual(resp[0]['itemType'], 'item')

