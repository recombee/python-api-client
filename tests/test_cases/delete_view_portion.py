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

class DeleteViewPortionTest(InteractionsTest, ABC):

    @abstractmethod
    def create_request(self,user_id,item_id,session_id=None):
        pass

    def test_delete_view_portion(self):

        # it 'does not fail with existing entity id'
        req = self.create_request('user', 'item')
        resp = self.client.send(req)
        req = self.create_request('user', 'item')
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)

