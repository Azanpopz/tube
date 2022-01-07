from pyrogram import Client ,filters
import os
from py_youtube import Data, Search 
from pyrogram.types import *

from config import Config

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config")


    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	await message.reply_text("Helo iam Youtube Video Search\nUse in inline mode")
	


@Client.on_inline_query()
async def search_video(client,query):
	search = []
	result = Search(query.query.strip()).videos()
	for i in result:
		try:
			title = i["title"]
			id = i["id"]
			thumb = i["thumb"][0]
			data = i["simple_data"]
		except:
			pass
		try:
			search.append(
                InlineQueryResultPhoto(
                    title=title,
                    description=data,
                    caption="https://youtu.be/"+id,
                    photo_url=thumb))
		
		except:
		          pass
            
	await query.answer(search)
	
