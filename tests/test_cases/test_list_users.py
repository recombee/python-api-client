#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.list_entities_with_properties import (
    ListEntitiesWithPropertiesTest,
)
from recombee_api_client.api_requests.list_users import ListUsers, DEFAULT


class ListUsersTestCase(ListEntitiesWithPropertiesTest):

    def create_request(
        self,
        filter=DEFAULT,
        count=DEFAULT,
        offset=DEFAULT,
        return_properties=DEFAULT,
        included_properties=DEFAULT,
    ):
        return ListUsers(
            filter=filter,
            count=count,
            offset=offset,
            return_properties=return_properties,
            included_properties=included_properties,
        )
