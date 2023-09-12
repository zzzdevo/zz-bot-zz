from pyrogram import filters, Client
from AnonX import app
import asyncio
from pyrogram.types import VideoChatEnded, Message
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonX.core.call import Anon
from AnonX.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall, TelegramServerError, AlreadyJoinedError)


@app.on_message(filters.regex("^کێ لە تێلە$"))
async def strcall(client, message):
    assistant = await group_assistant(Anon, message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./AnonX/assets/call.mp3"),
                                        stream_type=StreamType().pulse_stream)
        text = "•⎆┊**ئەو کەسانەی لە تێل بەشدارن♥•**:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if not info.muted:
                mut = "**قسەکەر**"
            else:
                mut = "**بێدەنگ**"
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"** {k} {user.mention}\n  {mut}**\n\n"
        text += f"\n**ژمارەیان : {len(participants)} **\n✔️"
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"•⎆┊**ببورە ئەزیزم تێل نەکراوتەوە♥•**")
    except TelegramServerError:
        await message.reply(f"•⎆┊**دووبارە فەرمانەکە بنێرە کێشەیەك هەیە لە سێرڤەری تێلەگرام💔•**")
    except AlreadyJoinedError:
        text = "•⎆┊**ئەو کەسانەی لە تێل بەشدارن♥•**:\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if not info.muted:
                mut = "**قسەکەر**"
            else:
                mut = "**بێدەنگ**"
            user = await client.get_users(participant.user_id)
            k += 1
            text += f" {k} {user.mention}\n  {mut}\n\n"
        text += f"\n**ژمارەیان : {len(participants)} **\n✔️"
        await message.reply(f"{text}")


@app.on_message(filters.video_chat_ended)
async def brah2(message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
        await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی {da} چرکە و داخرا⚡️♥️•**")
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی 1 خولەك⚡️♥️•**")
        elif 2 <= ma[0] < 3:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی 2 خولەك⚡️♥️•**")
        elif 3 <= ma[0] < 11:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی {ma[0]} خولەك⚡️♥️•**")
        else:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی {ma[0]} خولەك⚡️♥️•**")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی 1 کاتژمێر⚡️♥️•**")
        elif 2 <= ho[0] < 3:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی 2 کاتژمێر⚡️♥️•**")
        elif 3 <= ho[0] < 11:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی {ho[0]} کاتژمێر⚡️♥️•**")
        else:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی {ho[0]} کاتژمێر⚡️♥️•**")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی 1 ڕۆژ⚡️♥️•**")
        elif 2 <= day[0] < 3:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی 2 ڕۆژ⚡️♥️•**")
        elif 3 <= day[0] < 11:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی {day[0]} ڕۆژ⚡️♥️•**")
        else:
            await message.reply(f"•⎆┊**تێل کۆتایی پێھات، ماوەکەی {day[0]} ڕۆژ⚡️♥️•**")
