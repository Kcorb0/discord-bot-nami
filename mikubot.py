import discord
from discord.ext import commands
import logging
import os
import random
import json

logging.basicConfig(level=logging.INFO)
client = commands.Bot(command_prefix="$")
token = ""


# On bot startup events
@client.event
async def on_ready():
    activities = [
        "League of Legends",
        "Valheim",
        "Minecraft",
        "Doom",
        "Catgirl Sim",
        "Sims 3",
        "Netflix",
        "Escape from Tarkov",
        "Funimation",
        "FFXIV",
        "Twitch hot-tub stream",
        "consecutive backflips",
        "Grand Theft Auto V",
        "Rocket League",
        "Counter-Strike: Global Offensive",
        "Rust",
        "Dark Souls 3",
        "Dark Souls 2",
        "Dark Souls",
        "Demon Souls",
        "Gym-Gluteus Day",
    ]
    await client.change_presence(activity=discord.Game(random.choice(activities)))
    print("{0.user} online".format(client))


# Developer commands to change cogs without shutting off the bot
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    print(f"{extension} has been loaded.")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    print(f"{extension} has been unloaded.")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    print(f"{extension} has been reloaded.")


# Search and load all cogs within the cogs directory
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


# User leveling system
@client.event()
async def on_message(message):
    with open("users.json", "r") as jfile:
        users = json.load(jfile)

    # Leveling experience
    # 10 EXP per message, 30 EXP per Gif
    # Level calcualation 100*(curlvl)

    with open("users.json", "w") as jfile:
        json.dump(jfile)


# Profanity detection
# @client.event
# async def on_message(message):
#    profanity = ['dick', 'shit', 'fuck', 'crap', 'wanker', 'tosser', 'bollocks', 'cock', 'fuck',
#                 'cunt', 'stupid', 'toss', 'retard', 'crud', 'silly', 'bitch']

#    for w in profanity:
#        if w in message.content.lower():
#            responses = [
#                "That's mean >.<", "Don't use such mean words 0_0", "Fudge you for saying that!"]
#            await message.channel.send(random.choice(responses))
#            break
#    await client.process_commands(message)

client.run(token)
