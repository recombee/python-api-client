from tests.test_cases.recommendation import RecommendationTest
from recombee_api_client.api_requests import *

class ItemBasedRecommendationTestCase (RecommendationTest):

  def create_request(self, item_id, count, optional=dict()):
    optional['targetUserId'] = 'entity_id'
    return ItemBasedRecommendation(item_id, count, optional)