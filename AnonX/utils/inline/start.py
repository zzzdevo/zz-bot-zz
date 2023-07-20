from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from config import SUPPORT_CHANNEL



def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ زیادم بکە بۆ گرووپەکەت ›",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❈ فەرمانەکان ❈",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❈ یارمەتی ❈",
                callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ زیادم بکە بۆ گرووپەکەت ›",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❈ فەرمانەکان ❈", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="❈ کڕینی بۆت ❈", url=f"https://t.me/IQ7amo"
            ),
            InlineKeyboardButton(
                text="✪ خاوەنی بۆت ✪", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✬ کەناڵی بۆت ✬", url=f"https://t.me/MGIMT"
            )
        ],
     ]
    return buttons
