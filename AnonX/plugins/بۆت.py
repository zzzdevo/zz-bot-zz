import asyncio


import random
from AnonX import app
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from strings.filters import command
from pyrogram import filters, Client
import config



txt = [

            "**|| هەمیشە خودات لە بیربێت♥️! - [کەناڵەکەم](https://t.me/MGIMT) ||**",


             "**|| اللهم صَلِّ عَلَى سیدنا مُحَمَّدٍ، وَعَلَى آلِ سیدنا مُحَمَّدٍ🖤! - [کەناڵی قورئان](https://t.me/IQQUR) ||**",
            

             "**|| **هەمیشە بەروو پێشەوە بڕۆ تا دەگەیت بە ئامانجت👾🖤! - [جوانترین کەناڵ](https://t.me/xv7amo) ||**",
            
           
 
            
            

        ]


        


@app.on_message(command(["سلاو","Slaw","slaw","سڵاو","سلام",".","!","بۆت","بوت"]))


async def cutt(client: Client, message: Message):


      a = random.choice(txt)


      await message.reply(


        f"{a}")
