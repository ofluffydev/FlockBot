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
        
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        welcome_message = f"Welcome {member.mention} to Flocks official development server! We are glad you could make it! Make sure to check out https://discord.com/channels/1256396414658023535/1256396415186239606 for rules and info!"
        await channel.send(welcome_message)
