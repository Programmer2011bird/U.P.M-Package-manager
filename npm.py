# from os import mkdir
from os import mkdir
from pathlib import Path
import decompressor
import requests


class npm_handeler:
    def __init__(self, packageName: str, path: str) -> None:
        self.URL: str = f"https://registry.npmjs.org/{packageName}"
        
        RESPONSE: requests.Response = requests.get(self.URL)
        RESPONSE_JSON: dict = dict(RESPONSE.json())
        
        if "error" in RESPONSE_JSON.keys() and RESPONSE_JSON["error"] == "Not found":
            print("OOPS, looks like there is no package found ! ")
        
        else:
            self.TARBALL_URL: str = self.__get_download_link()
            print(self.TARBALL_URL)
            self.tarball_path: str = self.__download(self.TARBALL_URL, path)
            print(self.tarball_path)

            print(str(Path(self.tarball_path)), path)
            decompressor.extractTarball(str(Path(self.tarball_path)), path)

    def __get_download_link(self) -> str:
        RESPONSE: requests.Response = requests.get(self.URL)
        RESPONSE_JSON: dict = dict(RESPONSE.json())

        LATEST_VERSION: str = RESPONSE_JSON["dist-tags"]["latest"]
        LATEST_INFO: dict = dict(RESPONSE_JSON["versions"][LATEST_VERSION])
        
        TARBALL_URL: str = LATEST_INFO["dist"]["tarball"]
        
        return TARBALL_URL

    def __download(self, downloadUrl: str, path: str) -> str:
        RESPONSE: requests.Response = requests.get(downloadUrl)
        RESPONSE_CONTENT: bytes = RESPONSE.content
        
        FILE_NAME: str = downloadUrl.split("/")[-1]

        with open(f"{path}/{FILE_NAME}", "wb") as file:
            file.write(RESPONSE_CONTENT)

        print("downloaded !")

        return f"{path}/{FILE_NAME}"
