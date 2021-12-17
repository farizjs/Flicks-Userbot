# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import ALIVE_NAME, BOT_VER, LOGS, bot
from userbot.modules import ALL_MODULES
from telethon.tl.functions.channels import JoinChannelRequest


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


LOGS.info(
    f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"
    f"\n✘ 𝐅𝐥𝐢𝐜𝐤𝐬 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 ✘ v{BOT_VER} ⚙️ [Berhasil Diaktifkan 🔥]"
    f"\nSelamat memakai saya tuan {ALIVE_NAME}"
    f"\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

   except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@InfoFlicksUserbot"))
    except BaseException:
        pass


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
