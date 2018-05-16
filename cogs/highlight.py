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

        message_embed = discord.Embed(
            description = f'{react.message.clean_content}',
            color = discord.Color.gold()
        )
        message_embed.set_author(
                name = react.message.author.display_name,
                icon_url = react.message.author.avatar_url
            )

        reactions = ''
        for reaction in react.message.reactions:
            reactions = reactions + f'{reaction.emoji}{reaction.count} '

        await self.bot.send_message(self.bot.get_channel(self.highlight_channel),
            content = reactions,
            embed = message_embed
        )

def setup(bot):
    bot.add_cog(Highlight(bot))