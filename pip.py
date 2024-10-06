import platform
import requests
import sys


class pip_handler:
    def __init__(self, packageName: str, path: str) -> None:
        self.URL: str = f"https://pypi.org/pypi/{packageName}/json"
        
        self.RESPONSE: requests.Response = requests.get(self.URL)
        self.RESPONSE_JSON: dict = dict(self.RESPONSE.json())
       
        if "message" in self.RESPONSE_JSON.keys() and self.RESPONSE_JSON["message"] == "Not Found":
            print("OOPS, looks like there is no package found ! ")
        
        else:
            self.proper_downloadUrl: str = self.__get_proper_downloadUrl()
            self.__download(self.proper_downloadUrl, path)
        
    def __get_proper_downloadUrl(self) -> str:
        self.LATEST_VERSION: str = str(self.RESPONSE_JSON["info"]["version"])
        self.release: list = list(self.RESPONSE_JSON["releases"][self.LATEST_VERSION])
        self.desiredInfo: list[dict[str, str]] = []

        for _, release_info in enumerate(self.release):
            if release_info["packagetype"] == "bdist_wheel":
                self.desiredInfo.append({"pythonVersion":release_info["python_version"], "fileName":release_info["filename"], "downloadUrl":release_info["url"]})
        
        self.currentOs = platform.system().lower().replace("windows", "win")
        self.currentPYversion = f"cp{sys.version_info.major}{sys.version_info.minor}"
        
        return self.__check_compatibility(self.currentOs, self.currentPYversion)

    def __check_compatibility(self, currentOs: str, currentPYversion: str) -> str:
        CompatibleDownloadUrl: str = ""

        for _, info in enumerate(self.desiredInfo):
            currentPYversionCOMPATIBILITY: bool = currentPYversion in info["pythonVersion"] or "py3" in info["pythonVersion"]
            currentOsCOMPATIBILITY: bool = currentOs in info["fileName"] or "any" in info["fileName"].replace(".", "-").replace("_", "-").split("-")
            
            if currentPYversionCOMPATIBILITY and currentOsCOMPATIBILITY:
                CompatibleDownloadUrl = info["downloadUrl"]
        
        return CompatibleDownloadUrl

    def __download(self, downloadUrl: str, path: str) -> None:
        RESPONSE: requests.Response = requests.get(downloadUrl)
        RESPONSE_CONTENT: bytes = RESPONSE.content
        fileName: str = str(downloadUrl.split("/")[-1])
        
        with open(f"{path}/{fileName}", "wb") as file:
            file.write(RESPONSE_CONTENT)

        print("Downloaded !")
