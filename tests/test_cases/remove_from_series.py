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

class RemoveFromSeriesTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,series_id,item_type,item_id):
        pass

    def test_remove_from_series(self):

        # it 'does not fail when removing item that is contained in the set'
        req = self.create_request('entity_id', 'item', 'entity_id')
        resp = self.client.send(req)
        # it 'fails when removing item that is not contained in the set'
        req = self.create_request('entity_id', 'item', 'not_contained')
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)

