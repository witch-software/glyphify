# Code by @selfkilla666
# https://github.com/witch-software/glyphify
# MIT License

from __future__ import annotations

from typing import Any, AnyStr, Optional
from pathlib import Path

from random import choices


def choice_random_with_weights(
    values: list[dict[AnyStr, Any]], *, weight_key: str = "weight"
):
    weights = [item[weight_key] for item in values]
    return choices(values, weights=weights)[0]


def get_random_emoji_for_title(
    values: Optional[list[dict]],
    *,
    value_key: str = "value",
    weight_key: str = "weight",
) -> str:
    return choice_random_with_weights(values, weight_key=weight_key)[value_key]
