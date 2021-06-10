import discord
from discord import embeds
import pafy
from discord import client
from discord import guild
from discord.channel import VoiceChannel
from discord.ext import commands
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import urllib.request
import urllib.parse
import re
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

class music1(commands.Cog, name="Play"):
    """Music commands"""

    def __init__(self, bot: commands.Bot):
        self.bot=bot

    @commands.command(name='test')
    async def test(self, ctx):

        search = "morpheus tutorials discord bot python"

        if ctx.message.author.voice == None:
            await ctx.send(embed=embeds("No Voice Channel", "You need to be in a voice channel to use this command!", ctx.author))
            return

        channel = ctx.message.author.voice.channel

        voice = discord.utils.get(ctx.guild.voice_channels, name=channel.name)

        voice_client = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        if voice_client == None:
            voice_client = await voice.connect()
        else:
            await voice_client.move_to(channel)

        search = search.replace(" ", "+")

        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        
        await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])

        song = pafy.new(video_ids[0])  # creates a new pafy object

        audio = song.getbestaudio()  # gets an audio source

        source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use

        voice_client.play(source)  # play the source
        


def setup(bot: commands.Bot):
    bot.add_cog(music1(bot))
