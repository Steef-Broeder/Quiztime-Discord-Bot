from unicodedata import name
import discord
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

reactions = {
    "Silly":"Ga lekker onder n truck liggen man",
    "xshadowshots":"Jaja hou je bek maar",
    "CoasterCrazy42":"Ik hoop dat je achtbaan breekt"
}

with open('config.json', 'r') as cfg:
  data = json.load(cfg) 

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name == 'bot-testing':
        if message.author.name != 'Broeder':
            try:
                await message.channel.send(reactions[message.author.name])
            except:
                await message.channel.send(f"Hou je bek {message.author.name}")

client.run(token=data["token"])