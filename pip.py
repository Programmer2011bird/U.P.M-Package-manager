import requests


class pip_handler:
    def __init__(self, packageName: str) -> None:
        self.URL: str = f"https://pypi.org/pypi/{packageName}/json"
        
        self.RESPONSE: requests.Response = requests.get(self.URL)
        self.RESPONSE_JSON: dict = dict(self.RESPONSE.json())
        
        
        self.LATEST_VERSION: str = str(self.RESPONSE_JSON["info"]["version"])
        self.release: list = list(self.RESPONSE_JSON["releases"][self.LATEST_VERSION])
        
        self.download_urls: list[str] = []

        for _, release_info in enumerate(self.release):
            # print(release_info)
            if release_info["packagetype"] == "bdist_wheel":
                self.download_urls.append(release_info["url"])

        print(self.download_urls)


if __name__ == "__main__":
    try:
        PIP: pip_handler = pip_handler("requests")
    except KeyError:
        print("OOPS, looks like there is no package found !")

