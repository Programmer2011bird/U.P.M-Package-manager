from zipfile import ZipFile
import tarfile


class extractWheel:
    def __init__(self, path: str, output_dir: str) -> None:
        self.__decompress(path, output_dir)

    def __decompress(self, path: str, output_dir: str):
        with ZipFile(f"{path}", 'r') as obj:
            obj.extractall(output_dir)


class extractTarball:
    def __init__(self, path: str, output_dir: str) -> None:
        self.__decompress(path, output_dir)

    def __decompress(self, path: str, output_dir: str):
        with tarfile.open(path, "r") as tar:
            tar.extractall(output_dir)


if __name__ == "__main__":
    wheel_extractor: extractWheel = extractWheel("Test_Files/requests-2.32.3-py3-none-any.whl", "Test_Files/requests")
    tarball_extractor: extractTarball = extractTarball("Test_Files/express-4.21.0.tgz", "Test_Files/express")
    
