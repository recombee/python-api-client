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

class ListEntitiesTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self):
        pass

    def test_list_entities(self):

        time.sleep(10)
        # it 'lists entities'
        req = self.create_request()
        resp = self.client.send(req)
        self.assertEqual(resp, ['entity_id'])

