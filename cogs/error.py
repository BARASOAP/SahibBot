import asyncio
import traceback, sys
import discord
from discord.ext import commands

class Error:
    """Handle all the error conditions"""

    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, error, ctx):
        if (isinstance(error, commands.errors.BadArgument)) or (isinstance(error, commands.errors.MissingRequiredArgument)):
            await self.bot.send_message(ctx.message.channel, f'{ctx.message.author.name}: Please mention someone in your command.')
        elif isinstance(error, commands.errors.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await self.bot.send_message(ctx.message.channel, f'{ctx.message.author.name}: Cooldown for your user is active for {m:.0f} minutes and {s:.0f} seconds.')
        elif isinstance(error, commands.errors.CommandNotFound):
            await self.bot.send_message(ctx.message.channel, f'{ctx.message.author.name}: {error}')
        else:
        	print(f'Unhandled error: {error}')

def setup(bot):
    bot.add_cog(Error(bot))