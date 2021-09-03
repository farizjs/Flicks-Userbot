from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.pe(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamu'alaikum Warohmatullahi Wabarokatuh.**")


@register(outgoing=True, pattern='^.skp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SOKAP BANGET LU NAJIS ANJING GAUSAH REP REP CUIHHH!!!!**")


@register(outgoing=True, pattern='^.war(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WAR WAR TAI ANJING!!! SOK SOK AN NANTANG WAR, EH KE TRIGGERED MINTA SHARE LOCK. PAS UDAH DI SHARE LOCK NGILANG. MENTAL KEK TAI BHAAAKSSS!!!!**")


@register(outgoing=True, pattern='^.pp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PASANG PP DULU LU NGENTOT BIAR SEMUA ORANG TAU MUKA LU YANG HINA ITU CUIHHHH!!!!**")


@register(outgoing=True, pattern='^.wa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumssalam Warohmatullahi Wabarokatuh**")


@register(outgoing=True, pattern='^.ga(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK KEREN LU BEGITU GOBLOK, SINI KELUARGA LU GUA LUDAHIN SATU SATU...**")


CMD_HELP.update({
    "salam1":
    "Cmd: `.pe`\
\n↳ : Untuk Memberi salam.\
\n\nCmd: `.ga`\
\n↳ : Ngatain.\
\n\nCmd: `.pp`\
\n↳ : Coba Aja Sendiri.\
\n\nCmd: `.wa`\
\n↳ : Untuk Menjawab Salam."
})
