from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.gjm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK, JANGAN MAKSA LAH ANJEEENGGG!!!**")


@register(outgoing=True, pattern='^.yhh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAHAHA WAHYOOOOEEEEE**")


@register(outgoing=True, pattern='^.eg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH GOBLOK!!!**")


@register(outgoing=True, pattern='^.en(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH NGENTOTTT!!!**")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASTAGFIRULLAHALAZDIM....**")


@register(outgoing=True, pattern='^X(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GRUP SAMPAH KEK GINI MENDING BUBARIN AJA NGENTOT.**")


@register(outgoing=True, pattern='^.so(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SOK KERAS BANGET SI JAMET INI BHAAAKSSSS.**")


@register(outgoing=True, pattern='^O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JANGAN MAIN BOT MULU ALAY LU GOBLOK NORAK BANGET ANJING CUIHHHHH!!!**")


@register(outgoing=True, pattern='^D(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HEH LU BABU, HARUS SOPAN SAMA MAJIKAN LU GOBLOK. KERJA YANG BENER BIAR MAK LU KAGAK NGELONTE LAGI BUAT KASIH MAKAN LU TOLOL!!!**")


@register(outgoing=True, pattern='^F(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BHAAAAAAAAAKKKKKSSSSS**")


CMD_HELP.update({
    "salam2":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `F`\
\n↳ : Tersedak Meledek.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `X`\
\n↳ : Ngatain Grup.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.en`\
\n↳ : Coba Aja Sendiri Kontol.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ast`\
\n↳ : Istigfar.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gjm`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `eg`\
\n↳ : Coba Aja.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.yhh`\
\n↳ : Si Wahyu.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.so`\
\n↳ : Ngatain Orang Sok Keras.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `D`\
\n↳ : Cara Jadi Majikan Yang Benar.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `O`\
\n↳ : Ngatain Yang Main Bot Mulu."
})
