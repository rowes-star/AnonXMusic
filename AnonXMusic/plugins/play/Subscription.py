from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button
from pyrogram.enums import ChatType
from pyrogram.errors import UserNotParticipant
from AnonXMusic import app
from config import ROWES


@app.on_message(filters.incoming & filters.private, group=-1)
async def subscription(app: Client, msg: Message):
    if not ROWES:
        return
    try:
        try:
            await app.get_chat_member(ROWES, msg.from_user.id)
        except UserNotParticipant:
            if ROWES.isalpha():
                link = "https://t.me/" + ROWES
            else:
                chat_info = await app.get_chat(ROWES)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"~︙عزيزي {msg.from_user.mention} \n~︙عليك الأشتراك في قناة البوت \n~︙قناة البوت : @{ROWES}.",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("「 اشترك هنا 」", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat {ROWES}!")
