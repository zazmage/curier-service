from services.packages_requests import load_packages


class Packages_list:
    def __init__(self) -> None:
        self.__packages = load_packages()

    def get_packages(self):
        return self.__packages
