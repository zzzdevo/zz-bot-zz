import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
import random
@app.on_message(
    command(["فەرمان"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bd98a0645138a96e63b23.jpg",
        caption=f"""**[ᯓ 𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - فەرمانی بۆتی گۆرانی🧑🏻‍💻🖤](t.me/MGIMT)**\n••┉┉┉┉┉┉••🝢••┉┉┉┉┉┉••\n
**⎙ بۆ پەخشکردن :(gorani,play,پلەی) + ناوی گۆرانی **
**⎙ بۆ وەستاندنی کاتی پەخشکردن :(وەستانی کاتی,وسبە,pause) **
**⎙ بۆ دەستپێکردنەوەی پەخشکردن :(دەستپێکردنەوە,د,resume) **      
**⎙ بۆ کۆتایی هێنان بە پەخشکردن :(end,stop,ڕاگرتن,وەستان) **  
**⎙ بۆ تێپەڕاندنی گۆرانی بۆ گۆرانی دواتر :(skip,تێپەڕاندن,دواتر)**
**⎙ بۆ دەرکردنی یاریدەدەر :(left,جێهێشتن,پەیوەندیەکان جێبهێڵە)**
**⎙ فەرمانە کوردیەکانی بۆت :(فەرمان)**
**⎙ بۆ داگرتنی گۆرانی :(گۆرانی,ڤیدیۆ,میوزیک,vsong)**
**⎙ بۆ گەڕان بە دوای هەر شتێك کەتۆ بتەوێت :(گەڕان) **
\n••┉┉┉┉┉••🝢••┉┉┉┉┉••""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         "𐇮 ﮼ﺣ‌ّــەمــە 🇧🇷 𐇮", url=f"https://t.me/IQ7amo"),
                  ],[
                        InlineKeyboardButton(
                         "𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"t.me/MGIMT"),
                ],

            ]

        ),

    )

@app.on_message(command([f"گۆرانی","گۆرانیەکان","go"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,31)
    url = f"https://t.me/IQMUC/{rl}"
    await client.send_voice(message.chat.id,url,caption="**[ᯓ 𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - گۆرانی🧑🏻‍💻🖤](t.me/MGIMT)**\n✦▁ ▂ ▉ ▄ ▅ ▆ ▇▅ ▆ ▇ █ ▉ ▂ ▁\n\n** @IQMUC - کەناڵی گۆرانی♥•**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["وێنە","وێنەکان"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="**[ᯓ 𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 وێنەکان](t.me/MGIMT)**\n••┉┉┉┉┉••🝢••┉┉┉┉┉••\n**¦ وێنەکە دیاریکرا ♥•**",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        
@app.on_message(
    command(["ق"])
)
async def ihd(client: Client, message: Message):
    rl = random.randint(3, 104)
    url = f"https://t.me/IQQUR/{rl}"
    await client.send_voice(message.chat.id, url, caption="¦** قورئانی پیرۆز➧♥️**",
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
