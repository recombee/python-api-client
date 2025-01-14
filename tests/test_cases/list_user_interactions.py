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

class ListUserInteractionsTest(InteractionsTest, ABC):

    @abstractmethod
    def create_request(self,user_id):
        pass

    def test_list_user_interactions(self):

        time.sleep(10)
        # it 'lists user interactions'
        req = self.create_request('user')
        resp = self.client.send(req)
        self.assertEqual(len(resp), 1)
        self.assertEqual(resp[0]['itemId'], 'item')
        self.assertEqual(resp[0]['userId'], 'user')

