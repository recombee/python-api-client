#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.recommendation import RecommendationTest
from recombee_api_client.api_requests.recommend_users_to_item import (
    RecommendUsersToItem,
    DEFAULT,
)


class RecommendUsersToItemTestCase(RecommendationTest):

    def create_request(
        self,
        item_id,
        count,
        scenario=DEFAULT,
        cascade_create=DEFAULT,
        return_properties=DEFAULT,
        included_properties=DEFAULT,
        filter=DEFAULT,
        booster=DEFAULT,
        logic=DEFAULT,
        reql_expressions=DEFAULT,
        diversity=DEFAULT,
        expert_settings=DEFAULT,
        return_ab_group=DEFAULT,
    ):
        return RecommendUsersToItem(
            item_id,
            count,
            scenario=scenario,
            cascade_create=cascade_create,
            return_properties=return_properties,
            included_properties=included_properties,
            filter=filter,
            booster=booster,
            logic=logic,
            reql_expressions=reql_expressions,
            diversity=diversity,
            expert_settings=expert_settings,
            return_ab_group=return_ab_group,
        )
