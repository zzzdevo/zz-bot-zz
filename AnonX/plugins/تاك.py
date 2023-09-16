import asyncio
import os
from config import OWNER_ID
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from asyncio import gather
from pyrogram.errors import FloodWait
from pyrogram.enums import ParseMode, ChatMemberStatus




@app.on_message(command(["سەرۆکی گرووپ"]) & filters.group)
async def gak_owne(client: Client, message: Message):
      if len(message.command) >= 2:
         return 
      else:
            chat_id = message.chat.id
          
            async for member in client.get_chat_members(chat_id):
               if member.status == ChatMemberStatus.OWNER:
                 id = member.user.id
                 key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                 m = await client.get_chat(id)
                 if m.photo:
                       photo = await app.download_media(m.photo.big_file_id)
                       return await message.reply_photo(photo, caption=f"**✧ ¦زانیاری خاوەن گرووپ \n\n ✧ ¦ ناو ← {m.first_name} \n ✧ ¦ یوزەر ← @{m.username} \n ✧ ¦ بایۆ ← {m.bio}**",reply_markup=key)
                 else:
                    return await message.reply("•" + member.user.mention)
                       
                    
                    
@app.on_message(command(["گرووپ", "group"]) & filters.group)
async def ginnj(client: Client, message: Message):
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""**🦩 ¦ ꪀᥲ️ꪔᥱ » {chat_name}\n🐉 ¦ Ꭵժ ᘜᖇ᥆υρ »  -{chat_idd}\n🐊 ¦ ᥣᎥꪀk » {chat_username}**""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        chat_name, url=f"https://t.me/{message.chat.username}")
                ],
            ]
        ),
    )
    

@app.on_message(command(["گۆڕین","گۆڕینی ستیکەر"]))
async def sticker_image(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("**ڕپلەی ستیکەر بکە**")
    if not reply.sticker:
        return await message.reply("**ڕپلەی ستیکەر بکە**")
    m = await message.reply("**کەمێك چاوەڕێبە . .**")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)
      
   
@app.on_message(command(["ناوم","ناو"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""•⎆┊** ناوت 🔥♥**»»  {message.from_user.mention()}""") 

        

array = []
@app.on_message(command(["@all", "بانگکردن","تاگ"]) & ~filters.private)
async def nummmm(client: app, message):
  if message.chat.id in array:
     return await message.reply_text(f"•⎆┊**تاگکردن دەستی پێکرد♥**\n\n** لەلایەن ← ✧ ¦{message.from_user.mention}•**")
  dev = (OWNER_ID)
  haya = (1818734394,833360381)
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if message.from_user.id in haya:
         rotba= "پڕۆگرامساز" 
  elif message.from_user.id in dev:
         rotba = "گەشەپێدەر" 
  elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "سەرۆك"
  elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "ئەدمین"     
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in  [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply(f"•⎆┊**ببورە تۆ ئەدمین نیت🗿 {message.from_user.mention}•**")
    return
  await message.reply_text(f"•⎆┊**تاگکردن دەستی پێکرد♥🪐** \n\n** لەلایەن ← {rotba}✧ ¦{message.from_user.mention} **\n\n**بۆ کۆتایی هێنانی تاگ بنووسە وەستانی تاگ یان /cancel ♥🧩•**")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاگ","").replace("وەرن","")
  except:
    pass
  array.append(message.chat.id)
  async for x in client.get_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f" {x.user.mention} ،"
       if i == 5:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(2)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@app.on_message(command(["وەستانی تاگ", "/cancel","ڕاگرتنی تاگ"]))
async def stop(client, message):
  dev = (OWNER_ID)
  haya = (833360381,1818734394)
  get = await client.get_chat_member(message.chat.id, message.from_user.id)
  if get.status in [ChatMemberStatus.ADMINISTRATOR]:
         rotba = "ئەدمین"
  elif get.status in [ChatMemberStatus.OWNER]:
         rotba = "سەرۆك"
  elif message.from_user.id in haya:
         rotba= "پڕۆگرامساز" 
  elif message.from_user.id in dev:
         rotba = "گەشەپێدەر"           
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in  [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply(f"•⎆┊**ببورە تۆ ئەدمین نیت🗿 {message.from_user.mention}•**")
    return
  if message.chat.id not in array:
     await message.reply(f"•⎆┊**تاگکردن وەستاوە ئەزیزم♥ {message.from_user.mention}•**")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply(f"•⎆┊**تاگکردن وەستێنرا **\n\n **لەلایەن ← {rotba}✧ ¦{message.from_user.mention}•**")
    return
