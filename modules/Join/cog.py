import discord
from discord import embeds

from discord import client
from discord import guild
from discord.channel import VoiceChannel
from discord.ext import commands
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio, PCMVolumeTransformer

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

class music1(commands.Cog, name="Play"):
    """Music commands"""

    def __init__(self, bot: commands.Bot):
        self.bot=bot




def setup(bot: commands.Bot):
    bot.add_cog(music1(bot))
