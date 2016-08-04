#
# This file is auto-generated, do not edit
#

from tests.test_cases.recommendation import RecommendationTest
from recombee_api_client.api_requests import *

class UserBasedRecommendationTestCase (RecommendationTest):

    def create_request(self, user_id, count, optional=dict()):
        return UserBasedRecommendation(user_id, count, optional)
