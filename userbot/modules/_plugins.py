# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Credits King-Userbot <https://github.com/apisuserbot/King-Userbot>
# Ported by Flicks-Userbot
#
""" Userbot plugins command """

import asyncio
from userbot import ALIVE_NAME, UPSTREAM_REPO_BRANCH, BOT_VER, CMD_HELP, CMD_HANDLER as xd
from userbot.utils import flicks_cmd

plugins = CMD_HELP

@flicks_cmd(pattern="plugins")
async def help(event):
    """For plugins command,"""
    string = ""
    for i in CMD_HELP:
        string += "`" + str(i)
        string += f"`\t✘  "
    await event.edit(
            "**📙 Menu Help!**\n\n"
            f"**Master** {DEFAULTUSER}\n**◑» Plugins :** `{len(plugins)}`\n**◑» Branch :** __{UPSTREAM_REPO_BRANCH}__\n**◑» Versi Userbot :** `v{BOT_VER}`\n\n"
            f"**📚 Menu Help Inline** `{xd}help` \n\n"
            "**❒ Menu Plugin ↯**\n"
            f"╰►✘ {string} ◄─"
        )
    await event.reply(
            f"\n**Contoh : ketik** `{xd}help` <nama plugin> **Yang Sesuai Dengan Plugin Di Atas**\n\n**USERBOT TELEGRAM**"
        )
        await asyncio.sleep(2000)
        await event.delete()
