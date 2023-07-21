from pyrogram import Client, filters, idle
from pyrogram.enums import ChatMemberStatus
from pyrogram import filters
from AnonX import app


mutes = []
@app.on_message(filters.regex("^ئاگاداری$"))
async def mute(app, message):
   member = await message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await message.reply("•⎆┊**تەنیا ئەدمین دەتوانێت ئەم فەرمانە بەکاربھێنێت♥•**")
   else:
     if not message.reply_to_message:
       return await message.reply("•⎆┊**پێویستە ئەم فەرمانە بە وەڵامدانەوە بەکاربھێنیت نەك دانانی یوزەر لەگەڵ فەرمان♥•**")
     member = await message.chat.get_member(message.reply_to_message.from_user.id)
     if member.status in [ChatMemberStatus.OWNER]:
       return await message.reply("•⎆┊**تۆ ناتوانی گەشەپێدەر میوت بکەیت♥•**")
     chat_id = str(message.chat.id)
     user_id = str(message.reply_to_message.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
     if x in mutes:
       return await message.reply("•⎆┊**ئەم بەکارهێنەرە ئێستا میوتە لەم گرووپە♥•**")
     else:
       mutes.append(x)
       return await message.reply("•⎆┊** {} بە سەرکەوتوویی میوت کرا لەلایەن {} 🗿•**".format(message.reply_to_message.from_user.mention,message.from_user.mention))
       
@app.on_message(filters.regex("^لادانی ئاگاداری$"))
async def unmute(app,message):
   member = await message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await message.reply("•⎆┊**تەنیا ئەدمین دەتوانێت ئەم فەرمانە بەکاربھێنێت♥•**")
   else:
     if not message.reply_to_message:
       return await message.reply("•⎆┊**پێویستە ئەم فەرمانە بە وەڵامدانەوە بەکاربھێنیت نەك دانانی یوزەر لەگەڵ فەرمان♥•**")
     member = await message.chat.get_member(message.reply_to_message.from_user.id)
     if member.status in [ChatMemberStatus.OWNER]:
       return await message.reply("•⎆┊**تۆ ناتوانی لادانی میوتی گەشەپێدەر بکەیت♥•**")
     chat_id = str(message.chat.id)
     user_id = str(message.reply_to_message.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
     if not x in mutes:
       return await message.reply("•⎆┊**ئەم بەکارهێنەرە ئێستا میوتی لادراوە لەم گرووپە♥•**")
     else:
       mutes.remove(x)
       return await message.reply("•⎆┊** {} بە سەرکەوتوویی میوتی لادرا لەلایەن {} 🗿•**".format(message.reply_to_message.from_user.mention,message.from_user.mention))

@app.on_message(filters.regex("^میوتکراوەکان$"))
def get_dmute(app, message):
   if len(mutes) == 0: return
   member = message.chat.get_member(message.from_user.id)
   if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return message.reply("•⎆┊**تەنیا ئەدمین دەتوانێت ئەم فەرمانە بەکاربھێنێت♥•**")
   ch = message.chat.id
   c = 0
   text = "•⎆┊**لیستی میوت کراوەکان🗿** :\n\n"
   for a in mutes:
     chat_id = int(a.split("@")[0])
     user_id = int(a.split("@")[1])
     if chat_id == ch:
        user = app.get_users(user_id)
        text += f"- {user.mention}\n"
        c += 1
   if c == 0: return message.reply("•⎆┊**هیچ کەسێك میوت نەکراوە♥•**")
   message.reply(f"**{text}**")

@app.on_message(filters.group)
def del_msg(_,m):
   global x
   if m.from_user:
     chat_id = str(m.chat.id)
     user_id = str(m.from_user.id)
     x = "{}@{}".format(chat_id,user_id)
   for a in mutes:
     if a == x: 
       m.delete()
