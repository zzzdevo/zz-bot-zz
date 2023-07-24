
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AnonX import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.enums import ParseMode, ChatMemberStatus


##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]


iddof = []
@app.on_message(
     command(["قفل العاب","تعطيل العاب"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
   
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطـور اساسي"
    if get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــألك"
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمـــن"
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"**يا {message.from_user.mention}\n الالعاب مقفله من قبل**")
        iddof.append(message.chat.id)
        return await message.reply_text(f"**تم قفل الالعاب بنجاح\n\nبواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]
@app.on_message(
    command(["فتح العاب","تفعيل العاب"])
    & filters.group
)
async def idljjopen(client:Client, message:Message):
    dev = (OWNER_ID)
    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطـور اساسي"
    if get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــألك"
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمـــن"
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if not message.chat.id in iddof:
            return await message.reply_text(f"**يا {message.from_user.mention}\n الالعاب مفتوحه من قبل**")
        iddof.remove(message.chat.id)
        return await message.reply_text(f"**تم فتح الالعاب بنجاح\n\nبواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")
##|𓆩˹𓏺َِ 𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝞝𝙔 ٍٍٍٍٍٍّّّّّّّ『مـبـ ـࢪمـج ⏎』🇸🇦 ☬, [23/12/44 03:32 ص]  
@app.on_message(command(['زوجني','ز']))
def iddd(client:Client, message:Message):
    chat_id = message.chat.id
    if chat_id in iddof:
         return
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"• اخترت لك هذا الشخص {random_member_mention} \n 🙈♥️",
        f"• اخترت لك هذا الشخص \n {random_member_mention} \n **"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
@app.on_message(command(['وتە']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
        return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nپێویستە سێ جار هەوڵبدەیت پێش ئەوەی نائومێدبیت🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nهەموو ڕۆژێك هەلێك بدە، بۆ ئەوەی ببێتە باشترین ڕۆژی ژیانت🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nدانایی دەزانێت کەی کەسەکان پشتگوێ بخەیت🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nئارامگرتن کلیلی قفڵێکی بەهێزە🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nتۆ بەرپرسیاریت لەوەی کە هەست بەچی دەکەیت، بەڵام تۆ بەرپرس نیت لەوەی ئەوانی تر دەیکەن🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nئەگەر بەو شێوەیە ناژیت کە دەتەوێت، دەبێت بیگۆڕیت🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nبراوەکان نھێنی ڕاهێنانیان باس ناکەن ئەوان بەرەو ئامانجی گەورە دەڕۆن🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nهیچ شتێک لە ژیاندا لە خۆشەویستی و بەختەوەری باشتر نییە🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nکاتێك با دەگۆڕێت، پێویستە ئاڕاستەی دەریاکە ڕێکبخەین لەجیاتی ئەوەی گەشت بوەستێنین🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nژیان وەك شەپۆل وایە، تۆ تەنها پێویستە هاوسەنگی خۆت بدۆزیتەوە بۆ ئەوەی نوقم نەبیت🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nئەو درەختەی کە لە بادا چەماوەتەوە، ئەو درەختەیە کە لە زریاندا دەشکێت🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\n ئاواتی من ئەوەیە کە گۆشەی مەترسیداری تێدابێت هیچ شتێك ناتوانێت بەبێ بەرەنگاربوونەوە گەشەبکات🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nناتوانیت تاریکی لەبیربکەیت پێویستە مۆمێك دروست بکەیت🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nدووری تامێکی هەیە کە لە ئازارەوە دێت بۆ ئەو کەسەی کە لە خۆشەویستیدا نەدۆڕاوە🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nشتەکان لەسەر بنەمای تێپەڕبوونی بە باروودۆخ دیاری ناکرێت بەڵکو لەسەر بنەمای وەڵامەکانی ئەو باروودۆخە دیاری دەکرێت🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nهەڵبژاردن، لە کۆتاییدا، ڕێگایەک کە لە بەرژەوەندی تۆدا نەبوو ڕێگای تر بەجێبھێڵە کە نەدۆزراوەتەوە🖤•**",
         f"**-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nهیچ شتێکی باشت نەبوو بۆ ئەوەی بیڵێیت، بۆیە بێدەنگ بە🖤•**",
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
@app.on_message(command(['وەسف','و']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
         return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"**لە مانڴ جوانتریت🌚♥️{random_member_mention}",
        f"**جوانی تۆ بەهیچ شێوازێك باس ناکرێت{random_member_mention}",
        f"**خۆشەویستی لە دڵی هەموواندا🍭💘 {random_member_mention}",
        f"**دەڵێی هەنگوینی وەرە با بتخۆم😂♥{random_member_mention}",
        f"**شار بە جوانی تۆ سەرسامبوو😏💚{random_member_mention}",
        f"**دانشە خوئری😂🤭{random_member_mention}",
        f"**دەڵێی فیلی😔😹{random_member_mention}",
         f"**سوک مەبە کوڕم سوکی صه😳{random_member_mention}"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
