import discord
import discord.app_commands
import os
from get_info.get_atcoder_rating import get_atcoder_rating

intents = discord.Intents.default()
intents.message_content = True  # これが必要
token = os.environ["DISCORD_BOT_TOKEN"]
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client) #←ココ

@tree.command(name="rating", description="atcoderのratingを答えます")
@discord.app_commands.describe(username="atcoderのusername")
async def rating_command(ctx,username:str):
    info = get_atcoder_rating(username)
    if info:
        await ctx.response.send_message(f"{info[2]}のratingは{info[0]}です")
    else:
        await ctx.response.send_message("error")

@tree.command(name="highest", description="atcoderのhighestを答えます")
@discord.app_commands.describe(username="atcoderのusername")
async def rating_command(ctx,username:str):
    info = get_atcoder_rating(username)
    if info:
        await ctx.response.send_message(f"{info[2]}のhighestは{info[1]}です")
    else:
        await ctx.response.send_message("error")

    

@client.event
async def on_ready():
    await tree.sync()
    print("ready")
client.run(token)

