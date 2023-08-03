import asyncio

import os
from AnonX import app
from config import SUPPORT_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from strings.filters import command


@app.on_message(
    command(["کەناڵ"])

)
async def yas(client, message, user):
    user = await client.get_chat(SUPPORT_CHANNEL)
    name = user.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,
                              caption=f"**[ᯓ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - کەناڵی بۆت 🧑🏻‍💻](t.me/MGIMT)**\n**جۆینی کەناڵی بۆت بکە بۆ بینینی بابەتی جیاوازتر♥**\n\n** بەستەری کەناڵ : https://t.me/{usr.username}**",
                              reply_markup=InlineKeyboardMarkup(
                                  [
                                      [
                                          InlineKeyboardButton(
                                              name, url=f"https://t.me/{usr.username}")
                                      ],
                                  ]
                              ),
                          )
