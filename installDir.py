from pathlib import Path
import decompressor
import sysconfig
import npm
import pip
import os


def __get_Python_InstallDir() -> str:
    site_packages: str = sysconfig.get_paths()["purelib"]
    return site_packages

def __get_Node_InstallDir() -> str:
    node_modules: str = os.path.join(os.getcwd(), "node_modules")
    return node_modules

def install_PIP(packageName: str) -> None:
    Python_InstallDir: str = __get_Python_InstallDir()
    PIP: pip.pip_handler = pip.pip_handler(packageName, Python_InstallDir)

def install_NPM(packageName: str) -> None:
    JS_InstallDir: str = __get_Node_InstallDir()
    NPM: npm.npm_handeler = npm.npm_handeler(packageName, JS_InstallDir)

def decompress_PIP_packages(packageName: str) -> None:
    Python_Installdir: Path = Path(__get_Python_InstallDir())
    files: list[str] = list(Python_Installdir.walk())[0][2]
    parent_dir: Path = list(Python_Installdir.walk())[0][0]
    
    for _, file in enumerate(files):
        if packageName in str(file) and ".whl" in str(file):
            decompressor.extractWheel(str(Path(parent_dir/file)), str(parent_dir))
            print("decompressed !")

            break

def decompress_NPM_packages(packageName: str) -> None:
    NPM_instalDir: Path = Path(__get_Node_InstallDir())
    files: list[str] = list(NPM_instalDir.walk())[0][2]
    parent_dir: Path = list(NPM_instalDir.walk())[0][0]
    
    for _, file in enumerate(files):
        if packageName in str(file) and ".tgz" in str(file):
            decompressor.extractTarball(str(Path(parent_dir/file)), str(parent_dir))
            
            print("decompressed !")

            break
