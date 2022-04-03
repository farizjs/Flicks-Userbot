#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Recode by Fariz <Flicks-Userbot>

import asyncio
import html
import os
import re
from math import ceil

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest

from userbot import ALIVE_NAME, CMD_HELP, CMD_LIST, bot, tgbot, PMPERMIT_PIC, BOT_USERNAME, BOTLOG_CHATID

TELEPIC = PMPERMIT_PIC

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
user = bot.get_me()
myid = user.id
mybot = BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = BOTLOG_CHATID
CUSTOM_PMPERMIT = None
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`Keamanan Userbot PM! Tolong tunggu saya untuk menyetujui Anda. 😊"
)
DEFAULTUSER = user.first_name
USER_BOT_WARN_ZERO = "`Saya telah memperingatkan Anda untuk tidak melakukan spam. Sekarang Anda telah diblokir dan dilaporkan hingga pemberitahuan lebih lanjut.`\n\n**Selamat tinggal!** "

LOAD_MYBOT = "True"

if LOAD_MYBOT == "True":
    USER_BOT_NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n\n"
        "Untuk bantuan segera, PM saya melalui {}"
        "\nSilakan pilih mengapa Anda ada di sini, dari opsi yang tersedia\n\n".format(
            DEFAULTUSER, myid, MESAG, botname
        )
    )
elif LOAD_MYBOT == "False":
    USER_BOT_NO_WARN = (
        "**PM Security of [{}](tg://user?id={})**\n\n"
        "{}\n"
        "\nPlease choose why you are here, from the available options\n".format(
            DEFAULTUSER, myid, MESAG
        )
    )


    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == myid and query.startswith("Pmpermit"):
            TELEBT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=TELEPIC,
                text=TELEBT,
                buttons=[
                    [
                        custom.Button.inline("Meminta ", data="req"),
                        custom.Button.inline("Chat 💭", data="chat"),
                    ],
                    [custom.Button.inline("untuk spam 🚫", data="heheboi")],
                    [custom.Button.inline("Apa ini ❓", data="pmclick")],
                ],
            )
        await event.answer([result] if result else None)


    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmclick")))
    async def on_pm_click(event):
        if event.query.user_id == myid:
            reply_pop_up_alert = "Ini bukan untukmu, tuan!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Ini adalah Keamanan PM untuk {DEFAULTUSER} untuk menjauhkan spammer.\n\nDilindungi oleh [Userbot](t.me/FlicksSupport)"
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == myid:
            reply_pop_up_alert = "Ini bukan untukmu, tuan!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"baik, `{DEFAULTUSER}` akan segera menghubungi Anda!\nSampai saat itu mohon **tunggu dengan sabar dan jangan spam di sini.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) sedang **meminta** sesuatu di PM!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == myid:
            reply_pop_up_alert = "Ini bukan untukmu, tuan!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"wah, mau ngobrol...\nHarap tunggu dan lihat apakah {DEFAULTUSER} sedang dalam mood untuk mengobrol, jika ya, dia akan segera membalas!\nSampai saat itu, **jangan spam.**"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) ingin PM Anda untuk ** Obrolan Acak**!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"plshelpme")))
    async def on_pm_click(event):
        if event.query.user_id == myid:
            reply_pop_up_alert = "Ini bukan untukmu, tuan!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oh!\n{DEFAULTUSER} dengan senang hati akan membantu Anda...\nSilakan tinggalkan pesan Anda di sini **dalam satu baris** dan tunggu sampai saya membalas 😊"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) ingin PM Anda untuk **bantuan**!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"heheboi")))
    async def on_pm_click(event):
        if event.query.user_id == myid:
            reply_pop_up_alert = "Ini bukan untukmu, tuan!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oh, jadi Anda di sini untuk spam 😤\nSelamat tinggal.\nPesan Anda telah dibaca dan berhasil diabaikan."
            )
            await borg(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await tgbot.send_message(
                LOG_GP,
                f"[{first_name}](tg://user?id={ok}) tried to **spam** your inbox.\nHenceforth, **blocked**",
            )


async def userinfo(event):
    target = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(target.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
