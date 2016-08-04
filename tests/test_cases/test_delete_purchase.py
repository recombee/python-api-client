#
# This file is auto-generated, do not edit
#

from tests.test_cases.delete_interaction import DeleteInteractionTest
from recombee_api_client.api_requests import *

class DeletePurchaseTestCase (DeleteInteractionTest):

    def create_request(self, user_id, item_id, optional=dict()):
        return DeletePurchase(user_id, item_id, optional)
