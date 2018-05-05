# listen for ping on discord server (globally, all channels)
# Sends a ping to user's phone if outside of cooldown.
import discord
from discord.ext import commands
import asyncio
import keys
import sys,traceback
# from twilio.rest import Client

directory = keys.directory
discordBotToken = keys.botToken

# twilioNumber = keys.twilioNumber
# twilioAccountSid = keys.twilioAccountSid
# twilioAuthToken = keys.twilioAuthToken

# twilioClient = Client(twilioAccountSid, twilioAuthToken)
bot = commands.Bot(command_prefix='!')

initial_extensions = (
    "cogs.testload",
    "cogs.error"
)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

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

bot.run(discordBotToken)