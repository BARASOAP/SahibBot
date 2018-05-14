import asyncio

from discord.ext import commands

class TestLoad:
    """Test Cog"""

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def testload(self, ctx):
        """Tests the loading function in discord.py"""

        await self.bot.say("TestLoad loaded successfully.")

def setup(bot):
    bot.add_cog(TestLoad(bot))