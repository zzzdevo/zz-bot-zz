from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_8"],
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    return buttons


# noinspection PyTypeChecker
def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"], url=f"https://t.me/MGIMT"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"], url=f"https://t.me/IQSUPP"
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_7"], user_id=OWNER
            )

        ],
        [
            InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG"
            )
        ],
    ]
    return buttons
