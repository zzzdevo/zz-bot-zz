from pyrogram import *
from pyrogram.types import *


log_chat = int(-1001906948158)
token = "6357186923:AAEKydDxtzDe6C0u-F46QmCpabiodn8TOEA"

Main_developer_keyboard = ReplyKeyboardMarkup([
	[('تفعيل التواصل'),('تعطيل التواصل'),('حاله التواصل')],
	[('ضع قناة الاشتراك'),('حذف قناه الاشتراك')],
	[('تفعيل الاشتراك'),('تعطيل الاشتراك'),('قناه الاشتراك')],
	[('حاله الاشتراك'),('الاحصائيات')],
	[('تفعيل اليوتيوب'),('تعطيل اليوتيوب'),('حاله اليوتيوب')],
	[('حذف الاعضاء الفيك'),('حذف الجروبات الفيك')],
	[('الاصدار'),('تحديث السورس'),('سرعه السيرفر')],
	[('اذاعه للمستخدمين'),('اذاعه للجروبات')],
	[('اذاعه للمطورين'),('اذاعه للاساسيين'),('اذاعه للقنوات')],
	[('اذاعه للكل'),('توجيه للكل')],
	[('توجيه للمستخدمين'),('توجيه للجروبات'),('توجيه للقنوات')],
	[('توجيه للاساسيين'),('توجيه للمطورين')],
	[('رفع مطور'),('تنزيل مطور'),('عرض المطورين')],
	[('رفع مطور اساسي'),('تنزيل مطور اساسي')],
	[('عرض الاساسيين'),('مسح الاساسيين'),('مسح المطورين')],
	[('نسخه احتياطيه اساسيه'),('نسخه احتياطيه 2')],
	[('حظر عضو'),('الغاء حظر عضو'),('عرض المحظورين')],
	[('تغيير مالك البوت'),('تغيير اسم البوت')],
	[('تفعيل البوت'),('تعطيل البوت'),('حاله البوت')],
	[('مسح المحظورين'),('تغيير داتابيس البوت')],
	[('اخفاء الكيبورد ⚒️')]],
	resize_keyboard=True,
	one_time_keyboard=False
	)


dev_key = ReplyKeyboardMarkup([
	[('تفعيل التواصل'),('تعطيل التواصل'),('حاله التواصل')],
	[('ضع قناة الاشتراك'),('حذف قناه الاشتراك')],
	[('تفعيل الاشتراك'),('تعطيل الاشتراك'),('قناه الاشتراك')],
	[('حاله الاشتراك'),('الاحصائيات')],
	[('تفعيل اليوتيوب'),('تعطيل اليوتيوب'),('حاله اليوتيوب')],
	[('حذف الاعضاء الفيك'),('حذف الجروبات الفيك')],
	[('الاصدار'),('تحديث السورس'),('سرعه السيرفر')],
	[('اذاعه للمستخدمين'),('اذاعه للجروبات')],
	[('اذاعه للمطورين'),('اذاعه للاساسيين'),('اذاعه قنوات')],
	[('اذاعه للكل'),('توجيه للكل')],
	[('توجيه للمستخدمين'),('توجيه للجروبات'),('توجيه للقنوات')],
	[('توجيه للاساسيين'),('توجيه للمطورين')],
	[('حذف الكيبورد ⚒️')]],
	resize_keyboard=True,
	one_time_keyboard=False
	)



database_name = "DevBody.db"
