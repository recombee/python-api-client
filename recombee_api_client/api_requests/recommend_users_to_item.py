from recombee_api_client.api_requests.request import Request
import uuid

DEFAULT = uuid.uuid4()

class RecommendUsersToItem(Request):
    """
    This feature is currently in beta.
    
    Recommend users that are likely to be interested in a given item.
    
    It is also possible to use POST HTTP method (for example in case of very long ReQL filter) - query parameters then become body parameters.

    """

    def __init__(self, item_id, count, filter=DEFAULT, booster=DEFAULT, cascade_create=DEFAULT, scenario=DEFAULT, return_properties=DEFAULT, included_properties=DEFAULT, diversity=DEFAULT, expert_settings=DEFAULT):
        """
        Required parameters:
        @param item_id: ID of the item for which the recommendations are to be generated.
        
        @param count: Number of items to be recommended (N for the top-N recommendation).
        
        
        Optional parameters:
        @param filter: Boolean-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to filter recommended items based on the values of their attributes.
        
        @param booster: Number-returning [ReQL](https://docs.recombee.com/reql.html) expression which allows you to boost recommendation rate of some items based on the values of their attributes.
        
        @param cascade_create: If item of given *itemId* doesn't exist in the database, it creates the missing item.
        
        @param scenario: Scenario defines a particular application of recommendations. It can be for example "homepage", "cart" or "emailing". You can see each scenario in the UI separately, so you can check how well each application performs. The AI which optimizes models in order to get the best results may optimize different scenarios separately, or even use different models in each of the scenarios.
        
        @param return_properties: With `returnProperties=true`, property values of the recommended users are returned along with their IDs in a JSON dictionary. The acquired property values can be used for easy displaying the recommended users. 
        
        
        Example response:
        
        ```
        
        E{lb}
        
        "recommId": "9eeebc318508302529e3241f4570834d",
        
        "recomms":
        
        [
        
        E{lb}
        
        "id": "user-17",
        
        "values": E{lb}
        
        "country": "US",
        
        "sex": "F"
        E{rb}
        E{rb},
        
        E{lb}
        
        "id": "user-2",
        
        "values": E{lb}
        
        "country": "CAN",
        
        "sex": "M"
        E{rb}
        E{rb}
        
        ]
        E{rb}
        
        ```
        
        
        @param included_properties: Allows to specify, which properties should be returned when `returnProperties=true` is set. The properties are given as a comma-separated list. 
        
        
        Example response for `includedProperties=country`:
        
        ```
        
        E{lb}
        
        "recommId": "d4c826635efc3e01a83470008c5697f1",
        
        "recomms":
        
        [
        
        E{lb}
        
        "id": "user-17",
        
        "values": E{lb}
        
        "country": "US"
        E{rb}
        E{rb},
        
        E{lb}
        
        "id": "user-2",
        
        "values": E{lb}
        
        "country": "CAN"
        E{rb}
        E{rb}
        
        ]
        E{rb}
        
        ```
        
        
        @param diversity: **Expert option** Real number from [0.0, 1.0] which determines how much mutually dissimilar should the recommended items be. The default value is 0.0, i.e., no diversification. Value 1.0 means maximal diversification.
        
        
        @param expert_settings: Dictionary of custom options.
        
        
        """
        self.item_id = item_id
        self.count = count
        self.filter = filter
        self.booster = booster
        self.cascade_create = cascade_create
        self.scenario = scenario
        self.return_properties = return_properties
        self.included_properties = included_properties
        self.diversity = diversity
        self.expert_settings = expert_settings
        self.timeout = 3000
        self.ensure_https = False
        self.method = 'post'
        self.path = "/recomms/items/%s/users/" % (self.item_id)

    def get_body_parameters(self):
        """
        Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['count'] = self.count
        if self.filter is not DEFAULT:
            p['filter'] = self.filter
        if self.booster is not DEFAULT:
            p['booster'] = self.booster
        if self.cascade_create is not DEFAULT:
            p['cascadeCreate'] = self.cascade_create
        if self.scenario is not DEFAULT:
            p['scenario'] = self.scenario
        if self.return_properties is not DEFAULT:
            p['returnProperties'] = self.return_properties
        if self.included_properties is not DEFAULT:
            p['includedProperties'] = self.included_properties
        if self.diversity is not DEFAULT:
            p['diversity'] = self.diversity
        if self.expert_settings is not DEFAULT:
            p['expertSettings'] = self.expert_settings
        return p

    def get_query_parameters(self):
        """
        Values of query parameters as a dictionary (name of parameter: value of the parameter).
        """
        params = dict()
        return params
