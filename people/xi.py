import discord
import asyncio
import datetime
import tzlocal
import pytz

from util.state_predicates import person_just_joined, person_just_left

async def xi_greeting(client, before, after):
    if person_just_joined('Xi', before, after):
        channel = [c for c in client.get_all_channels() if c.name == 'general'][0]
        await client.send_message(channel, '你好，主人。')

async def xi_goodbye(client, before, after):
    if person_just_left('Xi', before, after):
        channel = [c for c in client.get_all_channels() if c.name == 'general'][0]
        await client.send_message(channel, '再见，主人。')