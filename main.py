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
    if user_message == '!scores' and channel == "wordle":
        scores = []
        users = []
        logs = await message.channel.history(limit=None).flatten()
        for i in logs:
            if '/6' in i.content:
                users.append(i.author.name)
                
        users = list(dict.fromkeys(users))
        for i in users:
            userScore = []
            for j in logs:
                if '/6' in j.content and 'X/6' not in j.content:
                    if i == j.author.name:
                        userScore.append(7-int(j.content.split(" ")[2].split("\n")[0].split("/")[0]))
            scores.append([i,sum(userScore)])
        scores = sorted(scores, key=lambda x: x[1],reverse=True)
        scores_string = "-----Wordle Leaderboard-----\n"
        for i in scores:
            scores_string = scores_string+i[0]+": "+str(i[1])+"\n"
        await message.channel.send(scores_string)
        

    if user_message == '!command':
        commands = "Blitz Bot Commands:\n!board - Show leaderboard of blitz in channel\n!blitz - Show current blitz"
        await message.channel.send(commands)
        return
    if user_message == '!board' and (channel == 'wordle' or channel == 'saltong'):
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
        blitz_embed = discord.Embed(
            colour = discord.Colour.green(),
            title = "Blitz Counter"
        )
        for i in range(len(lead_arr)):
            blitz_embed.add_field(value="#" + str(i+1) + "| " + str(lead_arr[i][0]) + " (" + str(lead_arr[i][1]) + ")\n")
        blitz_string = "-----{} Blitz Counter-----\n".format(channel)
        for i in lead_arr:
            blitz_string = blitz_string+i[0]+": "+str(i[1])+"\n"
        await message.channel.send(blitz_string)
        await message.channel.send(embed = blitz_embed)
        return
    if user_message == '!blitz' and (channel == 'wordle' or channel == 'saltong'):
        logs = await message.channel.history(limit=None).flatten()
        for i in logs:
            if 'X/6' in i.content:
                await message.channel.send(str(i.author.name)+" is the {} blitz haha".format(channel))
                return
    if channel == 'wordle':
        if 'X/6' in user_message:
            await message.channel.send(f'You are so stupid {name}!')
            return
    if channel == 'saltong':
        if 'X/6' in user_message:
            await message.channel.send(f'Napakatanga mo {name}!')
            return
    


client.run(TOKEN)
