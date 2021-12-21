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
from telethon.sync import TelegramClient, custom, events
from telethon.sessions import StringSession
from telethon import Button, events, functions, types
from telethon.utils import get_display_name

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
    basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
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

# KALO NGEFORK ID DEVS SAMA ID BLACKLIST_CHAT NYA GA USAH DI HAPUS YA GOBLOK 😡
DEVS = (
    1979717764,
    1514078508,
    1705562427,
    1663258664,
    1416529201,
    2081159749,
    1937084611,
)

# Telegram App KEY and HASH
API_KEY = int(os.environ.get("API_KEY") or 0)
API_HASH = str(os.environ.get("API_HASH") or None)

# Userbot Session String
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", ""))

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
    "https://github.com/fjgaming212/Flicks-Userbot")
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
BOT_VER = os.environ.get("BOT_VER", "5.1")

# Default .alive Username
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)

# Sticker Custom Pack Name
S_PACK_NAME = os.environ.get("S_PACK_NAME", None)

# Default .alive Logo
ALIVE_LOGO = os.environ.get(
    "ALIVE_LOGO") or "https://telegra.ph/file/808a9f8f047f9a7e67050.jpg"

# Default pmpermit logo
PMPERMIT_PIC = os.environ.get(
    "PMPERMIT_PIC") or "https://telegra.ph/file/e950cf06924c4e090d513.jpg"

# Default .helpme Logo
INLINE_PIC = os.environ.get(
    "INLINE_PIC") or "https://telegra.ph/file/808a9f8f047f9a7e67050.jpg"

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
            "valid entity. Check your environment variables/config.env file.")
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
    number_of_rows = 5
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


with bot:
    try:
        ken.tgbot = tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_KEY,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

        dugmeler = CMD_HELP
        me = bot.get_me()
        uid = me.id
        logo = ALIVE_LOGO

        kenlogo = INLINE_PIC
        plugins = CMD_HELP
        vr = BOT_VER

        @ken.tgbot.on(events.ChatAction)
        async def handler(event):
            if event.user_joined or event.user_added:
                u = await event.client.get_entity(event.chat_id)
                c = await event.client.get_entity(event.user_id)
                await event.reply(
                    f"**Hallo Kamu**\n**Welcome To** [{get_display_name(u)}](tg://user?id={u.id}) \n\n"
                    f"✥ **ᴘᴇɴɢɢᴜɴᴀ​ :** {get_display_name(c)} \n"
                    f"✥ **ɪᴅ ᴘᴇɴɢɢᴜɴᴀ​ :** {c.id} \n"
                    f"✥ **ᴜsᴇʀɴᴀᴍᴇ​ :** @{c.username} \n"
                    f"✥ **ᴍᴇɴᴛɪᴏɴ​ :** [{get_display_name(c)}](tg://user?id={c.id}) \n\n"
                    f"sᴇᴍᴏɢᴀ ʙᴇᴛᴀʜ ᴅɪsɪɴɪ ʏᴀ​ ✨\n",
                    buttons=[
                        [
                            Button.url("ʀᴇᴘᴏ ꜰʟɪᴄᴋs ᴜsᴇʀʙᴏᴛ​",
                                       "https://github.com/fjgaming212/Flicks-Userbot")],
                    ]
                )

        @ken.tgbot.on(events.NewMessage(pattern="/start"))
        async def handler(event):
            if event.message.from_id != uid:
                u = await event.client.get_entity(event.chat_id)
                await event.reply(
                    f"[👋](https://telegra.ph/file/296869330db1dec4e76e2.jpg) Hallo [{get_display_name(u)}](tg://user?id={u.id}) \nSelamat Datang Di **Flicks Userbot**\nGunakan saya untuk mempersantai grup anda\n\n➣ Botver : {BOT_VER}\n➣ Plugin : {len(plugins)}\n➣ Owner repo : [Fariz](tg://openmessage?user_id=1514078508)\n",
                    buttons=[
                        [
                            Button.url("ʀᴇᴘᴏ ꜰʟɪᴄᴋs ᴜsᴇʀʙᴏᴛ 🛠️",
                                       "https://github.com/fjgaming212/Flicks-Userbot")],
                    ]
                )

        @ ken.tgbot.on(events.NewMessage(pattern=r"/repo"))
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
                                       "https://github.com/fjgaming212/Flicks-Userbot"),
                            Button.url("Tutorial",
                                       "https://t.me/InfoFlicksUserbot/64")],
                    ]
                )

        @ ken.tgbot.on(events.NewMessage(pattern=r"/alive"))
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
                await ken.tgbot.send_file(event.chat_id, file=logo,
                                          caption=text,
                                          buttons=[
                                              [
                                                  custom.Button.url(
                                                      text="Rᴇᴘᴏ",
                                                      url="https://github.com/fjgaming212/Flicks-Userbot"),
                                                  custom.Button.url(
                                                      text="Lɪsᴇɴsɪ​",
                                                      url="https://github.com/fjgaming212/Flicks-Userbot/blob/Flicks-Userbot/LICENSE"
                                                  )
                                              ]
                                          ]
                                          )

        @ ken.tgbot.on(events.NewMessage(pattern=r"/string"))
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

        @ ken.tgbot.on(events.NewMessage(pattern="/ping"))
        async def handler(event):
            if event.message.from_id != uid:
                start = datetime.now()
                end = datetime.now()
                ms = (end - start).microseconds / 1000
                await tgbot.send_message(
                    event.chat_id,
                    f"**PONG!!**\n `{ms}ms`",
                )

        @ ken.tgbot.on(
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
                file=kenlogo,
                buttons=buttons,
                link_preview=False,
            )

        @ ken.tgbot.on(events.InlineQuery)
        async def inline_handler(event):
            builder = event.builder
            result = None
            query = event.text
            if event.query.user_id == uid and query.startswith(
                    "@FlicksSupport"):
                buttons = paginate_help(0, dugmeler, "helpme")
                result = builder.photo(
                    file=kenlogo,
                    link_preview=False,
                    text=f"\n**Flicks-Userbot**\n\n✥**Mᴀsᴛᴇʀ​** {ALIVE_NAME}\n\n✥**ʙʀᴀɴᴄʜ :** Flicks-Userbot\n✥**Vᴇʀsɪ :** {BOT_VER}\n✥**Plugin** : {len(plugins)}".format(
                        len(dugmeler),
                    ),
                    buttons=buttons,
                )
            elif query.startswith("about"):
                result = builder.article(
                    "Tentang Flicks-Userbot ",
                    text=f"Flicks-Userbot [☘️]({ALIVE_LOGO}) adalah userbot Telegram modular yang berjalan di Python 3.6 dengan database sqlalchemy\n[Fariz](tg://openmessage?user_id=1514078508) membuat dan menambahkan modul yang dibutuhkan.\nUntuk mengetahui perintah Flicks-Userbot gunakan perintah `.helpme` dan untuk mengecek userbot gunakan perintah `.alive`",
                    buttons=[
                        [
                            custom.Button.url(
                                "ᴅᴇᴘʟᴏʏ​",
                                "https://heroku.com/deploy?template=https://github.com/fjgaming212/Deploy-Flicks"),
                            custom.Button.url(
                                "ʀᴇᴘᴏ",
                                "https://github.com/fjgaming212/Flicks-Userbot")],
                        [custom.Button.url(
                            "ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ​",
                            "t.me/InfoFlicksUserbot")]],
                    link_preview=True)
            elif query.startswith("tutor"):
                result = builder.article(
                    "Tutorial memasang Flicks-Userbot ",
                    text=f"Buat teman teman yang ingin memasang userbot seperti saya anda bisa melihat tutorial di bawah ini\nDapatkan API_KEY dan API_HASH di web `my.telegram.org`.\nDapatkan STRING_SESSION di web replit atau bot\nDapatkan BOT_TOKEN dan BOT_USERNAME di [@BotFather](tg://user?id=93372553)\nDapatkan HEROKU_API_KEY di `dashboard.heroku.com/account`\nTerus Nyalakan, tutorial lengkap [klik disini](https://t.me/InfoFlicksUserbot/64)",
                    buttons=[
                        [
                            custom.Button.url(
                                "ᴅᴇᴘʟᴏʏ​",
                                "https://heroku.com/deploy?template=https://github.com/fjgaming212/Deploy-Flicks"),
                            custom.Button.url(
                                "sᴛʀɪɴɢ",
                                "https://t.me/InfoFlicksUserbot/110")],
                        [custom.Button.url(
                            "ʀᴇᴘᴏ",
                            "https://github.com/fjgaming212/Flicks-Userbot")]],
                    link_preview=False)
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
                            "https://github.com/fjgaming212/Flicks-Userbot")]],
                    link_preview=True,
                )
            await event.answer(
                [result], switch_pm=f"ASSISTANT BOT OF {ALIVE_NAME}", switch_pm_param="start"
            )

        @ ken.tgbot.on(
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

        @ ken.tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"helpme_close\((.+?)\)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # @Flicks_Userbot
                # https://t.me/TelethonChat/115200
                await event.edit(
                    file=kenlogo,
                    link_preview=True,
                    buttons=[
                        [
                            Button.url("Cʜᴀɴɴᴇʟ Uᴘᴅᴀᴛᴇ​",
                                       "t.me/SadRoomsInfo"),
                            Button.url("Gʀᴏᴜᴘ Sᴜᴘᴘᴏʀᴛ",
                                       "t.me/FlicksSupport")],
                        [Button.inline("Oᴘᴇɴ Mᴇɴᴜ", data="open")],
                        [custom.Button.inline(
                            "Cʟᴏsᴇ", b"close")],
                    ]
                )

        @ ken.tgbot.on(events.CallbackQuery(data=b"close"))
        async def close(event):
            buttons = [
                (custom.Button.inline("Bᴜᴋᴀ Mᴇɴᴜ", data="open"),),
            ]
            await event.edit("**Mᴇɴᴜ Dɪᴛᴜᴛᴜᴘ​!**", file=kenlogo, buttons=buttons)

        @ ken.tgbot.on(
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

        @ ken.tgbot.on(
            events.callbackquery.CallbackQuery(  # pylint:disable=E0602
                data=re.compile(rb"ub_modul_(.*)")
            )
        )
        async def on_plug_in_callback_query_handler(event):
            if event.query.user_id == uid:  # pylint:disable=E0602
                modul_name = event.data_match.group(1).decode("UTF-8")

                cmdhel = str(CMD_HELP[modul_name])
                if len(cmdhel) > 130:
                    help_string = (
                        str(CMD_HELP[modul_name]).replace(
                            '`', '')[:130] + "..."
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
