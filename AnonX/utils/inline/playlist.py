from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="کەسی",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="گشتی", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ داخستن ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="10 باشترین پەخش", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="کەسی", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="گشتی", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="گرووپەکان", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="گەڕانەوە", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="✯ داخستن ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="دەنگ", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="ڤیدیۆ", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="گەڕانەوە", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="✯ داخستن ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="10 باشترین لیستی پەخشکردن", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="کەسی", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="گشتی", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="گرووپەکان", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="گەڕانەوە", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="✯ داخستن ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="گەڕانەوە",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="✯ داخستن ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="سڕینەوە",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="گەڕانەوە",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="✯ داخستن ✯",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✯ داخستن ✯",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
