# free RT - official server bot

from asyncio import run

import discord
from discord.ext import commands

from ujson import load


with open("secret.json") as f:
    secret = load(f)

bot = commands.Bot("rs!", help_command=None)
bot.secret = secret


async def main():
    await bot.start(bot.secret["TOKEN"])

run(main())
