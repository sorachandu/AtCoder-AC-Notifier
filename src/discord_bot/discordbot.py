import discord
from discord.ext import commands
import os


# Botの準備
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Cogを読み込む
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    cogs_dir = os.path.join(os.path.dirname(__file__), 'cogs')
    for filename in os.listdir(cogs_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            cog_name = f"src.discord_bot.cogs.{filename[:-3]}"
            try:
                await bot.load_extension(cog_name)  # cogsフォルダ内のcommand定義ファイルを全部読み込む
                print(f"Loaded {cog_name}")
            except Exception as e:
                print(f"Failed to load {cog_name}: {e}")
    print("Cogs loaded")
    # コマンドツリーの同期を行う
    await bot.tree.sync()
    print("Commands synced")

# トークンで起動
bot.run(os.environ["DISCORD_BOT_TOKEN"])

