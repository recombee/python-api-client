#
# This file is auto-generated, do not edit
#

from tests.test_cases.add_rating import AddRatingTest
from recombee_api_client.api_requests import *

class AddRatingTestCase (AddRatingTest):

    def create_request(self, user_id, item_id, rating, optional=dict()):
        return AddRating(user_id, item_id, rating, optional)
