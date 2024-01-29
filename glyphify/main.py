# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from glyphify.classes.arguments import GlyphifyArguments
from glyphify.classes.application import GlyphifyApplication

import sys


def run_application() -> None:

    arguments: GlyphifyArguments = GlyphifyArguments()

    # Setup application
    application: GlyphifyApplication = GlyphifyApplication(sys.argv, arguments.arguments)

    # Execute application
    application.run()


if __name__ == "__main__":
    run_application()
