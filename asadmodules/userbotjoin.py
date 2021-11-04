# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad + Harshit


import asyncio
from config import BOT_USERNAME, SUDO_USERS
from rocksdriver.decorators import authorized_users_only, sudo_users_only, errors
from rocksdriver.filters import command, other_filters
from rocksdriver.asad import user as USER
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant


@Client.on_message(
    command(["join", f"join@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def join_group(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except BaseException:
        await message.reply_text(
            "• **I ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀ ᴘᴇʀᴍᴇssɪᴏɴ:**\n\n» ❌ __ᴀᴅᴅ ᴜsᴇʀs__",
        )
        return

    try:
        user = await USER.get_me()
    except BaseException:
        user.first_name = "music assistant"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 **Fʟᴏᴏᴅ ᴡᴀɪᴛ ᴇʀʀᴏʀ** 🛑 \n\n**Usᴇʀʙᴏᴛ ᴄᴀɴɴᴏᴛ ᴊᴏɪɴᴅ ʏᴏᴜʀ ᴄʜᴀᴛ ᴀᴅᴅ ᴀssɪsᴛᴀɴᴛ @{ASSISTANT_NAME} ᴍᴀɴᴜᴀʟʟʏ",
        )
        return
    await message.reply_text(
        f"✅ **Usᴇʀʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴊᴏɪɴᴅ ᴛʜᴇ ᴄʜᴀᴛ**",
    )


@Client.on_message(command(["userbotleave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leave_one(client, message):
    try:
        await USER.send_message(message.chat.id, "✅ **Usᴇʀʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴛʜᴇ ᴄʜᴀᴛ**")
        await USER.leave_chat(message.chat.id)
    except BaseException:
        await message.reply_text(
            "❌ **Fʟᴏᴏᴅ ᴡᴀɪᴛ ᴇʀʀᴏʀ.**\n\n**» Usᴇʀʙᴏᴛ ᴄᴀɴɴᴏᴛ ʟᴇᴀᴠᴇ ᴄʜᴀᴛ ᴋɪᴄᴋ ɪᴛ ᴍᴀɴᴜᴀʟʟʏ**"
        )

        return


# Roses are red, Violets are blue, A face like yours, Belongs in a zoo.

@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **Usᴇʀʙᴏᴛ** Lᴇᴀᴠɪɴɢ ᴀʟʟ ᴄʜᴀᴛs !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"**Usᴇʀʙᴏᴛ ʟᴇᴀᴠᴇ ᴀʟʟ ɢʀᴏᴜᴘ**...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"**Usᴇʀʙᴏᴛ ʟᴇᴀᴠɪɴɢ**...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ **Lᴇғᴛ ғʀᴏᴍ**: {left} chats.\n❌ Failed in: {failed} chats."
    )
