from services.packages_requests import load_packages


class Packages_list:
    def __init__(self):
        self.__packages = load_packages()

    def get_packages(self):
        return self.__packages

    def find_package(self, pkg_id):
        return next(
            (i for i in self.__packages if i.get_pkg_id() == pkg_id),
            None,
        )
