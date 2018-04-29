# listen for ping on discord server (globally, all channels)
# Sends a ping to user's phone if outside of cooldown.
import discord
from discord.ext import commands
import asyncio
import time
import keys
from twilio.rest import Client

botName      = 'Yukkuri'
# Eventually, we'll have Yukkuri talk more so
# this will be a safemeasure so there are no infinite loops
# of Yukkuri talking to itself

#Importing keys
directory = keys.directory
discordBotToken = keys.botToken

# requires twilio account and API keys.
# twilioNumber = keys.twilioNumber
# twilioAccountSid = keys.twilioAccountSid
# twilioAuthToken = keys.twilioAuthToken

# Initialize twilio and discord apis.
# twilioClient = Client(twilioAccountSid, twilioAuthToken)
# discordClient = discord.Client()
bot = commands.Bot(command_prefix='!')

# First test command
@bot.command(pass_context = True)
async def ping(ctx, *, member : discord.Member = None):
    if member is None:
        await bot.say(ctx.message.author.mention + ": A person is needs to be included when pinging someone!")
    else:
    # if len(message.mentions) == 1:
        print("MENTION PASS")
        print("User " + ctx.message.author.name + "(" + ctx.message.author.id + ")" + " is mentioning " + member.name + "(" + member.id + ")")
        for user in directory:
            if user == member.id:
                await bot.say("DEBUG OUT: User Found {}".format(directory[user]))
                # twilioClient.messages.create(
                #     to    = directory[user],
                #     from_ = twilioNumber,
                #     body  = "{} has pinged you in discord!".format(message.author.name),
                # )
                print("Message Sent: '{} has pinged you in discord!'".format(ctx.message.author.name))
                await bot.say(ctx.message.author.mention + ": Successfully pinged " + member.name + "(" + member.id + ")" + " at {}".format(directory[user]))

#Show Console we are logged in.
@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + " " + bot.user.id)
    print('------')


# @discordClient.event
# async def on_message(message):
#     if message.content.startswith('!ping '):
#         print("Message fits filter... {}: {}".format(message.author.name,message.content[6:]))

#         # Only process the mentions if they only mention one user. List is unreliable otherwise. Functionality will change later.
#         if len(message.mentions) == 1:
#             print("MENTION PASS")
#             for user in directory:
#                 if user == message.mentions[0].mention:
#                     await discordClient.send_message(message.channel, "DEBUG OUT: User Found {}".format(directory[user]))
#                     twilioClient.messages.create(
#                         to    = directory[user],
#                         from_ = twilioNumber,
#                         body  = "{} has pinged you in discord!".format(message.author.name),
#                     )
#                     print("Message Sent: '{} has pinged you in discord!'".format(message.author.name))
#         else:
#             await discordClient.send_message(message.channel, "ERR: Multiple mentions therefore list is unreliable.")

bot.run(discordBotToken)