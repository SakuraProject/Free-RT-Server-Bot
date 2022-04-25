# Free RT - down_check

from discord.ext import commands


class Down_check(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if after.id == 961521106227974174:
            if after.status == "offline":
                channel = self.bot.get_channel(968025143253295145)
                await channel.send(f"<@961521106227974174>がダウンしました。")


async def setup(bot):
    await bot.add_cog(Down_check(bot))
