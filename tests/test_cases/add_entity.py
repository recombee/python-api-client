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

class AddEntityTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,item_id):
        pass

    def test_add_entity(self):

        # it 'does not fail with valid entity id'
        req = self.create_request('valid_id')
        resp = self.client.send(req)
        # it 'fails with invalid entity id'
        req = self.create_request('***not_valid$$$')
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 400)
        # it 'really stores entity to the system'
        req = self.create_request('valid_id2')
        resp = self.client.send(req)
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 409)

