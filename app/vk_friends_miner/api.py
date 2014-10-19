# -*- coding: utf-8 -*-
import requests
import time

from functools import wraps

API_URL = 'https://api.vk.com/method/'

GET_COUNTRY_NAMES_URL = API_URL + "database.getCountriesById"
GET_CITY_NAMES_URL = API_URL + "database.getCitiesById"

GET_FRIENDS_URL = API_URL + "friends.get"
GET_USERS_INFO_URL = API_URL + "users.get"

ALLOWED_USER_INFO_FIELDS = [
    'relation',
    'sex',
    'bdate',
    'city',
    'country',
    'home_town',
    'education',
    'universities',
    'schools'
]

API_CALL_WAIT_TIME = 0.25


def wait(wait_time):
    def wrapper(fun):
        @wraps(fun)
        def wrapped(*args, **kwargs):
            time.sleep(wait_time)
            return fun(*args, **kwargs)
        return wrapped
    return wrapper


def comma_join(iterable):
    return ','.join(map(str, iterable))


def make_request(url, params, method='GET'):
    response = requests.request(method, url, params=params)
    data = response.json()  # ValueError if not json
    if 'error' in data:
        raise ValueError(data['error']['error_msg'])
    else:
        return data['response']


@wait(API_CALL_WAIT_TIME)
def get_city_names(city_ids):
    dicts = make_request(
        GET_CITY_NAMES_URL,
        params=dict(city_ids=comma_join(city_ids)),
    )
    return {int(item['cid']): item['name'] for item in dicts}


@wait(API_CALL_WAIT_TIME)
def get_country_names(country_ids):
    dicts = make_request(
        GET_COUNTRY_NAMES_URL,
        params=dict(country_ids=comma_join(country_ids)),
    )
    return {int(item['cid']): item['name'] for item in dicts}

@wait(API_CALL_WAIT_TIME)
def get_friend_uids(uid):
    return make_request(
        GET_FRIENDS_URL,
        params=dict(user_id=uid),
    )


@wait(API_CALL_WAIT_TIME)
def get_friends_data(uid, fields, remove_deactivated=True):
    item_list = make_request(
        GET_FRIENDS_URL,
        params=dict(
            user_id=uid,
            fields=comma_join(fields),
        ),
    )
    if remove_deactivated:
        item_list = [item for item in item_list if 'deactivated' not in item]

    return item_list


@wait(API_CALL_WAIT_TIME)
def get_users_data(uids, fields):
    return make_request(
        GET_USERS_INFO_URL,
        params=dict(
            user_ids=comma_join(uids),
            fields=comma_join(fields),
        )
    )






