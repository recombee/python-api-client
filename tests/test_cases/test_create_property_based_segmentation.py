#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.create_property_based_segmentation import CreatePropertyBasedSegmentationTest
from recombee_api_client.api_requests import *

class CreatePropertyBasedSegmentationTestCase(CreatePropertyBasedSegmentationTest):

    def create_request(self, segmentation_id, source_type, property_name, title=None, description=None):
        return CreatePropertyBasedSegmentation(segmentation_id, source_type, property_name, title=title, description=description)
