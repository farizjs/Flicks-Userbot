from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**LU KONTOL**")
    sleep(3)
    await typew.edit("**KONTOL KONTOL KONTOL!!!**")
    sleep(3)
    await typew.edit("**DASAR KEPALA KONTOL!!!**")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG GOBLOKK!!!**")
# Owner @Si_Dian


@register(outgoing=True, pattern='^ass(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Halo gaesss..**")
    sleep(2)
    await typew.edit("**ASSALAMU'ALAIKUM NGENTOT!!!**")
# Owner @manusiarakitann


@register(outgoing=True, pattern='^wss(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Jawab Salam Dulu Gaes**")
    sleep(2)
    await typew.edit("**WAALAIKUMSALAM GOBLOK!!!!!**")
# Owner @manusiarakitann


@register(outgoing=True, pattern='^Usage(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit("**Dyno Usage**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n" f"-> `Penggunaan Dyno ` **{ALIVE_NAME}**:\n" f" •**0 jam - " f"0 menit - 0%**" "\n ◐━─━─━─━─━──━─━─━─━─━◐\n" "-> `Sisa Dyno Bulan Ini`:\n" f" •**9999 jam - 9999 menit " f"- 100%**\n" "╰━━━━━━━━━━━━━━━━━━━━╯"
                     )
# @mixiologist


CMD_HELP.update({
    "fakedyno":
    "`Usage`\
\nUsage: tipu tipu anjeeeng.\
\n\n`kntl`\
\nUsage: Ngontolin Orang.\
\n\n`wss`\
\nUsage: Untuk Menjawab Salam.\
\n\n`.g`\
\nUsage: Member Goblok.\
\n\n`ass`\
\nUsage: Untuk Memberi Salam."
})
