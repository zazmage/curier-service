from classes.package import Package
from services.packages_requests import load_packages


class Packages_list:
    def __init__(self):
        packages = load_packages()
        self.__packages = []
        for i in packages:
            self.__packages.append(
                Package(
                    i.get("pkg_id"),
                    i.get("base_delivery_cost"),
                    i.get("pkg_weight_in_kg"),
                )
            )

    def get_packages(self):
        return self.__packages
