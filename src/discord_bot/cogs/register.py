import discord
from discord.ext import commands
from discord import app_commands
import os
import json
from src.get_info.atcoder_problems import renew
from src.get_info.get_atcoder_rating import get_atcoder_username
import time

class Register(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="register", description="指定したユーザーを登録してサーバーで読み込みます")
    @app_commands.describe(username="AtCoderのユーザー名")
    async def register(self, interaction: discord.Interaction, username: str):
        #登録済みかどうかを確認
        username = get_atcoder_username(username)
        if username == None:
            await interaction.response.send_message("通信に失敗したか、存在しないユーザーです")
            return
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "..", "..", "..", "data", "users")
        files = os.listdir(file_path)

        if username in files:
            await interaction.response.send_message("登録済みです")
            return

        file_path = os.path.join(file_path, username)
        os.mkdir(file_path)
        info_path = os.path.join(file_path, "info.json")
        ac_path = os.path.join(file_path, "ac.json")
        info = {"unix_second":0}
        with open (info_path, "w") as f:
            json.dump(info, f, indent=2)
        ac = dict()
        with open (ac_path, "w") as f:
            json.dump(ac, f, indent=2)


        await interaction.response.send_message("登録しています。処理のため一分ほどbotが応答できなくなります。")
       
        for i in range(20):
            renew(username)
            time.sleep(1)

        print("正しく実行されました")
        
            
    @app_commands.command(name="unregister", description="指定したユーザーの登録を解除してサーバー内のデータを削除します。")
    @app_commands.describe(username="AtCoderのユーザー名")
    async def unregister(self, interaction: discord.Interaction, username: str):
        #登録済みかどうかを確認
        username = get_atcoder_username(username)
        if username == None:
            await interaction.response.send_message("通信に失敗したか、存在しないユーザーです")
            return
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "..", "..", "..", "data", "users")
        files = os.listdir(file_path)
        if username not in files:
            await interaction.response.send_message("登録されていません。")
            return

        path = os.path.join(file_path, username)
        info_path = os.path.join(path, "info.json")
        ac_path = os.path.join(path, "ac.json")
        os.remove(info_path)
        os.remove(ac_path)
        os.rmdir(path)

        await interaction.response.send_message("削除しました。")
        
        
        
        
    


# BotにCogを登録
async def setup(bot: commands.Bot):
    await bot.add_cog(Register(bot))

