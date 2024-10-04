import sysconfig
import os


def get_Python_InstallDir() -> str:
    site_packages: str = sysconfig.get_paths()["purelib"]

    return site_packages


def get_Node_InstallDir() -> str:
    node_modules = os.path.join(os.getcwd(), "node_modules")
    
    return node_modules
