#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This file is auto-generated, do not edit
#

import unittest
import os, sys

sys.path.insert(0, os.path.abspath('.'))

if __name__ == '__main__':

    suite = unittest.TestSuite()

    from tests.test_cases.test_add_item import AddItemTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddItemTestCase))
    from tests.test_cases.test_delete_item import DeleteItemTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteItemTestCase))
    from tests.test_cases.test_set_item_values import SetItemValuesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(SetItemValuesTestCase))
    from tests.test_cases.test_get_item_values import GetItemValuesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(GetItemValuesTestCase))
    from tests.test_cases.test_list_items import ListItemsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListItemsTestCase))
    from tests.test_cases.test_add_item_property import AddItemPropertyTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddItemPropertyTestCase))
    from tests.test_cases.test_delete_item_property import DeleteItemPropertyTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteItemPropertyTestCase))
    from tests.test_cases.test_get_item_property_info import GetItemPropertyInfoTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(GetItemPropertyInfoTestCase))
    from tests.test_cases.test_list_item_properties import ListItemPropertiesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListItemPropertiesTestCase))
    from tests.test_cases.test_add_series import AddSeriesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddSeriesTestCase))
    from tests.test_cases.test_delete_series import DeleteSeriesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteSeriesTestCase))
    from tests.test_cases.test_list_series import ListSeriesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListSeriesTestCase))
    from tests.test_cases.test_list_series_items import ListSeriesItemsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListSeriesItemsTestCase))
    from tests.test_cases.test_insert_to_series import InsertToSeriesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(InsertToSeriesTestCase))
    from tests.test_cases.test_remove_from_series import RemoveFromSeriesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RemoveFromSeriesTestCase))
    from tests.test_cases.test_add_group import AddGroupTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddGroupTestCase))
    from tests.test_cases.test_delete_group import DeleteGroupTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteGroupTestCase))
    from tests.test_cases.test_list_groups import ListGroupsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListGroupsTestCase))
    from tests.test_cases.test_list_group_items import ListGroupItemsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListGroupItemsTestCase))
    from tests.test_cases.test_insert_to_group import InsertToGroupTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(InsertToGroupTestCase))
    from tests.test_cases.test_remove_from_group import RemoveFromGroupTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RemoveFromGroupTestCase))
    from tests.test_cases.test_add_user import AddUserTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddUserTestCase))
    from tests.test_cases.test_delete_user import DeleteUserTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteUserTestCase))
    from tests.test_cases.test_set_user_values import SetUserValuesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(SetUserValuesTestCase))
    from tests.test_cases.test_get_user_values import GetUserValuesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(GetUserValuesTestCase))
    from tests.test_cases.test_merge_users import MergeUsersTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(MergeUsersTestCase))
    from tests.test_cases.test_list_users import ListUsersTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListUsersTestCase))
    from tests.test_cases.test_add_user_property import AddUserPropertyTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddUserPropertyTestCase))
    from tests.test_cases.test_delete_user_property import DeleteUserPropertyTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteUserPropertyTestCase))
    from tests.test_cases.test_get_user_property_info import GetUserPropertyInfoTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(GetUserPropertyInfoTestCase))
    from tests.test_cases.test_list_user_properties import ListUserPropertiesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListUserPropertiesTestCase))
    from tests.test_cases.test_add_detail_view import AddDetailViewTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddDetailViewTestCase))
    from tests.test_cases.test_delete_detail_view import DeleteDetailViewTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteDetailViewTestCase))
    from tests.test_cases.test_list_item_detail_views import ListItemDetailViewsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListItemDetailViewsTestCase))
    from tests.test_cases.test_list_user_detail_views import ListUserDetailViewsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListUserDetailViewsTestCase))
    from tests.test_cases.test_add_purchase import AddPurchaseTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddPurchaseTestCase))
    from tests.test_cases.test_delete_purchase import DeletePurchaseTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeletePurchaseTestCase))
    from tests.test_cases.test_list_item_purchases import ListItemPurchasesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListItemPurchasesTestCase))
    from tests.test_cases.test_list_user_purchases import ListUserPurchasesTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListUserPurchasesTestCase))
    from tests.test_cases.test_add_rating import AddRatingTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddRatingTestCase))
    from tests.test_cases.test_delete_rating import DeleteRatingTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteRatingTestCase))
    from tests.test_cases.test_list_item_ratings import ListItemRatingsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListItemRatingsTestCase))
    from tests.test_cases.test_list_user_ratings import ListUserRatingsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListUserRatingsTestCase))
    from tests.test_cases.test_add_cart_addition import AddCartAdditionTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddCartAdditionTestCase))
    from tests.test_cases.test_delete_cart_addition import DeleteCartAdditionTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteCartAdditionTestCase))
    from tests.test_cases.test_list_item_cart_additions import ListItemCartAdditionsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListItemCartAdditionsTestCase))
    from tests.test_cases.test_list_user_cart_additions import ListUserCartAdditionsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListUserCartAdditionsTestCase))
    from tests.test_cases.test_add_bookmark import AddBookmarkTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(AddBookmarkTestCase))
    from tests.test_cases.test_delete_bookmark import DeleteBookmarkTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteBookmarkTestCase))
    from tests.test_cases.test_list_item_bookmarks import ListItemBookmarksTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListItemBookmarksTestCase))
    from tests.test_cases.test_list_user_bookmarks import ListUserBookmarksTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListUserBookmarksTestCase))
    from tests.test_cases.test_set_view_portion import SetViewPortionTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(SetViewPortionTestCase))
    from tests.test_cases.test_delete_view_portion import DeleteViewPortionTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(DeleteViewPortionTestCase))
    from tests.test_cases.test_list_item_view_portions import ListItemViewPortionsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListItemViewPortionsTestCase))
    from tests.test_cases.test_list_user_view_portions import ListUserViewPortionsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ListUserViewPortionsTestCase))
    from tests.test_cases.test_recommend_items_to_user import RecommendItemsToUserTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RecommendItemsToUserTestCase))
    from tests.test_cases.test_recommend_users_to_user import RecommendUsersToUserTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RecommendUsersToUserTestCase))
    from tests.test_cases.test_recommend_items_to_item import RecommendItemsToItemTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RecommendItemsToItemTestCase))
    from tests.test_cases.test_recommend_users_to_item import RecommendUsersToItemTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(RecommendUsersToItemTestCase))
    from tests.test_cases.test_search_items import SearchItemsTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(SearchItemsTestCase))
    from tests.test_cases.test_user_based_recommendation import UserBasedRecommendationTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(UserBasedRecommendationTestCase))
    from tests.test_cases.test_item_based_recommendation import ItemBasedRecommendationTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(ItemBasedRecommendationTestCase))
    from tests.test_cases.test_batch import BatchTestCase
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(BatchTestCase))


    unittest.TextTestRunner().run(suite)
