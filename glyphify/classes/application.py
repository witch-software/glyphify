# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Optional, TYPE_CHECKING
from pathlib import Path

from glyphify.classes.settings import TomlSettings
from glyphify.classes.discord_rpc import GlyphifyDiscordRPC
from glyphify.utils.thread import StoppableThread
from glyphify.utils.path import get_user_local_directory
from glyphify.utils.logs import generate_log_path
from glyphify.utils.debug import log_debug_info
from glyphify.utils.json import load_json_file
from glyphify.utils.random import get_random_emoji_for_title

import loguru
import eel

if TYPE_CHECKING:
    import argparse


# Paths
LOG_FILE_PATH: str = str(generate_log_path(get_user_local_directory()))
SETTINGS_PATH: str = str(Path(get_user_local_directory() / "settings.toml"))
EEL_DIRECTORY: Path = Path("web")
EMOJIS_FOR_TITLE_JSON_PATH: Path = Path("emoticons.json")


class GlyphifyApplication:
    """
    Main class representing the Glyphify application.

    Attributes:
        APPLICATION_NAME (str): The name of the Glyphify application.
        APPLICATION_VERSION (str): The version of the Glyphify application.
        APPLICATION_ORG_NAME (str): The organization name associated with Glyphify.
        APPLICATION_ORG_DOMAIN (str): The organization domain associated with Glyphify.

        logger (loguru.Logger): The logger instance for Glyphify.
        argv (list[str]): Command-line arguments for Glyphify.
        arguments (argparse.Namespace): Parsed command-line arguments.
        settings (TomlSettings): The settings instance for Glyphify.
        debug_mode (bool): Flag indicating whether Glyphify is running in debug mode.
        windowless (bool): Flag indicating whether Glyphify is running in windowless mode.

        discord_rpc (GlyphifyDiscordRPC): Discord RPC instance for Glyphify activity.

        discord_rpc_thread (StoppableThread): Thread for running the Discord RPC.
        eel_window_thread (StoppableThread): Thread for managing the Eel window.

    Methods:
        __init__(argv: list[str], arguments: argparse.Namespace, logger: Optional[loguru.Logger] = None, settings: Optional[TomlSettings] = None) -> None:
            Initialize the GlyphifyApplication instance.

        initialize_logger() -> None:
            Initialize the logger for Glyphify.

        initialize_settings() -> None:
            Initialize the settings for Glyphify.

        setup_eel_window() -> None:
            Set up the Eel window for Glyphify.

        run(argv: Optional[list[str]] = None) -> None:
            Run the Glyphify application.

        close() -> None:
            Close the Glyphify application.

        on_window_close() -> None:
            Handle the event when the application window is closed.

    """

    # TODO: Add application metadata
    # TODO: Add documentation for this code
    # TODO: Add CLI mode

    # Application metadata
    APPLICATION_NAME: str = "Glyphify"
    APPLICATION_VERSION: str = "1.0.0"
    APPLICATION_ORG_NAME: str = "Witch Software"
    APPLICATION_ORG_DOMAIN: str = "witch-software.com"

    APPLICATION_TITLE_FORMAT: str = "{name} {emoji}"
    APPLICATION_TITLE: str

    # Variables
    logger: loguru.Logger
    argv: list[str]
    arguments: argparse.Namespace
    settings: TomlSettings
    debug_mode: bool = False
    windowless: bool = False

    # Discord RPC for activity
    discord_rpc: GlyphifyDiscordRPC = GlyphifyDiscordRPC()

    # Threads
    discord_rpc_thread: StoppableThread
    eel_window_thread: StoppableThread

    def __init__(
        self,
        argv: list[str],
        arguments: argparse.Namespace,
        *,
        logger: Optional[loguru.Logger] = None,
        settings: Optional[TomlSettings] = None,
    ) -> None:
        """
        Initialize the GlyphifyApplication instance.

        Parameters:
            argv (list[str]): Command-line arguments for Glyphify.
            arguments (argparse.Namespace): Parsed command-line arguments.
            logger (Optional[loguru.Logger]): Optional logger instance for Glyphify.
            settings (Optional[TomlSettings]): Optional settings instance for Glyphify.
        """

        # Initialize logger
        if logger:
            self.logger = logger
        else:
            self.initialize_logger()

        # Store variables
        self.argv = argv
        self.arguments = arguments
        self.debug_mode = self.arguments.debug or False
        self.windowless = self.arguments.windowless or False

        # Log debug info about application
        log_debug_info(self)

        self.logger.info("Start application initialization...")

        # Initialize settings
        if settings:
            self.settings = settings
        else:
            self.initialize_settings()

        # Initialize eel and Discord RPC activity
        eel.init(str(EEL_DIRECTORY))
        self.discord_rpc.setup()

        self.APPLICATION_TITLE = self.application_title_with_emoji

    def initialize_logger(self):
        """
        Initialize the logger for Glyphify.
        """

        self.logger: loguru.Logger = loguru.logger
        self.logger.add(
            LOG_FILE_PATH,
            format="{time:HH:mm:ss.SS} ({file}) [{level}] {message}",
            colorize=True,
            backtrace=True,
        )

        self.logger.success("Logger initialized!")
        self.logger.debug(f'Logs stored into "{LOG_FILE_PATH}"')

    def initialize_settings(self):
        """
        Initialize the settings for Glyphify.
        """

        self.logger.info("Initialize application settings...")

        self.settings = TomlSettings(SETTINGS_PATH, logger=self.logger)
        self.settings.load_settings()

        self.logger.success("Settings initialized!")

    def setup_eel_window(self) -> None:
        """
        Set up the Eel window for Glyphify.
        """

        @eel.expose
        def onWindowClosed():
            self.on_window_close()
            return

        eel.start("index.html", mode="chrome", port=9876, allowed_extensions=['.js', '.html', '.css', '.png', '.jpg', '.jpeg', '.gif'])

    def run(self, *, argv: Optional[list[str]] = None) -> None:
        """
        Run the Glyphify application.

        Parameters:
            argv (Optional[list[str]]): Optional command-line arguments.
        """

        self.logger.info("Application start running...")

        self.discord_rpc_thread = StoppableThread(target=self.discord_rpc.run)
        self.discord_rpc_thread.start()

        self.logger.info("Discord RPC activity is set up!")

        self.eel_window_thread = StoppableThread(target=self.setup_eel_window)
        self.eel_window_thread.start()

        eel.setWindowTitle(self.APPLICATION_TITLE)  # type: ignore[attr-defined]

        self.logger.success("Application starts!")

        self.eel_window_thread.join()

    def close(self) -> None:
        """
        Close the Glyphify application.
        """

        self.logger.info("Terminate the application...")

        self.discord_rpc_thread.stop()
        self.eel_window_thread.stop()

        self.logger.info("All threads are stopped.")

        # FIXME: Make clearly exit

    def on_window_close(self) -> None:
        """
        Handle the event when the application window is closed.
        """

        self.logger.info("Window is closed! Stopping the application...")

        self.settings.save_settings()

        self.close()

    @property
    def application_title_with_emoji(self) -> str:
        # TODO: make this code better maybe? ¯\_(ツ)_/¯

        emojis: str = load_json_file(EMOJIS_FOR_TITLE_JSON_PATH)["titles"]
        emoji: str = get_random_emoji_for_title(emojis)
        return self.APPLICATION_TITLE_FORMAT.format(
            name=self.APPLICATION_NAME, emoji=emoji
        )
