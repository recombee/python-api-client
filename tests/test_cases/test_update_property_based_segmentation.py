#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.update_property_based_segmentation import UpdatePropertyBasedSegmentationTest
from recombee_api_client.api_requests import *

class UpdatePropertyBasedSegmentationTestCase(UpdatePropertyBasedSegmentationTest):

    def create_request(self, segmentation_id, property_name=None, title=None, description=None):
        return UpdatePropertyBasedSegmentation(segmentation_id, property_name=property_name, title=title, description=description)
