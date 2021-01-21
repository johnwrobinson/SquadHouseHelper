import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!foo'):
        await message.channel.send('bar!')

    if message.content.startswith('!help'):
        await message.channel.send('There is no helping you.')

client.run(os.getenv("TOKEN"))
