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
    if user_message == '!scores' and channel =="saltong":
        scores = []
        users = []
        await message.add_reaction('❤')
        logs = await message.channel.history(limit=None).flatten()
        for i in logs:
            if '/6' in i.content:
                users.append(i.author.name)
        print(list(logs[len(logs)-1].content.split(" ")[1])[4])        
        users = list(dict.fromkeys(users))
        for i in users:
            userScore = []
            for j in logs:
                if '/6' in j.content and 'X/6' not in j.content:
                    if i == j.author.name:
                        userScore.append(7-int(list(j.content.split(" ")[1])[4]))
            scores.append([i,sum(userScore)])
        scores = sorted(scores,key=lambda x: x[1],reverse=True)
        scores_embed = discord.Embed(
            colour = discord.Colour.green(),
            title = "Saltong Leaderboard"
        )
        scores_msg_rank = ""
        scores_msg_name = ""
        scores_msg_score = ""
        for i in range(len(scores)):
            scores_msg_rank = scores_msg_rank + "#" + str(i+1)+ "\n"
            scores_msg_name = scores_msg_name + str(scores[i][0])+ "\n"
            scores_msg_score = scores_msg_score + str(scores[i][1]) + "\n"
        scores_embed.add_field(name="Rank", value=scores_msg_rank)
        scores_embed.add_field(name="Name", value=scores_msg_name)
        scores_embed.add_field(name="Score", value=scores_msg_score)
        await message.channel.send(embed = scores_embed)
        return
    
    if user_message == '!scores' and channel == "wordle":
        scores = []
        users = []
        await message.add_reaction('❤')
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
        scores_embed = discord.Embed(
            colour = discord.Colour.green(),
            title = "Wordle Leaderboard"
        )
        scores_msg_rank = ""
        scores_msg_name = ""
        scores_msg_score = ""
        for i in range(len(scores)):
            scores_msg_rank = scores_msg_rank + "#" + str(i+1)+ "\n"
            scores_msg_name = scores_msg_name + str(scores[i][0])+ "\n"
            scores_msg_score = scores_msg_score + str(scores[i][1]) + "\n"
        scores_embed.add_field(name="Rank", value=scores_msg_rank)
        scores_embed.add_field(name="Name", value=scores_msg_name)
        scores_embed.add_field(name="Score", value=scores_msg_score)
        await message.channel.send(embed = scores_embed)
        return

    if user_message == '!command':
        commands = "Blitz Bot Commands:\n!board - Show leaderboard of blitz in channel\n!blitz - Show current blitz\n!scores - Show wordle leaderboards"
        await message.add_reaction('❤')
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
        blitz_msg_rank = ""
        blitz_msg_name = ""
        blitz_msg_ctr = ""
        for i in range(len(lead_arr)):
            blitz_msg_rank = blitz_msg_rank + "#" + str(i+1) + "\n"
            blitz_msg_name = blitz_msg_name + str(lead_arr[i][0]) + "\n"
            blitz_msg_ctr = blitz_msg_ctr + str(lead_arr[i][1]) + "\n"
        blitz_embed.add_field(name="Rank", value=blitz_msg_rank)
        blitz_embed.add_field(name="Name", value=blitz_msg_name)
        blitz_embed.add_field(name="Count", value = blitz_msg_ctr)
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
