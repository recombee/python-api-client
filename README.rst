*****************
RecombeeApiClient
*****************

A Python client for easy use of the `Recombee <https://www.recombee.com/>`_  recommendation API.

If you don't have an account at Recombee yet, you can create a free account `here <https://www.recombee.com/>`_.

Documentation of the API can be found at `docs.recombee.com <https://docs.recombee.com/)>`_.

=============
Installation
=============

Install the client with pip:

.. code-block:: bash

    $ pip install recombee-api-client

========
Examples
========

-------------
Basic example
-------------

.. code-block:: python

    from recombee_api_client.api_client import RecombeeClient
    from recombee_api_client.exceptions import APIException
    from recombee_api_client.api_requests import AddPurchase, UserBasedRecommendation, Batch
    import random

    client = RecombeeClient('client-test', 'jGGQ6ZKa8rQ1zTAyxTc0EMn55YPF7FJLUtaMLhbsGxmvwxgTwXYqmUk5xVZFw98L')

    #Generate some random purchases of items by users
    PROBABILITY_PURCHASED = 0.1
    NUM = 100
    purchase_requests = []

    for user_id in ["user-%s" % i for i in range(NUM) ]:
      for item_id in ["item-%s" % i for i in range(NUM) ]:
        if random.random() < PROBABILITY_PURCHASED:

          request = AddPurchase(user_id, item_id, cascade_create=True)
          purchase_requests.append(request)

    try:
        # Send the data to Recombee, use Batch for faster processing of larger data
        print('Send purchases')
        client.send(Batch(purchase_requests))

        # Get recommendations for user 'user-25'
        recommended = client.send(UserBasedRecommendation('user-25', 5))
        print("Recommended items: %s" % recommended)

    except APIException as e:
        print(e)


---------------------
Using property values
---------------------

.. code-block:: python


    from recombee_api_client.api_client import RecombeeClient
    from recombee_api_client.api_requests import AddItemProperty, SetItemValues, AddPurchase
    from recombee_api_client.api_requests import ItemBasedRecommendation, Batch, ResetDatabase
    import random

    NUM = 100
    PROBABILITY_PURCHASED = 0.1

    client = RecombeeClient('client-test', 'jGGQ6ZKa8rQ1zTAyxTc0EMn55YPF7FJLUtaMLhbsGxmvwxgTwXYqmUk5xVZFw98L')

    #Clear the entire database
    client.send(ResetDatabase())

    # We will use computers as items in this example
    # Computers have three properties 
    #   - price (floating point number)
    #   - number of processor cores (integer number)
    #   - description (string)

    # Add properties of items
    client.send(AddItemProperty('price', 'double'))
    client.send(AddItemProperty('num-cores', 'int'))
    client.send(AddItemProperty('description', 'string'))

    # Prepare requests for setting a catalog of computers
    requests = [SetItemValues(
        "computer-%s" % i, #itemId
        #values:
        { 
          'price': random.uniform(500, 2000),
          'num-cores': random.randrange(1,9),
          'description': 'Great computer',
        },
        cascade_create=True   # Use cascadeCreate for creating item
                              # with given itemId if it doesn't exist
      ) for i in range(NUM)]


    # Send catalog to the recommender system
    client.send(Batch(requests))

    # Prepare some purchases of items by users
    requests = []
    items = ["computer-%s" % i for i in range(NUM)]
    users = ["user-%s" % i for i in range(NUM)]

    for item_id in items:
        #Use cascadeCreate to create unexisting users
        purchasing_users = [user_id for user_id in users if random.random() < PROBABILITY_PURCHASED]
        requests += [AddPurchase(user_id, item_id, cascade_create=True) for user_id in purchasing_users]

    # Send purchases to the recommender system
    client.send(Batch(requests))

    # Get 5 recommendations for user-42, who is currently viewing computer-6
    recommended = client.send(ItemBasedRecommendation('computer-6', 5, target_user_id='user-42'))
    print("Recommended items: %s" % recommended)

    # Get 5 recommendations for user-42, but recommend only computers that
    # have at least 3 cores
    recommended = client.send(
        ItemBasedRecommendation('computer-6', 5, target_user_id='user-42', filter="'num-cores'>=3")
    )
    print("Recommended items with at least 3 processor cores: %s" % recommended)

    # Get 5 recommendations for user-42, but recommend only items that
    # are more expensive then currently viewed item (up-sell)
    recommended = client.send(
        ItemBasedRecommendation('computer-6', 5, target_user_id='user-42', filter="'price' > context_item[\"price\"]")
    )
    print("Recommended up-sell items: %s" % recommended)
  
------------------
Exception handling
------------------

For the sake of brevity, the above examples omit exception handling. However, various exceptions can occur while processing request, for example because of adding an already existing item, submitting interaction of nonexistent user or because of timeout.

We are doing our best to provide the fastest and most reliable service, but production-level applications must implement a fallback solution since errors can always happen. The fallback might be, for example, showing the most popular items from the current category, or not displaying recommendations at all.

Example:

.. code-block:: python

  try:
    recommended = client.send(
    ItemBasedRecommendation('computer-6', 5,target_user_id='user-42', filter="'price' > context_item[\"price\"]")
    )
  except ResponseException as e:
    #Handle errorneous request => use fallback
  except ApiTimeoutException as e:
    #Handle timeout => use fallback
  except APIException as e:
    #APIException is parent of both ResponseException and ApiTimeoutException