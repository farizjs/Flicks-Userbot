# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from platform import uname
from userbot.utils import flicks_cmd
from userbot import CMD_HANDLER as cmd

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@flicks_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(f"**Module** `{args}` **Tidak tersedia🚶**")
            await asyncio.sleep(6)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t|  "
        await event.edit("**✨𝐅𝐥𝐢𝐜𝐤𝐬-𝐔𝐬𝐞𝐫𝐛𝐨𝐭​✨**\n\n"
                         f"**❒ Bᴏᴛ ᴏꜰ {DEFAULTUSER} **\n**❒ Mᴏᴅᴜʟᴇꜱ : {len(modules)}**\n\n"
                         "**❒ Mᴀɪɴ Mᴇɴᴜ :**\n"
                         f"◉| {string}◉\n\n"
                         f"\n**Contoh** : Ketik <`{cmd}help offline`> Untuk Informasi Pengunaan Perintah.\nAtau Bisa Juga Ketik `{cmd}helpme` Untuk Main Menu Yang Lain-Nya.")
        await asyncio.sleep(360)
        await event.delete()
