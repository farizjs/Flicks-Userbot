# Credits: mrconfused
# Recode by @farizjs
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot

from telethon.utils import get_display_name
from telethon import events

from userbot import bot, CMD_HELP, CMD_HANDLER as cmd
from .sql_helper.echo_sql import (
    addecho,
    get_all_echos,
    get_echos,
    is_echo,
    remove_all_echos,
    remove_echo,
    remove_echos,
)
from userbot.utils import get_user_from_event, edit_delete, edit_or_reply, flicks_cmd


@flicks_cmd(pattern="addecho$")
async def echo(event):
    "To echo the user messages"
    if event.reply_to_msg_id is None:
        return await edit_or_reply(
            event, "`Balas pesan Pengguna untuk menggemakan pesannya`"
        )
    flicksevent = await edit_or_reply(event, "`Adding Echo to user...`")
    user, rank = await get_user_from_event(event, flicksevent, nogroup=True)
    if not user:
        return
    reply_msg = await event.get_reply_message()
    chat_id = event.chat_id
    user_id = reply_msg.sender_id
    if event.is_private:
        chat_name = user.first_name
        chat_type = "Personal"
    else:
        chat_name = get_display_name(await event.get_chat())
        chat_type = "Group"
    user_name = user.first_name
    user_username = user.username
    if is_echo(chat_id, user_id):
        return await edit_or_reply(event, "Pengguna sudah diaktifkan dengan echo ")
    try:
        addecho(
            chat_id,
            user_id,
            chat_name,
            user_name,
            user_username,
            chat_type)
    except Exception as e:
        await edit_delete(flicksevent, f"**Error:**\n`{e}`")
    else:
        await edit_or_reply(flicksevent, "Hi")


@flicks_cmd(pattern="rmecho$")
async def echo(event):
    "To stop echoing the user messages"
    if event.reply_to_msg_id is None:
        return await edit_or_reply(
            event, "Balas pesan Pengguna untuk menggemakan pesannya"
        )
    reply_msg = await event.get_reply_message()
    user_id = reply_msg.sender_id
    chat_id = event.chat_id
    if is_echo(chat_id, user_id):
        try:
            remove_echo(chat_id, user_id)
        except Exception as e:
            await edit_delete(flicksevent, f"**Error:**\n`{e}`")
        else:
            await edit_or_reply(event, "Echo telah dihentikan untuk pengguna")
    else:
        await edit_or_reply(event, "Pengguna tidak diaktifkan dengan echo")


@flicks_cmd(pattern="delecho( -a)?")
async def echo(event):
    "To delete echo in this chat."
    input_str = event.pattern_match.group(1)
    if input_str:
        lecho = get_all_echos()
        if len(lecho) == 0:
            return await edit_delete(
                event, "Anda belum mengaktifkan echo setidaknya untuk satu pengguna di obrolan apa pun."
            )
        try:
            remove_all_echos()
        except Exception as e:
            await edit_delete(event, f"**Error:**\n`{str(e)}`", 10)
        else:
            await edit_or_reply(
                event, "echo yang dihapus untuk semua pengguna yang diaktifkan di semua obrolan."
            )
    else:
        lecho = get_echos(event.chat_id)
        if len(lecho) == 0:
            return await edit_delete(
                event, "Anda belum mengaktifkan echo setidaknya untuk satu pengguna dalam obrolan ini."
            )
        try:
            remove_echos(event.chat_id)
        except Exception as e:
            await edit_delete(event, f"**Error:**\n`{e}`", 10)
        else:
            await edit_or_reply(
                event, "echo yang dihapus untuk semua pengguna yang diaktifkan dalam obrolan ini"
            )


@flicks_cmd(pattern="echolist( -a)?$")
async def echo(event):  # sourcery no-metrics
    "To list all users on who you enabled echoing."
    input_str = event.pattern_match.group(1)
    private_chats = ""
    output_str = "**Echo enabled users:**\n\n"
    if input_str:
        lsts = get_all_echos()
        group_chats = ""
        if len(lsts) <= 0:
            return await edit_or_reply(event, "Tidak ada pengguna yang mengaktifkan echo")
        for echos in lsts:
            if echos.chat_type == "Personal":
                if echos.user_username:
                    private_chats += (
                        f"☞ [{echos.user_name}](https://t.me/{echos.user_username})\n"
                    )
                else:
                    private_chats += (
                        f"☞ [{echos.user_name}](tg://user?id={echos.user_id})\n"
                    )
            elif echos.user_username:
                group_chats += f"☞ [{echos.user_name}](https://t.me/{echos.user_username}) dalam obrolan {echos.chat_name} dari id obrolan `{echos.chat_id}`\n"
            else:
                group_chats += f"☞ [{echos.user_name}](tg://user?id={echos.user_id}) dalam obrolan {echos.chat_name} dari id obrolan `{echos.chat_id}`\n"

        if private_chats != "":
            output_str += "**Private Chats**\n" + private_chats + "\n\n"
        if group_chats != "":
            output_str += "**Group Chats**\n" + group_chats
    else:
        lsts = get_echos(event.chat_id)
        if len(lsts) <= 0:
            return await edit_or_reply(
                event, "Tidak ada pengguna yang mengaktifkan echo dalam obrolan ini"
            )

        for echos in lsts:
            if echos.user_username:
                private_chats += (
                    f"☞ [{echos.user_name}](https://t.me/{echos.user_username})\n"
                )
            else:
                private_chats += (
                    f"☞ [{echos.user_name}](tg://user?id={echos.user_id})\n"
                )
        output_str = "**Pengguna yang mengaktifkan echo dalam obrolan ini adalah:**\n" + private_chats

    await edit_or_reply(event, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(event):
    if is_echo(event.chat_id, event.sender_id) and (
        event.message.text or event.message.sticker
    ):
        await event.reply(event.message)

CMD_HELP.update(
    {
        "echo":
        f"Perintah : `{cmd}addecho` \
    \nUsage : Untuk Menambahkan Followers Chat Kamu. \
    \nPerintah :`{cmd}delecho` \
    \nUsage : Untuk menghentikan echo. \
    \nPerintah :`{cmd}echolist`:\
    \nUsage: Untuk Melihat daftar penggunaan yang kamu echo."
    }
)
