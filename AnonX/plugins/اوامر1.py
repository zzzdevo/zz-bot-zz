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
        await message.reply_text(f"""**[ᯓ فەرمانی بۆتی زیرەکی گۆرانی🧑🏻‍💻🖤](t.me/MGIMT)**\n**بەخێربێی ئەزیزم{message.from_user.mention}**في قسم اوامر الفتح والقفل في بوت {MUSIC_BOT_NAME} ميوزك\n
𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼
**قفل / تعطيل + الامر**

ايدي / صورتي

صور / زوجني

نداء / زخرفه
⩹━⊶⊷⌯𖢿 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼 𖢿⌯⊶⊷⋗
**فتح / تفعيل + الامر**

ايدي / صورتي

صور / زوجني

نداء / زخرفه
لتنصيب بوت مشابه تواصل معي فالخاص @bp_bp
**""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼⚡", url=f"https://t.me/HL_BG"),                        
                 ],[
                InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
               ],
          ]
        ),
    )
