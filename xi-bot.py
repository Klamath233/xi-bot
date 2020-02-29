import discord
import asyncio

from util.state_predicates import person_just_left
from util.time import get_formatted_timestamp_in_LA as timestamp
from alias.cmd_set_alias import exec_set_alias, get_alias

client = discord.Client()
voice_client = None

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
    global voice_client
    
    if message.content.startswith('!hello'):
        await message.channel.send('Hello, {}!'.format(get_alias(message.author.name, message.author.discriminator)))

    if message.content.startswith('!hotpoint'):
        await exec_hotpoint(client, message.channel)

    if message.content.startswith('!set_alias'):
        argv = message.content.split()
        if (len(argv) != 4):
            await message.channel.send('Insufficient number of arguments, 4 required.')
        elif not message.author.server_permissions.administrator:
            await message.channel.send('Not enough privilege.')
        else:
            await exec_set_alias(client, message.channel, argv[1], argv[2], argv[3])

    if message.content.startswith('!come'):
        channel = message.author.voice.channel

        if channel:
            if voice_client:
                await voice_client.disconnect()
            voice_client = None
            voice_client = await channel.connect()


    if message.content.startswith('!go'):
        if voice_client:
            await voice_client.disconnect()
            voice_client = None
    
    if 'xgnb' in message.content.lower():
        if voice_client and not voice_client.is_playing():
            voice_client.play(discord.FFmpegPCMAudio('assets/xgnb.mp3'))


@client.event
async def on_member_join(member):
    pass

@client.event
async def on_voice_state_update(member, before, after):
    pass


token = open('token', 'r')
client.run(token.read())
