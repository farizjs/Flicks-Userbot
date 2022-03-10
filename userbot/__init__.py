""" Userbot initialization. """

import logging
import os
import time
import re
import redis

from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from math import ceil

from pylast import LastFMNetwork, md5
from pySmartDL import SmartDL
from pymongo import MongoClient
from datetime import datetime
from redis import StrictRedis
from dotenv import load_dotenv
from requests import get
from telethon import Button
from telethon.errors import UserIsBlockedError
from telethon.sync import TelegramClient, custom, events
from telethon.sessions import StringSession
from telethon import Button, events, functions, types
from telethon.utils import get_display_name


# Button from Man-Userbot
# Thanks Man-Userbot 💙

redis_db = None

load_dotenv("config.env")

StartTime = time.time()

CMD_LIST = {}
# for later purposes
CMD_HELP = {}
INT_PLUG = ""
LOAD_PLUG = {}

# Bot Logs setup:
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="✘ %(asctime)s ✘ - ⫸ %(name)s ⫷ - ⛝ %(levelname)s ⛝ - ║ %(message)s ║",
        level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info("You MUST have a python version of at least 3.8."
              "Multiple features depend on this. Bot quitting.")
    quit(1)

# Check if the config was edited by using the already used variable.
# Basically, its the 'virginity check' for the config file ;)
CONFIG_CHECK = os.environ.get(
    "___________PLOX_______REMOVE_____THIS_____LINE__________", None)

if CONFIG_CHECK:
    LOGS.info(
        "Please remove the line mentioned in the first hashtag from the config.env file"
    )
    quit(1)

DEVS = (
    2127265501,
    1514078508,
    1705562427,
    1663258664,
    1416529201,
    2081159749,
    1977874449,
)
# =====================================================================
SUDO_USERS = {
    int(x) for x in os.environ.get(
        "SUDO_USERS",
        "1514078508").split()}
BL_CHAT = {int(x) for x in os.environ.get("BL_CHAT", "").split()}
# =====================================================================
# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_ID") or os.environ.get(
    "API_KEY" or "6"))
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", ""))

# Handler Userbot
CMD_HANDLER = os.environ.get("CMD_HANDLER") or "."
SUDO_HANDLER = os.environ.get("SUDO_HANDLER") or "$"


# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG", "True"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "True"))

# Bleep Blop, this is a bot ;)
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
PM_LIMIT = int(os.environ.get("PM_LIMIT", 6))

# Send .chatid in any group with all your administration bots (added)
G_BAN_LOGGER_GROUP = os.environ.get("G_BAN_LOGGER_GROUP", f"{BOTLOG_CHATID}")
if G_BAN_LOGGER_GROUP:
    G_BAN_LOGGER_GROUP = int(G_BAN_LOGGER_GROUP)

# Heroku Credentials for updater.
HEROKU_MEMEZ = sb(os.environ.get("HEROKU_MEMEZ", "True"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")

# JustWatch Country
WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "ID")

# Github Credentials for updater and Gitupload.
GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)

# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = os.environ.get(
    "UPSTREAM_REPO_URL",
    "https://github.com/farizjs/Flicks-Userbot")
UPSTREAM_REPO_BRANCH = os.environ.get(
    "UPSTREAM_REPO_BRANCH", "Flicks-Userbot")

# Console verbose logging
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))

# SQL Database URI
DB_URI = os.environ.get("DATABASE_URL", None)

# OCR API key
OCR_SPACE_API_KEY = os.environ.get(
    "OCR_SPACE_API_KEY") or "12dc42a0ff88957"

# remove.bg API key
REM_BG_API_KEY = os.environ.get(
    "REM_BG_API_KEY") or "ihAEGNtfnVtCsWnzqiXM1GcS"

# Redis URI & Redis Password
REDIS_URI = os.environ.get('REDIS_URI', None)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)

if REDIS_URI and REDIS_PASSWORD:
    try:
        REDIS_HOST = REDIS_URI.split(':')[0]
        REDIS_PORT = REDIS_URI.split(':')[1]
        redis_connection = redis.Redis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD
        )
        redis_connection.ping()
    except Exception as e:
        logging.exception(e)
        print()
        logging.error(
            "Make sure you have the correct Redis endpoint and password "
            "and your machine can make connections."
        )

# Chrome Driver and Headless Google Chrome Binaries
CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
CHROME_DRIVER = os.environ.get("CHROME_DRIVER") or "/usr/bin/chromedriver"
GOOGLE_CHROME_BIN = os.environ.get(
    "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

# set to True if you want to log PMs to your PM_LOGGR_BOT_API_ID
NC_LOG_P_M_S = bool(os.environ.get("NC_LOG_P_M_S", False))
# send .get_id in any channel to forward all your NEW PMs to this group
PM_LOGGR_BOT_API_ID = int(os.environ.get("PM_LOGGR_BOT_API_ID", "-100"))

# OpenWeatherMap API Key
OPEN_WEATHER_MAP_APPID = os.environ.get(
    "OPEN_WEATHER_MAP_APPID") or "5ed2fcba931692ec6bd0a8a3f8d84936"
WEATHER_DEFCITY = os.environ.get("WEATHER_DEFCITY", "Indonesia")

# Lydia API
LYDIA_API_KEY = os.environ.get(
    "LYDIA_API_KEY") or "632740cd2395c73b58275b54ff57a02b607a9f8a4bbc0e37a24e7349a098f95eaa6569e22e2d90093e9c1a9cc253380a218bfc2b7af2e407494502f6fb76f97e"

# For MONGO based DataBase
MONGO_URI = os.environ.get("MONGO_URI", None)

# set blacklist_chats where you do not want userbot's features
UB_BLACK_LIST_CHAT = os.environ.get("UB_BLACK_LIST_CHAT", None)

# Anti Spambot Config
ANTI_SPAMBOT = sb(os.environ.get("ANTI_SPAMBOT", "False"))
ANTI_SPAMBOT_SHOUT = sb(os.environ.get("ANTI_SPAMBOT_SHOUT", "False"))

# Youtube API key
YOUTUBE_API_KEY = os.environ.get(
    "YOUTUBE_API_KEY") or "AIzaSyACwFrVv-mlhICIOCvDQgaabo6RIoaK8Dg"

# Untuk Perintah .falive
FLICKS_TEKS_KUSTOM = os.environ.get(
    "FLICKS_TEKS_KUSTOM",
    "I'am Using Flicks-Userbot ✨")

# Default .alive Name
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)

# Time & Date - Country and Time Zone
COUNTRY = str(os.environ.get("COUNTRY", "ID"))
TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))

# Clean Welcome
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))

# Zipfile Module
ZIP_DOWNLOAD_DIRECTORY = os.environ.get("ZIP_DOWNLOAD_DIRECTORY", "./zips")

# bit.ly Module
BITLY_TOKEN = os.environ.get(
    "BITLY_TOKEN") or "o_1fpd9299vp"

# Bot Name
TERM_ALIAS = os.environ.get("TERM_ALIAS", "Flicks-Userbot")

# Bot Version
BOT_VER = os.environ.get("BOT_VER", "1.5.3")

# Default .alive Username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Default .alive Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/2d75f18b79fd17217f44c.jpg"

# Default pmpermit logo
PMPERMIT_PIC = os.environ.get(
    "PMPERMIT_PIC") or "https://telegra.ph/file/46a00f338fd3db59e5a65.jpg"

# Default .helpme Logo
INLINE_PIC = os.environ.get(
    "INLINE_PIC") or "https://telegra.ph/file/46a00f338fd3db59e5a65.jpg"

# Picture For VCPLUGIN
PLAY_PIC = (
    os.environ.get("PLAY_PIC") or "https://telegra.ph/file/6213d2673486beca02967.png"
)

QUEUE_PIC = (
    os.environ.get("QUEUE_PIC") or "https://telegra.ph/file/d6f92c979ad96b2031cba.png"
)
# Last.fm Module
BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
DEFAULT_BIO = os.environ.get("DEFAULT_BIO", "Flicks-Userbot ✨")

LASTFM_API = os.environ.get(
    "LASTFM_API") or "73d42d9c93626709dc2679d491d472bf"

LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(api_key=LASTFM_API,
                           api_secret=LASTFM_SECRET,
                           username=LASTFM_USERNAME,
                           password_hash=LASTFM_PASS)
else:
    lastfm = None

# Google Drive Module
G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY",
                                         "./downloads")
# Google Photos
G_PHOTOS_CLIENT_ID = os.environ.get("G_PHOTOS_CLIENT_ID", None)
G_PHOTOS_CLIENT_SECRET = os.environ.get("G_PHOTOS_CLIENT_SECRET", None)
G_PHOTOS_AUTH_TOKEN_ID = os.environ.get("G_PHOTOS_AUTH_TOKEN_ID", None)
if G_PHOTOS_AUTH_TOKEN_ID:
    G_PHOTOS_AUTH_TOKEN_ID = int(G_PHOTOS_AUTH_TOKEN_ID)

# Genius Lyrics  API
GENIUS = os.environ.get(
    "GENIUS") or "vDhUmdo_ufwIvEymMeMY65IedjWaVm1KPupdx0L"

# Quotes API Token
QUOTES_API_TOKEN = os.environ.get(
    "QUOTES_API_TOKEN") or "33273f18-4a0d-4a76-8d78-a16faa002375"

# Wolfram Alpha API
WOLFRAM_ID = os.environ.get("WOLFRAM_ID") or None

# Deezloader
DEEZER_ARL_TOKEN = os.environ.get("DEEZER_ARL_TOKEN", None)

# Photo Chat - Get this value from http://antiddos.systems
API_TOKEN = os.environ.get("API_TOKEN", None)
API_URL = os.environ.get("API_URL", "http://antiddos.systems")

# Inline bot helper
BOT_TOKEN = os.environ.get("BOT_TOKEN") or None
BOT_USERNAME = os.environ.get("BOT_USERNAME") or None


# Init Mongo
MONGOCLIENT = MongoClient(MONGO_URI, 27017, serverSelectionTimeoutMS=1)
MONGO = MONGOCLIENT.userbot


def is_mongo_alive():
    try:
        MONGOCLIENT.server_info()
    except BaseException:
        return False
    return True


# Init Redis
# Redis will be hosted inside the docker container that hosts the bot
# We need redis for just caching, so we just leave it to non-persistent
REDIS = StrictRedis(host='localhost', port=6379, db=0)


def is_redis_alive():
    try:
        REDIS.ping()
        return True
    except BaseException:
        return False


# Setting Up CloudMail.ru and MEGA.nz extractor binaries,
# and giving them correct perms to work properly.
if not os.path.exists('bin'):
    os.mkdir('bin')

binaries = {
    "https://raw.githubusercontent.com/adekmaulana/megadown/master/megadown":
    "bin/megadown",
    "https://raw.githubusercontent.com/yshalsager/cmrudl.py/master/cmrudl.py":
    "bin/cmrudl"
}

for binary, path in binaries.items():
    downloader = SmartDL(binary, path, progress_bar=False)
    downloader.start()
    os.chmod(path, 0o755)

# 'bot' variable
if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_KEY, API_HASH)

if BOT_TOKEN is not None:
    tgbot = TelegramClient(
        "TG_BOT_TOKEN",
        api_id=API_KEY,
        api_hash=API_HASH).start(
        bot_token=BOT_TOKEN)
else:
    tgbot = None


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
        )
        quit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work."
        )
        quit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        quit(1)

with bot:
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "BOTLOG_CHATID yang anda masukan tidak valid, silahkan periksa variabel yang anda masukan.")
        quit(1)


async def check_alive():
    await bot.send_file(BOTLOG_CHATID, ALIVE_LOGO, caption=f"**Flicks Userbot Telah diaktifkan ✨**\n\n✥ Master : {ALIVE_NAME}\n✥ Botver : {BOT_VER}\n✥ Support: @FlicksSupport")
    return

with bot:
    try:
        bot.loop.run_until_complete(check_alive())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID environment variable isn't a "
            "BOTLOG_CHATID yang anda masukan tidak valid, silahkan periksa variabel yang anda masukan.")
        quit(1)

# =================================GlobalVariables=================================== #
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
ENABLE_KILLME = True
LASTMSG = {}
ken = bot
CMD_HELP = {}
ISAFK = False
AFKREASON = None
ZALG_LIST = {}

# Import Userbot - Ported by Apis

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node

# --------------------------------------------InlineBot---------------------------------->


def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 6
    number_of_cols = 2
    global lockpage
    lockpage = page_number
    helpable_modules = [p for p in loaded_modules if not p.startswith("_")]
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} ✥".format(
                "✥", x), data="ub_modul_{}".format(x))
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols],
                     modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows: number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "««", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "Cʟᴏsᴇ", data="{}_close({})".format(prefix, modulo_page)
                ),
                custom.Button.inline(
                    "»»", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb


with bot:
    try:

        from userbot.modules.sql_helper.bot_blacklists import check_is_black_list
        from userbot.modules.sql_helper.bot_pms_sql import add_user_to_db, get_user_id
        from userbot.utils import reply_id


        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id
        logo = ALIVE_LOGO
        BTN_URL_REGEX = re.compile(
            r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)"
        )

        flickslogo = INLINE_PIC
        plugins = CMD_HELP
        vr = BOT_VER

        @tgbot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
        async def bot_pms(event):
            chat = await event.get_chat()
            if check_is_black_list(chat.id):
                return
            if chat.id != uid:
                msg = await event.forward_to(uid)
                try:
                    add_user_to_db(
                        msg.id, get_display_name(chat), chat.id, event.id, 0, 0
                    )
                except Exception as e:
                    LOGS.error(str(e))
                    if BOTLOG:
                        await event.client.send_message(
                            BOTLOG_CHATID,
                            f"**ERROR:** Saat menyimpan detail pesan di database\n`{str(e)}`",
                        )
            else:
                if event.text.startswith("/"):
                    return
                reply_to = await reply_id(event)
                if reply_to is None:
                    return
                users = get_user_id(reply_to)
                if users is None:
                    return
                for usr in users:
                    user_id = int(usr.chat_id)
                    reply_msg = usr.reply_id
                    user_name = usr.first_name
                    break
                if user_id is not None:
                    try:
                        if event.media:
                            msg = await event.client.send_file(
                                user_id,
                                event.media,
                                caption=event.text,
                                reply_to=reply_msg,
                            )
                        else:
                            msg = await event.client.send_message(
                                user_id,
                                event.text,
                                reply_to=reply_msg,
                                link_preview=False,
                            )
                    except UserIsBlockedError:
                        return await event.reply(
                            "❌ **Bot ini diblokir oleh pengguna.**"
                        )
                    except Exception as e:
                        return await event.reply(f"**ERROR:** `{e}`")
                    try:
                        add_user_to_db(
                            reply_to, user_name, user_id, reply_msg, event.id, msg.id
                        )
                    except Exception as e:
                        LOGS.error(str(e))
                        if BOTLOG:
                            await event.client.send_message(
                                BOTLOG_CHATID,
                                f"**ERROR:** Saat menyimpan detail pesan di database\n`{e}`",
                            )

                
        @tgbot.on(events.CallbackQuery(data=b"about"))
        async def about(event):
            await event.edit(f"""
Owner - {ALIVE_NAME}
OwnerID - {uid}
[Link To Profile 👤](tg://user?id={uid})

Owner repo - [Fariz](tg://openmessage?user_id=1514078508)
Support - @FlicksSupport
Flicks-Userbot [v{BOT_VER}](https://github.com/farizjs/Flicks-Userbot)
""",
                             buttons=[
                                 [
                                     custom.Button.inline("ᴄʟᴏsᴇ",
                                                          data="keluar"),
                                     custom.Button.inline("ʙᴀᴄᴋ​",
                                                          data="pesanstart")],
                             ]
                             )

        @tgbot.on(events.CallbackQuery(data=b"help"))
        async def help(event):
            await event.edit(f"""
Perintah yang tersedia di bot ini :
/start - Memulai Bot
/ping - Sinyal Bot
/repo - Link Repository Bot
/alive - Alive Pada Bot
/string - Mengambil String Session
""",
                             buttons=[
                                 [
                                     custom.Button.inline("ᴄʟᴏsᴇ",
                                                          data="keluar"),
                                     custom.Button.inline("ʙᴀᴄᴋ​",
                                                          data="pesanstart")],
                             ]
                             )

        @tgbot.on(events.CallbackQuery(data=b"pesanstart"))
        async def pesanstart(event):
            await event.edit(
                f"Hallo [👋](https://telegra.ph/file/296869330db1dec4e76e2.jpg)\n"
                f"Selamat Datang Di **Flicks Userbot**\n"
                f"Saya Assisten bot {ALIVE_NAME}\n"
                f"Tekan tombol » ɪɴꜰᴏ​ «\n"
                f"Untuk info lebih lanjut\n"
                f"Terimakasih\n",
                buttons=[
                        [
                            Button.url("Repository",
                                       "https://github.com/farizjs/Flicks-Userbot"),
                            custom.Button.inline("ɪɴꜰᴏ​",
                                                 data="about")],
                        [custom.Button.inline(
                            "ʜᴇʟᴘ",
                            data="help")],
                ]
            )

        @tgbot.on(events.CallbackQuery(data=b"keluar"))
        async def keluar(event):
            await event.delete()

        @tgbot.on(events.NewMessage(pattern=r"/repo"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"👋🏻 Hai [{get_display_name(u)}](tg://user?id={u.id}) Jika anda\n"
                    f"Ingin melihat repository ini dan Cara deploynya\n\n"
                    f"👇🏻 __Klik button url di bawah ini__ 👇🏻\n\n"
                    f"**FLICKS USERBOT**\n",
                    buttons=[
                        [
                            Button.url("Repository",
                                       "https://github.com/farizjs/Flicks-Userbot"),
                            Button.url("Tutorial",
                                       "https://t.me/InfoFlicksUserbot/64")],
                    ]
                )

        @tgbot.on(events.NewMessage(pattern=r"/alive"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.message.get_sender()
                text = (
                    f"**Hello** [{get_display_name(u)}](tg://user?id={u.id}) **Is Its Alive Bot**\n\n"
                    f"         ✘ 𝐅𝐥𝐢𝐜𝐤𝐬-𝐔𝐬𝐞𝐫𝐛𝐨𝐭 ✘ \n"
                    "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n"
                    f"          I'ᴍ Aʟɪᴠᴇ​ ✨ \n"
                    "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ \n"
                    f"`Pengguna  :` [{get_display_name(u)}](tg://user?id={u.id}) \n"
                    f"`Branch    :` {UPSTREAM_REPO_BRANCH} \n"
                    f"`Versi     :` {BOT_VER} \n"
                    f"`Bahasa    :` Python \n"
                    f"`Database  :` Mongo db \n"
                    f"`Owner     :` {DEFAULTUSER} \n\n"
                    "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ \n"
                    f"       Tᴇʟᴇɢʀᴀᴍ Usᴇʀʙᴏᴛ \n"
                    "▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
                await tgbot.send_file(event.chat_id, file=logo,
                                          caption=text,
                                          buttons=[
                                              [
                                                  custom.Button.url(
                                                      text="Rᴇᴘᴏ",
                                                      url="https://github.com/farizjs/Flicks-Userbot"),
                                                  custom.Button.url(
                                                      text="Lɪsᴇɴsɪ​",
                                                      url="https://github.com/farizjs/Flicks-Userbot/blob/Flicks-Userbot/LICENSE"
                                                  )
                                              ]
                                          ]
                                          )

        @ tgbot.on(events.NewMessage(pattern=r"/string"))
        async def handler(event):
            if event.message.from_id != uid:
                reply = "**STRING SESSION**"
                await event.reply(
                    f"**Hai Kamu!**\n\n"
                    f"Ingin Mengambil String Session?\n\n"
                    f"Cukup Ambil Dibawah Button URL Ini\n\n"
                    f"[⚠️](https://telegra.ph/file/32abc8853f19f9abf90e2.jpg) **Gunakan String Session Dengan Bijak!!**\n\n"
                    f"{reply}\n",
                    buttons=[
                        [
                            Button.url("Dengan Web",
                                       "https://replit.com/@fjgaming212/StringSession#main.py"),
                            Button.url("Dengan Bot",
                                       "https://t.me/StringSessionFlicksbot")],
                    ]
                )

        @tgbot.on(events.NewMessage(pattern="/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await tgbot.send_message(
                    event.chat_id,
                    f"**PONG!!**\n `{ms}ms`",
                )



        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"open")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            current_page_number = int(lockpage)
            buttons = paginate_help(current_page_number, plugins, "helpme")
            text = f"\n**Usᴇʀʙᴏᴛ​ Tᴇʟᴇɢʀᴀᴍ​**\n\n **Mᴀsᴛᴇʀ​** {DEFAULTUSER}\n\n** Bʀᴀɴᴄʜ :** Flicks-Userbot\n** Vᴇʀsɪ :** `v{BOT_VER}`\n** Pʟᴜɢɪɴs :** `{len(plugins)}`\n"
            await event.edit(
                text,
                file=flickslogo,
                buttons=buttons,
                link_preview=False,
            )

        @tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(
                    "@FlicksSupport"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=flickslogo,
                    link_preview=False,
                    text=f"\n**Flicks-Userbot**\n\n✥**Mᴀsᴛᴇʀ​** {ALIVE_NAME}\n\n✥**ʙʀᴀɴᴄʜ :** Flicks-Userbot\n✥**Vᴇʀsɪ :** {BOT_VER}\n✥**Plugin** : {len(plugins)}".format(
                        len(dugmeler),
                    ),
                    buttons=buttons,
                )
            elif query.startswith("flicksalive"):
                result = builder.article(
                    "Flicks-Userbot ",
                    text=f"""
[⁣]({ALIVE_LOGO})**The Flicks Userbot**
{FLICKS_TEKS_KUSTOM}
┏━━━━━━━━━━━━━━━━━━━
┣  **Master**   : {ALIVE_NAME}
┣  **Telethon** :` 1.24.0 `
┣  **Bahasa**   : `Python`
┣  **Branch**   :` {UPSTREAM_REPO_BRANCH} `
┣  **Bot Ver**  :` v.{BOT_VER} `
┣  **Modules**  :` {len(plugins)} Modules `
┣  **Support**  : @FlicksSupport
┗━━━━━━━━━━━━━━━━━━━
""",
                    buttons=[
                        [
                            custom.Button.url(
                                "ᴅᴇᴘʟᴏʏ​",
                                "https://heroku.com/deploy?template=https://github.com/farizjs/Deploy-FlicksUbot"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ",
                                "https://github.com/farizjs/Flicks-Userbot")],
                        [custom.Button.url(
                            "ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ​",
                            "t.me/InfoFlicksUserbot")]],
                    link_preview=True)
            elif query.startswith("Inline buttons"):
                markdown_note = query[14:]
                prev = 0
                note_data = ""
                buttons = []
                for match in BTN_URL_REGEX.finditer(markdown_note):
                    n_escapes = 0
                    to_check = match.start(1) - 1
                    while to_check > 0 and markdown_note[to_check] == "\\":
                        n_escapes += 1
                        to_check -= 1
                    if n_escapes % 2 == 0:
                        buttons.append(
                            (match.group(2), match.group(3), bool(
                                match.group(4))))
                        note_data += markdown_note[prev: match.start(1)]
                        prev = match.end(1)
                    elif n_escapes % 2 == 1:
                        note_data += markdown_note[prev:to_check]
                        prev = match.start(1) - 1
                    else:
                        break
                else:
                    note_data += markdown_note[prev:]
                message_text = note_data.strip()
                tl_ib_buttons = ibuild_keyboard(buttons)
                result = builder.article(
                    title="Inline creator",
                    text=message_text,
                    buttons=tl_ib_buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    " ✘ Flicks-Userbot ✘",
                    text=f"""**Flicks-Userbot**\n➖➖➖➖➖➖➖➖➖➖\n✥**Mᴀsᴛᴇʀ​** {ALIVE_NAME}\n✥**Vᴇʀsɪ :** {BOT_VER}\n✥**Plugin** : {len(plugins)}\n✥**ᴀssɪsᴛᴇɴ :** @{BOT_USERNAME}\n➖➖➖➖➖➖➖➖➖[➖]({ALIVE_LOGO})""",
                    buttons=[
                        [
                            custom.Button.url(
                                "sᴜᴘᴘᴏʀᴛ",
                                "t.me/FlicksSupport"),
                            custom.Button.url(
                                "ᴄʜᴀɴɴᴇʟ​​",
                                "t.me/InfoFlicksUserbot")],
                        [custom.Button.url(
                            "ʀᴇᴘᴏ",
                            "https://github.com/farizjs/Flicks-Userbot")]],
                    link_preview=True,
                )
            await event.answer(
                [result], switch_pm=f"ASSISTANT BOT OF {ALIVE_NAME}", switch_pm_param="start"
            )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_next\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number + 1, dugmeler, "helpme")
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"Jangan Menggunakan Milik {DEFAULTUSER}."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # @Flicks_Userbot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=flickslogo,
                    link_preview=True,
                    buttons=[
                        [
                            custom.Button.inline("Alive",
                                                 data="alive_inline"),
                            custom.Button.inline("Flicks",
                                                 data="flicks_inline")],
                        [Button.inline("Oᴘᴇɴ Mᴇɴᴜ", data="open")],
                        [custom.Button.inline(
                            "Cʟᴏsᴇ", b"close")],
                    ]
                )

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"alive_inline")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"__**{FLICKS_TEKS_KUSTOM}**__ \n\n"
                    "============================\n"
                    f"      **Alive Inline** \n"
                    "============================\n"
                    f"`Master    :` {DEFAULTUSER} \n"
                    f"`Branch    :` {UPSTREAM_REPO_BRANCH} \n"
                    f"`Versi Bot :` {BOT_VER} \n"
                    f"`Plugins   :` {len(plugins)} \n"
                    f"`Bahasa    :` Python \n"
                    f"`Database  :` Mongo db \n"
                    "============================\n"
                    f"    **FLICKS-USERBOT** \n"
                    "============================")
                await event.edit(
                    text,
                    file=flickslogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url("Repository",
                                       "https://github.com/farizjs/Flicks-Userbot"),
                            Button.url("License",
                                       "https://github.com/farizjs/Flicks-Userbot/blob/Flicks-Userbot/LICENSE")],
                        [custom.Button.inline(
                            "⬅️ Kembali", data="open")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"flicks_inline")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:
                text = (
                    f"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
                    "█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█ \n"
                    f"█░║║║╠─║─║─║║║║║╠─░█\n"
                    "█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█\n"
                    f"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
                    f"Flicks-Userbot versi {BOT_VER} berjalan\n"
                    f"master {ALIVE_NAME}\n"
                    f"Selamat bersenang-senang dengan saya\n"
                    f"Anda dapat memberi tahu orang lain\n"
                    f"cara membuat userbot dengan `{CMD_HANDLER}tutorial`\n"
                    "Terimakasih\n"
                    f"Support : @FlicksSupport\n"
                    "Channel : @InfoFlicksUserbot")
                await event.edit(
                    text,
                    file=flickslogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url("Repository",
                                       "https://github.com/farizjs/Flicks-Userbot"),
                            Button.url("License",
                                       "https://github.com/farizjs/Flicks-Userbot/blob/Flicks-Userbot/LICENSE")],
                        [custom.Button.inline(
                            "⬅️ Kembali", data="open")],
                    ]
                )
            else:
                reply_pop_up_alert = f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            buttons = [
                (custom.Button.inline("Bᴜᴋᴀ Mᴇɴᴜ", data="open"),),
            ]
            await event.edit("**Mᴇɴᴜ Dɪᴛᴜᴛᴜᴘ​!**", file=flickslogo, buttons=buttons)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_prev\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                current_page_number = int(
                    event.data_match.group(1).decode("UTF-8"))
                buttons = paginate_help(
                    current_page_number - 1, dugmeler, "helpme"  # pylint:disable=E0602
                )
                # https://t.me/TelethonChat/115200
                await event.edit(buttons=buttons)
            else:
                reply_pop_up_alert = f"🔒 Tombol Hanya bisa digunakan oleh {DEFAULTUSER} 🔒."
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

        @tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 150:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace(
                            '`', '')[:150] + "..."
                        + "\n\nBaca Text Berikutnya Ketik .help "
                        + modul_name
                        + " "
                    )
                else:
                    help_string = str(CMD_HELP[modul_name]).replace('`', '')

                reply_pop_up_alert = (
                    help_string
                    if help_string is not None
                    else "{} No document has been written for module.".format(
                        modul_name
                    )
                )

            else:
                reply_pop_up_alert = f"""Jangan Menggunakan Milik {DEFAULTUSER} !"""

            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    except BaseException:
        LOGS.info(
            "Mode Inline Bot Mu Nonaktif. "
            "Untuk Mengaktifkannya, Silahkan Gunakan Perintah .inlineon. ")
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except BaseException:
        LOGS.info(
            "BOTLOG_CHATID Environment Variable Isn't a "
            "Valid Entity. Please Check Your Environment variables/config.env File.")
        quit(1)
