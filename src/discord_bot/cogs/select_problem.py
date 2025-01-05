import discord
from discord.ext import commands
from discord import app_commands
from src.get_info.select_problem import select_problem

class select_random(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="select", description="指定された範囲のdiffで指定されたユーザーがACしたことない問題を一つランダムに選びます")
    @app_commands.describe(min_diff="min diff", max_diff="max diff", username="username")
    async def select(self, interaction: discord.Interaction, min_diff:int, max_diff:int, username:str):
        ans = select_problem(min_diff,max_diff,username)
        await interaction.response.send_message(ans)
        



# BotにCogを登録
async def setup(bot: commands.Bot):
    await bot.add_cog(select_random(bot))

