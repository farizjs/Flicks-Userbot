# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# Thanks Man-Userbot for autobot
""" Userbot start point """

from importlib import import_module
from sys import argv

from telethon import version
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import ALIVE_NAME, BOT_VER, LOGS, BOT_TOKEN, BOT_USERNAME, BOTLOG_CHATID, bot
from userbot.modules import ALL_MODULES
from userbot.utils import autobot



INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    user = bot.get_me()
    saya = f"{user.first_name}"
except BaseException:
    pass

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

    LOGS.info(f"Berhasil Login sebagai {saya}")
    LOGS.info(f"Python Version - 3.6")
    LOGS.info(f"Telethon Version - {version.__version__}")
    LOGS.info(f"Userbot Version - {BOT_VER}")
    LOGS.info(
        f"\n✘ 𝐅𝐥𝐢𝐜𝐤𝐬 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 ✘ [Berhasil Diaktifkan 🔥]")


    await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [f"@{BOT_USERNAME}"]))


if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
