# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from glyphify.classes.application import GlyphifyApplication

import sys
import argparse


def get_run_arguments() -> argparse.Namespace:
    """Get application startup arguments"""

    argument_parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog="glyphify",
        description="Create ASCII art and stylized UTF-8 text effortlessly!",
    )

    argument_parser.add_argument(
        "--windowless",
        action="store_true",
        help="run in windowless mode",
        default=False,
    )
    argument_parser.add_argument(
        "--debug",
        action="store_true",
        help="run application in debug mode",
        default=False,
    )

    return argument_parser.parse_args()


def run_application() -> None:
    arguments = get_run_arguments()

    # Setup application
    application: GlyphifyApplication = GlyphifyApplication(sys.argv, arguments)

    # Execute application
    application.run()


if __name__ == "__main__":
    run_application()
