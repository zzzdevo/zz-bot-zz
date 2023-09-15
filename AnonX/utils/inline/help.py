from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonX import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text="⟲ گـەڕانـەوە ⟳",
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ئەدمین",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="ڕێپێدان",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="بلۆكکردن",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="فۆروارد",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="زیادە",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="لیست",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ئامار",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="پەخشکردن",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="گەشەپێدەر",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="چالاکی",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="بۆت",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="باندی گشتی",
                    callback_data="help_callback hb12",
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
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="یارمەتی",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
