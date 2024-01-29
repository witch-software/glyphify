# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Optional
from abc import ABC, abstractmethod

from glyphify.services.fonts.map import FontMap


IS_USABLE_FONT: bool = False


class BaseFontProcessor(ABC):
    """
    Abstract Base Class for font processors.

    This class defines the interface for font processing and provides a common structure
    for classes implementing specific font processing logic.

    Attributes:
    - NAME (str): The name of the font processor.
    - MAP (dict[str, str | list[str]]): Mapping for font-related information.
    - input_text (str): The input text to be processed.

    Methods:
    - __init__(self, input_text: str, *args, **kwargs) -> None: Constructor to initialize the input_text attribute.
    - process(cls, text: str, *args, **kwargs) -> str: Class method to initiate font processing on a given text.
    - _process(self, text: Optional[str] = None, *args, **kwargs) -> str: Abstract method to be implemented by subclasses
      for the actual font processing logic.
    """

    NAME: str = "base"
    MAP: FontMap

    input_text: str

    def __init__(self, input_text: str, *args, **kwargs) -> None:
        """
        Constructor for the BaseFontProcessor class.

        Parameters:
        - input_text (str): The input text to be processed.
        """

        self.input_text: str = input_text

    @classmethod
    @abstractmethod
    def process(cls, text: str, *args, **kwargs) -> str:
        """
        Class method to initiate font processing on a given text.

        Parameters:
        - text (str): The text to be processed.

        Returns:
        - str: The processed text.
        """

        return cls(text)._process(*args, **kwargs)

    @abstractmethod
    def _process(self, text: Optional[str] = None, *args, **kwargs) -> str:
        """
        Abstract method to be implemented by subclasses for the actual font processing logic.

        Parameters:
        - text (Optional[str]): The text to be processed. Default is None.

        Returns:
        - str: The processed text.
        """

        raise NotImplementedError
