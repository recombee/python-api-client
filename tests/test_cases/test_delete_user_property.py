#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_property import DeletePropertyTest
from recombee_api_client.api_requests import *

class DeleteUserPropertyTestCase (DeletePropertyTest):

    def create_request(self, property_name):
        return DeleteUserProperty(property_name)
