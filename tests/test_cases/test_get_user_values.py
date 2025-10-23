#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.get_values import GetValuesTest
from recombee_api_client.api_requests.get_user_values import GetUserValues, DEFAULT


class GetUserValuesTestCase(GetValuesTest):

    def create_request(self, user_id):
        return GetUserValues(user_id)
