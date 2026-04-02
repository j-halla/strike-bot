import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from bot.db import init_db

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN is not set in the .env file")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.polls = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await init_db()
    await bot.load_extension("bot.cogs.strike")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command()
async def sync(ctx):
    bot.tree.copy_global_to(guild=ctx.guild)
    await bot.tree.sync(guild=ctx.guild)
    await ctx.send("Commands synced.")

bot.run(TOKEN)
