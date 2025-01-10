#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

import time
from abc import ABC, abstractmethod
from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class ListSetItemsTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,series_id):
        pass

    def test_list_set_items(self):

        time.sleep(10)
        # it 'lists set items'
        req = self.create_request('entity_id')
        resp = self.client.send(req)
        self.assertEqual(len(resp), 1)
        self.assertEqual(resp[0]['itemId'], 'entity_id')
        self.assertEqual(resp[0]['itemType'], 'item')

