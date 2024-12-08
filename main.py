import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("Accessing the mainframe")
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
        # reverse the message, send it back
        await message.channel.send(message.content[::-1])

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
