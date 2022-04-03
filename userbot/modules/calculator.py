# Copyright (C) 2021 Ultroid <https://github.com/Teamultroid/Ultroid>
# Recode by @farizjs
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot

import re
from telethon import Button
from telethon.events import CallbackQuery, InlineQuery, NewMessage

from userbot import *
from userbot.utils import *

user = bot.get_me()
OWNER_ID = user.id
CALC = {}

m = [
    "AC",
    "C",
    "⌫",
    "%",
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "x",
    "00",
    "0",
    ".",
    "÷",
]
tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
lst.append([Button.inline("=", data="calc=")])


@flicks_cmd(pattern="calc")
async def icalc(e):
    if e.client._bot:
        return await e.reply("• Flicks Inline Calculator •", buttons=lst)
    results = await e.client.inline_query(BOT_USERNAME, "calc")
    await results[0].click(e.chat_id, silent=True, hide_via=True)
    await e.delete()


@tgbot.on(InlineQuery)  # pylint:disable=E0602
async def inline_handler(event):
    builder = event.builder
    result = None
    query = event.text
    if event.query.user_id == OWNER_ID and query.startswith("calc"):
        result = event.builder.article("Calc", text="Inline Calculator", buttons=lst)
    await event.answer([result])


@callback(data=re.compile(b"calc(.*)"))
async def _(e):
    if e.query.user_id == OWNER_ID:
        x = (e.data_match.group(1)).decode()
        user = e.query.user_id
        get = None
        if x == "AC":
            if CALC.get(user):
                CALC.pop(user)
            await e.edit(
                "• Flicks Inline Calculator •",
                buttons=[Button.inline("Buka Kalkulator Lagi", data="recalc")],
            )
        elif x == "C":
            if CALC.get(user):
                CALC.pop(user)
            await e.answer("cleared")
        elif x == "⌫":
            if CALC.get(user):
                get = CALC[user]
            if get:
                CALC.update({user: get[:-1]})
                await e.answer(str(get[:-1]))
        elif x == "%":
            if CALC.get(user):
                get = CALC[user]
            if get:
                CALC.update({user: get + "/100"})
                await e.answer(str(get + "/100"))
        elif x == "÷":
            if CALC.get(user):
                get = CALC[user]
            if get:
                CALC.update({user: get + "/"})
                await e.answer(str(get + "/"))
        elif x == "x":
            if CALC.get(user):
                get = CALC[user]
            if get:
                CALC.update({user: get + "*"})
                await e.answer(str(get + "*"))
        elif x == "=":
            if CALC.get(user):
                get = CALC[user]
            if get:
                if get.endswith(("*", ".", "/", "-", "+")):
                    get = get[:-1]
                out = eval(get)
                try:
                    num = float(out)
                    await e.answer(f"Answer : {num}", cache_time=0, alert=True)
                except BaseException:
                    CALC.pop(user)
                    await e.answer("Kesalahan", cache_time=0, alert=True)
            await e.answer("None")
        else:
            if CALC.get(user):
                get = CALC[user]
            if get:
                CALC.update({user: get + x})
                return await e.answer(str(get + x))
            CALC.update({user: x})
            await e.answer(str(x))

    else:
        reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
        await e.answer(reply_pop_up_alert, cache_time=0, alert=True)


@callback(data=re.compile(b"recalc"))
async def _(e):
    if e.query.user_id == OWNER_ID:
        m = [
            "AC",
            "C",
            "⌫",
            "%",
            "7",
            "8",
            "9",
            "+",
            "4",
            "5",
            "6",
            "-",
            "1",
            "2",
            "3",
            "x",
            "00",
            "0",
            ".",
            "÷",
        ]
        tultd = [Button.inline(f"{x}", data=f"calc{x}") for x in m]
        lst = list(zip(tultd[::4], tultd[1::4], tultd[2::4], tultd[3::4]))
        lst.append([Button.inline("=", data="calc=")])
        await e.edit("• Flicks Inline Calculator •", buttons=lst)

    else:
        reply_pop_up_alert = f"Kamu Tidak diizinkan, ini Userbot Milik {ALIVE_NAME}"
        await e.answer(reply_pop_up_alert, cache_time=0, alert=True)


CMD_HELP.update({"calkulator": f"{CMD_HANDLER}calc\n"
                 f"usage : Inline Calcuator.\n"})
