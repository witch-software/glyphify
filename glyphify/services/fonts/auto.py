# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Optional

from glyphify.services.fonts.base import BaseFontProcessor
from glyphify.services.fonts.map import FontMap


IS_USABLE_FONT: bool = False


class AutoFontProcessor(BaseFontProcessor):
    NAME: str = "auto"
    MAP: FontMap

    def __init__(
        self, input_text: str, NAME: str, MAP: FontMap, *args, **kwargs
    ) -> None:
        self.NAME: str = NAME
        self.MAP: FontMap = MAP

        super(AutoFontProcessor, self).__init__(input_text, *args, **kwargs)

    def _process(self, text: Optional[str] = None, *args, **kwargs) -> str:
        if text:
            self.input_text = text

        result: str = ""

        for char in self.input_text:
            if char in self.MAP["input"]:
                char = self.MAP["output"][self.MAP["input"].index(char)]
            result += char

        return result
