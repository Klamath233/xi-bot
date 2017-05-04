import discord
import asyncio

def person_just_joined(name, before, after):
    return before.name == name and before.voice.voice_channel is None and after.voice.voice_channel is not None

def person_just_left(name, before, after):
    return before.name == name and after.voice.voice_channel is None and before.voice.voice_channel is not None