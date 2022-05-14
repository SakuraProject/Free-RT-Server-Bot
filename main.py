# free RT - official server bot

from asyncio import run

import discord
from discord.ext import commands

from ujson import load


with open("secret.json") as f:
    secret = load(f)

intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="rs!",
    activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=f"起動準備",
    ),
    application_id=967729996221259836,
    status=discord.Status.dnd,
    intents=intents,
    help_command=None,
)
bot.secret = secret

@bot.listen()
async def setup_hook():
    for name in listdir("cogs"):
        if not name.startswith(("_", ".")):
            await bot.load_extension(f"cogs.{name[:-3] if name.endswith('.py') else name}")
    await bot.load_extension("jishaku")

@bot.listen()
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="free RT Server",
        ),
    )

async def main():
    await bot.start(bot.secret["TOKEN"])

run(main())
