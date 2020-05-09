import asyncio
import os
import random

import aiohttp
import discord
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks


def random_caps(string: str):
    return random.choice([string.upper(), string.lower()])


class FakeSplashes(commands.Cog, name="FakeSplashes"):
    def __init__(self, bot):
        self.bot = bot
        self.send_fake_splashes.start()

    def cog_unload(self):
        self.send_fake_splashes.cancel()

    @tasks.loop(minutes=3.0)
    async def send_fake_splashes(self):
        await asyncio.sleep(random.randint(0, 120))

        guild = self.bot.get_guild(int(os.environ.get("GUILD_ID")))
        channel = guild.get_channel(int(os.environ.get("PUBLIC_CHANNEL")))
        splash_role = guild.get_role(int(os.environ.get("SPLASH_ROLE")))
        splasher_role = guild.get_role(int(os.environ.get("SPLASHER_ROLE")))
        random_splasher = random.choice(splasher_role.members)
        webhook_url = os.environ.get("PUBLIC_CHANNEL_WEBHOOK")

        hub = random.choice(
            [
                f"mega{str(random.randint(1, 10)) + random.choice(['A', 'B', 'C', 'D'])} ",
                f"hub {str(random.randint(1, 28))} "
            ]
        )

        hub_locations = [
            "sven pond",
            "sven",
            "pond",
            "birch park",
            "carpetner",
            "wizard tower",
            "map",
            "gh",
            "guild house",
            "bank",
            "bank hole",
            "behind bazaar"
        ]

        location = hub + random.choice(hub_locations)

        join = random.choice(
            [
                f"/p join {random_splasher.name.split('#')[0]}",
                f"party join {random_splasher}",
                "walk",
                f"go to {location}"
            ]
        )

        fake_splash_text = f"**{random.randint(3, 7) * '='} {random_caps('splash')} {random.randint(3, 7) * '='}**\n" \
                           f"{random_caps('location')}: {location}\n" \
                           f"{random_caps('how can i join')}: {join}\n" \
                           f"{splash_role.mention}"

        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(webhook_url, adapter=AsyncWebhookAdapter(session))
            message = await webhook.send(
                content=fake_splash_text,
                username=random_splasher.name,
                avatar_url=random_splasher.avatar_url,
                allowed_mentions=discord.AllowedMentions(roles=False)
            )
        await channel.purge(limit=1)

    @send_fake_splashes.before_loop
    async def before_tasks(self):
        await self.bot.wait_until_ready()
