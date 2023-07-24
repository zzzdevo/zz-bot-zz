from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from AnonX import app
from AnonX.utils.database import is_on_off

async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "**چاتی تایبەت**"
        logger_text = f"""**[ᯓ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - ئاماری پەخشکردن](https://t.me/MGIMT)\n••┉┉┉┉┉┉┉••🝢••┉┉┉┉┉┉┉••\n
**گرووپ:** {message.chat.title} [`{message.chat.id}`]
**یوزەر:** @{message.from_user.username}
**ناسنامە:** `{message.from_user.id}`
**بەستەر چات:** {chatusername}
**گەڕان کرا لەلایەن:** {message.text}
**جۆری پەخشکردن:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
