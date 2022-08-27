import json
from classes.offer import Offer


def load_offers():
    try:
        with open("./databases/offers.json", "r") as file:
            offers = json.loads(file.read())
            offers_list = [
                Offer(
                    i.get("offer_code"),
                    i.get("discount"),
                    i.get("distance_in_km"),
                    i.get("weight_in_kg"),
                )
                for i in offers
            ]
            return offers_list
    except:
        return []


def query_offer(offer_code):
    try:
        with open("./databases/offers.json", "r") as file:
            offers = json.loads(file.read())
            offers_list = [
                Offer(
                    i.get("offer_code"),
                    i.get("discount"),
                    i.get("distance_in_km"),
                    i.get("weight_in_kg"),
                )
                for i in offers
            ]
            offer = next(
                (i for i in offers_list if i.get_offer_code() == offer_code),
                None,
            )
            return offer
    except:
        return None
