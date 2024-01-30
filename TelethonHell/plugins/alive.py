import datetime
import random
import time
from unicodedata import name

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from TelethonHell.DB.gvar_sql import gvarstat, addgvar
from TelethonHell.plugins import *

# -------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>⚡️𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥-𝗕𝗢𝗧⚡️</i></b>

<b><i> 𝗢ᴡɴᴇʀ:</i></b> : 『 {hell_mention} 』
╭──────────────
┣─ <b>»𝗧ᴇʟᴇᴛʜᴏɴ:</b> <i>{telethon_version}</i>
┣─ <b>»𝗦ᴛʀᴀɴɢᴇʀ:</b> <i>{hellbot_version}</i>
┣─ <b>»𝗦ᴜᴅᴏ:</b> <i>{is_sudo}</i>
┣─ <b>»𝗨ᴘᴛɪᴍᴇ:</b> <i>{uptime}</i>
┣─ <b>»𝗣ɪɴɢ:</b> <i>{ping}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/SHIVANSH474'>⚡️𝗖𝗛𝗔𝗡𝗡𝗘𝗟⚡️</a> «««</i></b>
<b><i>⛧ <a href='https://t.me/mastiwithfriendsx'>⚡️𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️</a> ⛧</i></b>
<b><i>⛧ <a href='https://t.me/SHIVANSH39'>⚡️𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛-𝗫𝗗⚡️</a> ⛧</i></b>
"""

msg = """{}\n
<b><i>⚡️𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥-𝗕𝗢𝗧⚡️</b></i>
<b>𝗧ᴇʟᴇᴛʜᴏɴ ≈</b>  <i>{}</i>
<b>𝗦ᴛʀᴀɴɢᴇʀ ≈</b>  <i>{}</i>
<b>𝗨ᴘᴛɪᴍᴇ ≈</b>  <i>{}</i>
<b>𝗔ʙᴜsᴇ ≈</b>  <i>{}</i>
<b>𝗦ᴜᴅᴏ ≈</b>  <i>{}</i>
"""
# -------------------------------------------------------------------------------


@hell_cmd(pattern="alivetemp$")
async def set_alive_temp(event):
    hell = await eor(event, "`Fetching template ...`")
    reply = await event.get_reply_message()
    if not reply:
        alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
        to_reply = await hell.edit("Below is your current alive template 👇")
        await event.client.send_message(event.chat_id, alive_temp, parse_mode=None, link_preview=False, reply_to=to_reply)
        return
    addgvar("ALIVE_TEMPLATE", reply.text)
    await hell.edit(f"`ALIVE_TEMPLATE` __changed to:__ \n\n`{reply.text}`")


@hell_cmd(pattern="alive$")
async def _(event):
    start = datetime.datetime.now()
    userid, hell_user, hell_mention = await client_id(event, is_html=True)
    hell = await eor(event, "`Ruk Jra Sabar Karo 🫴🥺❤️‍🩹`")
    reply = await event.get_reply_message()
    uptime = await get_time((time.time() - StartTime))
    name = gvarstat("ALIVE_NAME") or hell_user
    alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://graph.org/file/c6a2ed96648fd03377dc9.jpg"
    end = datetime.datetime.now()
    ping = (end - start).microseconds / 1000
    alive = alive_temp.format(
        hell_mention=hell_mention,
        telethon_version=telethon_version,
        hellbot_version=hellbot_version,
        is_sudo=is_sudo,
        uptime=uptime,
        ping=ping,
    )
    await event.client.send_file(
        event.chat_id,
        file=PIC,
        caption=alive,
        reply_to=reply,
        parse_mode="HTML",
    )
    await hell.delete()


@hell_cmd(pattern="shivop$")
async def hell_a(event):
    userid, _, _ = await client_id(event)
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>⚡️𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥-𝗕𝗢𝗧⚡️</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == userid:
            await event.delete()
    except (noin, dedbot):
        await eor(
            event,
            msg.format(am, telethon_version, hellbot_version, uptime, abuse_m, is_sudo),
            parse_mode="HTML",
        )


CmdHelp("alive").add_command(
    "alive", None, "Shows the default Alive message."
).add_command(
    "shivop", None, "Shows inline Alive message."
).add_warning(
    "✅ Harmless Module"
).add()
