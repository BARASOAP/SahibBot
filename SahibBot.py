# listen for ping on discord server (globally, all channels)
# Sends a ping to user's phone if outside of cooldown.
import discord
from discord.ext import commands
import asyncio
import keys
# from twilio.rest import Client

botName      = 'Yukkuri'
# Eventually, we'll have Yukkuri talk more so
# this will be a safemeasure so there are no infinite loops
# of Yukkuri talking to itself

directory = keys.directory
discordBotToken = keys.botToken

# twilioNumber = keys.twilioNumber
# twilioAccountSid = keys.twilioAccountSid
# twilioAuthToken = keys.twilioAuthToken

# twilioClient = Client(twilioAccountSid, twilioAuthToken)
bot = commands.Bot(command_prefix='!')

@commands.cooldown(1, 60 * 30, commands.cooldowns.BucketType.user)
@bot.command(pass_context = True)
async def ping(ctx, member: discord.Member):
    sent = False
    for user in directory:
        if user == member.mention:
            # twilioClient.messages.create(
            #     to    = directory[user],
            #     from_ = twilioNumber,
            #     body  = "{} has pinged you in discord!".format(message.author.name),
            # )
            print("Message Sent: '{} has pinged you in discord!'".format(
                ctx.message.author.name
                ))
            await bot.say("{}: Ping sent to {} at {}!".format(
                ctx.message.author.mention, 
                member.mention, 
                directory[user]
                ))
            sent = True
    if not sent:
        await bot.say("{}: I couldn't find {} in the directory.".format(
            ctx.message.author.mention,
            member.mention
            ))
        ping.reset_cooldown(ctx)

@bot.event
async def on_ready():
    print('Logged in as {} {}'.format(
        bot.user.name, 
        bot.user.id
        ))
    print('------')

@ping.error
async def ping_error(error, ctx):
    if (isinstance(error, commands.errors.BadArgument)) or (isinstance(error, commands.errors.MissingRequiredArgument)):
        await bot.say("{}: Please mention someone in your command.".format(
        	ctx.message.author.mention
        	))
    elif isinstance(error, commands.errors.CommandOnCooldown):
        m, s = divmod(error.retry_after, 60)
        await bot.say("{}: Cooldown for your user is active for {:.0f} minutes and {:.0f} seconds.".format(
            ctx.message.author.mention, m, s
        ))
    else:
    	print("Unhandled error for ping module: {}".format(error))

bot.run(discordBotToken)