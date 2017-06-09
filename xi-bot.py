import discord
import asyncio
import people.shuji
import people.xi

from util.state_predicates import person_just_left
from util.time import get_formatted_timestamp_in_LA as timestamp
from alias.cmd_set_alias import exec_set_alias, get_alias
from hotpoint.cmd_hotpoint import exec_hotpoint

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    # for member in client.get_all_members():
    #     print(member.server_permissions.administrator)

@client.event
async def on_message(message):
    
    if message.content.startswith('!hello'):
        await client.send_message(message.channel, 'Hello, {}!'.format(message.author))

    if message.content.startswith('!hotpoint'):
        await exec_hotpoint(client, message.channel)

    if message.content.startswith('!set_alias'):
        argv = message.content.split()
        if (len(argv) != 4):
            await client.send_message(message.channel, 'Insufficient number of arguments, 4 required.')
        elif not message.author.server_permissions.administrator:
            await client.send_message(message.channel, 'Not enough privilege.')
        else:
            await exec_set_alias(client, message.channel, argv[1], argv[2], argv[3])

@client.event
async def on_member_join(member):
    pass

@client.event
async def on_voice_state_update(before, after):

    channel = [c for c in client.get_all_channels() if c.name == 'general'][0]

    person_name = before.name
    person_discriminator = before.discriminator

    if not person_just_left(person_name, before, after):
        if after.voice.voice_channel != before.voice.voice_channel:
            await client.send_message(channel, '{} 欢迎`{}`加入频道`{}`!'.format(timestamp(), get_alias(person_name, person_discriminator), after.voice.voice_channel))
    else:
        await client.send_message(channel, '{} 恭送`{}`！'.format(timestamp(), get_alias(person_name, person_discriminator)))

    await people.shuji.shuji_chishi_test(client, before, after)
    await people.xi.xi_greeting(client, before, after)
    await people.xi.xi_goodbye(client, before, after)

token = open('token', 'r')
client.run(token.read())
