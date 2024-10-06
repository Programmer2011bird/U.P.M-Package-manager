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
