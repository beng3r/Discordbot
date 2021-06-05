import discord
from discord import client
from discord import guild
from discord.channel import VoiceChannel
from discord.ext import commands
from youtube_dl import YoutubeDL

class music1(commands.Cog, name="Play"):
    """Music commands"""

    def __init__(self, bot: commands.Bot):
        self.bot=bot



def setup(bot: commands.Bot):
    bot.add_cog(music1(bot))