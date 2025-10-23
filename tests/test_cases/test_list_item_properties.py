#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_properties import ListPropertiesTest
from recombee_api_client.api_requests.list_item_properties import (
    ListItemProperties,
    DEFAULT,
)


class ListItemPropertiesTestCase(ListPropertiesTest):

    def create_request(self):
        return ListItemProperties()
