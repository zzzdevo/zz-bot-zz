import asyncio

import os
import time
import requests
from config import START_IMG_URL,  MUSIC_BOT_NAME
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["ف1"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**[ᯓ فەرمانی داخستن و کردنەوە 🧑🏻‍💻🖤](t.me/MGIMT)**\n**بەخێربێی ئەزیزم{message.from_user.mention}بۆ بەشی داخستن و کردنەوەی فەرمان{MUSIC_BOT_NAME}**\n••┉┉┉┉┉┉••🝢••┉┉┉┉┉┉••\n
⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌

** کردنەوەی + فەرمان 👾✅**

** ئایدی | وێنە **

** وەڵامدانەوە | ستیکەر **

⩹━⊶⊷⌯⧉• 𓏺ᯓ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 •⧉⊶⊷⋗

** داخستنی + فەرمان 👾❎**

** ئایدی | وێنە **

** وەڵامدانەوە | ستیکەر **

**نموونە : کردنەوەی ئایدی یان داخستنی ئایدی♥🧩**

@IQ7amo - 🖤👾باشترین بۆتی گۆرانی و پاراستن و وەڵامدانەوە
**""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 ♥", url=f"https://t.me/MGIMT"),                        
                 ],[
                InlineKeyboardButton(
                        "پڕۆگرامساز⚡", url=f"https://t.me/IQ7amo"),
               ],
          ]
        ),
    )
