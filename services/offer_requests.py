import json
from classes.offer import Offer


def load_offers():
    # try:
    with open("./databases/offers.json", "r") as file:
        offers = json.loads(file.read())
        offers_list = [
            Offer(
                i.get("offer_code"),
                float(i.get("discount")),
                {
                    "min": i.get("distance_in_km").get("min"),
                    "max": i.get("distance_in_km").get("max"),
                },
                {
                    "min": i.get("weight_in_kg").get("min"),
                    "max": i.get("weight_in_kg").get("max"),
                },
            )
            for i in offers
        ]
        return offers_list
    # except:
    #     return []


def query_offer(offer_code):
    # try:
    with open("./databases/offers.json", "r") as file:
        offers = json.loads(file.read())

        offers_list = [
            Offer(
                i.get("offer_code"),
                float(i.get("discount")),
                {
                    "min": i.get("distance_in_km").get("min"),
                    "max": i.get("distance_in_km").get("max"),
                },
                {
                    "min": i.get("weight_in_kg").get("min"),
                    "max": i.get("weight_in_kg").get("max"),
                },
            )
            for i in offers
        ]
        offer = next(
            (i for i in offers_list if i.get_offer_code() == offer_code),
            None,
        )

        return offer
    # except:
    #     return None
