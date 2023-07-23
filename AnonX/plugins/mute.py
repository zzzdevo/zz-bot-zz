import pyrogram
from pyrogram import filters
from pyrogram.types import Message

from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils.database import is_muted, mute_on
from AnonX.utils.decorators import AdminRightsCheck
from config import BANNED_USERS
from strings import get_command

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(filters.command(MUTE_COMMAND)
                & filters.group
                & ~BANNED_USERS
                )
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await Anon.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention)
    )


@app.on_message(filters.command(["ڕێکلام"])
& filters.forwarded
)
@AdminRightsCheck
def gjgh(client, message, m):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        if message.chat.id in message:
            return await message.reply_text(f" {message.from_user.mention} پێشتر چالاککراوە  ")
        message.append(message.chat.id)
        return await message.reply_text(f"چالاککراوا  ←{message.from_user.mention}")
    else:
        return await message.reply_text(f" {message.from_user.mention} تۆ ئەدمحن نییت ")
    m.delete()
