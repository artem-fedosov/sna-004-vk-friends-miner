# -*- coding: utf-8 -*-
import unittest
import time

import api


TEST_UID = 2806883
TEST_FIELDS = ['city', 'sex']
KNOWN_FRIENDS_OF_TEST_UID = [5534170, 5555900, 5627563, 5744904, 5928888, 6023659, 6249178, 6303430, 6547938]
KNOWN_DEACTIVATED_FRIENDS = [2548, ]
KNOWN_COUNTRY_NAMES = {1: u'Россия', 2: u'Украина', 3: u'Беларусь'}
KNOWN_CITY_NAMES = {1: u'Москва', 11: u'Северодвинск', 23: u'Астрахань'}


class WaitDecoratorTest(unittest.TestCase):
    def test_ok(self):
        wait_time = 1

        @api.wait(wait_time)
        def test_function(x, y):
            return x + y

        start = time.time()
        test_function(1, 2)
        stop = time.time()

        self.assertAlmostEqual(stop - start, 1, 2)


class BaseIntegrationTest(unittest.TestCase):
    pass


class GetUsersDataTest(BaseIntegrationTest):
    def test_ok(self):
        users_data = api.get_users_data(uids=KNOWN_FRIENDS_OF_TEST_UID, fields=api.ALLOWED_USER_INFO_FIELDS)
        data_uids = {data['uid'] for data in users_data}
        self.assertEqual(data_uids, set(KNOWN_FRIENDS_OF_TEST_UID))


class GetFriendsUidsTest(BaseIntegrationTest):
    def test_ok(self):
        friends_uids = api.get_friend_uids(uid=TEST_UID)
        for uid in KNOWN_FRIENDS_OF_TEST_UID + KNOWN_DEACTIVATED_FRIENDS:
            self.assertIn(uid, friends_uids)


class GetFriendsDataTest(BaseIntegrationTest):
    def test_ok(self):
        friends_data = api.get_friends_data(uid=TEST_UID, fields=TEST_FIELDS, remove_deactivated=False)
        data_uids = {data['uid'] for data in friends_data}
        for uid in KNOWN_FRIENDS_OF_TEST_UID + KNOWN_DEACTIVATED_FRIENDS:
            self.assertIn(uid, data_uids)

    def test_remove_deactivated_ok(self):
        friends_data = api.get_friends_data(uid=TEST_UID, fields=TEST_FIELDS)
        data_uids = {data['uid'] for data in friends_data}
        for uid in KNOWN_FRIENDS_OF_TEST_UID:
            self.assertIn(uid, data_uids)

        for uid in KNOWN_DEACTIVATED_FRIENDS:
            self.assertNotIn(uid, data_uids)


class GetCountryNamesTest(BaseIntegrationTest):
    def test_ok(self):
        country_names = api.get_country_names(country_ids=KNOWN_COUNTRY_NAMES.keys())
        self.assertDictEqual(country_names, KNOWN_COUNTRY_NAMES)


class GetCityNamesTest(BaseIntegrationTest):
    def test_ok(self):
        city_names = api.get_city_names(city_ids=KNOWN_CITY_NAMES.keys())
        self.assertDictEqual(city_names, KNOWN_CITY_NAMES)



