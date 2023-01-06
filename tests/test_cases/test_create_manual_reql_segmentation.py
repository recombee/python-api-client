#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.create_manual_reql_segmentation import CreateManualReqlSegmentationTest
from recombee_api_client.api_requests import *

class CreateManualReqlSegmentationTestCase(CreateManualReqlSegmentationTest):

    def create_request(self, segmentation_id, source_type, title=None, description=None):
        return CreateManualReqlSegmentation(segmentation_id, source_type, title=title, description=description)
