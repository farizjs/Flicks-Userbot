# Credits: @mrconfused
# Recode by @farizjs
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot
import re

from telethon.utils import get_display_name
from telethon import events

from userbot.utils import edit_or_reply, flicks_cmd
from .sql_helper.filter_sql import (
    add_filter,
    get_filters,
    remove_all_filters,
    remove_filter,
)
from userbot import BOTLOG, BOTLOG_CHATID, bot, CMD_HELP, CMD_HANDLER as cmd

user = bot.get_me()
OWNER_ID = user.id

@bot.on(events.NewMessage(incoming=True))
async def filter_incoming_handler(event):  # sourcery no-metrics
    if event.sender_id == OWNER_ID:
        return
    name = event.raw_text
    filters = get_filters(event.chat_id)
    if not filters:
        return
    a_user = await event.get_sender()
    chat = await event.get_chat()
    me = await event.client.get_me()
    title = get_display_name(await event.get_chat()) or "this chat"
    participants = await event.client.get_participants(chat)
    count = len(participants)
    mention = f"[{a_user.first_name}](tg://user?id={a_user.id})"
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    first = a_user.first_name
    last = a_user.last_name
    fullname = f"{first} {last}" if last else first
    username = f"@{a_user.username}" if a_user.username else mention
    userid = a_user.id
    my_first = me.first_name
    my_last = me.last_name
    my_fullname = f"{my_first} {my_last}" if my_last else my_first
    my_username = f"@{me.username}" if me.username else my_mention
    for trigger in filters:
        pattern = r"( |^|[^\w])" + re.escape(trigger.keyword) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            file_media = None
            filter_msg = None
            if trigger.f_mesg_id:
                msg_o = await event.client.get_messages(
                    entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id)
                )
                file_media = msg_o.media
                filter_msg = msg_o.message
                link_preview = True
            elif trigger.reply:
                filter_msg = trigger.reply
                link_preview = False
            await event.reply(
                filter_msg.format(
                    mention=mention,
                    title=title,
                    count=count,
                    first=first,
                    last=last,
                    fullname=fullname,
                    username=username,
                    userid=userid,
                    my_first=my_first,
                    my_last=my_last,
                    my_fullname=my_fullname,
                    my_username=my_username,
                    my_mention=my_mention,
                ),
                file=file_media,
                link_preview=link_preview,
            )


@flicks_cmd(pattern="filter (.*)")
async def add_new_filter(event):
    "To save the filter"
    keyword = event.pattern_match.group(1)
    string = event.text.partition(keyword)[2]
    msg = await event.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#FILTER\
            \nCHAT ID: {event.chat_id}\
            \nPEMICU: {keyword}\
            \n\nPesan berikut disimpan sebagai data balasan filter untuk obrolan, mohon JANGAN dihapus !!",
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                event,
                "__Menyimpan media sebagai balasan ke filter memerlukan __ `BOTLOG_CHATID` __untuk disetel.__",
            )
            return
    elif msg and msg.text and not string:
        string = msg.text
    elif not string:
        return await edit_or_reply(event, "__Apa yang harus saya lakukan ?__")
    success = "`Filter` **{}** `{} successfully`"
    if add_filter(str(event.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(event, success.format(keyword, "added"))
    remove_filter(str(event.chat_id), keyword)
    if add_filter(str(event.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(event, success.format(keyword, "Updated"))
    await edit_or_reply(event, f"Kesalahan saat menyetel filter untuk {keyword}")


@flicks_cmd(pattern="filters$")
async def on_snip_list(event):
    "To list all filters in that chat."
    OUT_STR = "Tidak ada filter dalam obrolan ini."
    filters = get_filters(event.chat_id)
    for filt in filters:
        if OUT_STR == "Tidak ada filter dalam obrolan ini.":
            OUT_STR = "Filter aktif dalam obrolan ini:\n"
        OUT_STR += "👉 `{}`\n".format(filt.keyword)
    await edit_or_reply(
        event,
        OUT_STR,
        caption="Filter yang Tersedia di Obrolan Saat Ini",
        file_name="filters.text",
    )


@flicks_cmd(pattern="stop ([\s\S]*)")
async def remove_a_filter(event):
    "Stops the specified keyword."
    filt = event.pattern_match.group(1)
    if not remove_filter(event.chat_id, filt):
        await event.edit("Filter` {} `tidak ada.".format(filt))
    else:
        await event.edit("Filter `{} `berhasil dihapus".format(filt))


@flicks_cmd(pattern="rmfilters$")
async def on_all_snip_delete(event):
    "To delete all filters in that group."
    filters = get_filters(event.chat_id)
    if filters:
        remove_all_filters(event.chat_id)
        await edit_or_reply(event, "filter dalam obrolan saat ini berhasil dihapus")
    else:
        await edit_or_reply(event, "Tidak ada filter di grup ini")

CMD_HELP.update({
    "filter":
    f"`{cmd}filters`\
    \nUsage: Melihat filter userbot yang aktif di obrolan.\
    \n\n`{cmd}filter` <keyword> <balasan> atau balas ke pesan ketik .filter <keyword>\
    \nUsage: Membuat filter di obrolan.\
    \nBot Akan Membalas Jika Ada Yang Menyebut 'keyword' yang dibuat.\
    \nBisa dipake ke media/sticker/vn/file.\
    \n\n`{cmd}rmfilters` <keyword>\
    \nUsage: Untuk Nonaktifkan Filter."
})
