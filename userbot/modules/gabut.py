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
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG GOBLOKK!!!**")
# Pantun


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Salam Dulu Biar Sopan...**")
    sleep(2)
    await typew.edit("__السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ__")
# Salam


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Kalo Orang Salam Itu Dijawab Ya...**")
    sleep(2)
    await typew.edit("__وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ__")
# Menjawab Salam


@register(outgoing=True, pattern="^.kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ **Lu Semua Wibu**")
    sleep(2)
    await typew.edit("✅ **Lu Semua Wibu**")
    sleep(1)
    await typew.edit("☑️ **Tonic Ngentod**")
    sleep(2)
    await typew.edit("✅ **Tonic Ngentod**")
    sleep(1)
    await typew.edit("☑️ **Pariz Palkon**")
    sleep(2)
    await typew.edit("✅ **Pariz Palkon**")
    sleep(1)
    await typew.edit("☑️ **Kyy Buaya**")
    sleep(2)
    await typew.edit("✅ **Kyy Buaya**")
    sleep(1)
    await typew.edit("☑️ **Skyzo Ganteng**")
    sleep(2)
    await typew.edit("✅ **Skyzo Ganteng**")
    sleep(1)
    await typew.edit(
        "🔰 **Cuma Skyzo Yang Paling Waras, Baik Hati, Dan Tidak Sombong :v**"
    )


# King Userbot Support


@register(outgoing=True, pattern=r"^\.virtual(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**OOOO**")
    sleep(1.5)
    await typew.edit("**INI YANG VIRTUAL**")
    sleep(1.5)
    await typew.edit("**YANG KATANYA SAYANG BANGET**")
    sleep(1.5)
    await typew.edit("**TAPI TETEP AJA DI TINGGAL**")
    sleep(1.5)
    await typew.edit("**NI INGET**")
    sleep(1.5)
    await typew.edit("**TANGANNYA AJA GA BISA DI PEGANG**")
    sleep(1.5)
    await typew.edit("**APALAGI OMONGANNYA**")
    sleep(1.5)
    await typew.edit("**BHAHAHAHA**")
    sleep(1.5)
    await typew.edit("**KASIAN MANA MASIH MUDA**")


@register(outgoing=True, pattern="^.alay(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Halo kak**")
    sleep(1)
    await typew.edit("**Gua liat-liat lu main bot mulu**")
    sleep(2)
    await typew.edit("**Alay banget sumpah**")
    sleep(2)
    await typew.edit("**Baru pasang ucelbot ya?**")
    sleep(2)
    await typew.edit("**Pantesan norak yahaha**")
    sleep(2)
    await typew.edit("**Kalo mau coba coba command di gc pribadi aja**")
    sleep(2)
    await typew.edit("**Jangan di publik, jijik liatnya anjg:v**")
    sleep(2)
    await typew.edit("**Intinya lo alay maen bot mulu**")
    sleep(2)
    await typew.edit("**Lawriiiiiiieeeee:v")
# Alay maen bot mulu ngentot!


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")
# Istigfar


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")
# Perkenalan


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.alay`\
        \nUsage : Ngatain yang main bot mulu\
        \n\n Cmd : `.kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Memberi Salam\
        \n\n Cmd : `.virtual`\
        \nUsage: Buat Ngasi Tau Orang Virtual Awok\
        "
    }
)
