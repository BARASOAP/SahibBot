# listen for ping on discord server (globally, all channels)
# Sends a ping to user's phone if outside of cooldown.
import asyncio
import logging
import sys
import traceback

import discord
from discord.ext import commands

import keys

# logging snippet
logger = logging.getLogger('SahibBot')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

discordBotToken = keys.botToken

bot = commands.Bot(command_prefix='!')

initial_extensions = (
    "cogs.testload",
    # "cogs.ping",
    "cogs.highlight",
    "cogs.error"
)

if __name__ == '__main__':
    logger.info('Loading Extensions...')
    for extension in initial_extensions:
        try:
            logger.debug(f'Loading {extension}')
            bot.load_extension(extension)
        except Exception as e:
            logger.warning(f'Failed to load extension {extension}.', exc_info=True)
    logger.info('Extensions Loaded.')

@bot.event
async def on_ready():
    logger.info(f'Ready! Logged in as {bot.user.name} {bot.user.id}')
    print(f'Logged in as {bot.user.name} {bot.user.id}\n------')

bot.run(discordBotToken)
