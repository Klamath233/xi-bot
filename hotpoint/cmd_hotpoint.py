import discord
import json
import asyncio
from .config import GOOGLE_API_KEY
import googlemaps
import datetime

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

def get_duration_to_hp(dt):
    routes = gmaps.directions("UCLA", 
        "8508 Valley Blvd, Ste 102", 
        mode="driving", 
        traffic_model="best_guess", 
        departure_time=dt)

    duration = routes[0]['legs'][0]['duration_in_traffic']

    return duration

async def exec_hotpoint(client, channel):
    
    half_hour = datetime.timedelta(minutes=30)
    an_hour = datetime.timedelta(hours=1)

    time = datetime.datetime.now()

    message = "Now: {}\n+30 min: {}\n+1 hour: {}\n+2 hours: {}".format(
        get_duration_to_hp(time)['text'],
        get_duration_to_hp(time + half_hour)['text'],
        get_duration_to_hp(time + an_hour)['text'],
        get_duration_to_hp(time + an_hour + an_hour)['text']
        )
    await client.send_message(channel, message)

