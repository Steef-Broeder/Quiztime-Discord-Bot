import discord
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

with open('config.json', 'r') as cfg:
  data = json.load(cfg) 

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>Make'):
        await message.channel.send('Hello!')

client.run(token=data["discord_token"])