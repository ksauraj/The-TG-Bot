# For UniBorg
# Syntax .restart
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd


@borg.on(admin_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    await asyncio.sleep(2)
    await event.edit("Restarting./n████░░░░")
    await asyncio.sleep(2)
    await event.edit("Restarting./n██████░░")
    await asyncio.sleep(2)
    await event.edit("Restarted./nSend .alive or .ping to check if i am online./n████████")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()