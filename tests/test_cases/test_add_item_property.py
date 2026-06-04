#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_item_property import AddItemPropertyTest
from recombee_api_client.api_requests.add_item_property import AddItemProperty, DEFAULT


class AddItemPropertyTestCase(AddItemPropertyTest):

    def create_request(self, property_name, type, role=DEFAULT, metadata=DEFAULT):
        return AddItemProperty(property_name, type, role=role, metadata=metadata)
