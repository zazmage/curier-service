import json
from classes.package import Package


def load_packages():
    try:
        with open("./databases/packages.json", "r") as file:
            packages = json.loads(file.read())
            packages_list = [
                Package(
                    i.get("pkg_id"),
                    i.get("distance_in_km"),
                    i.get("offer_code"),
                )
                for i in packages
            ]
            return packages_list
    except:
        return []


def query_packages_ids(pkg_id_list):
    try:
        with open("./databases/packages.json", "r") as file:
            packages = json.loads(file.read())
            packages_list = [
                Package(
                    i.get("pkg_id"),
                    i.get("distance_in_km"),
                    i.get("offer_code"),
                )
                for i in packages
            ]
            packages_list = [
                i for i in packages_list if i.get_pkg_id() in pkg_id_list
            ]
            return packages_list
    except:
        return []


def query_package_id(pkg_id):
    try:
        with open("./databases/packages.json", "r") as file:
            packages = json.loads(file.read())
            packages_list = [
                Package(
                    i.get("pkg_id"),
                    i.get("distance_in_km"),
                    i.get("offer_code"),
                )
                for i in packages
            ]
            package = next(
                (i for i in packages_list if i.get_pkg_id() in pkg_id), None
            )
            return package
    except:
        return []
