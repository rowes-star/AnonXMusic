import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
                
@app.on_message(
    command(["سيمو","اسلام","عم الكون","Simo","SIMO","eslam","ESLAM","المطور اسلام"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("DaRrKNneSs_1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\nNamE : {name}\nUseR : @{usr.username}\niD : {usr.id}\nBiO : {usr.bio}\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

@app.on_message(
    command(["رويس","روس","RoWeS","ROWES","rowes","Rowes"])
    & filters.group
)
@app.on_message(
    command(["‹ رويس ›"])
    & filters.private 
)
async def yas(client, message):
    usr = await client.get_chat("R7_OX")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\nNamE : {name}\nUseR : @{usr.username}\niD : {usr.id}\nBiO : {usr.bio}\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
@app.on_message(
    command(["بوت"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("AIleXaBoT")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"Hi My Name iS AleXa\n\nA Strong Telegram Bot To Play Music & Video iN The Voice Chat.\n\nJust Add Me To Your Group And Send /help . ", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/AIleXaBoT?startgroup=true")
                ],
            ]
        ),
    )

@app.on_message(
    command(["جينيص","GENIUS ","Genius"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("gs_y1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\nNamE : {name}\nUseR : @{usr.username}\niD : {usr.id}\nBiO : {usr.bio}\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )

@app.on_message(
    command(["رعد","الراعي","العباس"])
    & filters.group
)
async def yas(client, message):
    usr = await client.get_chat("QIIIlIP")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"\nNamE : {name}\nUseR : @{usr.username}\niD : {usr.id}\nBiO : {usr.bio}\n\n", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
