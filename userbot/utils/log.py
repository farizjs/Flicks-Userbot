# Copyright (c) 2020 TeamUltroid
# <https://github.com/TeamUltroid/Ultroid>
# Recode by farizjs
# <t.me/TheFlicksUserbot>

import asyncio
import importlib
import logging
import sys
from pathlib import Path
from random import randint
import os
import random
import time
from random import randint

from telethon.errors import (
    BotMethodInvalidError,
    ChannelPrivateError,
    ChannelsTooMuchError,
    ChatAdminRequiredError,
    UserNotParticipantError,
)
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    InviteToChannelRequest,
    JoinChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatAdminRights,
    ChatPhotoEmpty,
    InputChatUploadedPhoto,
    InputMessagesFilterDocument,
)
from telethon.utils import get_peer_id

import heroku3

from userbot import tgbot, bot, HEROKU_API_KEY, HEROKU_APP_NAME, LOGS

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None

async def autolog():
     if BOTLOG_CHATID:
        return
    await bot.start()
        LOGS.info("'BOTLOG_CHATID' not found! Add it in order to use 'BOTMODE'")
        LOGS.info("Creating a Log Channel for You!")
        try:
            r = await bot(
                CreateChannelRequest(
                    title="My Flicks Logs",
                    about="My Userbot Log Group\n\n Join @TheFlicksUserbot",
                    megagroup=True,
                ),
            )
        except ChannelsTooMuchError:
            LOGS.info(
                "You Are in Too Many Channels & Groups , Leave some And Restart The Bot"
            )
            import sys

            sys.exit(1)
        except BaseException as er:
            LOGS.info(er)
            LOGS.info(
                "Something Went Wrong , Create A Group and set its id on config var LOG_CHANNEL."
            )


            sys.exit(1)
        chat = r.chats[0]
        channel = get_peer_id(chat)

        heroku_var["BOTLOG_CHATID"] = channel

    assistant = True
    try:
        await bot.get_permissions(int(channel), tgbot.me.username)
    except UserNotParticipantError:
        try:
            await bot(InviteToChannelRequest(int(channel), [tgbot.me.username]))
        except BaseException as er:
            LOGS.info("Error while Adding Assistant to Log Channel")
            LOGS.exception(er)
            assistant = False
    except BaseException as er:
        assistant = False
        LOGS.exception(er)
    if assistant:
        try:
            achat = await tgbot.get_entity(int(channel))
        except BaseException as er:
            achat = None
            LOGS.info("Error while getting Log channel from Assistant")
            LOGS.exception(er)
        if achat and not achat.admin_rights:
            rights = ChatAdminRights(
                add_admins=True,
                invite_users=True,
                change_info=True,
                ban_users=True,
                delete_messages=True,
                pin_messages=True,
                anonymous=False,
                manage_call=True,
            )
            try:
                await bot(
                    EditAdminRequest(
                        int(channel), tgbot.me.username, rights, "Assistant"
                    )
                )
            except ChatAdminRequiredError:
                LOGS.info(
                    "Failed to promote 'Assistant Bot' in 'Log Channel' due to 'Admin Privileges'"
                )
            except BaseException as er:
                LOGS.info("Error while promoting assistant in Log Channel..")
                LOGS.exception(er)
    if isinstance(chat.photo, ChatPhotoEmpty):
        photo = "userbot/files/20211115_142004.jpg"
        ll = await bot.upload_file(photo)
        try:
            await bot(
                EditPhotoRequest(int(channel), InputChatUploadedPhoto(ll))
            )
        except BaseException as er:
            LOGS.exception(er)
        os.remove(photo)
