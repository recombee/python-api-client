#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.search import SearchTest
from recombee_api_client.api_requests.search_items import SearchItems, DEFAULT


class SearchItemsTestCase(SearchTest):

    def create_request(
        self,
        user_id,
        search_query,
        count,
        scenario=DEFAULT,
        cascade_create=DEFAULT,
        return_properties=DEFAULT,
        included_properties=DEFAULT,
        filter=DEFAULT,
        booster=DEFAULT,
        logic=DEFAULT,
        reql_expressions=DEFAULT,
        expert_settings=DEFAULT,
        return_ab_group=DEFAULT,
    ):
        return SearchItems(
            user_id,
            search_query,
            count,
            scenario=scenario,
            cascade_create=cascade_create,
            return_properties=return_properties,
            included_properties=included_properties,
            filter=filter,
            booster=booster,
            logic=logic,
            reql_expressions=reql_expressions,
            expert_settings=expert_settings,
            return_ab_group=return_ab_group,
        )
