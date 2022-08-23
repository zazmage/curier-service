import json


def load_offers():
    try:
        with open("./databases/offers.json", "r") as file:
            offers = json.loads(file.read())
            return offers
    except:
        return []
