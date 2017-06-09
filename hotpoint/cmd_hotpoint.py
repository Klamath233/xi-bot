import discord
import json
import asyncio
from .config import GOOGLE_API_KEY
import googlemaps
import datetime

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

async def exec_hotpoint(client, channel):
    routes = gmaps.directions("UCLA", 
        "8508 Valley Blvd, Ste 102", 
        mode="driving", 
        traffic_model="best_guess", 
        departure_time=datetime.datetime.now())

    duration = routes[0]['legs'][0]['duration_in_traffic']

    await client.send_message(channel, duration['text'])

