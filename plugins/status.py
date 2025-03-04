import os
import traceback
import logging

from pyrogram import Client
from pyrogram import StopPropagation, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import con


from plugins.check_user import handle_user_status
from plugins.database import Database

LOG_CHANNEL = con.LOG_CHANNEL
AUTH_USERS = con.AUTH_USERS
DB_URL = con.DB_URL
DB_NAME = con.DB_NAME





db = Database(DB_URL, DB_NAME)



@Client.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)




@Client.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂:** `{await db.total_users_count()}`\n\n**Total Users with Notification Enabled 🔔 :** `{await db.total_notif_users_count()}`",
        parse_mode="Markdown",
        quote=True
    )
