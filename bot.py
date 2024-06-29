from os import getenv

import discord
from discord import Client
from discord.ext.commands import Bot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

# Create client
DISCORD_APPLICATION_ID = getenv('DISCORD_APPLICATION_ID')
if DISCORD_APPLICATION_ID is None:
    raise ValueError('DISCORD_APPLICATION_ID is not set')
client = Client(intents=intents, application_id=DISCORD_APPLICATION_ID)

# Create bot
bot = Bot(command_prefix='/', intents=intents)

tree = bot.tree


@tree.command(
    name="commandname",
    description="My first application Command",
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")


@bot.event
async def on_ready():
    # Wait until the bot is fully connected to Discord
    await bot.wait_until_ready()

    print(f'{bot.user} has connected to Discord!')
    try:
        print('Loading commands')
        await bot.load_extension('commands')
    except Exception as e:
        print(f'Error while loading commands: {e}')

    print('About to sync tree')
    try:
        await bot.tree.sync()
    except Exception as e:
        print(f'Error while syncing tree: {e}')
    else:
        print('Tree synced')


async def main():
    async with bot:
        await bot.start(getenv('DISCORD_BOT_TOKEN'))


@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        welcome_message = f"Welcome {member.mention} to Flocks official development server! We are glad you could make it! Make sure to check out https://discord.com/channels/1256396414658023535/1256396415186239606 for rules and info!"
        await channel.send(welcome_message)
