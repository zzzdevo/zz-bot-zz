import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "**|| @MGIMT - ♥️ هەمیشە خودات لە بیربێت ||**",


             "**||@IQQUR - ♥️ اللهم صَلِّ عَلَى سیدنا مُحَمَّدٍ، وَعَلَى آلِ سیدنا مُحَمَّدٍ ||**",
            

             "**|| @xv7amo - 🖤👾 هەمیشە بەروو پێشەوە بڕۆ تا دەگەیت بە ئامانجت ||**",
            
           
 
            
            

        ]


        


@app.on_message(command(["سلاو","Slaw","slaw","سڵاو","سلام",".","!","بۆت","بوت"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
