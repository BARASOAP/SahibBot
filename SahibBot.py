# listen for ping on discord server (globally, all channels)
# Sends a ping to user's phone if outside of cooldown.
import discord
import asyncio
import time
import keys

botName      = 'Yukkuri' 
# Eventually, we'll have Yukkuri talk more so 
# this will be a safemeasure so there are no infinite loops
# of Yukkuri talking to itself

directory = keys.directory 
discordBotToken = keys.botToken
discordClient = discord.Client()

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