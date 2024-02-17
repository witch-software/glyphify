# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Optional
from pathlib import Path

import os


DEFAULT_PATHS: dict[str, dict[str, str]] = {
    "nt": {"org": "Witch Software", "application": "Glyphify"},
    "posix": {"org": "witchsoftware", "application": "glyphify"},
}


def get_user_local_directory(paths: Optional[dict[str, dict[str, str]]] = None) -> Path:
    """ "
    Get the user's local directory for the specified application.

    Args:
        paths (Optional[dict[str, dict[str, str]]]): Dictionary containing platform-specific directory details.
            Defaults to DEFAULT_PATHS.

    Returns:
        Path: The user's local directory for the application.

    Examples:
        Example 1:
        ```
        >>> get_user_local_directory()
        PosixPath('/home/user/.witchsoftware/glyphify/')
        ```

        Example 2:
        ```
        >>> custom_paths = {"nt": {"org": "CustomOrg", "application": "CustomApp"}}
        >>> get_user_local_directory(paths=custom_paths)
        WindowsPath('C:/Users/user/AppData/Local/CustomOrg/CustomApp/')
        ```
    """

    if paths is None:
        paths = DEFAULT_PATHS

    org = paths.get(os.name, {}).get("org", "organization")
    application = paths.get(os.name, {}).get("application", "application")

    if os.name == "posix":
        user_home = Path.home()
        return user_home / f".{org.lower()}/{application.lower()}"
    elif os.name == "nt":
        appdata_path = os.getenv("APPDATA")
        if appdata_path:
            return Path(appdata_path) / org / application
        else:
            raise ValueError("Unable to determine the APPDATA directory.")
    else:
        raise ValueError("Unsupported operating system.")
