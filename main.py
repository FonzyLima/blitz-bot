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

    if user_message == '!blitz':
        blitz_arr = []
        lead_arr = []
        visited = []
        logs = await message.channel.history(limit=None).flatten()
        for i in logs:
            if 'X/6' in i.content:
                blitz_arr.append(i.author.name)
        for i in blitz_arr:
            if i not in visited:
                lead_arr.append([i,blitz_arr.count(i)])
                visited.append(i)
        lead_arr = sorted(lead_arr, key=lambda x: x[1],reverse=True)
        blitz_string = "-----{} Blitz Counter-----\n".format(channel)
        for i in lead_arr:
            blitz_string = blitz_string+i[0]+": "+str(i[1])+"\n"
        await message.channel.send(blitz_string)
                


    if channel == 'wordle':
        if 'X/6' in user_message:
            await message.channel.send(f'You are so stupid {name}!')
            return
    if channel == 'saltong':
        if 'X/6' in user_message:
            await message.channel.send(f'Napakatanga mo {name}!')
            return
    


client.run(TOKEN)
