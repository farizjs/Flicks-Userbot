import functools
from telethon import events
from telethon import Button
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name

from userbot import *

user = bot.get_me()
OWNER_NAME = user.first_name
OWNER_ID = user.id
FLICKS_PIC = INLINE_PIC

MSG = f"""
**Flicks - UserBot**
➖➖➖➖➖➖➖➖➖➖
**Owner**: [{OWNER_NAME}](tg://user?id={OWNER_ID})
**Assistant** : @{BOT_USERNAME}
➖➖➖➖➖➖➖➖➖➖
"""

IN_BTTS = [
    [
        Button.url(
            "Repository",
            url="https://github.com/farizjs/Flicks-Userbot",
        ),
        Button.url("Channel", url="https://t.me/TheFlicksUserbot"),
    ]
]


def in_owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.sender_id in OWNER_ID:
                try:
                    await function(event)
                except BaseException as be:
                    pass
            else:
                try:
                    builder = event.builder
                    sur = builder.article(
                        title="Flicks Userbot",
                        url="https://t.me/FlicksSupport",
                        description="(c) FlicksUserbot",
                        text=MSG,
                        thumb=InputWebDocument(FLICKS_PIC, 0, "image/jpeg", []),
                        buttons=[
                            [
                                Button.url(
                                    "Repository",
                                    url="https://github.com/farizjs/Flicks-Userbot"
                                ),
                                Button.url(
                                    "Channel",
                                    url="https://t.me/TheFlicksUserbot"
                                ),
                            ]
                        ],
                    )
                    await event.answer(
                        [sur],
                        switch_pm=f"🤖: Asisten dari {OWNER_NAME}",
                        switch_pm_param="start",
                    )
                except BaseException as bexc:
                    pass

        return wrapper

    return decorator



def inline():
    def flicks(func):
        tgbot.add_event_handler(func, events.InlineQuery)

    return flicks


def in_pattern(pat):
    def don(func):
        pattern = pat
        tgbot.add_event_handler(func, events.InlineQuery(pattern=pattern))

    return don


def owner():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.sender_id in OWNER_ID:
                await function(event)
            else:
                try:
                    await event.answer(f"Ini adalah botnya {OWNER_NAME}!!", alert=True)
                except BaseException:
                    pass

        return wrapper

    return decorator
