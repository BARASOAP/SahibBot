import asyncio
import discord
from discord.ext import commands
import keys
from newsapi import NewsApiClient
from newsapi.newsapi_exception import NewsAPIException
import requests
import json

#   Bot command which retrieves JSON file from a NewsAPI.org and displays the top 5 popular articles from Google News.
class news:

    def __init__(self, bot):
        self.bot = bot
        self.directory = keys.directory
        self.NewsApiToken = keys.NewsApiToken

    @commands.command(pass_context=True)
    async def news(self, ctx):
        
        #   Generates a valid URL with the desired parameters and valid NewsApiToken. Currently hardcoded the parameters.
        url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&' +
        'published_at.start=NOW-1DAYS%2FDAY&published_at.end=NOW&' +
        'source.name[]=Google+News&' +
        'language=en&' +
        'sort_by=popularity&' +
        'pageSize=5&' +
        'apiKey=' + self.NewsApiToken)

        #   HTTP GET request to retrieve data from URL generated from the previous block of code
        r = requests.get(url, timeout=5)

        #   Raises an exception if the status of the HTTP request is not 'OK' (<StatusCode: 200> = OK)
        if r.status_code != 200:
            raise NewsAPIException(r.json())
        else:
            json_data = r.json()
            
            #   Loop that commands the discord bot to print each article URL
            for x in json_data['articles']:
                await self.bot.say('--------------------------------------------------------------------------------------------------------------')
                await self.bot.say(x['url'])

def setup(bot):
    bot.add_cog(news(bot))