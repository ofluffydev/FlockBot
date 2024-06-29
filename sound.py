import asyncio

from discord import FFmpegPCMAudio
from discord.ext.commands import Context


async def bugatti(ctx: Context) -> None:
    # See if user is in a voice channel
    if ctx.author.voice is None:
        print('User is not in a voice channel.')
    else:
        # Join the voice channel
        print('User is in a voice channel.')
        voice_channel = ctx.author.voice.channel
        print(f'Connecting to {voice_channel}')
        voice_client = await voice_channel.connect()
        # Play the audio file
        audio_source = 'sound/bugatti.mp3'
        print(f'Playing {audio_source}')
        voice_client.play(FFmpegPCMAudio(audio_source))
        # Wait for the audio to finish
        while voice_client.is_playing():
            await asyncio.sleep(1)
        # Disconnect from the voice channel
        await voice_client.disconnect()
