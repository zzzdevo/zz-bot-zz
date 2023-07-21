from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="فەرمانی ئەدمین",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="فەرمانی ڕێپێدان",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="لیستی ڕەش",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="فۆڕوارد",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="دەرکردنی گشتی",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="ʟʏʀɪᴄs",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="پینگ",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="پەخشکردن",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="لیستی پەخشکردن",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="چالاکی بۆت",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="دەستپێکردن",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="گەشەپێدەر",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❄ ʜᴇʟᴩ ❄",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
