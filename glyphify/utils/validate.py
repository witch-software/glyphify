# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Any


def are_keys_present(
    dictionary_to_check: dict[Any, Any], dictionary_pattern: dict[Any, Any]
) -> bool:
    """
    Check if a set of keys and values are present in a given dictionary.

    Args:
        dictionary_to_check (dict[Any, Any]): The dictionary to check for the presence of keys and values.
        dictionary_pattern (dict[Any, Any]): The dictionary specifying the keys and values to check for.

    Returns:
        bool: True if all keys and values in `dictionary_pattern` are present in `dictionary_to_check`,
            False otherwise.

    Examples:
        Example 1:
        ```
        >>> are_keys_present({'name': 'John', 'age': 30}, {'name': 'John'})
        True
        ```

        Example 2:
        ```
        >>> are_keys_present({'name': 'John', 'age': 30}, {'name': 'John', 'city': 'New York'})
        False
        ```
    """

    for key, value in dictionary_pattern.items():
        if key not in dictionary_to_check:
            return False

        if isinstance(value, dict):
            if not isinstance(dictionary_to_check[key], dict) or not are_keys_present(
                dictionary_to_check[key], value
            ):
                return False
        elif value is not None and dictionary_to_check[key] != value:
            return False

    return True


def add_missing_values(
    dictionary_to_check: dict[Any, Any], dictionary_pattern: dict[Any, Any]
) -> dict[Any, Any]:
    """
    Add missing keys and values from `dictionary_pattern` to `dictionary_to_check`.

    Args:
        dictionary_to_check (dict[Any, Any]): The dictionary to which missing keys and values will be added.
        dictionary_pattern (dict[Any, Any]): The dictionary specifying the keys and values to add.

    Returns:
        dict[Any, Any]: The updated dictionary with missing keys and values added.

    Examples:
        Example 1:
        ```
        >>> add_missing_values({'name': 'John', 'age': 30}, {'name': 'John', 'city': 'New York'})
        {'name': 'John', 'age': 30, 'city': 'New York'}
        ```

        Example 2:
        ```
        >>> add_missing_values({'name': 'John'}, {'name': 'John', 'city': 'New York'})
        {'name': 'John', 'city': 'New York'}
        ```
    """

    result = dictionary_to_check.copy()

    for key, value in dictionary_pattern.items():
        if key not in result:
            result[key] = value
        elif isinstance(value, dict) and isinstance(result[key], dict):
            result[key] = add_missing_values(result[key], value)

    return result
