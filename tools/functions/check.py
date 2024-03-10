import subprocess
import sys


def current_version():
    return "Dev-0.1"


def wsl():
    linux = system("linux")
    if linux is True:
        response = subprocess.run(["cat", "/proc/version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "microsoft-standard-WSL2" in response.stdout:
            return True
        else:
            return False
    else:
        return False


def system(platform: str):
    """
    Allows for checking which system one is in.
    Available options:
    macOS:     darwin
    Linux:     linux
    Windows:   win32
    :param platform: linux, win32, darwin
    :return: True or False
    """
    os_platform = sys.platform
    if os_platform == platform:
        return True
    else:
        return False
