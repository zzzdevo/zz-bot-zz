
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
@app.on_message(command(['اقتباس','ق']))
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
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\nپێویستە سێ جار هەوڵبدەیت پێش ئەوەی نائومێدبیت**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\nهەموو ڕۆژێك هەلێك بدە، بۆ ئەوەی ببێتە باشترین ڕۆژی ژیانت**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\nدانایی دەزانێت کەی کەسەکان پشتگوێ بخەیت**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\nئارامگرتن کلیلی قفڵێکی بەهێزە**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n أنت مسؤول عن ماتشعر به، ولكنك لست مسؤولًا عن ما يفعله الآخرون**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n حكمتي تقول: دع الغضب يقتلع من قلبك السعادة كما تقتل الفحم النار من طريقه**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n إذا لم تكن تعيش بالطريقة التي تريدها، يجب عليك أن تغيرها**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n الفائزون لا يقومون بممارسة الأسرار. إنهم يتوجهون نحو الأهداف الكبيرة**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n ليس هناك شيء أفضل في الحياة من أن تكون في حالة حب وسعادة**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n عندما يتغير الريح، يجب علينا أن نعدل اتجاه الشراع بدلاً من أن نتوقف عن السفر**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n الحياة مثل الموج عليك فقط أن تجد توازنك حتى لا تسقط**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n العلم يجري كالماء، ولا يتوقف أبدًا - لا على الجدران ولا على السور، لكنه يصب في نهاية المطاف في ثنايا الإنسان**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n الشجرة التي لا تنحني عند الريح، هي التي تتحطم في الاعاصير**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n امنيتي ان يكون فيها زوايا خطرة ، فلا شي يمكن ان ينمي من دون التحدي**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n لا يمكنك تجاهل الظلام. يجب أن تنشئ شمعة**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n إن للبُعدِ طعمً يُصدِرُه الألمْ، ولكنَّ مِن يُجيد العِشقَ يجفَل الأميال **",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n المرء لا يتشكل على أساس المواقف التي يمر بها بل على أساس الردود التي يمنحها لتلك المواقف **",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n أن تختار، في النهاية، طريقًا واحدًا، لم يكن في صالحك أن تترك طرقاً أخرى غير مستكشفة ",
         f"-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n إن لم يكن عندك شيء جيد ليقال، فابقَ صامتًا**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n النجاح هو القدرة على الذهاب من فشل إلى فشل بدون فقد أرزاقك الحماس **", 
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
@app.on_message(command(['نداء','ن']))
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
        f"** جوانی تۆ بەهیچ شێوازێك باس ناکرێت{random_member_mention}",
        f"**خۆشەویستی لە دڵی هەموواندا🍭💘 {random_member_mention}",
        f"**دەڵێی هەنگوینی وەرە با بتخۆم😂♥{random_member_mention}",
        f"**شار بە جوانی تۆی سەرسامبوو{random_member_mention}"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
