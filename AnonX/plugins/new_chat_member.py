from pyrogram import Client, filters, types
from datetime import datetime
import asyncio 

# Start Bot Client
app = Client('bots',
    bot_token='<API_KEY>',  # BOT_TOKN or API_KEY
    api_id=123457678, # API_ID TELEGRAM ACCOUNT
    api_hash='95f5f60466a64ttn7a34f297c734d0568') # API_HASH TELEGRAM ACCOUNT

#Welcoem message
WELCOME_MESSAGE = """ ↫ Welcome To From Group .
    •╭ID        : ❲ @{} ❳ .
    •╰NAMEE     : ❲ {} ❳ .
    •╭USERNAEM  : ❲ {} ❳ .
    •╰Date      : ❲ {} ❳ .
    •╰Pio       : ❲ {} ❳ . 


"""

# On /start From Private
@app.on_message(filters.regex('/start') & filters.private)
async def ON_START(_, Message: types.Message):
    chat_id, message_id, user_id = Message.chat.id, Message.id, Message.from_user.id
    await app.send_message(text='Welcome To Group Security Bot .', chat_id=chat_id)



# On Join Group member . 
@app.on_message(filters.group & filters.new_chat_members)
async def ON_NEW_CHAT_MEMBER(_, Message: types.Message):
    chat_id, message_id, user_id = Message.chat.id, Message.id, Message.from_user.id
    new_memeber = await app.get_chat(user_id) # get member data
    # Welcome Message
    message = WELCOME_MESSAGE.format(
        Message.from_user.id,
        Message.from_user.first_name,
        Message.from_user.username,
        str(datetime.now()),
        new_memeber.bio)
    new_memeber_photo = None
    # get member profile photo
    async for photo in app.get_chat_photos(user_id, limit=1):
        new_memeber_photo = photo
    # send Welcome Message
    if new_memeber_photo != None:
        message_data = await app.send_photo(photo=new_memeber_photo.file_id,chat_id=chat_id,caption=message, reply_to_message_id=message_id) 
    else:
        message_data = await app.send_message(text=message, chat_id=chat_id,reply_to_message_id=message_id)
    await asyncio.sleep(1.8) # sleep 1.8 sc
    # # delete join memeber message
    await app.delete_messages(chat_id, message_id) 
    await asyncio.sleep(8) # seelp 8 sc
    # delete Welcome memeber message
    await app.delete_messages(chat_id , message_data.id)


asyncio.run(app.run())  # on start run bot.
