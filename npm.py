import platform
import requests
import sys


class npm_handeler:
    def __init__(self, packageName: str) -> None:
        self.URL: str = f"https://registry.npmjs.org/{packageName}"
        self.__get_download_link()

    def __get_download_link(self) -> None:
        self.RESPONSE: requests.Response = requests.get(self.URL)
        self.RESPONSE_JSON: dict = dict(self.RESPONSE.json())

        self.LATEST_VERSION: str = self.RESPONSE_JSON["dist-tags"]["latest"]
        self.LATEST_INFO: dict = dict(self.RESPONSE_JSON["versions"][self.LATEST_VERSION])
        
        self.TARBALL_URL: str = self.LATEST_INFO["dist"]["tarball"]

        print(self.TARBALL_URL)


if __name__ == "__main__":
    try:
        PIP: npm_handeler = npm_handeler("express")

    except KeyError:
        print("OOPS, looks like there is no package found ! ")

