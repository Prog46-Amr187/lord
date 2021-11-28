# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit


from rocksdriver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
    MY_BRO,
    REPO_OWNER,
    MY_SERVER,
    BOT_UPDATE,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await message.reply_text(
        f"""<b>✨ **Welcome {message.from_user.mention} Sweet Heart How Are You!** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Aɢᴀʀ ᴀᴘᴋᴏ ᴠᴄ ᴘᴇʏ sᴏɴɢ ᴘʟᴀʏ ᴋᴀʀɴᴇʏ ʜᴀɪɴ ᴛᴏ ᴍᴜᴊʜᴇʏ ᴀᴘɴᴇʏ ɢʀᴏᴜᴘ ᴍᴀɪɴ ᴀᴅᴍɪɴ ʙᴀɴᴀ ᴅᴏ ᴠᴄ ʀɪɢʜᴛ ᴋᴇʏ sᴀᴛʜ ᴀᴜʀ /join ᴋɪ ᴄᴏᴍᴍᴀɴᴅ ᴅᴀʟᴀɪɴ ᴀɢᴀʀ ғɪʀ ʙʜɪ ɪssᴜ ʜᴀɪ ᴛᴏ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ ᴛᴏ 👉 [ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/{REPO_OWNER}) ᴏʀ [ᴅᴇᴠᴇʟᴏᴘᴇʀ ʙʀᴏ](https://t.me/{MY_BRO})**

 👨‍🔧 **Tʜɪs ᴡɪʟʟ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴏɴʟʏ ᴠɪᴅᴇᴏ ᴍᴜsɪᴄ ᴏɴ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠᴄ ᴄʜᴀᴛ ɢʀᴏᴜᴘ**

💡 **Find ᴏᴜᴛ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜɪs ʙᴜᴛᴛᴏɴ. ᴍᴀᴅᴇ ᴡɪᴛʜ ❤️ .👉 » 📚 Cᴏᴍᴍᴀɴᴅs Bᴜᴛᴛᴏɴ 📚 **

❔ **How ᴛᴏ ᴜsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜɪs ʙᴜᴛᴛᴏɴ...👉  » ❓ Bᴀsɪᴄ Gᴜɪᴅᴇ Button!** 
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⚙️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("👩‍💻 ʙᴀsɪᴄ Gᴜɪᴅᴇ👩‍💻 ", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 ᴜᴘᴅᴀᴛᴇs 📚", url=f"https://t.me/{BOT_UPDATE}"),
                    InlineKeyboardButton("💝 ᴏᴡɴᴇʀ 💝", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [ 
                    InlineKeyboardButton(
                        "👥 ɢʀᴏᴜᴘ 👥︎", url=f"https://t.me/{GROUP_SUPPORT}"),
                    InlineKeyboardButton(
                        "📣 cʜᴀɴɴᴇʟ 📣", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "👑 kɪɴɢ 👑", url="https://t.me/Dr_Asad_Ali"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **ʙᴀsɪᴄ ɢᴜɪᴅᴇ ᴀᴛ** [ʀᴏᴄᴋs sᴇʀᴠᴇʀ](https://t.me/{MY_SERVER})

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /join to invite her.**
4.) **Turn on the video chat first before start to play video.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /join again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**


» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} 

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /join - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("**ʏᴏᴜ'ʀᴇ ᴀɴ Aɴᴏɴʏᴍᴏᴜs Aᴅᴍɪɴ !**\n\n**» ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.**")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 **ᴄʜᴏᴢᴇʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ !**", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **sᴇᴛᴛɪɴɢs ᴏғ** {query.message.chat.title}\n\n⏸ : **ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ**\n▶️ : **ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ**\n🔇 : **ᴍᴜᴛᴇ ᴜsᴇʀʙᴏᴛ**n🔊 : **ᴜɴᴍᴜᴛᴇ ᴜsᴇʀʙᴏᴛ**\n⏹ : **ᴇɴᴅ sᴛʀᴇᴀᴍ**",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 ᴄʟᴏsᴇ", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ **ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ**", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 **ᴄʜᴏᴢᴇʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ !**!", show_alert=True)
    await query.message.delete()