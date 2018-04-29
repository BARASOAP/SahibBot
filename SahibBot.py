# listen for messages on a discord server (globally, all channels)
# send to specified phone number if the message wasn't sent from the bot
import discord
import asyncio
import time

# discord.py has logging available: see docs. you probs won't need.

botName      = 'Yukkuri' # IMPORTANT! must be real bot username
#       otherwise you'll get infinite loops of the bot responding to itself

keysFile = open("keys.txt")
keys = keysFile.readlines()

# pull the discord bot token from 
discordBotToken = keys[0].rstrip()

###############################################################################
# auth client objects
discordClient = discord.Client()

directory = {<DICTIONARY OF EVERYONES PHONES AND @REPLY NAMES>}

@discordClient.event
async def on_ready():
    print('Logged in as ' + discordClient.user.name + " " + discordClient.user.id)
    print('------')

@discordClient.event
async def on_message(message):
    if message.content.startswith('!ping '):
        print("Message fits filter... {}: {}".format(message.author.name,message.content[6:]))
        #await discordClient.send_message(message.channel, "DEBUG OUT: Author:{} Mentions:{} Message:{} Match:{}".format(message.author.name, message.mentions, message.content, directory[message.mentions[0].mention]))

        # Only process the mentions if they only mention one user. List is unreliable otherwise. Functionality will change later.
        if len(message.mentions) == 1:
            print("MENTION PASS")
            for user in directory:
                print("{} {}".format(user, message.mentions[0].mention))
                if user == message.mentions[0].mention:
                    await discordClient.send_message(message.channel, "DEBUG OUT: User Found {}".format(directory[user]))
        else:
            await discordClient.send_message(message.channel, "ERR: Multiple mentions therefore list is unreliable.")


    #if message.author.name != botName:
    #    twilioClient.messages.create(
    #        to    = phoneNumber,
    #        from_ = twilioNumber,
    #        body  = "{} - {}".format(message.author.name,message.content),
    #    )
    #    print("sent message: {} - {}".format(message.author.name,message.content))

discordClient.run(discordBotToken)