# Free RT - Q&A

import asyncio
import datetime

from discord.ext import commands
import discord


class FAQ(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Q&A")
    async def q_and_a(self, ctx):
        embed = discord.Embed(
            title="Free RTのQ&A",
            description="1️⃣: Free-RT-Botを入れられない\n\n2️⃣: その他の質問\n\n> **上記以外**\n<#962648434316296224>でtiketを立てて質問してください。",
            color=0x0066FF,
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        try:
            reaction, user = await self.bot.wait_for(
                "reaction_add", timeout=60.0,
                check=lambda r,u: u == ctx.author and str(r.emoji) in ["1️⃣", "2️⃣"]
            )
        except asyncio.TimeoutError:
            await msg.clear_reactions()
        else:
            if str(reaction.emoji) == "1️⃣":
                await ctx.send(
                    "botが認証されていないせいです。(ボットマークの横に:white_check_mark:がつく状態)\n今は100サーバー以上にbotを入れることができなくなっている状態です。\n申し訳ありませんが認証までお待ちください。",
                    delete_after=5.0
                )
            else:
                ch = self.bot.get_channel(967556131377545237)
                await ch.send(f"<@{ctx.author.id}>さんは質問があるみたいです。")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == 961521106227974174 or payload.channel_id != 967554887833509968:
            return
        if payload.emoji.name == "1️⃣":
            logchannel = self.bot.get_channel(967556039933304842)
            await logchannel.send(f"> <@{payload.user_id}>が1️⃣リアクションをつけました。\n{datetime.datetime.utcnow()}(UTC)")
            channel = self.bot.get_channel(967554887833509968)
            await channel.send(
                "botが認証されていないせいです。(ボットマークの横に:white_check_mark:がつく状態)\n今は100サーバー以上にbotを入れることができなくなっている状態です。\n申し訳ありませんが認証までお待ちください。",
                delete_after=5.0
            )
        if payload.emoji.name == "2️⃣":
            logchannel2 = self.bot.get_channel(967556039933304842)
            await logchannel2.send(f"> <@{payload.user_id}>が2️⃣リアクションをつけました。\n{datetime.datetime.utcnow()}(UTC)")
            channel2 = self.bot.get_channel(967556131377545237)
            await channel2.send(f"<@{payload.user_id}>さんは質問があるみたいです。")


async def setup(bot):
    await bot.add_cog(FAQ(bot))
