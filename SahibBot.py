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
twilioNumber = keys.twilioNumber
twilioAccountSid = keys.twilioAccountSid
twilioAuthToken = keys.twilioAuthToken

# Initialize twilio and discord apis.
twilioClient = Client(twilioAccountSid, twilioAuthToken)
# discordClient = discord.Client()
bot = commands.Bot(command_prefix='!')

# First test command
@bot.command()
async def test(ctx):
    pass

# #Show Console we are logged in.
# @discordClient.event
# async def on_ready():
#     print('Logged in as ' + discordClient.user.name + " " + discordClient.user.id)
#     print('------')


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

# discordClient.run(discordBotToken)