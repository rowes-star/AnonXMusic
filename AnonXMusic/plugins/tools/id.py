from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.enums import ChatMemberStatus, ChatMemberStatus
from AnonXMusic import app 

iddof = []
@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "")& filters.group)
async def iddlock(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("<b>الامر معطل من قبل .</b>")
      iddof.append(message.chat.id)
      return await message.reply_text("<b>تم تعطيل الايدي بنجاح .</b>")
   else:
      return await message.reply_text("<b>عذرا عزيزي هذا الامر للادمن الجروب فقط .</b>")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "")& filters.group)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("<b>الايدي مفعل من قبل .</b>")
      iddof.remove(message.chat.id)
      return await message.reply_text("<b>تم تفعيل الايدي بنجاح .</b>")
   else:
      return await message.reply_text("<b>عذرا عزيزي هذا الامر للادمن الجروب فقط .</b>")

@app.on_message(filters.command(["ايدي"], ""))
async def muid(client: Client, message):
       if message.chat.id in iddof:
         return await message.reply_text("<b>تم تعطيل امر الايدي من قبل المشرفين .</b>")
       user = await client.get_chat(message.from_user.id)
       user_id = user.id
       username = user.username
       first_name = user.first_name
       bioo = user.bio
       photo = user.photo.big_file_id
       photo = await client.download_media(photo)
       if not id.get(message.from_user.id):
         id[user.id] = []
       idd = len(id[user.id])
       await message.reply_photo(photo=photo, caption=f"<b>name : {first_name}\nid : {user_id}\nuser : [@{username}]\nbio : {bioo}</b>",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 💕", callback_data=f"heart{user_id}")],]),)
            


id = {}
@app.on_callback_query(filters.regex("heart"))  
async def heart(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("heart", "")  
    username = int(callback_request)
    usr = await client.get_chat(username)
    if not query.from_user.mention in id[usr.id]:
         id[usr.id].append(query.from_user.mention)
    else:
         id[usr.id].remove(query.from_user.mention)
    idd = len(id[usr.id])
    await query.edit_message_text(f"<b>name : {usr.first_name}\nid : {usr.id}\nuser : [@{usr.username}]\nbio : {usr.bio}</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{idd} 💕", callback_data=f"heart{usr.id}")]]))
