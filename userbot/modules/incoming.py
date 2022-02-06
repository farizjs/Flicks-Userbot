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

# Incoming message checker.
from userbot.modules.sql_helper.users_sql import add_user_to_db
from userbot.modules.sql_helper.blacklistbot_sql import check_is_black_list
from telethon import events
from userbot import OWNER_ID, API_KEY, API_HASH, BOT_TOKEN
from telethon.sync import TelegramClient

# if incoming

tgbot = TelegramClient(
    "TG_BOT_TOKEN",
    api_id=API_KEY,
    api_hash=API_HASH).start(
    bot_token=BOT_TOKEN)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def one_new_mssg(event):
    incoming = event.raw_text
    who = event.sender_id
    if check_is_black_list(who):
        return
    if incoming.startswith("/"):
        pass
    elif who == OWNER_ID:
        return
    else:
        await event.get_sender()
        event.chat_id
        to = await event.forward_to(OWNER_ID)
        add_user_to_db(to.id, who, event.id)
