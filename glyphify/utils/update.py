# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

import urllib.request
import json


def get_latest_version(
    owner: str = "witch-software", repo: str = "glyphify"
) -> str | None:
    """
    Get the latest version tag of a GitHub repository.

    Args:
        owner (str): The owner or organization name of the GitHub repository.
            Defaults to "witch-software".
        repo (str): The name of the GitHub repository. Defaults to "glyphify".

    Returns:
        str | None: The latest version tag of the repository, or None if the request fails or the tag is not available.

    Examples:
        Example 1:
        ```
        >>> get_latest_version()
        'v1.2.3'
        ```

        Example 2:
        ```
        >>> get_latest_version(owner="custom-owner", repo="custom-repo")
        'v2.0.1'
        ```
    """

    url: str = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

    with urllib.request.urlopen(url) as response:
        data = response.read()
        encoding = response.info().get_content_charset("utf-8")
        json_data = json.loads(data.decode(encoding))

    return json_data["tag_name"] or None
