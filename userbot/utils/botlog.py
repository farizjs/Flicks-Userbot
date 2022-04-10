# Credits: @mrconfused
# Recode by @farizjs
# FROM Flicks-Userbot <https://github.com/farizjs/Flicks-Userbot>
# t.me/TheFlicksUserbot

import os
import sys
import heroku3
from telethon import types

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HANDLER, HEROKU_API_KEY, HEROKU_APP_NAME, LOGS

from .xxd import create_supergroup

cmdhr = CMD_HANDLER

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await bot.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.info(
                "BOTLOG_CHATID cannot be found. Make sure it's correct."
            )
        except TypeError:
            LOGS.info(
                "BOTLOG_CHATID is unsupported. Make sure it's correct."
            )
        except Exception as e:
            LOGS.info(
                "An Exception occured upon trying to verify the PRIVATE_GROUP_BOT_API_ID.\n" +
                str(e))
    else:
        descript = "Jangan hapus grup ini atau ubah ke grup (Jika Anda mengubah grup semua potongan sebelumnya, selamat datang akan hilang.)"
        _, groupid = await create_supergroup(
            "Flicks-Userbot BotLog Group", bot, BOT_USERNAME, descript
        )

        heroku_var["BOTLOG_CHATID"] = groupid

        LOGS.info(
            "Private Group for BOTLOG_CHATID is created successfully and added to vars."
        )
        flag = True
    if BOTLOG_CHATID != -100:
        try:
            entity = await bot.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified BOTLOG_CHATID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified BOTLOG_CHATID."
                    )
        except ValueError:
            LOGS.info("BOTLOG_CHATID cannot be found. Make sure it's correct.")
        except TypeError:
            LOGS.info("BOTLOG_CHATID is unsupported. Make sure it's correct.")
        except Exception as e:
            LOGS.info(
                "An Exception occured upon trying to verify the BOTLOG_CHATID.\n" +
                str(e))
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "userbot"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)
