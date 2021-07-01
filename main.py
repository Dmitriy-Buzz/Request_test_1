import requests
import operator

TOKEN = "2619421814940190"

hero_lict= []
def test_request_h():
    url = "https://superheroapi.com/api/2619421814940190/search/Hulk"
    headers = {"Authorization": TOKEN}
    response = requests.get(url=url, headers=headers, timeout=5)
    hulk = response.json()
    name = hulk["results-for"]
    intel = int(hulk["results"][0]["powerstats"]["intelligence"])
    hero_dict = {"Имя":name, "Интелект": intel}
    hero_lict.append(hero_dict)

def test_request_t():
    url = "https://superheroapi.com/api/2619421814940190/search/Thanos"
    headers = {"Authorization": TOKEN}
    response = requests.get(url=url, headers=headers, timeout=5)
    thanos = response.json()
    name = thanos["results-for"]
    intel = int(thanos["results"][0]["powerstats"]["intelligence"])
    hero_dict = {"Имя":name, "Интелект": intel}
    hero_lict.append(hero_dict)
def test_request_ca():
    url = "https://superheroapi.com/api/2619421814940190/search/Captain America"
    headers = {"Authorization": TOKEN}
    response = requests.get(url=url, headers=headers, timeout=5)
    cap = response.json()
    name = cap["results-for"]
    intel = int(cap["results"][0]["powerstats"]["intelligence"])
    hero_dict = {"Имя":name, "Интелект": intel}
    hero_lict.append(hero_dict)

def sort_():
    hero_lict.sort(key=operator.itemgetter("Интелект"))
    print(f"Самый умный герой:{hero_lict[-1]}")

test_request_h()
test_request_t()
test_request_ca()
sort_()
