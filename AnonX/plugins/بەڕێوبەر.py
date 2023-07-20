from pyrogram import Client , filters
from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPrivileges)
from pyrogram.enums import ChatMemberStatus
from pyrogram import filters, Client
from AnonX import app


async def PROMOTE_OWNER(c:Client,m:Message):
    ChatID = m.chat.id
    TargetID = m.reply_to_message.from_user.id
    UserID = m.from_user.id
    KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("تغيير معلومات المجموعة",
    callback_data=f"can_change {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حذف الرسائل",
    callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حظر المستخدمين",
    callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
    callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("تثبيت الرسائل",
    callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إداره البثوث المباشره",
    callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إضافه مشرفين جدد",
    callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
	callback_data="delete"),
	InlineKeyboardButton("المزيد",
	callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]])
    
    await m.reply(f"ابشر عيني 「{m.from_user.mention}」\n لديك قائمه يمكنك التحكم فيها في رفع المستخدم مشرف\nاذا ضغط علي زر 1 ترفع فقط صلاحيه\n ضغطت علي زر 2 يرفع زر 1,2\nضغطت علي زر 3 يرفع زر 1,2,3 وهكذا\nلذللك ضفنالك زر المزيد تصفحه",reply_markup=KEYBOARD)


async def PROMOTE(c:Client,m:Message):
    ChatID = m.chat.id
    TargetID = m.reply_to_message.from_user.id
    UserID = m.from_user.id
    KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("تغيير معلومات المجموعة",
    callback_data=f"can_change {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حذف الرسائل",
    callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("حظر المستخدمين",
    callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
    callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("تثبيت الرسائل",
    callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("إداره البثوث المباشره",
    callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
	callback_data="delete"),
	InlineKeyboardButton("المزيد",
	callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]])
    
    await m.reply(f"ابشر عيني 「{m.from_user.mention}」\n لديك قائمه يمكنك التحكم فيها في رفع المستخدم مشرف\nمع العلم اذا ضغط علي زر 1 ترفع فقط صلاحيه\n ضغطت علي زر 2 يرفع زر 1+ 2\nضغطت علي زر 3 يرفع زر 1 + 2 +  3 وهكذا",reply_markup=KEYBOARD)





@app.on_message(filters.command(["رفع"],[""]),group=1)
async def New(c:Client,m:Message):
	Ra = await m.chat.get_member(m.from_user.id)
	if Ra.status == ChatMemberStatus.OWNER:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await PROMOTE_OWNER(c,m)
				
				
	elif Ra.status == ChatMemberStatus.ADMINISTRATOR:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await PROMOTE(c,m)
			
	elif Ra.status == ChatMemberStatus.MEMBER:
		if m.reply_to_message and m.reply_to_message.from_user:
			if m.command[1] == "مشرف":
				await m.reply(f"عزيزي 「{m.from_user.mention}」\nانت مجرد عضو في هذه المجموعة")

@app.on_callback_query(~filters.regex('^delete$'),group=2)
async def MoreAndSet(c:Client,m:CallbackQuery):
	ChatID = m.message.chat.id
	TargetID = m.message.reply_to_message.from_user.id
	UserID = m.from_user.id
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])
	
	MORE_PROMOTE = InlineKeyboardMarkup([
    [InlineKeyboardButton("1,2,3,4,5,6,7",
    callback_data=f"Seven {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,2,4,5,6",
    callback_data=f"Five {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("2,4,5,6",
    callback_data=f"Four {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,3,6",
    callback_data=f"Three {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("4,6",
    callback_data=f"Two {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("4",
    callback_data=f"One {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
    callback_data="delete")]])

	
	if m.data == f"MoreAndMore {ChatID} {TargetID} {UserID}":
		return await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n",
		reply_markup=MORE_PROMOTE)
		
	if m.data == "delete":
		await m.message.delete()
		
    
    



@app.on_callback_query(~filters.regex('^delete$'),group=3)
async def SetPromote(c:Client,m:CallbackQuery):
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])

	
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_change":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه تغيير معلومات المجموعه",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("حذف الرسائل",
		callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("حظر المستخدمين",
		callback_data=f"can_restrict {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_delete":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_change_info=True,
		can_delete_messages=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه مسح الرسائل",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("حظر المستخدمين",
		callback_data=f"can_delete {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	
	elif len(PromoteList) == 4 and PromoteList[0] == "can_restrict":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه حظر المستخدمين",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("دعوه المستخدمين عبر الرابط",
		callback_data=f"can_invite {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_invite":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه دعوه المستخدمين",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("تثبيت الرسائل",
		callback_data=f"can_pin {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_pin":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه تثبيت الرسائل",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("إداره البثوث المباشره",
		callback_data=f"can_manage_video {ChatID} {TargetID} {UserID}")],
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
	
	elif len(PromoteList) == 4 and PromoteList[0] == "can_manage":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه التحكم في المحادثه الصوتية",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("إضافه مشرفين جدد",
		callback_data=f"can_promote {ChatID} {TargetID} {UserID}")],
		
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "can_promote":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_promote_members=True,
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text("تم اعطائه صلاحيه رفع مشرفين جدد",
		reply_markup=
		InlineKeyboardMarkup([
		[InlineKeyboardButton("مسح الرساله",
		callback_data="delete"),
		InlineKeyboardButton("المزيد",
		callback_data=f"MoreAndMore {ChatID} {TargetID} {UserID}")]]))
		
		
		
@app.on_callback_query(~filters.regex('^delete$'),group=4)
async def SetMorePromote(c:Client,m:CallbackQuery):
	msg = m.data
	PromoteList = msg.split(" ")
	ChatID = m.message.chat.id
	TargetID = int(PromoteList[2])
	UserID = int(PromoteList[3])
	
	MORE_PROMOTE = InlineKeyboardMarkup([
    [InlineKeyboardButton("1,2,3,4,5,6,7",
    callback_data=f"Seven {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,2,4,5,6",
    callback_data=f"Five {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("2,4,5,6",
    callback_data=f"Four {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("1,3,6",
    callback_data=f"Three {ChatID} {TargetID} {UserID}"),
    InlineKeyboardButton("4,6",
    callback_data=f"Two {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("4",
    callback_data=f"One {ChatID} {TargetID} {UserID}")],
    [InlineKeyboardButton("مسح الرساله",
    callback_data="delete")]])

    
	
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Seven":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_promote_members=True,
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_restrict_members=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,2,3,4,5,6,7) ",reply_markup=MORE_PROMOTE)
			
	elif len(PromoteList) == 4 and PromoteList[0] == "Five":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_delete_messages=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,2,4,5,6) ",reply_markup=MORE_PROMOTE)
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Four":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_pin_messages=True,
		can_invite_users=True,
		can_delete_messages=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (2,4,5,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Three":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_restrict_members=True,
		can_change_info=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (1,3,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "Two":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_manage_video_chats=True,
		can_invite_users=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (4,6) ",reply_markup=MORE_PROMOTE)
		
		
	elif len(PromoteList) == 4 and PromoteList[0] == "One":
		CHATID = int(PromoteList[1])
		USERID = int(PromoteList[2])
		try:
			await app.promote_chat_member(
		chat_id=CHATID,
		user_id=USERID,
		privileges=ChatPrivileges(
		can_invite_users=True))
		except Exception as e:
			return await m.message.edit_text(f"**عزيزي :**\n「{m.from_user.mention}」\nهذا لم يتم رفعه من خلالي\n\n**Error**:\n"+ str(e))
		await m.message.edit_text(f"مرحبا عزيزي\n「{m.from_user.mention}」\nاليك قائمه اختر ما تريد\n1- تغيير معلومات المجموعة\n2- حذف الرسائل\n3- حظر المستخدمين\n4- دعوه المستخدمين عبر الرابط\n5- تثبيت الرسائل\n6- إداره البثوث المباشره\n7- اضافه مشرفين جدد\n\n\nتم اعطاء المستخدم الصلاحيات الاتيه (4) ",reply_markup=MORE_PROMOTE)


@app.on_callback_query(filters.regex("^delete$"),group=5)
async def DelMessage(c:Client,m:CallbackQuery):
	UserID = m.from_user.id
	if m.from_user.id !=UserID:
		await c.answer_callback_query(
		m.id,
		text="هذا الأمر لايخصك",
		show_alert=True)
	else:
		await m.message.delete()

