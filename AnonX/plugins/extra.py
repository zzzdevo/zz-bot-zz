from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os
from strings.filters import command
from AnonX import app

@app.on_message(command(["تێلەگراف","telegraph"]))
async def get_link_group(client, message):
    try:
        text = await message.reply("•⎆┊**دروست دەکرێت ..**")
        async def progress(current, total):
            await text.edit_text(f"•⎆┊**میدیا دروست کرا🕷  ... **{current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("•⎆┊**بەستەری میدیا لە هێناندایە ..🕷️•**")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"•⎆┊**  𝒕𝒆𝒍𝒆 𝒍𝒊𝒏𝒌 **:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"•⎆┊**فایلەکە شکستی هێنا♥•**\n\n<i>**هۆکار**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass
