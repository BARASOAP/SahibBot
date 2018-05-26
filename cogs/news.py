import asyncio
import aiohttp
import discord
from discord.ext import commands
import keys
from newsapi import NewsApiClient
from newsapi import const
from newsapi.newsapi_exception import NewsAPIException
import json

class news:
    """Grabs first top five news headlines from ______."""

    def __init__(self, bot):
        self.bot = bot
        self.directory = keys.directory
        self.NewsApiToken = keys.NewsApiToken
        # self.newsapi = NewsApiClient(api_key=keys.NewsApiToken)

    @commands.command(pass_context=True)
    async def news(self, ctx):
        # await self.bot.say(self.string1)
        
        # url = ('https://newsapi.org/v2/top-headlines?'
        # 'country=us&'
        # 'apiKey=' + self.NewsApiToken)
        # print("URL: " + url)

        newsapi = NewsApiClient(api_key=self.NewsApiToken)
        top_headlines = newsapi.get_top_headlines(q='bitcoin', sources='bbc-news,the-verge', category='business', language='en', country='us')
        
        # payload = {}
        # payload['q'] = q
        # payload['sources'] = sources
        # payload['language'] = language
        # payload['country'] = country
        # payload['category'] = category
        # payload['pageSize'] = page_size
        # payload['page'] = page

        r = requests.get(const.TOP_HEADLINES_URL, auth=newsapi, timeout=30, params=payload)
        if r.status_code != requests.codes.ok:
            raise NewsAPIException(r.json())

        return r.json()


def setup(bot):
    bot.add_cog(news(bot))