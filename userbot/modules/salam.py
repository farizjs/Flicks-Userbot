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
    await typew.edit("**SOKAP BANGET LU GAUSAH REP REP !!!!**")


@register(outgoing=True, pattern='^.war(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WAR WAR OI!!! SOK SOK AN NANTANG WAR, EH KE TRIGGERED MINTA SHARE LOCK. PAS UDAH DI SHARE LOCK NGILANG. MENTAL PANTUNGAN BHAAAKSSS!!!!**")


@register(outgoing=True, pattern='^.wa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumssalam Warohmatullahi Wabarokatuh**")


CMD_HELP.update({
    "salam1":
    "Cmd: `.pe`\
\n↳ : Untuk Memberi salam.\
\n\nCmd: `.skp`\
\n↳ : Ngatain.\
\n\nCmd: `.war`\
\n↳ : Coba Aja Sendiri.\
\n\nCmd: `.wa`\
\n↳ : Untuk Menjawab Salam."
})
