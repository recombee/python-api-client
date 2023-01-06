#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.get_segmentation import GetSegmentationTest
from recombee_api_client.api_requests import *

class GetSegmentationTestCase(GetSegmentationTest):

    def create_request(self, segmentation_id):
        return GetSegmentation(segmentation_id)
