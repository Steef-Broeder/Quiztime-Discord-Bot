import discord
import os

client = discord.Client(intents=discord.Intents.default())
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

client.run(token=TOKEN)




