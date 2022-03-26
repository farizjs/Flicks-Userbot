# Credits: @mrconfused
# Recode by @farizjs
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot

from userbot.utils import reply_id, edit_delete, edit_or_reply, flicks_cmd
from .sql_helper.notes_sql import add_note, get_note, get_notes, rm_note
from userbot import BOTLOG, BOTLOG_CHATID, bot, CMD_HELP, CMD_HANDLER as i

async def get_message_link(client, event):
    chat = await event.get_chat()
    if event.is_private:
        return f"tg://openmessage?user_id={chat.id}&message_id={event.id}"
    return f"https://t.me/c/{chat.id}/{event.id}"


@flicks_cmd(pattern="\#(\S+)")
async def incom_note(event):
    if not BOTLOG:
        return
    try:
        if not (await event.get_sender()).bot:
            notename = event.text[1:]
            notename = notename.lower()
            note = get_note(notename)
            message_id_to_reply = await reply_id(event)
            if note:
                if note.f_mesg_id:
                    msg_o = await event.client.get_messages(
                        entity=BOTLOG_CHATID, ids=int(note.f_mesg_id)
                    )
                    await event.delete()
                    await event.client.send_message(
                        event.chat_id,
                        msg_o,
                        reply_to=message_id_to_reply,
                        link_preview=False,
                    )
                elif note.reply:
                    await event.delete()
                    await event.client.send_message(
                        event.chat_id,
                        note.reply,
                        reply_to=message_id_to_reply,
                        link_preview=False,
                    )
    except AttributeError:
        pass


@flicks_cmd(pattern="save (\w*)")
async def add_snip(event):
    "To save notes to bot."
    if not BOTLOG:
        return await edit_delete(
            event, "`Untuk menyimpan snip atau catatan, Anda perlu mengatur BOTLOG_CHATID`"
        )
    keyword = event.pattern_match.group(1)
    string = event.text.partition(keyword)[2]
    msg = await event.get_reply_message()
    msg_id = None
    keyword = keyword.lower()
    if msg and not string:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#NOTE\
            \n**Keyword :** `#{keyword}`\
            \n\nPesan berikut disimpan sebagai snip di bot Anda, JANGAN dihapus !!",
        )
        msg_o = await event.client.forward_messages(
            entity=BOTLOG_CHATID, messages=msg, from_peer=event.chat_id, silent=True
        )
        msg_id = msg_o.id
    elif msg:
        return await edit_delete(
            event,
            "`Apa yang harus saya simpan untuk snip Anda, baik membalas atau memberikan teks snip bersama dengan kata kunci`",
        )
    if not msg:
        if string:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#NOTE\
            \n**Kata kunci :** `#{keyword}`\
            \n\nPesan berikut disimpan sebagai snip di bot Anda, JANGAN dihapus !!",
            )
            msg_o = await event.client.send_message(BOTLOG_CHATID, string)
            msg_id = msg_o.id
            string = None
        else:
            return await edit_delete(event, "`apa yang harus saya simpan untuk snip Anda?`")
    success = "Catatan {} berhasil {}. gunakan` #{} `untuk mendapatkan"
    if add_note(keyword, string, msg_id) is False:
        rm_note(keyword)
        if add_note(keyword, string, msg_id) is False:
            return await edit_or_reply(
                event, f"Kesalahan dalam menyimpan snip yang diberikan {keyword}"
            )
        return await edit_or_reply(event, success.format(keyword, "updated", keyword))
    return await edit_or_reply(event, success.format(keyword, "added", keyword))


@flicks_cmd(pattern="notes$")
async def on_snip_list(event):
    "To list all notes in bot."
    message = "Anda belum menyimpan catatan/snip"
    notes = get_notes()
    if not BOTLOG:
        return await edit_delete(
            event, "`Untuk menyimpan snip Anda harus mengatur BOTLOG_CHATID`"
        )
    for note in notes:
        if message == "Anda belum menyimpan catatan/snip":
            message = "Catatan yang disimpan di bot Anda adalah\n\n"
        message += f"👉 `#{note.keyword}`"
        if note.f_mesg_id:
            msglink = await get_message_link(BOTLOG_CHATID, note.f_mesg_id)
            message += f"  [preview]({msglink})\n"
        else:
            message += "  No preview\n"
    await edit_or_reply(event, message)


@flicks_cmd(pattern="clear (\S+)")
async def on_snip_delete(event):
    "To delete paticular note in bot."
    name = event.pattern_match.group(1)
    name = name.lower()
    catsnip = get_note(name)
    if catsnip:
        rm_note(name)
    else:
        return await edit_or_reply(
            event, f"Apakah kamu yakin itu? #{name} disimpan sebagai catatan?"
        )
    await edit_or_reply(event, f"`catatan #{name} berhasil dihapus`")

CMD_HELP.update({
    "notes":
    f"\
#<nama_catatan>\
\nUsage: Mendapat catatan yang ditentukan.\
\n\n`{i}save` <nama catatan> <catatan> atau balas pesan dengan {i}save <nama catatan>\
\nUsage: Menyimpan pesan balasan sebagai catatan dengan nama catatan. (Bekerja dengan foto, dokumen, dan stiker juga!)\
\n\n`{i}notes`\
\nUsage: Dapatkan semua catatan yang disimpan dalam obrolan.\
\n\n`{i}clear` <nama catatan>\
\nUsage: Menghapus catatan yang ditentukan."
})
