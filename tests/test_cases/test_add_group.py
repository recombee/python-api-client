#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_entity import AddEntityTest
from recombee_api_client.api_requests import *

class AddGroupTestCase (AddEntityTest):

    def create_request(self, group_id):
        return AddGroup(group_id)
