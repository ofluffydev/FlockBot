import os

from discord.ext import commands
from discord.ext.commands import Context, Cog

from github import get_github_repo


class BotCommands(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello! I\'m a bot.')

    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        latency = round(latency * 1000)
        await ctx.send(f'Pong! {latency}ms')

    @commands.command()
    async def contact(self, ctx):
        email = 'developmentflock@gmail.com'
        website = 'https://developmentflock.com'
        embed = self.bot.embed(title='Contact Information', description=f'Email: {email}\nWebsite: {website}')
        await ctx.send(embed=embed)

    @commands.command()
    async def prefix(self, ctx):
        if ctx.author.guild_permissions.administrator:
            self.bot.command_prefix = ctx.message.content.split()[1]
            await ctx.send(f'Prefix updated to {self.bot.command_prefix}')
        else:
            await ctx.send('You do not have permission to change the prefix.')

    @commands.command()
    async def filter(self, ctx):
        text = ctx.message.content.split()[1]
        await ctx.send(f'Filtering messages with {text}...')
        await ctx.channel.purge(limit=1000, check=lambda message: text in message.content not in message.author.bot)

    @commands.command()
    async def purge(self, ctx):
        amount = ctx.message.content.split()[1]
        await ctx.channel.purge(limit=int(amount) + 1)
        await ctx.send(f'Deleted {amount} messages.')

    @commands.command()
    async def github(self, ctx: Context):
        """
        Get the GitHub repo information and send it as an embed
        :param ctx: Context of the command
        :return: None
        """
        repo_owner = os.getenv('GITHUB_REPO_OWNER')
        repo_name = os.getenv('GITHUB_REPO_NAME')
        embed = get_github_repo(repo_owner, repo_name)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Process commands first, no need for any additional code since this happens automatically

        if not message.content.startswith(self.bot.command_prefix) and message.author != self.bot.user:
            message_str = message.content.lower()
            if message_str == 'hello' or message_str == 'hi':
                await message.channel.send('Hello!')
            elif message_str == 'meow':
                await message.channel.send('meow')
            elif message_str == 'woof':
                await message.channel.send('woof')
            elif 'furry' in message_str:
                await message.channel.send('uwu')


async def setup(bot):
    await bot.add_cog(BotCommands(bot))
