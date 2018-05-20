import asyncio
import logging
import sys
import traceback

import discord
from discord.ext import commands

logger = logging.getLogger(f'SahibBot.{__name__}')

class Error:
    """Handle all the error conditions"""

    def __init__(self, bot):
        self.bot = bot
        logger.debug('loaded')

    async def on_command_error(self, error, ctx):
        if (isinstance(error, commands.errors.BadArgument)) or (isinstance(error, commands.errors.MissingRequiredArgument)):
            await self.bot.send_message(ctx.message.channel, f'{ctx.message.author.name}: Please mention someone in your command.')
            logger.info(f'BadArgument: \'{ctx.message.author.name}: {ctx.message.clean_content}\'')
        elif isinstance(error, commands.errors.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            await self.bot.send_message(ctx.message.channel, f'{ctx.message.author.name}: Cooldown for your user is active for {m:.0f} minutes and {s:.0f} seconds.')
            logger.info(f'CommandOnCooldown: \'{ctx.message.author.name}: {ctx.message.clean_content}\'')
        elif isinstance(error, commands.errors.CommandNotFound):
            await self.bot.send_message(ctx.message.channel, f'{ctx.message.author.name}: {error}')
            logger.info(f'CommandNotFound: \'{ctx.message.author.name}: {ctx.message.clean_content}\'')
        else:
            logger.error(f'Unhandled error:\n{error}')

def setup(bot):
    bot.add_cog(Error(bot))
