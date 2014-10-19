# -*- coding: utf-8 -*-
import unittest

import output


TEST_USERS_DATA = [
    {u'uid': 1, u'first_name': u'FirstNameTest1', u'last_name': u'LastNameTest1', u'property1': 14, u'property2': u'op'},
    {u'uid': 2, u'first_name': u'FirstNameTest2', u'last_name': u'LastNameTest2', u'property1': 13, u'property2': u'op'},
    {u'uid': 3, u'first_name': u'ТестовоеИмя3', u'last_name': u'ТестоваяФамилия3', u'property1': 10, u'property2': u'op'},
    {u'uid': 4, u'first_name': u'FirstNameTest4', u'last_name': u'LastNameTest4', u'property1': 11, u'property2': u'op'},
    {u'uid': 5, u'first_name': u'Ира', u'last_name': u'Чигрина', u'sex': 1, u'city': 2, u'user_id':107177}

]

TEST_FRIENDSHIPS = {
    1: [2, 3],
    2: [4, 5],
    3: [5, 6],
    4: [1, 3],
    5: [3, 2],
}

TEST_FILE_NAME = 'test.gml'


class BaseOutputTest(unittest.TestCase):
    pass


class OutputToGlmTest(unittest.TestCase):
    def test_ok(self):
        print output.to_glm(TEST_USERS_DATA, TEST_FRIENDSHIPS, TEST_FILE_NAME)


