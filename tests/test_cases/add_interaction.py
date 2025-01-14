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

class AddInteractionTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,user_id,item_id,timestamp=None,cascade_create=None,recomm_id=None,additional_data=None):
        pass

    def test_add_interaction(self):

        # it 'does not fail with cascadeCreate'
        req = self.create_request('u_id', 'i_id', cascade_create=True, additional_data={'answer': 42})
        resp = self.client.send(req)
        # it 'does not fail with existing item and user'
        req = self.create_request('entity_id', 'entity_id')
        resp = self.client.send(req)
        # it 'does not fail with valid timestamp'
        req = self.create_request('entity_id', 'entity_id', timestamp='2013-10-29T09:38:41.341Z')
        resp = self.client.send(req)
        # it 'fails with nonexisting item id'
        req = self.create_request('entity_id', 'nonex_id')
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)
        # it 'fails with nonexisting user id'
        req = self.create_request('nonex_id', 'entity_id')
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)
        # it 'really stores interaction to the system'
        req = self.create_request('u_id2', 'i_id2', cascade_create=True, timestamp=5)
        resp = self.client.send(req)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 409)

