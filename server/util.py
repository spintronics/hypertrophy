import json

cached_fixtures = {}


def get_fixture(name):
    if name in cached_fixtures:
        return cached_fixtures[name]
    with open(f"../fixtures/{name}.json", "r") as file:
        data = json.loads(file.read().strip())
        cached_fixtures[name] = data
        return data
