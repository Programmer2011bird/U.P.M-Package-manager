import platform
import requests
import sys


class pip_handler:
    def __init__(self, packageName: str) -> None:
        self.URL: str = f"https://pypi.org/pypi/{packageName}/json"
        self.proper_downloadUrl: str = self.get_proper_downloadUrl()
        print(self.proper_downloadUrl)
        
    def get_proper_downloadUrl(self) -> str:
        self.RESPONSE: requests.Response = requests.get(self.URL)
        self.RESPONSE_JSON: dict = dict(self.RESPONSE.json())
       
        self.LATEST_VERSION: str = str(self.RESPONSE_JSON["info"]["version"])
        self.release: list = list(self.RESPONSE_JSON["releases"][self.LATEST_VERSION])
        self.desiredInfo: list[dict[str, str]] = []

        for _, release_info in enumerate(self.release):
            if release_info["packagetype"] == "bdist_wheel":
                self.desiredInfo.append({"pythonVersion":release_info["python_version"], "fileName":release_info["filename"], "downloadUrl":release_info["url"]})
        
        self.currentOs = platform.system().lower().replace("windows", "win")
        self.currentPYversion = f"cp{sys.version_info.major}{sys.version_info.minor}"
        
        return self.check_compatibility(self.currentOs, self.currentPYversion)

    def check_compatibility(self, currentOs: str, currentPYversion: str) -> str:
        CompatibleDownloadUrl: str = ""

        for _, info in enumerate(self.desiredInfo):
            currentPYversionCOMPATIBILITY: bool = currentPYversion in info["pythonVersion"] or "py3" in info["pythonVersion"]
            currentOsCOMPATIBILITY: bool = currentOs in info["fileName"] or "any" in info["fileName"].replace(".", "-").replace("_", "-").split("-")
            
            if currentPYversionCOMPATIBILITY and currentOsCOMPATIBILITY:
                CompatibleDownloadUrl = info["downloadUrl"]
        
        return CompatibleDownloadUrl


if __name__ == "__main__":
    try:
        PIP: pip_handler = pip_handler("torch")

    except KeyError:
        print("OOPS, looks like there is no package found ! ")

