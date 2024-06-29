import os

from discord.ext.commands import Context


async def print_stats(ctx: Context):
    bot_latency = ctx.bot.latency
    bot_up_time = ctx.bot.up_time
    bot_version = ctx.bot.version
    bot_prefix = ctx.bot.command_prefix
    bot_guilds = len(ctx.bot.guilds)
    bot_users = len(ctx.bot.users)
    bot_commands = len(ctx.bot.commands)
    bot_cogs = len(ctx.bot.cogs)
    bot_channels = len(ctx.bot.channels)
    bot_text_channels = len(ctx.bot.text_channels)
    bot_voice_channels = len(ctx.bot.voice_channels)
    bot_categories = len(ctx.bot.categories)
    bot_roles = len(ctx.bot.roles)
    bot_emojis = len(ctx.bot.emojis)

    embed_color = os.getenv('EMBED_COLOR')
    text = f'Bot Latency: {bot_latency}\n Bot Uptime: {bot_up_time}\n Bot Version: {bot_version}\n Bot Prefix: {bot_prefix}\n Bot Guilds: {bot_guilds}\n Bot Users: {bot_users}\n Bot Commands: {bot_commands}\n Bot Cogs: {bot_cogs}\n Bot Channels: {bot_channels}\n Bot Text Channels: {bot_text_channels}\n Bot Voice Channels: {bot_voice_channels}\n Bot Categories: {bot_categories}\n Bot Roles: {bot_roles}\n Bot Emojis: {bot_emojis}'
    embed = ctx.bot.embed(title='Bot Stats', description=text, color=embed_color)
    await ctx.send(embed=embed)
