import os
import random
import discord
import clipperTwitch
import json

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
B_ID = os.getenv('BROADCASTER_ID')

bot = commands.Bot(command_prefix='!')

# @bot.command(name='roll_dice', help='Simulates rolling dice.')
# async def roll(ctx, number_of_dice: int, number_of_sides: int):
#     dice = [
#         str(random.choice(range(1, number_of_sides + 1)))
#         for _ in range(number_of_dice)
#     ]
#     await ctx.send(', '.join(dice))

# @bot.command(name='create-channel', help= 'Allows an admin to create a channel')
# @commands.has_role('admin')
# async def create_channel(ctx, channel_name='real-python'):
#     guild = ctx.guild
#     existing_channel = discord.utils.get(guild.channels, name=channel_name)
#     if not existing_channel:
#         print(f'Creating a new channel: {channel_name}')
#         await guild.create_text_channel(channel_name)

@bot.command(name='get-clip', help= 'Allows a user to grab first 5 clips from twitch')
async def get_clip(ctx):
    query= clipperTwitch.get_clips_query(B_ID)
    response= clipperTwitch.get_response(query)
    data = readJSON(response)['data']
    urls = [clip['url'] for clip in data]
    
    for url in urls:
        await ctx.send(url)
    


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

def readJSON(response):
    return response.json()


def runBot():  
    bot.run(TOKEN)
