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
    from recombee_api_client.api_requests import AddUser, AddItem, AddPurchase, UserBasedRecommendation, Batch
    import random

    # Prepare some items and users
    NUM = 100
    my_users = ["user-%s" % i for i in range(NUM) ]
    my_items = ["item-%s" % i for i in range(NUM) ]

    #Generate some random purchases of items by users
    PROBABILITY_PURCHASED = 0.1
    my_purchases = []
    for user_id in my_users:
        p = [item_id for item_id in my_items if random.random() < PROBABILITY_PURCHASED]
        for item_id in p:
            my_purchases.append({'userId': user_id, 'itemId': item_id})

    # Use Recombee recommender
    client = RecombeeClient('client-test', 'jGGQ6ZKa8rQ1zTAyxTc0EMn55YPF7FJLUtaMLhbsGxmvwxgTwXYqmUk5xVZFw98L')

    try:
        # Send the data to Recombee, use Batch for faster processing
        print('Send users')
        client.send(Batch([AddUser(user_id) for user_id in my_users]))
        print('Send items')
        client.send(Batch([AddItem(item_id) for item_id in my_items]))
        print('Send purchases')
        client.send(Batch([AddPurchase(p['userId'], p['itemId']) for p in my_purchases]))

        # Get recommendations for user 'user-25'
        print('Recommend for a user')
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
          '!cascadeCreate': True   # Use !cascadeCreate for creating item
                                   # with given itemId, if it doesn't exist
        }
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