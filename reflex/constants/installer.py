"""File for constants related to the installation process. (Bun/FNM/Node)."""

from __future__ import annotations

import os
import platform
from types import SimpleNamespace

from .base import IS_WINDOWS, Reflex


def get_fnm_name() -> str | None:
    """Get the appropriate fnm executable name based on the current platform.

    Returns:
            The fnm executable name for the current platform.
    """
    platform_os = platform.system()

    if platform_os == "Windows":
        return "fnm-windows"
    elif platform_os == "Darwin":
        return "fnm-macos"
    elif platform_os == "Linux":
        machine = platform.machine()
        if machine == "arm" or machine.startswith("armv7"):
            return "fnm-arm32"
        elif machine.startswith("aarch") or machine.startswith("armv8"):
            return "fnm-arm64"
        return "fnm-linux"
    return None


# Bun config.
class Bun(SimpleNamespace):
    """Bun constants."""

    # The Bun version.
    VERSION = "1.1.10"
    # Min Bun Version
    MIN_VERSION = "0.7.0"
    # The directory to store the bun.
    ROOT_PATH = os.path.join(Reflex.DIR, "bun")
    # Default bun path.
    DEFAULT_PATH = os.path.join(
        ROOT_PATH, "bin", "bun" if not IS_WINDOWS else "bun.exe"
    )
    # URL to bun install script.
    INSTALL_URL = "https://bun.sh/install"
    # URL to windows install script.
    WINDOWS_INSTALL_URL = (
        "https://raw.githubusercontent.com/reflex-dev/reflex/main/scripts/install.ps1"
    )
    # Path of the bunfig file
    CONFIG_PATH = "bunfig.toml"


# FNM config.
class Fnm(SimpleNamespace):
    """FNM constants."""

    # The FNM version.
    VERSION = "1.35.1"
    # The directory to store fnm.
    DIR = os.path.join(Reflex.DIR, "fnm")
    FILENAME = get_fnm_name()
    # The fnm executable binary.
    EXE = os.path.join(DIR, "fnm.exe" if IS_WINDOWS else "fnm")

    # The URL to the fnm release binary
    INSTALL_URL = (
        f"https://github.com/Schniz/fnm/releases/download/v{VERSION}/{FILENAME}.zip"
    )


# Node / NPM config
class Node(SimpleNamespace):
    """Node/ NPM constants."""

    # The Node version.
    VERSION = "18.17.0"
    # The minimum required node version.
    MIN_VERSION = "18.17.0"

    # The node bin path.
    BIN_PATH = os.path.join(
        Fnm.DIR,
        "node-versions",
        f"v{VERSION}",
        "installation",
        "bin" if not IS_WINDOWS else "",
    )
    # The default path where node is installed.
    PATH = os.path.join(BIN_PATH, "node.exe" if IS_WINDOWS else "node")

    # The default path where npm is installed.
    NPM_PATH = os.path.join(BIN_PATH, "npm")


class PackageJson(SimpleNamespace):
    """Constants used to build the package.json file."""

    class Commands(SimpleNamespace):
        """The commands to define in package.json."""

        DEV = "next dev"
        EXPORT = "next build"
        EXPORT_SITEMAP = "next build && next-sitemap"
        PROD = "next start"

    PATH = "package.json"

    DEPENDENCIES = {
        "@babel/standalone": "7.25.3",
        "@emotion/react": "11.11.1",
        "axios": "1.6.0",
        "json5": "2.2.3",
        "next": "14.0.1",
        "next-sitemap": "4.1.8",
        "next-themes": "0.2.1",
        "react": "18.2.0",
        "react-dom": "18.2.0",
        "react-focus-lock": "2.11.3",
        "socket.io-client": "4.6.1",
        "universal-cookie": "4.0.4",
    }
    DEV_DEPENDENCIES = {
        "autoprefixer": "10.4.14",
        "postcss": "8.4.31",
        "postcss-import": "16.1.0",
    }
