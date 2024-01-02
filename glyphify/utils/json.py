# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Any
from pathlib import Path

from json import load, dump


def load_json_file(path: Path) -> dict[Any, Any]:
    """
    Load JSON data from a file.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        dict[Any, Any]: A dictionary containing the loaded JSON data.

    Example:
        ```
        >>> load_json_file(Path("data.json"))
        {'key': 'value', 'number': 42}
        ```
    """

    with open(path, "r", encoding="UTF-8") as file:
        return load(file)


def save_json_file(dictionary: dict[Any, Any], path: Path) -> None:
    """
    Save a dictionary as JSON data to a file.

    Args:
        dictionary (dict[Any, Any]): The dictionary to be saved as JSON.
        path (Path): The path to the JSON file.

    Returns:
        None

    Example:
        ```
        >>> save_json_file({'key': 'value', 'number': 42}, Path("data.json"))
        ```
    """

    with open(path, "w") as file:
        dump(dictionary, file, indent=4)
