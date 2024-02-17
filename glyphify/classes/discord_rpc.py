# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from discordrpc import RPC as DiscordRPCActivity  # type: ignore[import-untyped]
from discordrpc import button
from discordrpc.exceptions import Error

if TYPE_CHECKING:
    from loguru import Logger


class GlyphifyDiscordRPC:
    """
    Class for managing Discord Rich Presence integration for Glyphify.

    Attributes:
        DISCORD_RPC_APPLICATION_ID (int): Default Discord RPC application ID for Glyphify.
        rpc (DiscordRPCActivity): Discord RPC activity instance.
        buttons (list[dict[str, str]]): List of buttons for the Discord Rich Presence.

    Methods:
        __init__(application_id: Optional[int] = None) -> None:
            Initialize the GlyphifyDiscordRPC instance.

        create_buttons() -> list[dict[str, str]]:
            Create and return a list of buttons for the Discord Rich Presence.

        setup() -> None:
            Set up the Discord Rich Presence with default or user-specified buttons.

        set_activity(**kwargs) -> None:
            Set the Discord Rich Presence activity with the specified parameters.

        run() -> None:
            Run the Discord Rich Presence.

    """

    logger: Optional[Logger] = None

    DISCORD_RPC_APPLICATION_ID: int = 1191380153335566426

    rpc: DiscordRPCActivity
    buttons: list[dict[str, str]]

    def __init__(self, *, application_id: Optional[int] = None, logger: Optional[Logger] = None) -> None:
        """
        Initialize the GlyphifyDiscordRPC instance.

        Parameters:
            application_id (Optional[int]): Optional Discord RPC application ID.
                Defaults to None.

        Returns:
            None
        """

        if application_id is not None:
            self.DISCORD_RPC_APPLICATION_ID = application_id

        if logger is not None:
            self.logger = logger

        try:
            self.rpc = DiscordRPCActivity.set_id(self.DISCORD_RPC_APPLICATION_ID)
        except Error:
            if self.logger is not None:
                self.logger.warning("Failed to connect to Discord RPC")

    def create_buttons(self) -> list[dict[str, str]]:
        """
        Create and return a list of buttons for the Discord Rich Presence.

        Returns:
            list[dict[str, str]]: Formatted payload of buttons for RPC
        """

        buttons: list[dict[str, str]]

        buttons = button(
            button_one_label="GitHub Repository",
            button_one_url="https://github.com/witch-software/glyphify",
            button_two_label="Download too!",
            button_two_url="https://witchsoftware.itch.io/glyphify",
        )

        return buttons

    def setup(self) -> None:
        """
        Set up the Discord Rich Presence.
        """

        self.buttons = self.create_buttons()

        try:
            self.rpc.set_activity(
                state="idk",
                details="Make it in future...",
                buttons=self.buttons,
                timestamp=self.rpc.timestamp,
            )

            if self.logger is not None:
                self.logger.info("Discord RPC activity is set up!")
        except:
            if self.logger is not None:
                self.logger.error("Unable to initialize Discord RPC")

    def set_activity(self, **kwargs) -> None:
        """
        Set the Discord Rich Presence activity with the specified parameters.

        Parameters:
            **kwargs: Keyword arguments for setting the activity.
        """

        self.rpc.set_activity(**kwargs)

    def run(self) -> None:
        """
        Run the Discord Rich Presence.
        """

        try:
            self.rpc.run()
        except AttributeError:
            if self.logger is not None:
                self.logger.warning("Discord RPC cannot be started")
