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


@register(outgoing=True, pattern='^.so(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SOK KERAS BANGET SI JAMET INI BHAAAKSSSS.**")


CMD_HELP.update({
    "salam2":
    "Cmd: `.en`\
\n↳ : Coba aja.\
\n\nCmd: `.ast`\
\n↳ : Istigfar.\
\n\nCmd: `.gjm`\
\n↳ : Coba Aja Sendiri.\
\n\nCmd: `eg`\
\n↳ : Coba Aja.\
\n\nCmd: `.yhh`\
\n↳ : Coba aja.\
\n\nCmd: `.so`\
\n↳ : Si sokap."
})
