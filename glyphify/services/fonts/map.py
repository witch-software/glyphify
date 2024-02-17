# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import TypedDict


IS_USABLE_FONT: bool = False


class FontMap(TypedDict):
    input: str | list[str]
    output: str | list[str]
