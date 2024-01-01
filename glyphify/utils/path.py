# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from pathlib import Path

import os


DEFAULT_PATHS: dict[str, dict[str, str]] = {
    "nt": {"org": "Witch Software", "application": "Glyphify"},
    "posix": {"org": "witchsoftware", "application": "glyphify"},
}


def get_user_local_directory(paths: dict[str, dict[str, str]] = DEFAULT_PATHS) -> Path:
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

    path: Path

    # Determine the user's local application directory
    if os.name == "posix":
        path = Path(
            os.path.expanduser(
                f"~/.{paths[os.name]['org']}/{paths[os.name]['application']}/"
            )
        )
    elif os.name == "nt":
        path = Path(
            os.path.expanduser(
                f"C:/Users/{os.getlogin()}/AppData/Local/{paths[os.name]['org']}/{paths[os.name]['application']}/"
            )
        )
    else:
        path = Path("./")

    # Create the log directory if it doesn't exist
    os.makedirs(path, exist_ok=True)

    return path
