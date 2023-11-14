import pprint
import random

import pytest
import requests

from selenium_ui_api_tests.api_tests.data_generator import data_generator

BASE_URL = 'https://reqres.in'


def test_positive_check_list_users():
    random_page = random.randint(1, 2)
    res = requests.get(BASE_URL + '/api/users?page=' + str(random_page))

    # print(pprint.pprint(res.json()))
    res_body = res.json()

    assert res.status_code == 200
    assert res_body['page'] == random_page
    assert res_body['total'] == 12
    assert res_body['total_pages'] == 2
    assert len(res_body['data']) == 6


@pytest.mark.parametrize('page', (-1, 0, 3))
def test_negative_check_list_users(page):
    res = requests.get(BASE_URL + '/api/users?page=' + str(page))
    # print(pprint.pprint(res.json()))

    assert res.status_code == 200
    assert res.json()['page'] == 1


def test_create_user():
    name = data_generator.random_name()
    job = data_generator.random_name()
    data = {
        'name': name,
        'job': job
    }

    res = requests.post(BASE_URL + '/api/users', json=data)
    # print(pprint.pprint(res.json()))

    assert res.status_code == 201
    assert name in res.json()['name']
    assert 'id' in res.json()
    assert 'createdAt' in res.json()
