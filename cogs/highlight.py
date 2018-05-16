import asyncio
import discord
from discord.ext import commands

class Highlight:
    """Post messages with reactions on them to a highlight channel."""

    def __init__(self, bot):
        self.bot = bot
        self.highlight_channel = 446287440920182784

    @commands.command(pass_context = True)
    async def hlstatus(self, ctx):
        await self.bot.say(f'{__name__} is active')

    async def on_reaction_add(self, react, user):
        await self.bot.send_message(self.bot.get_channel(self.highlight_channel), f'```{user}: {react.message.channel} {react.emoji}```')

def setup(bot):
    bot.add_cog(Highlight(bot))