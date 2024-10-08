import decompressor
import sysconfig
import npm
import pip
import os


def get_Python_InstallDir() -> str:
    site_packages: str = sysconfig.get_paths()["purelib"]

    return site_packages

def get_Node_InstallDir() -> str:
    node_modules = os.path.join(os.getcwd(), "node_modules")
    
    return node_modules

def install_PIP_InstallDir(packageName: str) -> None:
    Python_InstallDir: str = get_Python_InstallDir()
    PIP: pip.pip_handler = pip.pip_handler(packageName, Python_InstallDir)

def install_Node_InstallDir(packageName: str) -> None:
    JS_InstallDir: str = get_Node_InstallDir()
    NPM: npm.npm_handeler = npm.npm_handeler(packageName, JS_InstallDir)


if __name__ == "__main__":
    # install_PIP_InstallDir("tqdm")
    install_Node_InstallDir("express")
