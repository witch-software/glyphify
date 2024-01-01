# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from pathlib import Path
from datetime import datetime


def generate_log_path(
    directory: Path, *, timestamp_format: str = "%Y%m%d_%H%M%S"
) -> Path:
    """
    Generate a log file path within the specified directory with a timestamp.

    Args:
        directory (Path): The base directory where the log file will be stored.
        timestamp_format (str, optional): The format for the timestamp in the log file name.
            Defaults to "%Y%m%d_%H%M%S".

    Returns:
        Path: The generated log file path, including the timestamp.

    Example:
        ```
        >>> generate_log_path_with_time(Path("/path/to/logs"))
        PosixPath('/path/to/logs/log_20220101_120000.log')
        ```
    """

    path: Path = (
        Path(directory)
        / "logs"
        / f"log_{datetime.now().strftime(timestamp_format)}.log"
    )
    return path
