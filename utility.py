import os

from discord.ext.commands import Context


async def print_stats(ctx: Context):
    await ctx.send('Getting bot latency...')
    bot_latency = ctx.bot.latency
    await ctx.send('Getting bot version...')
    bot_prefix = ctx.bot.command_prefix
    await ctx.send('Getting bot guilds...')
    bot_guilds = len(ctx.bot.guilds)
    await ctx.send('Getting bot users...')
    bot_users = len(ctx.bot.users)
    await ctx.send('Getting bot commands...')
    bot_commands = len(ctx.bot.commands)
    await ctx.send('Getting bot cogs...')

    embed_color = os.getenv('EMBED_COLOR')
    text = f'Bot Latency: {bot_latency}\n' \
           f'Bot Prefix: {bot_prefix}\n' \
           f'Bot Guilds: {bot_guilds}\n' \
           f'Bot Users: {bot_users}\n' \
           f'Bot Commands: {bot_commands}\n'
    await ctx.send('Creating embed...')
    embed = ctx.bot.embed(title='Bot Stats', description=text, color=embed_color)
    return embed
