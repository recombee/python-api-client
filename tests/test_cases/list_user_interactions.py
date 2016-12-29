#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class ListUserInteractionsTest (InteractionsTest ):

    def create_request(self,user_id):
        pass

    def test_list_user_interactions(self):

        # it 'lists user interactions'
        req = self.create_request('user')
        resp = self.client.send(req)
        self.assertEqual(len(resp), 1)
        self.assertEqual(resp[0]['itemId'], 'item')
        self.assertEqual(resp[0]['userId'], 'user')

