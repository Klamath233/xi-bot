import discord
import asyncio

from util.state_predicates import person_just_left
from util.time import get_formatted_timestamp_in_LA as timestamp
from alias.cmd_set_alias import exec_set_alias, get_alias

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
    pass


token = open('token', 'r')
client.run(token.read())
