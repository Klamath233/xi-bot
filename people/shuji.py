import discord
import asyncio
import datetime
import tzlocal
import pytz

from util.state_predicates import person_just_joined

async def shuji_chishi_test(client, before, after):
    if person_just_joined('市委书记', before, after):
        if datetime.datetime.now().hour < 23 and datetime.datetime.now().hour > 6:
            channel = [c for c in client.get_all_channels() if c.name == 'general'][0]
            utc_dt = datetime.datetime.now(datetime.timezone.utc)
            # await client.send_message(channel, 'hi')
            await client.send_message(channel, '书记登录服务器的时间是{} 吃屎!'.format(utc_dt.astimezone(pytz.timezone('US/Pacific-New')).strftime('%H:%M:%S')))