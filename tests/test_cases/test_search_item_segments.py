#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.search_item_segments import SearchItemSegmentsTest
from recombee_api_client.api_requests.search_item_segments import (
    SearchItemSegments,
    DEFAULT,
)


class SearchItemSegmentsTestCase(SearchItemSegmentsTest):

    def create_request(
        self,
        user_id,
        search_query,
        count,
        scenario=DEFAULT,
        cascade_create=DEFAULT,
        filter=DEFAULT,
        booster=DEFAULT,
        logic=DEFAULT,
        expert_settings=DEFAULT,
        return_ab_group=DEFAULT,
    ):
        return SearchItemSegments(
            user_id,
            search_query,
            count,
            scenario=scenario,
            cascade_create=cascade_create,
            filter=filter,
            booster=booster,
            logic=logic,
            expert_settings=expert_settings,
            return_ab_group=return_ab_group,
        )
