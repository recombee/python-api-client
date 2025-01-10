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

class DeleteMoreItemsTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,filter):
        pass

    def test_delete_more_items(self):

        # it 'deletes more items'
        req = self.create_request('\'int_property\' == 42')
        resp = self.client.send(req)
        self.assertEqual(len(resp['itemIds']), 1)
        self.assertEqual(resp['count'], 1)

