#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_interaction import AddInteractionTest
from recombee_api_client.api_requests.add_cart_addition import AddCartAddition, DEFAULT


class AddCartAdditionTestCase(AddInteractionTest):

    def create_request(
        self,
        user_id,
        item_id,
        timestamp=DEFAULT,
        cascade_create=DEFAULT,
        amount=DEFAULT,
        price=DEFAULT,
        recomm_id=DEFAULT,
        additional_data=DEFAULT,
    ):
        return AddCartAddition(
            user_id,
            item_id,
            timestamp=timestamp,
            cascade_create=cascade_create,
            amount=amount,
            price=price,
            recomm_id=recomm_id,
            additional_data=additional_data,
        )
