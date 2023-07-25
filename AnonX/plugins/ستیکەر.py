from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from AnonX import app

stiklok = []


@app.on_message(
    filters.command(["داخستنی ستیکەر"])

)
async def block_stickers(client: Client, message: Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"•⎆┊**{message.from_user.mention} ستیکەر پێشتر داخستراوە♥•**")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"•⎆┊**ستیکەر داخسترا\n\n پێشتر ←{message.from_user.mention}♥•**")
    else:
        return await message.reply_text(f"•⎆┊**{message.from_user.mention}ببورە تۆ ئەدمین نیت🗿•**")


@app.on_message(
    filters.command(["کردنەوەی ستیکەر"])

)
async def block_stickers(client: Client, message: Message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in ["creator", "administrator"]:
        if message.chat.id in stiklok:
            return await message.reply_text(f"•⎆┊**{message.from_user.mention} ستیکەر پێشتر کراوەتەوە♥•**")
        stiklok.append(message.chat.id)
        return await message.reply_text(f"•⎆┊**ستیکەر کراوەتەوە\n\n پێشتر ←{message.from_user.mention}♥•**")
    else:
        return await message.reply_text(f"•⎆┊**{message.from_user.mention}ببورە تۆ ئەدمین نیت🗿•**")
