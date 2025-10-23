#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.get_property_info import GetPropertyInfoTest
from recombee_api_client.api_requests.get_item_property_info import (
    GetItemPropertyInfo,
    DEFAULT,
)


class GetItemPropertyInfoTestCase(GetPropertyInfoTest):

    def create_request(self, property_name):
        return GetItemPropertyInfo(property_name)
