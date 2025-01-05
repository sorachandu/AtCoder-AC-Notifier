import discord
from discord.ext import commands
from discord import app_commands
from src.get_info.get_atcoder_rating import get_atcoder_rating, get_atcoder_highest, get_atcoder_username

class AtCoderCog(commands.Cog):
    """AtCoder関連のコマンドを管理するCog"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="rating", description="指定したユーザーのAtCoderのratingを返します")
    @app_commands.describe(username="AtCoderのユーザー名")
    async def rating(self, interaction: discord.Interaction, username: str):
        username = get_atcoder_username(username) 
        if username == None:
            await interaction.response.send_message("通信に失敗したか存在しないユーザーです。")
            return
        info = get_atcoder_rating(username)
        if info == None:
            await interaction.response.send_message("通信に失敗したか、atcoderページの読み込みでエラーが発生しました。")
        else:
            await interaction.response.send_message(f"{username}のratingは{info}です")

    @app_commands.command(name="highest", description="指定したユーザーのAtCoderの最高ratingを返します")
    @app_commands.describe(username="AtCoderのユーザー名")
    async def highest(self, interaction: discord.Interaction, username: str):
        username = get_atcoder_username(username) 
        if username == None:
            await interaction.response.send_message("通信に失敗したか存在しないユーザーです。")
            return
        info = get_atcoder_highest(username)
        if info == None:
            await interaction.response.send_message("通信に失敗したか、atcoderページの読み込みでエラーが発生しました。")
        else:
            await interaction.response.send_message(f"{username}の最高ratingは{info}です")


# BotにCogを登録
async def setup(bot: commands.Bot):
    await bot.add_cog(AtCoderCog(bot))

