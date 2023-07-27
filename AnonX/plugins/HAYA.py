import asyncio

import os
import time
import requests
from config import USER_OWNER, OWNER_ID, SUPPORT_CHANNEL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["/source", "سەرچاوە", "سۆرس", "گەشەپێدەران"])
)
async def huhh(message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/665afaab6f33082506442.jpg",
        caption=f"""**[ᯓ 𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 گەشەپێدەران](t.me/MGIMT)**\n••┉┉┉┉┉••🝢••┉┉┉┉┉••\n**بەخێربێی ئەزیزم{message.from_user.mention} بۆ بەشی گەشەپێدەرانی بۆت🕷️•**\n**بۆ هەبوونی هەرکێشە و پرسیارێك پەیوەندی بە گەشەپێدەر بکە لەڕێگای دووگمەکانی خوارەوە♥•**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ محمد ✬", url=f"https://t.me/IQ7amo"),
                ], [

                InlineKeyboardButton(
                    "𐇮 ﮼ﺣ‌ّــەمــە 🇧🇷 𐇮", url=f"https://t.me/VTVIT"),
            ], [

                InlineKeyboardButton(
                    "★𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌🖤", url=f"https://t.me/MGIMT"),

            ], [

                InlineKeyboardButton(
                    "『𓏺کەناڵی سەرەکی』", url=f"https://t.me/xv7amo"),
            ],

            ]

        ),

    )


@app.on_message(
    command(["حەمە", "@VTVIT", "گەشەپێدەری 2"])

)
async def yas(client, message):
    usr = await client.get_chat("VTVIT")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,
                              caption=f"**[ᯓ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - سەرچاوەی زیرەك 🧑🏻‍💻](t.me/MGIMT)**\n**زانیاری گەشەپێدەری دووەمی بۆت**\n↜︙Dev 𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙Dev 𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙Dev 𝐈𝐃 ↬ :{usr.id}\n↜︙Dev 𝐁𝐈𝐎 ↬: {usr.bio}",
                              reply_markup=InlineKeyboardMarkup(
                                  [
                                      [
                                          InlineKeyboardButton(
                                              name, url=f"https://t.me/{usr.username}")
                                      ],
                                  ]
                              ),
                              )


@app.on_message(
    command(["سەرۆک", "@IQ7amo"])

)
async def yas(client, message):
    usr = await client.get_chat("IQ7amo")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,
                              caption=f"**[ᯓ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - سەرچاوەی زیرەك 🧑🏻‍💻](t.me/MGIMT)**\n**زانیاری خاوەنی بۆت**\n↜︙Dev 𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙Dev 𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙Dev 𝐈𝐃 ↬ :{usr.id}\n↜︙Dev 𝐁𝐈𝐎 ↬: {usr.bio} ",
                              reply_markup=InlineKeyboardMarkup(
                                  [
                                      [
                                          InlineKeyboardButton(
                                              name, url=f"https://t.me/{usr.username}")
                                      ], [
                                      InlineKeyboardButton(
                                          "🝢 پەیوەندی کردن 🝢", url=f"https://t.me/{usr.username}"),
                                  ],
                                  ]
                              ),
                             )


@app.on_message(
    command(["کەناڵی بۆت"])

)
async def yas(client, message):
    usr = await client.get_chat(SUPPORT_CHANNEL)
    name = usr.first_name
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


@app.on_message(
    command(["قورئان"])
)
async def ihd(client: Client, message: Message):
    rl = random.randint(3, 104)
    url = f"https://t.me/IQQUR/{rl}"
    await client.send_voice(message.chat.id, url, caption="¦ قورئانی پیرۆز➧♥️",
                           reply_markup=InlineKeyboardMarkup(
                               [
                                   [
                                       InlineKeyboardButton(
                                           message.from_user.first_name,
                                           url=f"https://t.me/{message.from_user.username}")
                                   ],
                               ]
                           )
                     )

@app.on_message(
   command(["قرأن"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4c0e63af8a410d9a53fa0.jpg",
        caption=f"""**𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس حياه\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩𓏺᭙ɦᎥ᥉ƙᥱᥡ ˹َّّ", url=f"https://t.me/bp_bp"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼⚡", url=f"https://t.me/HL_BG"),
                ],

            ]

        ),

    )
