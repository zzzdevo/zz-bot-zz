from pyrogram import filters

import config
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database import autoend_off, autoend_on
from AnonX.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**بەکارهێنان:**\n\n/autoend [چالاک|ناچالاک]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "**کۆتایی هات.\n\nدەرچووم چونکە کەسی لێ نەبوو**"
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("**دەرچوونی خودکار ناچالاکە**")
    else:
        await message.reply_text(usage)
