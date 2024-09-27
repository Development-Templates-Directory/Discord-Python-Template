"""
An example discord cog for greeting.
"""

import discord
from discord.ext import commands


class Greetings(commands.Cog):
    """Greetings A cog grouping features related to greeting."""

    _last_member: discord.Member | None

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """on_member_join Handler of member joining the guild event.

        Args:
            member (discord.Member): A discord guild member.
        """
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member.mention}.")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member | None = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"Hello {member.name}~")
        else:
            await ctx.send(f"Hello {member.name}... This feels familiar.")
        self._last_member = member


async def setup(bot: commands.Bot):
    """setup Loads the cog.

    Args:
        bot (commands.Bot): Cog loader.
    """
    await bot.add_cog(Greetings(bot=bot))
