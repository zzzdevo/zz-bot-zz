import pyrogram
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters, idle
from pyrogram.enums import ChatMemberStatus
from config import BANNED_USERS
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils.database import is_muted, mute_on
from AnonX.utils.decorators import AdminRightsCheck

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


@app.on_message(pyrogram.filters.forwarded)
& ChatMemberStatus.OWNER
& ChatMemberStatus.ADMINISTRATOR
def gjgh(client, m, message):
    m.delete()
