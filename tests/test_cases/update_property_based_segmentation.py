#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recombee_test import RecombeeTest, InteractionsTest, RecommendationsTest
from recombee_api_client.exceptions import ResponseException
from recombee_api_client.api_requests import *

class UpdatePropertyBasedSegmentationTest(RecombeeTest):

    def create_request(self,segmentation_id,property_name=None,title=None,description=None):
        pass

    def test_update_property_based_segmentation(self):

        # it 'updates property based segmentation'
        req = CreatePropertyBasedSegmentation('seg1', 'items', 'str_property')
        resp = self.client.send(req)
        req = self.create_request('seg1', title='New title', property_name='str_property', description='Updated')
        resp = self.client.send(req)

