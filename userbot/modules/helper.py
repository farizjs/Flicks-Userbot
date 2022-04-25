""" 
Plugin : helper

Perintah : `{i}ghelp`
Penggunaan : bantuan Flicks-Userbot

Perintah : `{i}vars`
Penggunaan : melihat daftar vars Flicks-Userbot
"""
from userbot import CMD_HELP, ALIVE_NAME
from userbot import CMD_HANDLER
from userbot.utils import flicks_cmd


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@flicks_cmd(pattern="ghelp(?: |$)(.*)")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Owner](t.me/farizjs)"
        "\n[Repo](https://github.com/farizjs/Flicks-Userbot)"
        "\nTeam [Klick Here](https://t.me/devoloperflicks/32)")


@flicks_cmd(pattern="vars(?: |$)(.*)")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/farizjs/Flicks-Userbot/Flicks-Userbot/sample_config.env)")


CMD_HELP.update({"helper": f"{__doc__.format(i=CMD_HANDLER)}"})

