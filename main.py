import discord
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print('Blitz Bot is Online')
    
@client.event
async def on_message(message):
    name = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return
    logs = await message.channel.history(limit=10).flatten()
    print(logs.messages)
    if channel == 'wordle':
        if 'X/6' in user_message:
            await message.channel.send(f'You are so stupid {name}!')
            return
    if channel == 'saltong':
        if 'X/6' in user_message:
            await message.channel.send(f'Napakatanga mo {name}!')
            return
    


client.run(TOKEN)
