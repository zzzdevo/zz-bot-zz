from pyrogram import Client, filters, idle
from AnonX import app
  
@app.on_message(filters.regex("^بڵێ|^بلی") & filters.group)
async def say(app,message):
   if message.text.startswith("بڵێ") and message.reply_to_message:
     txt = message.text.sfage.reply_to_message.reply(txt)
     
   elif message.text.startswith("بڵێ"):
     txt = message.text.split(None, 1)[1]
     return await message.reply(txt)
     
