import aiohttp
import os
import discord
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands


class Bridge(commands.Cog, name="Bridge"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild.id != int(os.environ.get("GUILD_ID")):
            return
        if message.channel.id != int(os.environ.get("PUBLIC_BRIDGE_CHANNEL")):
            return

        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(os.environ.get("PUBLIC_CHANNEL_WEBHOOK"), adapter=AsyncWebhookAdapter(session))
            await webhook.send(
                message.content,
                username=message.author.name,
                avatar_url=message.author.avatar_url,
                allowed_mentions=discord.AllowedMentions(everyone=False)
            )