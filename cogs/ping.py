import asyncio
import discord
from discord.ext import commands
import keys
from twilio.rest import Client

class Ping:
    """Handle all the error conditions"""

    def __init__(self, bot):
        self.bot = bot
        self.directory = keys.directory
        self.twilioNumber = keys.twilioNumber
        self.twilioClient = Client(keys.twilioAccountSid, keys.twilioAuthToken)
        print("!!!Warning: Twilio Client is LIVE!!!")
        
    @commands.cooldown(1, 60 * 30, commands.cooldowns.BucketType.user)
    @commands.command(pass_context = True)
    async def ping(self, ctx, member: discord.Member):
        sent = False
        for user in self.directory:
            if user == member.mention:
                self.twilioClient.messages.create(
                    to    = self.directory[user],
                    from_ = self.twilioNumber,
                    body  = "{} has pinged you in discord!".format(ctx.message.author.name),
                )
                print("Message Sent: '{} has pinged you in discord!'".format(
                    ctx.message.author.name
                    ))
                await self.bot.say("{}: Ping sent to {} at {}!".format(
                    ctx.message.author.mention, 
                    member.mention, 
                    self.directory[user]
                    ))
                sent = True
        if not sent:
            await self.bot.say("{}: I couldn't find {} in the directory.".format(
                ctx.message.author.mention,
                member.mention
                ))
            self.bot.cooldown.reset_cooldown(ctx)

def setup(bot):
    bot.add_cog(Ping(bot))