import discord
import os

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

