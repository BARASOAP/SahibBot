import asyncio
import logging

import discord
from discord.ext import commands
from twilio.rest import Client

import keys

logger = logging.getLogger(f'SahibBot.{__name__}')

class Ping:
    """Ping a user using the Twilio API."""

    def __init__(self, bot):
        self.bot = bot
        self.directory = keys.directory
        self.twilioNumber = keys.twilioNumber
        self.twilioClient = Client(keys.twilioAccountSid, keys.twilioAuthToken)
        logger.debug('loaded')
        
    @commands.cooldown(1, 60 * 30, commands.cooldowns.BucketType.user)
    @commands.command(pass_context = True)
    async def ping(self, ctx, member: discord.Member):
        sent = False
        for user in self.directory:
            if user == member.mention:
                self.twilioClient.messages.create(
                    to    = self.directory[user],
                    from_ = self.twilioNumber,
                    body  = f'{ctx.message.author.name} has pinged you in discord!'
                )
                await self.bot.say(f'{ctx.message.author.name}: Ping sent to {member.name} at {self.directory[user]}!')
                logger.info(f'OK! {ctx.message.author.name} -> {member.name}@{self.directory[user]}')
                sent = True
        if not sent:
            await self.bot.say(f'{ctx.message.author.name}: I couldn\'t find {member.name} in the directory.')
            logger.info(f'UserNotInDict: \'{member.name}\'')
            self.ping.reset_cooldown(ctx)

def setup(bot):
    bot.add_cog(Ping(bot))
