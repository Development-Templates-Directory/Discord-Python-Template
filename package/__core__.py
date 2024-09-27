"""
Core loader of the discord cogs.
"""

import os

from discord import Intents
from discord.ext import commands

from .utils.logger import logger


class Core(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!", intents=Intents.all())

    async def on_ready(self):
        await self.tree.sync()
        logger.info("Bot is ready!")

    async def setup_hook(self):
        for filename in os.listdir("./package/cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"package.cogs.{filename[:-3]}")
                logger.info(f"#{filename[:-3]} cog loaded.")
