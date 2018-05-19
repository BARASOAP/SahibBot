import asyncio
import discord
from discord.ext import commands
import keys
from newsapi import NewsApiClient
import json

class news:
    """Grabs first top five news headlines from ______."""

    def __init__(self, bot):
        self.bot = bot
        self.directory = keys.directory
        self.NewsApiToken = keys.NewsApiToken
    
    @commands.command(pass_context=True)
    async def news(self, ctx):
        # await self.bot.say(self.string1)
        
        url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=' + self.NewsApiToken)
        print("URL: " + url)


def setup(bot):
    bot.add_cog(news(bot))