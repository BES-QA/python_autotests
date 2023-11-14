import pprint
import random

import pytest
import requests


BASE_URL = 'https://reqres.in'


def test_positive_check_list_users():
    random_page = random.randint(1, 2)
    res = requests.get(BASE_URL + '/api/users?page=' + str(random_page))

    print(pprint.pprint(res.json()))
    res_body = res.json()

    assert res.status_code == 200
    assert res_body['page'] == random_page
    assert res_body['total'] == 12
    assert res_body['total_pages'] == 2
    assert len(res_body['data']) == 6


@pytest.mark.parametrize('page', (-1, 0, 3))
def test_negative_check_list_users(page):
    res = requests.get(BASE_URL + '/api/users?page=' + str(page))
    print(pprint.pprint(res.json()))
    assert res.status_code == 200
    assert res.json()['page'] == 1
