# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from pathlib import Path

from glyphify.services.fonts.auto import AutoFontProcessor
from glyphify.services.fonts.map import FontMap
from glyphify.utils.json import load_json_file


IS_USABLE_FONT: bool = False


class JsonBasedFontProcessor(AutoFontProcessor):
    NAME: str = "json-based"
    MAP: FontMap

    def __init__(
        self, input_text: str, NAME: str, json_path: Path, *args, **kwargs
    ) -> None:
        json: dict = load_json_file(json_path)

        self.NAME: str = json.get("name") or NAME
        self.MAP: FontMap = FontMap(input=json.get("input"), output=json.get("output"))  # type: ignore[typeddict-item]

        super(JsonBasedFontProcessor, self).__init__(input_text, *args, **kwargs)
