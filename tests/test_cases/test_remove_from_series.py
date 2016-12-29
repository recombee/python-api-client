#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.remove_from_series import RemoveFromSeriesTest
from recombee_api_client.api_requests import *

class RemoveFromSeriesTestCase (RemoveFromSeriesTest):

    def create_request(self, series_id, item_type, item_id, time):
        return RemoveFromSeries(series_id, item_type, item_id, time)
