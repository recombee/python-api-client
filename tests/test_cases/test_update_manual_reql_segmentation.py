#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.update_manual_reql_segmentation import UpdateManualReqlSegmentationTest
from recombee_api_client.api_requests import *

class UpdateManualReqlSegmentationTestCase(UpdateManualReqlSegmentationTest):

    def create_request(self, segmentation_id, title=None, description=None):
        return UpdateManualReqlSegmentation(segmentation_id, title=title, description=description)
