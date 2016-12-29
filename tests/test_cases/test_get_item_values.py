#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.get_values import GetValuesTest
from recombee_api_client.api_requests import *

class GetItemValuesTestCase (GetValuesTest):

    def create_request(self, item_id):
        return GetItemValues(item_id)
