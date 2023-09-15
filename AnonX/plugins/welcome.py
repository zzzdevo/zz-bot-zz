import asyncio
from pyrogram.types import ChatMemberUpdated
from pyrogram import Client, filters, types
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from AnonX import app

# Welcoem message
WELCOME_MESSAGE = """** ↫ بەخێربێیت ئەزیزم بۆ گرووپ♥️•**\n
**✧ ¦ ناوت** ← {}
**✧ ¦ یوزەرت** ← @{}
**✧ ¦ ئایدیت** ← `{}`
**✧ ¦ بەروار** ← {}
**✧ ¦ بایۆ** ← **{}** 


"""


# On /start From Private
@app.on_message(filters.regex('/jstart') & filters.private)
async def ON_START(_, Message: types.Message):
    chat_id, message_id, user_id = Message.chat.id, Message.id, Message.from_user.id
    await app.send_message(text='Welcome To Group Security Bot .', chat_id=chat.id)


# On Join Group member .
@app.on_chat_member_updated(filters.group)
async def addtsrb(client, m):
    global new_memeber_photo, message
    if m.new_chat_member and not m.old_chat_member:
        chat_id = m.chat.id
        user_id = m.from_user.id
        new_memeber = await app.get_chat(m.from_user.id)  # get member data
        # Welcome Message
        message = WELCOME_MESSAGE.format(
            m.from_user.mention,
            m.from_user.username,
            m.from_user.id,
            str(datetime.now()),
            new_memeber.bio)
        new_memeber_photo = None
    # get member profile photo
    async for photo in app.get_chat_photos(m.from_user.id, limit=1):
        new_memeber_photo = photo
    # send Welcome Message
    if new_memeber_photo != None:
        message_data = await app.send_photo(
        photo=new_memeber_photo.file_id, chat_id=chat_id, caption=message,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="➕ زیادم بکە بۆ گرووپت ➕",
                                         url=f"https://t.me/IQMCBOT?startgroup=true"),
                                                
                ],[
                    InlineKeyboardButton(text="• کەناڵی بۆت •",
                                         url=f"https://t.me/MGIMT"),
                ]
                
              ],  
     
           ),
        )
    else:
        message_data = await app.send_message(text=message, chat_id=chat_id,
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="➕ زیادم بکە بۆ گرووپت ➕",
                                         url = f"https://t.me/IQMCBOT?startgroup=true"),
                ],[
                    InlineKeyboardButton(text="• کەناڵی بۆت •",
                                          url=f"https://t.me/MGIMT"),
                ]  

            ],

        ),
                                              )
