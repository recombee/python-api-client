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

class GetValuesTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,item_id):
        pass

    def test_get_values(self):

        # it 'gets values'
        req = self.create_request('entity_id')
        resp = self.client.send(req)
        self.assertEqual(resp['int_property'], 42)
        self.assertEqual(resp['str_property'], 'hello')

