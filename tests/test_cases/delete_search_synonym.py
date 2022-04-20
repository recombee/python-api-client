#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class DeleteSearchSynonymTest(RecombeeTest):

    def create_request(self,id):
        pass

    def test_delete_search_synonym(self):

        # it 'deletes search synonym'
        req = AddSearchSynonym('sci-fi', 'science fiction')
        resp = self.client.send(req)
        req = self.create_request(resp['id'])
        resp = self.client.send(req)
        req = self.create_request('a968271b-d666-4dfb-8a30-f459e564ba7b')
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 404)

