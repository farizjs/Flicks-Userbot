from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamu'alaikum Warohmatullahi Wabarokatuh.**")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SOKAP BANGET LU NAJIS ANJING GAUSAH REP REP CUIHHH!!!!**")


@register(outgoing=True, pattern='^W(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WAR WAR TAI ANJING!!! SOK SOK AN NANTANG WAR, EH KE TRIGGERED MINTA SHARE LOCK. PAS UDAH DI SHARE LOCK NGILANG. MENTAL KEK TAI BHAAAKSSS!!!!**")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**APAAN SI LU TOLOOLLLLL!!!!**")


@register(outgoing=True, pattern='^.pp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PASANG PP DULU LU NGENTOT BIAR SEMUA ORANG TAU MUKA LU YANG HINA ITU CUIHHHH!!!!**")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumssalam Warohmatullahi Wabarokatuh**")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT BANGET LU ANJEEEENGGGG!!!!**")


@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAUDAH IYAAIN AJA GOBLOK!!!**")


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK KEREN LU BEGITU GOBLOK, SINI KELUARGA LU GUA LUDAHIN SATU SATU...**")


CMD_HELP.update({
    "salam1":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.P`\
\n↳ : Untuk Memberi salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `G`\
\n↳ : Ngatain.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `A`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pp`\
\n↳ : Hina Yang Gapake PP.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `B`\
\n↳ : Buat Dikasih Ke Yang Banyak Bacot.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `W`\
\n↳ : Ngatain Anak Sok Ngewar.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `S`\
\n↳ : Ngatain Orang Sok Akrab.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Y`\
\n↳ : Kalo Debat Pake Aja.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.L`\
\n↳ : Untuk Menjawab Salam."
})
