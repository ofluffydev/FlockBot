from os import getenv

import discord
import dotenv
from discord.ext import commands
import asyncio

from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.load_extension('commands')

async def main():
    async with bot:
        load_dotenv()
        DISCORD_BOT_TOKEN = getenv('DISCORD_BOT_TOKEN')
        await bot.start(DISCORD_BOT_TOKEN)
