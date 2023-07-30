import asyncio
import pyrogram
import random
import datetime
from AnonX import app
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,

                            InlineKeyboardMarkup, Message)


@app.on_message(filters.regex(r'تەمەنم',))
async def calculate_age(client: Client, message: Message):
    try:
        birth_date = datetime.datetime.strptime(message.text.split(" ")[2],
                                                "%d-%m-%Y") 
    except:
        await message.reply_text(f"•⎆┊**ئەزیزم {message.from_user.mention} ببورە تۆ فەرمانی هەڵەت نوسیووە، ئاوا بینووسە ( تەمەنم 1-1-2000 ) **")
        return

    alyawm = datetime.datetime.today()
    age = alyawm.year - birth_date.year - ((alyawm.month, alyawm.day) < (birth_date.month, birth_date.day))
    months = (alyawm.year - birth_date.year) * 12 + alyawm.month - birth_date.month
    days = (alyawm - birth_date).days
    next_birthday = datetime.datetime(alyawm.year, birth_date.month, birth_date.day)
    if alyawm > next_birthday:
        next_birthday = datetime.datetime(alyawm.year + 1, birth_date.month, birth_date.day)
    remaining_days = (next_birthday - alyawm).days

    await message.reply_text(
        f"•⎆┊**پیرۆزە {message.from_user.mention} • تەمەنت → {age} ساڵ**\n\n** • تەمەنت بە مانگ → {months} مانگ **\n\n** • تەمەنت بە ڕۆژ → {days} ڕۆژ**\n\n** • ڕۆژی لەدایکبوونت دوای → {remaining_days} ڕۆژ **\n\n** بانگمان بکە کیان😂♥•**")
