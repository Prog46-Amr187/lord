# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit

import re
import asyncio

from config import ASSISTANT_NAME, BOT_USERNAME, IMG_1, IMG_2, GROUP_SUPPORT
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, add_to_queue
from rocksdriver.asad import call_py, user
from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            if len(r["title"]) > 34:
                songname = r["title"][:70]
            else:
                songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@Client.on_message(command(["vplay", f"vplay@{BOT_USERNAME}"]) & other_filters)
async def vplay(c: Client, m: Message):
    replied = m.reply_to_message
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Dev Bot .", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )
    if m.sender_chat:
        return await m.reply_text("**Your An __Anonymous Admin__ !\n\n» Revert Back To User Account From Rights.**")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"**Error**:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"📽️ لاستخدامي ، أحتاج إلى أن أكون مسؤولاً مع الإذن التالي‌‌**:\n\n» ❌ __حذف الرسائل__\n» ❌ __تقييد المستخدمين__\n» ❌ __اضافه المستخدمين__\n» ❌ __أداره المحادثات الصوتيه__\n\nيتم تحديث البيانات تلقائيًا بعد ترقيتي‌‌"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "**يرجي اعطائي الصلاحيه التاليه:**" + "\n\n» ❌ **__أداره المحادثات الصوتيه__**"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "**يرجي اعطائي الصلاحيه التاليه:**" + "\n\n» ❌ **__حذف الرسائل__**"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("**الإذن المطلوب مفقود**:" + "\n\n» ❌ **__اضافه المستخدمين__**")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **محظور في المجموعة** {m.chat.title}\n\n» **قم بإلغاء حظر الحساب المساعد اولاً إذا كنت تريد استخدام هذا البوت.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **فشل انضمام الحساب المساعد**\n\n**السبب**: `{e}`")
                return
        else:
            try:
                user_id = (await user.get_me()).id
                link = await c.export_chat_invite_link(chat_id)
                if "+" in link:
                    link_hash = (link.replace("+", "")).split("t.me/")[1]
                    await ubot.join_chat(link_hash)
                await c.promote_member(chat_id, user_id)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **فشل انضمام الحساب المساعد**\n\n**السبب**: `{e}`"
                )

    if replied:
        if replied.video or replied.document:
            loser = await replied.reply("📥 *Downloading Video...**")
            dl = await replied.download()
            link = replied.link
            if len(m.command) < 2:
                Q = 720
            else:
                pq = m.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await loser.edit(
                      "» **__Only 720, 480, 360 Allowed__** \n📽️ **Now Streaming video in 720ᴘ**"
                    )
            try:
                if replied.video:
                    songname = replied.video.file_name[:70]
                elif replied.document:
                    songname = replied.document.file_name[:70]
            except BaseException:
                songname = "Video"

            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"📽️ **Track added to queue »** `{pos}`\n📮 **Name:** [{songname[:10]}]({link})\n💭 **Chat:** `{chat_id}`\n🔋 **Request By:** {requester}",
                reply_markup=keyboard,
                )
            else:
                if Q == 720:
                    amaze = HighQualityVideo()
                elif Q == 480:
                    amaze = MediumQualityVideo()
                elif Q == 360:
                    amaze = LowQualityVideo()
                await loser.edit("🔄 **جاري تشغيل الفديو...**")
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(
                        dl,
                        HighQualityAudio(),
                        amaze,
                    ),
                    stream_type=StreamType().local_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_2}",
                    caption=f"📽️ **Video Streaming Started**\n📮 **Name:** [{songname[:10]}]({url})\n\n🚨 **Status:** `Playing`\n🔋 **Request By:** {requester}",
                    reply_markup=keyboard,
              )
        else:
            if len(m.command) < 2:
                await m.reply(
                    "**» الرد على الفديو او إعطاء شيء للبحث.**"
                )
            else:
                loser = await c.send_message(chat_id, "🔎 **يتم البحث عن الفديو...**")
                query = m.text.split(None, 1)[1]
                search = ytsearch(query)
                Q = 720
                amaze = HighQualityVideo()
                if search == 0:
                    await loser.edit("❌ **لم يتم العثور على نتائج.**")
                else:
                    songname = search[0]
                    url = search[1]
                    veez, ytlink = await ytdl(url)
                    if veez == 0:
                        await loser.edit(f"❌ yt-dl **تم الكشف عن مشاكل**\n\n» `{ytlink}`")
                    else:
                        if chat_id in QUEUE:
                            pos = add_to_queue(
                                chat_id, songname, ytlink, url, "Video", Q
                            )
                            await loser.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_1}",
                                caption=f"📽️ **Song Added to Queue »** `{pos}`\n📮 **Name:** [{songname[:10]}]({url})\n🔋 **Required By:** {requester}",
                                reply_markup=keyboard,
                            )
                        else:
                            try:
                                await loser.edit("🔄 **جاري تشغيل الفديو...**")
                                await call_py.join_group_call(
                                    chat_id,
                                    AudioVideoPiped(
                                        ytlink,
                                        HighQualityAudio(),
                                        amaze,
                                    ),
                                    stream_type=StreamType().local_stream,
                                )
                                add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                                await loser.delete()
                                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                                await m.reply_photo(
                                    photo=f"{IMG_2}",
                                    caption=f"📽️ **Video Streaming Started.**\n📮 **Name:** [{songname[:10]}]({url})\n\n🚨 **Status:** `Playing`\n🔋 **Required By:** {requester}",
                                    reply_markup=keyboard,
                                )
                            except Exception as ep:
                                await loser.delete()
                                await m.reply_text(f"🚫 هناك خطأ: `{ep}`")

    else:
        if len(m.command) < 2:
            await m.reply(
                    "**» الرد على الفديو او إعطاء شيء للبحث.**"
                )
        else:
            loser = await c.send_message(chat_id, "🔎 **يتم البحث عن الفديو...**")
            query = m.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            amaze = HighQualityVideo()
            if search == 0:
                await loser.edit("❌ **لم يتم العثور على نتائج.**")
            else:
                songname = search[0]
                url = search[1]
                veez, ytlink = await ytdl(url)
                if veez == 0:
                    await loser.edit(f"❌ yt-dl **تم الكشف عن مشاكل**\n\n» `{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await loser.delete()
                        requester = (
                            f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                        )
                        await m.reply_photo(
                            photo=f"{IMG_1}",
                            caption=f"📽️ **Track added to queue »** `{pos}`\n📮 **Name:** [{songname[:10]}]({url})\n🔋 **Required By:** {requester}",
                            reply_markup=keyboard,
                        )
                    else:
                        try:
                            await loser.edit("🔄 **جاري تشغيل الفديو...**")
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(
                                    ytlink,
                                    HighQualityAudio(),
                                    amaze,
                                ),
                                stream_type=StreamType().local_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await loser.delete()
                            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                            await m.reply_photo(
                                photo=f"{IMG_2}",
                                caption=f"📽️ **Video Streaming Started.**\n📮 **Name:** [{songname[:10]}]({url})\n\n🚨 **Status:** `Playing`\n🔋 **Request By:** {requester}",
                                reply_markup=keyboard,
                            )
                        except Exception as ep:
                            await loser.delete()
                            await m.reply_text(f"🚫 **هناك خطأ: `{ep}`")


@Client.on_message(command(["vstream", f"vstream@{BOT_USERNAME}"]) & other_filters)
async def vstream(c: Client, m: Message):
    m.reply_to_message
    chat_id = m.chat.id
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("- Dev Bot .", url=f"https://t.me/libcubehawk"),
                InlineKeyboardButton("- Channel .", url=f"https://t.me/{GROUP_SUPPORT}"),
            ]
        ]
    )
    if m.sender_chat:
         return await m.reply_text("**Your An __Anonymous Admin__ !\n\n» Revert Back To User Account From Rights.**")
    try:
        aing = await c.get_me()
    except Exception as e:
        return await m.reply_text(f"*هناك خطأ**:\n\n{e}")
    a = await c.get_chat_member(chat_id, aing.id)
    if a.status != "administrator":
        await m.reply_text(
            f"📽️ لاستخدامي ، أحتاج إلى أن أكون مسؤولاً مع الإذن التالي‌‌**:\n\n» ❌ __حذف الرسائل__\n» ❌ __تقييد المستخدمين__\n» ❌ __اضافه المستخدمين__\n» ❌ __أداره المحادثات الصوتيه__\n\nيتم تحديث البيانات تلقائيًا بعد ترقيتي‌‌"
        )
        return
    if not a.can_manage_voice_chats:
        await m.reply_text(
            "**يرجي اعطائي الصلاحيه التاليه:**" + "\n\n» ❌ **__أداره المحادثات الصوتيه__**"
        )
        return
    if not a.can_delete_messages:
        await m.reply_text(
            "**يرجي اعطائي الصلاحيه التاليه:**" + "\n\n» ❌ **__حذف الرسائل__**"
        )
        return
    if not a.can_invite_users:
        await m.reply_text("**الإذن المطلوب مفقود**:" + "\n\n» ❌ **__اضافه المستخدمين__**")
        return
    try:
        ubot = (await user.get_me()).id
        b = await c.get_chat_member(chat_id, ubot)
        if b.status == "kicked":
            await m.reply_text(
                f"@{ASSISTANT_NAME} **محظور في المجموعة** {m.chat.title}\n\n» **قم بإلغاء حظر الحساب المساعد اولاً إذا كنت تريد استخدام هذا البوت.**"
            )
            return
    except UserNotParticipant:
        if m.chat.username:
            try:
                await user.join_chat(m.chat.username)
            except Exception as e:
                await m.reply_text(f"❌ **فشل انضمام الحساب المساعد**\n\n**السبب**: `{e}`")
                return
        else:
            try:
                user_id = (await user.get_me()).id
                link = await c.export_chat_invite_link(chat_id)
                if "+" in link:
                    link_hash = (link.replace("+", "")).split("t.me/")[1]
                    await ubot.join_chat(link_hash)
                await c.promote_member(chat_id, user_id)
            except UserAlreadyParticipant:
                pass
            except Exception as e:
                return await m.reply_text(
                    f"❌ **فشل انضمام الحساب المساعد**\n\n**السبب**: `{e}`"
                )

    if len(m.command) < 2:
        await m.reply("» give me a live-link/m3u8 url/youtube link to stream.")
    else:
        if len(m.command) == 2:
            link = m.text.split(None, 1)[1]
            Q = 720
            loser = await c.send_message(chat_id, "🔄 **Processing Stream...**")
        elif len(m.command) == 3:
            op = m.text.split(None, 1)[1]
            link = op.split(None, 1)[0]
            quality = op.split(None, 1)[1]
            if quality == "720" or "480" or "360":
                Q = int(quality)
            else:
                Q = 720
                await m.reply(
                    "**» __Only 720, 480, 360 Allowed__ **\n📽️ **Now Streaming video in 720p**"
                )
            loser = await c.send_message(chat_id, "🔄 **Processing Stream...**")
        else:
            await m.reply("**/vstream {link} {720/480/360}**")

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, link)
        if match:
            asad, livelink = await ytdl(link)
        else:
            livelink = link
            asad = 1

        if asad == 0:
            await loser.edit(f"❌ yt-dl ****\n\n» `{livelink}`")
        else:
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, "Live Stream", livelink, link, "Video", Q)
                await loser.delete()
                requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                await m.reply_photo(
                    photo=f"{IMG_1}",
                    caption=f"📽️ **Track added to queue »** `{pos}`\n\n🔋 **Required By:** {requester}",
                    reply_markup=keyboard,
                )
            else:
                if Q == 720:
                    amaze = HighQualityVideo()
                elif Q == 480:
                    amaze = MediumQualityVideo()
                elif Q == 360:
                    amaze = LowQualityVideo()
                try:
                    await loser.edit("🔄 **يتم تشغيل الفديو...**")
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(
                            livelink,
                            HighQualityAudio(),
                            amaze,
                        ),
                        stream_type=StreamType().live_stream,
                    )
                    add_to_queue(chat_id, "Live Stream", livelink, link, "Video", Q)
                    await loser.delete()
                    requester = (
                        f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
                    )
                    await m.reply_photo(
                        photo=f"{IMG_2}",
                        caption=f"📽️ **[Video Live]({link}) Stream Startes.**\n\n💭 **Chat:** `{chat_id}`\n\n🚨 **Status:** `Playing`\n🔋 **Request By:** {requester}",
                        reply_markup=keyboard,
                    )
                except Exception as ep:
                    await loser.delete()
                    await m.reply_text(f"🚫 **هناك خطأ**: `{ep}`")
