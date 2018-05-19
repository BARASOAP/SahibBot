import asyncio
import discord
from discord.ext import commands
import keys
import requests
# from newsapi import NewsAPI

class news:
    """Grabs first top five news headlines from ______."""

    def __init__(self, bot):
        self.bot = bot
        self.directory = keys.directory
        self.string1 = keys.string1
        # self.NewsApiToken = NewsApiClient(api_key=keys.NewsApiToken)
        
    async def news(self):
        await self.bot.say(self.string1)
        
        # url = ('https://newsapi.org/v2/top-headlines?'
        # 'country=us&'
        # 'apiKey=' + self.NewsApiToken)
        # response = requests.get(url)
        # print(response.json())

def setup(bot):
    bot.add_cog(news(bot))