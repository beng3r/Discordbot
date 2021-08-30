import os
import discord
from discord.ext import commands,tasks
from dotenv.main import load_dotenv
from discord.ext import commands
import youtube_dl
import asyncio

def main():
    #intents = discord.Intents().all()
    #client = discord.Client(intents=intents)
    #bot = commands.Bot(command_prefix='!',intents=intents)
    client = commands.Bot(command_prefix=".")
    players = {}
    load_dotenv()
    
    @client.event
    async def on_ready():
    
        print(f"{client.user.name} has connected to Discord.")


        # Setting `Streaming ` status
        await bot.change_presence(activity=discord.Streaming(name="Don't click my Stream", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

        # Setting `Listening ` status
        #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your conversation"))

        # Setting `Watching ` status
        #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="this server die"))
        
    for folder in os.listdir("modules"):
        if os.path.exists(os.path.join("modules", folder, "cog.py")):
            client.load_extension(f"modules.{folder}.cog")
    

    client.run(os.getenv("DISCORD_TOKEN"))







if __name__ == '__main__':
    main()
