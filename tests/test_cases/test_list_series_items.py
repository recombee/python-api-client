#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_set_items import ListSetItemsTest
from recombee_api_client.api_requests import *

class ListSeriesItemsTestCase(ListSetItemsTest):

    def create_request(self, series_id):
        return ListSeriesItems(series_id)
