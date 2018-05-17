import asyncio
import discord
from discord.ext import commands

class Highlight:
    """Post messages with reactions on them to a highlight channel."""

    def __init__(self, bot):
        self.bot = bot
        self.highlight_channel = '446287440920182784'
        self.message_bank = {}

    def create_embed(self, react, user):
        payload = discord.Embed(
            description = f'{react.message.clean_content}',
            color = discord.Color.gold(),
            timestamp = react.message.timestamp
        )
        payload.set_author(
            name = react.message.author.display_name,
            icon_url = react.message.author.avatar_url
        )
        return payload

    def create_content(self, react):
        reactions = ''
        for reaction in react.message.reactions:
            reactions = reactions + f'{reaction.emoji}{reaction.count} '
        return reactions

    @commands.command(pass_context = True)
    async def hlstatus(self, ctx):
        await self.bot.send_message(ctx.message.channel, 
            embed = discord.Embed(
                title = 'Highlight Status', 
                description = f'{__name__} is active',
                color = discord.Color.green()
            )
        )

    async def on_reaction_add(self, react, user):
        if react.message.author.id != self.bot.connection.user.id:
            if react.message in self.message_bank:
                await self.bot.edit_message(self.message_bank[react.message],
                    new_content = self.create_content(react),
                    embed = self.create_embed(react, user)
                )
            else:
                new_message = await self.bot.send_message(self.bot.get_channel(self.highlight_channel),
                    content = self.create_content(react),
                    embed = self.create_embed(react, user)
                )
                self.message_bank.update({react.message: new_message})
        else:
            pass

    async def on_reaction_remove(self, react, user):
        if len(react.message.reactions) == 0:
            if react.message in self.message_bank:
                await self.bot.delete_message(self.message_bank[react.message])
                del self.message_bank[react.message]
            else:
                pass
        else:
            await self.bot.edit_message(self.message_bank[react.message],
                new_content = self.create_content(react),
                embed = self.create_embed(react, user)
            )

def setup(bot):
    bot.add_cog(Highlight(bot))