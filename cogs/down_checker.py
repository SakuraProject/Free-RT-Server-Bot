# Free RT - down_check

from discord.ext import commands


class DownChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_id = 961521106227974174
        self.log_ch = 968025143253295145

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if after.id == self.bot_id and after.status == "offline":
            channel = self.bot.get_channel(self.log_ch)
            await channel.send(f"<@`{self.bot_id}>がダウンしました。")


async def setup(bot):
    await bot.add_cog(DownChecker(bot))
