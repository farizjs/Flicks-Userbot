from time import sleep
from platform import uname
from userbot import ALIVE_NAME, WEATHER_DEFCITY, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG GOBLOKK!!!**")
# Pantun


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0, 1)
    await typew.edit(f"**Halo gaesss..**")
    sleep(1)
    await typew.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")
# Salam


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0, 1)
    await typew.edit(f"**Jawab Salam Dulu Gaes**")
    sleep(2)
    await typew.edit("**وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")
# Menjawab Salam


@register(outgoing=True, pattern='^.usangen(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit("**Dyno Usage**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n" f"-> `Penggunaan Dyno ` **{DEFAULTUSER}**:\n" f" •**0 jam - " f"0 menit - 0%**" "\n ◐━─━─━─━─━──━─━─━─━─━◐\n" "-> `Sisa Dyno Bulan Ini`:\n" f" •**9999 jam - 9999 menit " f"- 100%**\n" "╰━━━━━━━━━━━━━━━━━━━━╯"
                     )
# Dyno fake


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"**Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}**")
    sleep(2)
    await event.edit(f"**Gw Tinggal Di {WEATHER_DEFCITY}**")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")
# Perkenalan


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.usangen`\
        \nUsage : Dyno fake\
        \n\n 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.perkenalan`\
        \nUsage : Memperkenalkan Diri\
        \n\n 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.g`\
        \nUsage : Member Goblok\
        \n\n 𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
