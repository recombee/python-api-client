#
# This file is auto-generated, do not edit
#

from tests.test_cases.insert_to_series import InsertToSeriesTest
from recombee_api_client.api_requests import *

class InsertToSeriesTestCase (InsertToSeriesTest):

    def create_request(self, series_id, item_type, item_id, time, optional=dict()):
        return InsertToSeries(series_id, item_type, item_id, time, optional)
