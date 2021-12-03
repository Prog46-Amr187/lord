# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @JAI6H © Rocks
# Owner Asad + Harshit
 

from cache.admins import admins
from rocksdriver.asad import call_py
from pyrogram import Client, filters
from rocksdriver.decorators import authorized_users_only
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, clear_queue
from rocksdriver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL, REPO_OWNER, BOT_UPDATE, MY_BRO, MY_SERVER, BOT_NAME, MY_HEART
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 ɢᴏ ʙᴀᴄᴋ", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 ᴄʟᴏsᴇ", callback_data="cls")]]
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(f"""**━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.
┏━━━━━━━━━━━━━━━━━┓
┣★ ʙᴏᴛ : [ʀᴇʟᴏᴀᴅᴇᴅ](t.me/{BOT_USERNAME})
┣★ ᴀᴅᴍɪɴ : At [{BOT_NAME}](t.me/roottuxido) ʀᴇғʀᴇsʜᴇᴅ
┣★ sᴜᴘᴘᴏʀᴛ : [ʙᴏᴛ ᴜᴘᴅAtᴇs](t.me/BOT_UPDATE)
┗━━━━━━━━━━━━━━━━━┛
• ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴛʜᴇɴ [ᴊᴀᴠᴀ](t.me/JAI6H) ᴍᴇ
• ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ » ǫᴜᴇsᴛɪᴏɴ
ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](t.me/uu_ak)
━━━━━━━━━━━━━━━━━━━**""",
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/JAI6H"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ **لا يوجد شيء مشغل**")
        elif op == 1:
            await m.reply("✅ قوائم **الإنتظار فارغه.**\n\n**• توقف [تشغيل الموسيقى](t.me/roottuxido) وترك الحساب المساعد المحادثه الصوتيه**")
        elif op == 2:
            await m.reply("🗑️ **مسح قوائم الانتظار**\n\n**توقف [تشغيل الموسيقى](t.me/roottuxido) وترك الحساب المساعد المحادثه الصوتيه**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **Skipped to next tarck.**\n\n🎙️ **Name:** [{op[0]}]({op[1]})\n\n🔋 **Status:** `Playing`\n🎧 **Request by:** {m.from_user.mention()}",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **تم ازاله الاغنيه**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ **تم ايقاف** [تشغيل](t.me/libcubehawk) **الموسيقي في المجموعه**")
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"🚫 **هناك خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ لا توجد موسيقى مشغله الان**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **تم إيقاف المسار مؤقتًا.**\n\n• **لاستئناف استخدام**\n» /resume ."
            )
        except Exception as e:
            await m.reply(f"🚫 **هناك خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ لا توجد موسيقى مشغله الان**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **At** [تشغيل الموسيقى](t.me/roottuxido) **Tʀᴀᴄᴋ ɪs ʀᴇsᴜᴍᴇᴅ.**\n\n• **To pause the stream, use the**\n» /pause command."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"🚫 **هناك خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ لا توجد موسيقى مشغله الان**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 تم كتم الصوت بنجاح .**\n\n• **استخدم هذا الامر لالغاء الكتم**\n» /unmute ."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"🚫 **هناك خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ لا توجد موسيقى مشغله الان**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **تم الغاء الكتم عند تشغيل الموسيقى ، يكون البوت غير مكتوم.**\n\n• **لكتم صوت الاغاني ارسل امر**\n» /mute ."
            )
            keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )
        except Exception as e:
            await m.reply(f"🚫 **هناك خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ لا توجد موسيقى مشغله الان**")
        keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Rino .️", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/roottuxido"),
            ]
        ]
    )


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("هناك خطا يا عزيزي !\n\n» يرجي إيقاف صلاحيه البقاء مختفياً.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "⏸ the streaming has paused", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **هناك خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ لا يوجد شئ مشغل الان", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("هناك خطا يا عزيزي !\n\n» يرجي إيقاف صلاحيه البقاء مختفياً.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "▶️ تم استئناف البث", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **هناك خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ لا يوجد شئ مشغل الان", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("هناك خطا يا عزيزي !\n\n» يرجي إيقاف صلاحيه البقاء مختفياً.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("✅ **انتهى تشغيل هذا الشئ**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **هناك خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ لا يوجد شئ مشغل الان", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("هناك خطا يا عزيزي !\n\n» يرجي إيقاف صلاحيه البقاء مختفياً.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "🔇 تم الغاء الوضع الصامت بنجاح", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **هناك خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ لا يوجد شئ مشغل الان", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("هناك خطا يا عزيزي !\n\n» يرجي إيقاف صلاحيه البقاء مختفياً.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("🔋 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "🔊 تم الغاء الصمت بنجاح**", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **هناك خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("❌ **لا يوجد شئ مشغله الان**", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **تم ضبط الصوت على** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **هناك خطأ:**\n\n`{e}`")
    else:
        await m.reply("❌ **لا يوجد موسيقى مشغله الان**")