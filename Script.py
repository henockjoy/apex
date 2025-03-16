class script(object):

    START_TXT = """𝖧𝖾𝗅𝗅𝗈 {}.𝖭𝗂𝖼𝖾 𝖬𝖾𝖾𝗍𝗂𝗇𝗀 𝖸𝗈𝗎.!!

𝖨'𝗆 𝖩𝗎𝗌𝗍 𝖺 𝖲𝗂𝗆𝗉𝗅𝖾 𝖺𝗇𝖽 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖠𝗎𝗍𝗈-𝖥𝗂𝗅𝗍𝖾𝗋𝖻𝗈𝗍. 𝖳𝗁𝖺𝗍 𝖼𝖺𝗇 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖺𝗇𝖽 𝗌𝖾𝗋𝗂𝖾𝗌 𝖤𝖺𝗌𝗂𝗅𝗒."""

    MY_ABOUT_TXT = """★ Server: <a href=https://www.app.koyeb.com>Koyeb</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>
★ Language: <a href=https://www.python.org>Python</a>
★ Library: <a href=https://pyrogram.org>Pyrogram</a>"""

    MY_OWNER_TXT = """★ Name: FT Admin
★ Username: @FTAdminbot
★ Country: India"""

    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
✨ Used Storage: <code>{}</code>
🗳 Free Storage: <code>{}</code>
🚀 Bot Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NOT_FILE_TXT = """👋 Hello {},

I can't find the <b>{}</b> in my database! 🥲

👉 Google Search and check your spelling is correct.
👉 Please read the Instructions to get better results.
👉 Or not been released yet."""
    
    EARN_TXT = """<b>📯 𝖣𝗂𝗌𝖼𝗅𝖺𝗂𝗆𝖾𝗋:</b>
<i>All the Files in this bot are freely available on the internet or posted by somebody else.

This bot is indexing files which are already uploaded on Internet or Telegram for easy of Searching.
We Respect all the Copyright Laws and works in Compilance With DMCA and EUCD.

If anything is against law please contact us so that it can be Removed ASAP.</i>"""

    HOW_TXT = """Nothing to see!!!"""

    IMDB_TEMPLATE = """<u><b>{title}</b></u>
    
‣ 𝖦𝖾𝗇𝗋𝖾𝗌: {genres}
‣ 𝖸𝖾𝖺𝗋: {year}
‣ 𝖱𝖺𝗍𝗂𝗇𝗀: {rating}/10
‣ 𝖱𝗎𝗇𝖳𝗂𝗆𝖾: {runtime} 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
‣ 𝖠𝖼𝗍𝗈𝗋𝗌: {cast}
‣ 𝖣𝗂𝗋𝖾𝖼𝗍𝗈𝗋: {director}

‣ 𝖯𝗅𝗈𝗍: {plot}

‣ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<code>||{file_name}||\n\n{file_caption}\n\nSize: {file_size}</code>

🚫 ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ 🚫"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/set_fsub - to set force subscribe channels
/remove_fsub - to remove all force subscribe channel</b>"""
    
    SOURCE_TXT = """<b>ʙᴏᴛ ɢɪᴛʜᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ -

- ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

- ꜱᴏᴜʀᴄᴇ - <a href=https://google.com/>ʜᴇʀᴇ</a>

- ᴅᴇᴠʟᴏᴘᴇʀ - @FTAdminbot"""

