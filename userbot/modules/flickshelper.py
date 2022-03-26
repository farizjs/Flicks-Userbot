""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot import CMD_HANDLER as cmd
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
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/fjgaming212/Flicks-Userbot/Flicks-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    f"`{cmd}ghelp`\
\nUsage: Bantuan Untuk Flicks-Userbot.\
\n`{cmd}vars`\
\nUsage: Melihat Daftar Vars."
})
