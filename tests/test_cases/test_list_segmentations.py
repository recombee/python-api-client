#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_segmentations import ListSegmentationsTest
from recombee_api_client.api_requests.list_segmentations import (
    ListSegmentations,
    DEFAULT,
)


class ListSegmentationsTestCase(ListSegmentationsTest):

    def create_request(self, source_type):
        return ListSegmentations(source_type)
