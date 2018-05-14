# listen for ping on discord server (globally, all channels)
# Sends a ping to user's phone if outside of cooldown.
import discord
from discord.ext import commands
import asyncio
import keys
import sys,traceback

discordBotToken = keys.botToken

bot = commands.Bot(command_prefix='!')

initial_extensions = (
    "cogs.testload",
    "cogs.ping",
    "cogs.error"
)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} {bot.user.id}')
    print('------')

bot.run(discordBotToken)