# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# Thanks Man-Userbot for autobot
""" Userbot start point """

from importlib import import_module
from sys import argv
from platform import python_version

from telethon import version
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import ALIVE_NAME, BOT_VER, LOGS, BOT_TOKEN, BOT_USERNAME, BOTLOG_CHATID, bot
from userbot.modules import ALL_MODULES
from userbot.utils import autobot
from userbot.pytgcalls import call_py
from userbot.utils.botlog import verifyLoggerGroup


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'



try:
    bot.start()
    call_py.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

if not BOTLOG_CHATID:
    bot.loop.run_until_complete(verifyLoggerGroup())

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

    LOGS.info(
        f"Python Version - {python_version()} \
          \nTelethon Version - {version.__version__} \
          \nUserbot Version - {BOT_VER} \
          \n✘ 𝐅𝐥𝐢𝐜𝐤𝐬 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 ✘ [Berhasil Diaktifkan 🔥]")


    try:
        bot(JoinChannelRequest("@TheFlicksUserbot"))
    except BaseException:
        pass
    try:
        bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
