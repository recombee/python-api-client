#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class GetSegmentationTest(RecombeeTest):

    def create_request(self,segmentation_id):
        pass

    def test_get_segmentation(self):

        # it 'gets existing segmentation'
        req = CreatePropertyBasedSegmentation('seg1', 'items', 'str_property')
        resp = self.client.send(req)
        req = self.create_request('seg1')
        resp = self.client.send(req)
        self.assertEqual(resp['segmentationId'], 'seg1')

