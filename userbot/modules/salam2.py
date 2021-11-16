from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.sk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("__Shalom...__")


@register(outgoing=True, pattern='^.sh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("__Om Swastyastu__")


@register(outgoing=True, pattern='^.sb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("__Namo Buddhaya__")


@register(outgoing=True, pattern='^.skh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("__Salam kebajikan...__")


CMD_HELP.update({
    "salam2":
    "Cmd: `.sk`\
\n↳ : Salam Kristen/Katolik.\
\n\nCmd: `.sh`\
\n↳ : Salam Hindu.\
\n\nCmd: `.sb`\
\n↳ : Salam Budha.\
\n\nCmd: `.skh`\
\n↳ : Salam Konghucu."
})
