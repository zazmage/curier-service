import json


def load_packages():
    try:
        with open("./databases/packages.json", "r") as file:
            packages = json.loads(file.read())
            return packages
    except:
        return []
