#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.get_property_info import GetPropertyInfoTest
from recombee_api_client.api_requests import *

class GetUserPropertyInfoTestCase (GetPropertyInfoTest):

    def create_request(self, property_name):
        return GetUserPropertyInfo(property_name)
