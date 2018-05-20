import asyncio
import logging

from discord.ext import commands

logger = logging.getLogger(f'SahibBot.{__name__}')
class TestLoad:
    """Test Cog"""

    def __init__(self,bot):
        self.bot = bot
        logger.debug('loaded')

    @commands.command(pass_context=True)
    async def testload(self, ctx):
        """Tests the loading function in discord.py"""

        await self.bot.say("TestLoad loaded successfully.")

def setup(bot):
    bot.add_cog(TestLoad(bot))
