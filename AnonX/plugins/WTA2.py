import asyncio

import random
from AnonX import app
from pyrogram.types import Message
from strings.filters import command
from pyrogram import filters, Client


txt = [

    "**|| @MGIMT - ♥️ هەمیشە خودات لە بیربێت ||**",

    "**||@IQQUR - ♥️ اللهم صَلِّ عَلَى سیدنا مُحَمَّدٍ، وَعَلَى آلِ سیدنا مُحَمَّدٍ ||**",

    "**|| @xv7amo - 🖤👾 هەمیشە بەروو پێشەوە بڕۆ تا دەگەیت بە ئامانجت ||**",

]


@app.on_message(command(["سڵاو" ,"سلام", ".", "!"]))
async def cutt(client: Client, message: Message):
    a = random.choice(txt)

    await message.reply(

        f"{a}")
