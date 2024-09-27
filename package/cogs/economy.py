"""
Economy Cog

Example of a cog that is just an interface
"""

import discord
from discord.ext import commands


class Economy(commands.Cog):
    """Economy Interface for economy interactions."""

    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.ledger: dict[discord.Member | discord.User, int] = {}

    async def withdraw_money(
        self, member: discord.Member | discord.User, money: int
    ):
        """withdraw_money Withdraw money from user account.

        Args:
            member (discord.Member): A discord member of the guild.
            money (int): Amount of money.
        """

        if not self.ledger[member]:
            self.ledger[member] = 0
        self.ledger[member] -= money

    async def deposit_money(
        self, member: discord.Member | discord.User, money: int
    ):
        """deposit_money Deposit money into user account.

        Args:
            member (discord.Member): A discord member of the guild.
            money (int): Amount of money.
        """
        if not self.ledger[member]:
            self.ledger[member] = 0

        self.ledger[member] += money


async def setup(bot: commands.Bot):
    """setup Loads the cog.

    Args:
        bot (commands.Bot): Cog loader.
    """
    await bot.add_cog(Economy(bot=bot))
