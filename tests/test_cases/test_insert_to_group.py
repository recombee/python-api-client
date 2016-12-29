#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.insert_to_group import InsertToGroupTest
from recombee_api_client.api_requests import *

class InsertToGroupTestCase (InsertToGroupTest):

    def create_request(self, group_id, item_type, item_id, cascade_create=None):
        return InsertToGroup(group_id, item_type, item_id, cascade_create=cascade_create)
