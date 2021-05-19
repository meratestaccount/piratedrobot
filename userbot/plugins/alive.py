"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`PIRATED IS ONLINE MASTER`**\n\n"
                     "**PIRATED version:- 0.2.5 -BETAV2**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**✅Python: 3.7.3**\n"
                     "**Database Status: Databases functioning normally!**\n💞Always with you, my peru master!\n`"
                     f"`My peru owner`: {DEFAULTUSER}.")
