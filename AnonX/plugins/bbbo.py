
import time
import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus

iddof = []
@app.on_message(
    command(["داخستنی وتە"])
    & filters.group
)
async def lllock(client, message):
    dev = (OWNER_ID)
    haya = (833360381)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "ئەدمین"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "سەرۆك"
    elif message.from_user.id in haya:
         rotba= "پڕۆگرامساز" 
    elif message.from_user.id in dev:
         rotba = "گەشەپێدەر"
  
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in iddof:
        return await message.reply_text(f"**{message.from_user.mention}\n وتە پێشتر داخراوە♥️❎•**")
      iddof.append(message.chat.id)
      return await message.reply_text(f"**بە سەرکەوتوویی فەرمانی وتە داخرا\n\n لەلایەن {rotba} ←{message.from_user.mention}♥️❎•**")

@app.on_message(
    command(["کردنەوەی وتە"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = (833360381)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "ئەدمین"
    elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "سەرۆك"
    elif message.from_user.id in haya:
         rotba= "پڕۆگرامساز" 
    elif message.from_user.id in dev:
         rotba = "گەشەپێدەر"
    
   
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"**{message.from_user.mention}\n وتە پێشتر کراوەتەوە♥️✅•**")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**بە سەرکەوتوویی فەرمانی وتە کرایەوە\n\n لەلایەن {rotba} ←{message.from_user.mention}♥️✅•**")
 



@app.on_message(
    command(["سلاو", "slaw", "."])
    
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = [


 "**|| @MGIMT - ♥️ هەمیشە خودات لە بیربێت ||**",
 "**||@IQQUR - ♥️ اللهم صَلِّ عَلَى سیدنا مُحَمَّدٍ، وَعَلَى آلِ سیدنا مُحَمَّدٍ ||**",
 "**|| @xv7amo - 🖤👾 هەمیشە بەروو پێشەوە بڕۆ تا دەگەیت بە ئامانجت ||**",

]

    ik = random.choice(i)
    await message.reply_text(f"❤️\n \n: {ik}")
