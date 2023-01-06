#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.update_auto_reql_segmentation import UpdateAutoReqlSegmentationTest
from recombee_api_client.api_requests import *

class UpdateAutoReqlSegmentationTestCase(UpdateAutoReqlSegmentationTest):

    def create_request(self, segmentation_id, expression=None, title=None, description=None):
        return UpdateAutoReqlSegmentation(segmentation_id, expression=expression, title=title, description=description)
