#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_segmentation import DeleteSegmentationTest
from recombee_api_client.api_requests import *

class DeleteSegmentationTestCase(DeleteSegmentationTest):

    def create_request(self, segmentation_id):
        return DeleteSegmentation(segmentation_id)
