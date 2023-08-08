##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]

import asyncio
from config import OWNER_ID
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode, ChatMemberStatus

#       #             #  #####  #####      ####
#        #  كود الرتبه الوهميه برمجة ##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]         #  #         #            #     #
#          #        #  #####  #            #####    
#           #    #    #          #     ##   #     #
#              #      #####   ######   #     #

iddof = []

@app.on_message(
     command(["داخستنی ئایدی"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
    haya = (833360381,1818734394)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
       rotba= "پڕۆگرامساز"
    elif message.from_user.id in dev:
        rotba = "خاوەنی بۆت"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "سەرۆك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "ئەدمین"
    else:   
        return await message.reply_text(f"** {message.from_user.mention} تۆ ئەدمین نیت لێرە💔•**")    
     
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"**{message.from_user.mention}\n ئایدی پێشتر داخراوە♥️❎•**")
        iddof.append(message.chat.id)
        return await message.reply_text(f"**بە سەرکەوتوویی فەرمانی ئایدی داخسترا\n\n لەلایەن {rotba} ←{message.from_user.mention}♥️❎•**")

@app.on_message(
    command(["کردنەوەی ئایدی"])
    & filters.group
)
async def idljjopen(client, message):
    dev = (OWNER_ID)
    haya = (833360381,1818734394)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
       rotba= "پڕۆگرامساز"
    elif message.from_user.id in dev:
        rotba = "خاوەنی بۆت"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "سەرۆك"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "ئەدمین"
    else:
        return await message.reply_text(f"**{message.from_user.mention} تۆ ئەدمین نیت لێرە💔•**")       
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"**{message.from_user.mention}\nئایدی پێشتر کراوەتەوە♥️✅•**")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**بە سەرکەوتوویی فەرمانی ئایدی کرایەوە\n\n لەلایەن {rotba} ←{message.from_user.mention}♥️✅•**")
 
   



@app.on_message(
    command(["id","ا","ئایدی"])
    & filters.group
)

async def iddd(client, message):# البريميوم الوهمي كتابة ##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
   
    member_count = app.get_chat_members_count(message.chat.id)
    txt = ["زانیاری بەڕێزت♥🙇🏻‍♂️"]
    xtxk = random.choice(txt)
    botdev= (OWNER_ID)
    haya = (833360381,1818734394)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
       rotba= "پڕۆگرامساز"
    elif message.from_user.id in botdev:
        rotba = "خاوەنی بۆت"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "ئەدمین"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "سەرۆك"
    else: 
        rotba= " ئەندام"
    
    if message.from_user.id in haya:
       prim= "پریمیومی بەرز"
    elif message.from_user.id in botdev:
       prim = "پریمیوم"
    else: 
       prim= "ئاسایی"
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""**✧ ¦{xtxk}\n\n✧ ¦ نـاوت ← {message.from_user.mention}\n✧ ¦ یـوزەرت ← @{message.from_user.username}\n✧ ¦ ئـایدی ← `{message.from_user.id}`\n✧ ¦ ڕۆڵـت ← {rotba} \n✧ ¦ جۆری ئەکاونت ← {prim}\n✧ ¦ نامەکانت ← {member_count}\n✧ ¦ بـایـۆ ← {usr.bio}**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )


# noinspection PyRedeclaration
iddof = []
@app.on_message(
    command(["داخستنی وێنە"])
    & filters.group
)
async def lllock(client, message):
    global rotba
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
         rotba = "خاوەنی بۆت"
  
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if message.chat.id in iddof:
        return await message.reply_text(f"** {message.from_user.mention}\n پێشتر داخراوە🎈•**")
      iddof.append(message.chat.id)
      return await message.reply_text(f"**فەرمانی وێنەکەم داخسترا\n\n لەلایەن {rotba} ←{message.from_user.mention}♥️❎•**")
    
@app.on_message(
    command(["کردنەوەی وێنە"])
    & filters.group
)
async def idljjopen(client, message):
    global rotba
    dev = (OWNER_ID)
    haya = (833360381,1818734394)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
       rotba= "پڕۆگرامساز"
    elif message.from_user.id in dev:
        rotba = "خاوەنی بۆت"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "ئەدمین"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "سەرۆك"
    else :
        await message.reply_text(f"**تۆ ئەدمین نیت لێرە💔•**")   
   
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
      if not message.chat.id in iddof:
        return await message.reply_text(f"**{message.from_user.mention} پێشتر کراوەتەوە🎈•**")
      iddof.remove(message.chat.id)
      return await message.reply_text(f"**فەرمانی وێنەکەم کرایەوە\n\n لەلایەن {rotba} ←{message.from_user.mention}♥️✅•**")
 



@app.on_message(
    command(["وێنەکەم"])
    & filters.group
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**ڕێژەی جوانیت \n│ \n└ʙʏ: {ik} %😂❤️**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
@app.on_message(
    command(["ڕۆڵم"])
    & filters.group
)
async def rotba(client, message):
    dev = (OWNER_ID)
    haya = (833360381,1818734394)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in haya:
       rotba= "پڕۆگرامساز"
    elif message.from_user.id in dev:
        rotba = "خاوەنی بۆت"
    elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "ئەدمین"
    elif get.status in [ChatMemberStatus.OWNER]:
        rotba= "سەرۆك"
    else:
         rotba = "ئەندام"
    await message.reply_text(f"**ڕۆڵی تۆیە لەم گرووپە\n\nڕۆڵت ← « {rotba} »♥️**")
       

bio = []

@app.on_message(
    command(["بایۆ"])
    & filters.group
)
async def idjjdd(client, message:Message):
    if message.chat.id in bio:
      return
    usr = await client.get_chat(message.from_user.id)
    await message.reply_text(f"**ئەوە بایۆیی تۆیە\n│ \n└ʙʏ: {usr.bio}**")
