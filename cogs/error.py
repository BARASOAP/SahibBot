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
            await self.bot.send_message(ctx.message.channel, "{}: Please mention someone in your command.".format(
            	ctx.message.author.mention
            	))
        elif isinstance(error, commands.errors.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await self.bot.send_message(ctx.message.channel, "{}: Cooldown for your user is active for {:.0f} minutes and {:.0f} seconds.".format(
                ctx.message.author.mention, m, s
            ))
        elif isinstance(error, commands.errors.CommandNotFound):
            await self.bot.send_message(ctx.message.channel, "{}: {}".format(
                ctx.message.author.mention,
                error
            ))
        else:
        	print("Unhandled error: {}".format(error))

def setup(bot):
    bot.add_cog(Error(bot))