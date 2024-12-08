import discord
import os
from dotenv import load_dotenv
import random

# Load environment variables from .env file
load_dotenv()

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("Drinking from the well...")
    print(client.user)

quotes = ["Cattle die, kinsmen die, all men are mortal. But I know one thing that never dies: the reputation of each dead man.", "It is better to fight and fall than to live without hope.", "The loyalty of those who count on you is a currency that can't be devalued.", "I have no fear of death, it just means dreaming in silence. A dream that lasts for eternity.", "All the gear in the world won't help you if you don't have the heart to use it.", "Wisdom is welcome wherever it comes from.", "The gods do not give us the same gifts, but they give us each the gifts that we need."]

@client.event
async def on_message(message):
    # message is from a user, not the bot
    if message.author != client.user:
        if (message.content == "!help"):
            await message.channel.send("!help will show the available commands. !quote will generate a random quote. If you say hello mimir, or hi mimir I will respond accordingly. If all else fails, I'll reverse your message and send it back.")
        elif (message.content == "!quote"):
            newQuote = random.choice(quotes)
            await message.channel.send(newQuote)
        elif (message.content.startswith("hello mimir") or message.content.startswith("hi mimir")):
            await message.channel.send("Guardian of the well, reporting for duty.")
        else:
            # reverse the message, send it back
            await message.channel.send(message.content[::-1])

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
