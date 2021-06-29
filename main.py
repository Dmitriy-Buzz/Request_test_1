from pprint import pprint

import requests

TOKEN = "2619421814940190"


def test_request_h():
    url = "https://superheroapi.com/api/2619421814940190/search/Thanos"
    headers = {"Authorization": TOKEN}
    response = requests.get(url=url, headers=headers, timeout=5)
    pprint(response.json())


test_request_h()
