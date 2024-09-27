"""
Gambling Cog

Example of how to reference another cog by name.
"""

import random
from discord.ext import commands

from .economy import Economy


class Gambling(commands.Cog):
    """Gambling Gambling system."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def coinflip(self):
        """coinflip Simulates a coinflip.

        Returns:
            int: Either 0 or 1.
        """
        return random.randint(0, 1)

    @commands.command()
    async def gamble(self, ctx: commands.Context, money: int):
        """Gambles some money."""

        economy = self.bot.get_cog("Economy")

        if economy is not None:
            assert isinstance(economy, Economy)
            await economy.withdraw_money(ctx.author, money)

            if self.coinflip() == 1:
                await economy.deposit_money(ctx.author, money * 2)


async def setup(bot: commands.Bot):
    """setup Loads the cog.

    Args:
        bot (commands.Bot): Cog loader.
    """
    await bot.add_cog(Gambling(bot=bot))
