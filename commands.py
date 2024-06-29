from discord.ext import commands


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello! I\'m a bot.')

    @commands.command()
    async def ping(self, ctx):
        # Get the latency of the bot
        latency = self.bot.latency
        # Humanize the latency
        latency = round(latency * 1000)
        # Send the latency
        await ctx.send(f'Pong! {latency}ms')

    @commands.command()
    async def prefix(self, ctx):
        # Update the prefix if user is an admin
        if ctx.author.guild_permissions.administrator:
            self.bot.command_prefix = ctx.message.content.split()[1]
            await ctx.send(f'Prefix updated to {self.bot.command_prefix}')
        else:
            await ctx.send('You do not have permission to change the prefix.')


async def setup(bot):
    await bot.add_cog(BotCommands(bot))
