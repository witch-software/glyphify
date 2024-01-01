# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import TYPE_CHECKING

import platform

if TYPE_CHECKING:
    from glyphify.classes.application import GlyphifyApplication


def log_debug_info(application: GlyphifyApplication) -> None:
    """
    Log debug information about the Glyphify application.

    This function logs various pieces of debug information if the application is running in debug mode.

    Args:
        application (GlyphifyApplication): The Glyphify application instance.

    Returns:
        None

    Example:
        ```
        >>> log_debug_info(my_glyphify_application_instance)
        # Logs debug information based on the application's state and configuration.
        ```
    """

    if application.debug_mode:
        application.logger.debug("Application running in debug mode.")

    application.logger.debug(f"Application version: {application.APPLICATION_VERSION}")

    # Debug data about user system
    application.logger.debug(
        f"Platform: {platform.system()} {platform.release()} ({platform.architecture()[0]})"
    )

    if len(application.argv) > 1:
        application.logger.debug(
            f"Running application with arguments: {' '.join(application.argv[1:])}"
        )
