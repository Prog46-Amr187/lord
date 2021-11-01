# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit
 

from cache.admins import admins
from rocksdriver.asad import call_py
from pyrogram import Client, filters
from rocksdriver.decorators import authorized_users_only
from rocksdriver.filters import command, other_filters
from rocksdriver.queues import QUEUE, clear_queue
from rocksdriver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.

@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        f"""**━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ @Dr_Asad_Ali's ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴠɪᴅᴇᴏ & ᴀᴜᴅɪᴏ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.
┏━━━━━━━━━━━━━━━━━┓
┣★ ʙᴏᴛ : [ʀᴇʟᴏᴀᴅᴇᴅ](https://t.me/Asad_Music_Bot)
┣★ ᴀᴅᴍɪɴ : [ʀᴇғʀᴇsʜᴇᴅ](https://t.me/Shayri_Music_Lovers)
┣★ sᴜᴘᴘᴏʀᴛ : [ʙᴏᴛ ᴜᴘᴅᴀᴛᴇs](https://t.me/AsadSupport)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ » ǫᴜᴇsᴛɪᴏɴ
ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/Dr_Asad_Ali).
━━━━━━━━━━━━━━━━━━━**""",
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❤️ ʜᴇᴀʀᴛ", url=f"https://t.me/Give_Me_Heart"),
                    InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url=f"https://t.me/Dr_Asad_Ali"),
                ],
                [
                    InlineKeyboardButton(
                        "👨‍👨‍👧‍👦 Gʀᴏᴜᴘ 👨‍👨‍👧‍👦", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],
            ]
        )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ **ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ ᴘʟᴀʏɪɴɢ..😊**")
        elif op == 1:
            await m.reply("✅ __Qᴜᴇᴜᴇs__ ɪs ᴇᴍᴘᴛʏ.\n\n• **ᴜsᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ**")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **Sᴋɪᴘᴘᴇᴅ ɴᴏᴡ ᴘʟᴀʏɪɴɢ ❤️.**\n\n🏷 **Nᴀᴍᴇ:** [{op[0]}]({op[1]})\n💡 **Sᴛᴀᴛᴜs:** `Playing`\n🎧 **Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ:** {m.from_user.mention()}\nVia [Asᴀᴅ ᴀʟɪ sᴇʀᴠᴇʀ](https://t.me/Give_Me_Heart)",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **Sᴏɴɢ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ǫᴜᴇᴜᴇ:**"
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
            await m.reply("✅ **Sᴏɴɢ ᴇɴᴅ ǫᴜᴇ ᴋɪʏᴀ ʙᴇ ᴀᴜʀ ᴋᴏᴇ ᴋᴀᴀᴍ ɴᴀɪ ʜᴀɪ...**")
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ..😔**")


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
                "⏸ **Sᴏɴɢ ᴘᴀᴜsᴇᴅ.**\n\n• **Tᴏ ʀᴇsᴜᴍᴇ ᴛʜᴇ sᴏɴɢ, ᴜsᴇ ᴛʜᴇ**\n» /resume ᴄᴏᴍᴍᴀɴᴅ."
            )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀ**\n\n`{e}`")
    else:
        await m.reply("❌ **Nᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ..😔**")


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
                "▶️ **Sᴏɴɢ ʀᴇsᴜᴍᴇᴅ.**\n\n• **Tᴏ ᴘᴀᴜsᴇ ᴛʜᴇ sᴏɴɢ, ᴜsᴇ ᴛʜᴇ**\n» /pause ᴄᴏᴍᴍᴀɴᴅ."
            )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀr:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ..😔**")


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
                "🔇 **Usᴇʀʙᴏᴛ ᴍᴜᴛᴇ ʜᴏ ɢᴀʏᴀ.**\n\n• **Tᴏ ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ, ᴜsᴇ ᴛʜᴇ**\n» /unmute ᴄᴏᴍᴍᴀɴᴅ."
            )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ...**")


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
                "🔊 **Usᴇʀʙᴏᴛ ᴜɴᴍᴜᴛᴇ ʜᴏ ɢᴀʏᴀ.**\n\n• **Tᴏ ᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ, ᴜsᴇ ᴛʜᴇ**\n» /mute ᴄᴏᴍᴍᴀɴᴅ."
            )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ..😔**")


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo. Asad Ali

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
                f"✅ **Vᴏʟᴜᴍᴇ sᴇᴛ ᴛᴏ** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **Eʀʀᴏʀ:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ😉..**")
