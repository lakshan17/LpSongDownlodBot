improt os
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

Jebot = Client(
   "JESongBot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jebot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Hey {}, I'm Song Downloader Bot 🎵

😉 Just send me the song name you want to download.😋
      eg:/song Faded
      
A bot by @Lakshan_Pathum 🇱🇰</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "✍️Help👨‍💻", callback_data="help"),
                                        InlineKeyboardButton(
                                            "✅Channel✅", url="https://t.me/Lakshan_Pathum")
                                    ],[
                                      InlineKeyboardButton(
                                            "📦Source Code📦", url="https://github.com/lakshan17/LpSongDownlodBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jebot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Help Menu 
     /song {song name} - Download The Song🎧
     
    /song {youtube link} - Download The Song🎧</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            " 🔙  Back 🔙", callback_data="start"),
                                        InlineKeyboardButton(
                                            " 🌀About 🌀", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "📦 Source Code 📦", url="https://github.com/lakshan17/LpSongDownlodBot)
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
            
@Jebot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jebot.send_message(
               chat_id=message.chat.id,
               text="""<b>Song Download Bot🎧</b>

<b>🔥 Developer:</b> <a href="https://t.me/Lakshan_Pathum">Lakshan</a>

<b>🔥 Contact Me:</b> <a href="https://t.me/Lakshan_Pathum_Bot">My Assistant</a>

<b>🔥 Library:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙  Back 🔙  ", callback_data="help"),
                                        InlineKeyboardButton(
                                            "📦Source Code 📦", url="https://github.com/lakshan17/LpSongDownlodBot")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")   
            
@Jebot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)                              


app.start()
LOGGER.info("✅ mySongBot is online.")
idle()
