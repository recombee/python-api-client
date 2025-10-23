#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.item_to_item_recommendation import ItemToItemRecommendationTest
from recombee_api_client.api_requests.recommend_items_to_item import (
    RecommendItemsToItem,
    DEFAULT,
)


class RecommendItemsToItemTestCase(ItemToItemRecommendationTest):

    def create_request(
        self,
        item_id,
        target_user_id,
        count,
        scenario=DEFAULT,
        cascade_create=DEFAULT,
        return_properties=DEFAULT,
        included_properties=DEFAULT,
        filter=DEFAULT,
        booster=DEFAULT,
        logic=DEFAULT,
        reql_expressions=DEFAULT,
        user_impact=DEFAULT,
        diversity=DEFAULT,
        min_relevance=DEFAULT,
        rotation_rate=DEFAULT,
        rotation_time=DEFAULT,
        expert_settings=DEFAULT,
        return_ab_group=DEFAULT,
    ):
        return RecommendItemsToItem(
            item_id,
            target_user_id,
            count,
            scenario=scenario,
            cascade_create=cascade_create,
            return_properties=return_properties,
            included_properties=included_properties,
            filter=filter,
            booster=booster,
            logic=logic,
            reql_expressions=reql_expressions,
            user_impact=user_impact,
            diversity=diversity,
            min_relevance=min_relevance,
            rotation_rate=rotation_rate,
            rotation_time=rotation_time,
            expert_settings=expert_settings,
            return_ab_group=return_ab_group,
        )
