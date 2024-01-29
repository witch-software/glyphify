# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Any

from random import choices


def choice_random_with_weights(
    values: list[dict[str, Any]], *, weight_key: str = "weight"
):
    weights = [item[weight_key] for item in values]
    return choices(values, weights=weights)[0]


def get_random_emoji_for_title(
    values: list[dict[str, str]],
    *,
    value_key: str = "value",
    weight_key: str = "weight",
) -> str:
    return choice_random_with_weights(values, weight_key=weight_key)[value_key]


def get_random_discord_rpc_image():
    # TODO
    raise NotImplementedError


def get_random_discord_rpc_details():
    # TODO
    raise NotImplementedError


def get_random_index_page_background():
    # TODO
    raise NotImplementedError
