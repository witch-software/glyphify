# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

import argparse


class GlyphifyArguments:

    APPLICATION_NAME: str = "glyphify"
    APPLICATION_DESCRIPTION: str = "Create ASCII art and stylized UTF-8 text effortlessly!"

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog=APPLICATION_NAME, description=APPLICATION_DESCRIPTION
    )

    def __init__(self) -> None:
        self.initialize_arguments()

    def initialize_arguments(self) -> None:

        self.parser.add_argument(
            "--windowless",
            action="store_true",
            help="run in windowless mode",
            default=False,
        )

        self.parser.add_argument(
            "--debug",
            action="store_true",
            help="run application in debug mode",
            default=False,
        )

    @property
    def arguments(self) -> argparse.Namespace:
        """ Get application startup arguments """
        return self.parser.parse_args()
