import discord
import asyncio
import people.shuji
import people.xi

from util.state_predicates import person_just_left
from util.time import get_formatted_timestamp_in_LA as timestamp
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    for channel in client.get_all_channels():
        print(channel)

@client.event
async def on_message(message):
    
    if message.content.startswith('!hello'):
        await client.send_message(message.channel, 'Hello, {}!'.format(message.author))

@client.event
async def on_member_join(member):
    pass

@client.event
async def on_voice_state_update(before, after):

    channel = [c for c in client.get_all_channels() if c.name == 'general'][0]

    person_name = before.name

    if not person_just_left(person_name, before, after):
        if after.voice.voice_channel != before.voice.voice_channel:
            await client.send_message(channel, '{} 欢迎`{}`加入频道`{}`!'.format(timestamp(), person_name, after.voice.voice_channel))
    else:
        await client.send_message(channel, '{} 恭送`{}`！'.format(timestamp(), person_name))

    await people.shuji.shuji_chishi_test(client, before, after)
    await people.xi.xi_greeting(client, before, after)
    await people.xi.xi_goodbye(client, before, after)

token = open('token', 'r')
client.run(token.read())
