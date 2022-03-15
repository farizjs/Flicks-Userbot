from telethon import events, utils
from telethon.tl import types

from userbot import bot, tgbot
from userbot.modules.sql_helper.snips_sql import (
    add_snip,
    get_all_snips,
    get_snips,
    remove_snip,
)
from userbot.utils import asst_cmd

# ===================== Constants =====================
user = bot.get_me()
OWNER_ID = user.id
TYPE_TEXT = 0
TYPE_PHOTO = 1
TYPE_DOCUMENT = 2
MAX_MESSAGE_SIZE_LIMIT = 4095
# =====================================================

@asst_cmd(pattern=r"\#(\S+)")
async def on_snip(event):
    name = event.pattern_match.group(1)
    snip = get_snips(name)
    if snip:
        if snip.snip_type == TYPE_PHOTO:
            media = types.InputPhoto(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference,
            )
        elif snip.snip_type == TYPE_DOCUMENT:
            media = types.InputDocument(
                int(snip.media_id),
                int(snip.media_access_hash),
                snip.media_file_reference,
            )
        else:
            media = None
        message_id = event.message.id
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        await tgbot.send_message(
            event.chat_id, snip.reply, reply_to=message_id, file=media
        )


@asst_cmd(pattern="^/save$", from_users=OWNER_ID)
async def _(event):
    name = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if msg:
        snip = {"type": TYPE_TEXT, "text": msg.message or ""}
        if msg.media:
            media = None
            if isinstance(msg.media, types.MessageMediaPhoto):
                media = utils.get_input_photo(msg.media.photo)
                snip["type"] = TYPE_PHOTO
            elif isinstance(msg.media, types.MessageMediaDocument):
                media = utils.get_input_document(msg.media.document)
                snip["type"] = TYPE_DOCUMENT
            if media:
                snip["id"] = media.id
                snip["hash"] = media.access_hash
                snip["fr"] = media.file_reference
        add_snip(
            name,
            snip["text"],
            snip["type"],
            snip.get("id"),
            snip.get("hash"),
            snip.get("fr"),
        )
        await event.reply(
            "Catatan {name} berhasil disimpan. Dapatkan dengan #{name}".format(name=name)
        )
    else:
        await event.reply("Balas pesan dengan `snips keyword` untuk menyimpan snip")


@asst_cmd(pattern="^/notes")
async def on_snip_list(event):
    all_snips = get_all_snips()
    OUT_STR = "Available Snips:\n"
    if len(all_snips) > 0:
        for a_snip in all_snips:
            OUT_STR += f"➤ `#{a_snip.snip}` \n"
    else:
        OUT_STR = "Tidak ada Snip. Mulai Menyimpan menggunakan `/save`"
    if len(OUT_STR) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "snips.text"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Available Snips",
                reply_to=event,
            )
    else:
        await event.reply(OUT_STR)


@asst_cmd(pattern="^/rmnote (\S+)", from_users=OWNER_ID)
async def on_snip_delete(event):
    name = event.pattern_match.group(1)
    remove_snip(name)
    await event.reply("Catatan #{} berhasil dihapus".format(name))
