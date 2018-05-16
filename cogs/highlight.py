import asyncio
import discord
from discord.ext import commands

class Highlight:
    """Post messages with reactions on them to a highlight channel."""

    def __init__(self, bot):
        self.bot = bot
        self.highlight_channel = '446287440920182784'

    @commands.command(pass_context = True)
    async def hlstatus(self, ctx):
        # await self.bot.say(f'{__name__} is active')
        await self.bot.send_message(ctx.message.channel, 
            embed = discord.Embed(
                title = 'Highlight Status', 
                description = f'{__name__} is active',
                color = discord.Color.green()
            )
        )

    async def on_reaction_add(self, react, user):
        e = discord.Embed(
            description = f'{react.message.clean_content}',
            color = discord.Color.gold()
        )
        e.set_author(
                name = react.message.author.display_name,
                icon_url = react.message.author.avatar_url
            )
        c = ''
        for reaction in react.message.reactions:
            c = c + f'{reaction.emoji}{reaction.count} '
        await self.bot.send_message(self.bot.get_channel(self.highlight_channel), 
            # f'{user}: {react.message.channel} {react.emoji}'
            content = c,
            embed = e
        )

def setup(bot):
    bot.add_cog(Highlight(bot))