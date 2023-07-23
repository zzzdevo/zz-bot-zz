import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**ᯓ تاقیکردنەوەی خێرایی دابەزاندن...**")
        test.download()
        m = m.edit("**ᯓ بارکردنی تاقیکردنەوەی خێرایی... **")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**ᯓ ئەنجامی تاقیکردنەوەی خێرایی هاوبەش بکە...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("**•⎆┊تاقیکردنەوەی خێرایی ئەنجام بدە...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**[ᯓ 𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - فەرمانی خێرایی🧑🏻‍💻🖤](t.me/MGIMT)•\n••┉┉┉┉┉┉┉••🝢••┉┉┉┉┉┉┉••\n**
<u>**•⎆┊کڕیار :**</u>
**•⎆┊𝙄𝙎𝙋 :** {result['client']['isp']}
**•⎆┊وڵات :** {result['client']['country']}
  
<u>**•⎆┊سێرڤەر :**</u>
**•⎆┊ناو :** {result['server']['name']}
**•⎆┊وڵات :** {result['server']['country']}, {result['server']['cc']}
**•⎆┊سپۆنسەر :** {result['server']['sponsor']}
**•⎆┊دواکەوتن :** {result['server']['latency']}  
**•⎆┊پینگ :** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
