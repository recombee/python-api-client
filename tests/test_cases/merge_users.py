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

class MergeUsersTest(RecombeeTest, ABC):

    @abstractmethod
    def create_request(self,target_user_id,source_user_id,cascade_create=None):
        pass

    def test_merge_users(self):

        # it 'does not fail with existing users'
        req = AddUser('target')
        resp = self.client.send(req)
        req = self.create_request('target', 'entity_id')
        resp = self.client.send(req)
        # it 'fails with nonexisting user'
        req = self.create_request('nonex_id', 'entity_id')
        try:
            self.client.send(req)
            self.fail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)

