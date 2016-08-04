#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_interaction import AddInteractionTest
from recombee_api_client.api_requests import *

class AddCartAdditionTestCase (AddInteractionTest):

    def create_request(self, user_id, item_id, optional=dict()):
        return AddCartAddition(user_id, item_id, optional)
