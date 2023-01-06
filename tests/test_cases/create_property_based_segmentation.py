#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class CreatePropertyBasedSegmentationTest(RecombeeTest):

    def create_request(self,segmentation_id,source_type,property_name,title=None,description=None):
        pass

    def test_create_property_based_segmentation(self):

        # it 'creates property based segmentation'
        req = self.create_request('seg1', 'items', 'str_property', title='Test Segmentation', description='For test purposes')
        resp = self.client.send(req)
        req = self.create_request('seg1', 'items', 'str_property', title='Test Segmentation', description='For test purposes')
        try:
            self.client.send(req)
            self.assertFail()
        except ResponseException as ex:
            self.assertEqual(ex.status_code, 409)

