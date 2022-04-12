# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot module containing commands for interacting with dogbin(https://del.dog)"""

import os
from requests import get, post, exceptions
from userbot import BOTLOG_CHATID, BOT_USERNAME, CMD_HELP, CMD_HANDLER, TEMP_DOWNLOAD_DIRECTORY
from userbot.utils import flicks_cmd

DOGBIN_URL = "https://del.dog/"


@flicks_cmd(pattern="paste(?: |$)([\s\S]*)")
async def paste(pstl):
    """ For .paste command, pastes the text directly to dogbin. """
    dogbin_final_url = ""
    match = pstl.pattern_match.group(1).strip()
    reply_id = pstl.reply_to_msg_id

    if not (match or reply_id):
        return await pstl.edit("`Elon Musk berkata saya tidak bisa menempelkan kekosongan Master....⚡.`")

    if match:
        message = match
    elif reply_id:
        message = await pstl.get_reply_message()
        if message.media:
            downloaded_file_name = await pstl.client.download_media(
                message, TEMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8")
            os.remove(downloaded_file_name)
        else:
            message = message.message

    # Dogbin
    await pstl.edit("`Menempelkan teks . . .🚀`")
    resp = post(DOGBIN_URL + "documents", data=message.encode("utf-8"))

    if resp.status_code == 200:
        response = resp.json()
        key = response["key"]
        dogbin_final_url = DOGBIN_URL + key

        if response["isUrl"]:
            reply_text = (
                "`Berhasil ditempel!`\n\n"
                f"[Shortened URL]({dogbin_final_url})\n\n"
                "`Original(non-shortened) URLs`\n"
                f"[Dogbin URL]({DOGBIN_URL}v/{key})\n"
                f"[View RAW]({DOGBIN_URL}raw/{key})"
            )
        else:
            reply_text = (
                "`Berhasil ditempel!`\n\n"
                f"[Dogbin URL]({dogbin_final_url})\n"
                f"[View RAW]({DOGBIN_URL}raw/{key})"
            )
    else:
        reply_text = "`Gagal menjangkau Dogbin`"

    await pstl.edit(reply_text)
    if BOTLOG_CHATID:
        await pstl.client.send_message(
            BOTLOG_CHATID, "Kueri tempel berhasil dijalankan",
        )
    q = f"pasta-{key}"
    reply_text = (
        "`Berhasil ditempel!`\n\n"
        f"[Dogbin URL]({dogbin_final_url})\n"
        f"[View RAW]({DOGBIN_URL}raw/{key})"
    )
    try:
        ok = await bot.inline_query(BOT_USERNAME, q)
        await ok[0].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
        await xx.delete()
    except BaseException:
        await xx.edit(reply_text)


CMD_HELP.update(
    {
        "paste": f"**•Plugin :** `Paste`\
        \n\n  •  **•Perintah :** `{CMD_HANDLER}paste` <text/reply>\
        \n  •  **•Function : **Untuk Menyimpan text ke ke layanan Nekobin \
    "
    }
)
