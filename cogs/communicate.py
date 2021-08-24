import discord
from discord.ext import commands
import random


class Communicate(commands.Cog):
    """Some funny communication commands with the bot and other members of the server"""

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['hey_nami', 'hi_nami', 'greet_cat'])
    async def greet_nami(self, ctx):
        sender = str(ctx.message.author)[:-5]

        responses = ['Ossu!', 'Moshi Moshi', 'Kon\'nichiwa', 'Ohayou gozaimasu o.0', ':cat:']
        await ctx.send(random.choice(responses))

    @commands.command(aliases=['party_time'])
    async def party(self, ctx):
        sender = str(ctx.message.author)[:-5]

        responses = ['P P Partee time!', 'UwU time for party', 'Bois will now commence in darnce or die']
        await ctx.send(random.choice(responses))

    @commands.command(aliases=['night_nami', 'goodnight_nami', 'night_cat'])
    async def night(self, ctx):
        sender = str(ctx.message.author)[:-5]

        responses = ['Night {} :3'.format(
            sender), 'Night! *Falls asleep* -.-']
        await ctx.send(random.choice(responses))

    @commands.command(aliases=['murder', 'assassinate', 'scratch'])
    async def kill(self, ctx, target):
        sender = str(ctx.message.author)[:-5]

        if target == "<@!253640969122086922>":
            await ctx.send("No! {0}. I would never hurt master Kcorb".format(sender))

        elif target == "<@!814909398031794256>":
            await ctx.send("AHHH I WONT DO THAT")

        else:
            responses = ['*nami obeys master {0}, proceeds to scratch {1} down to the bone.* \n*{1} is dead.* Mission complete {0}\'*'.format(sender, target),
                         'HAKAAAAIIIIIIIIIII.\n*{0} Dies.*'.format(target)]
            await ctx.send(random.choice(responses))

    @commands.command()
    async def summon(self, ctx):
        sender = str(ctx.message.author)[:-5]
        responses = [
        "Come on {0} it's time, {1} wants to play some games.".format(ctx.message.guild.default_role, sender), 
        "What's good {0} it's time for hardcore gaming.".format(ctx.message.guild.default_role), 
        "{0} has requested that {1} must attend the ceremonial gathering of the bois.".format(sender, ctx.message.guild.default_role)]

        await ctx.send(random.choice(responses))

    @commands.command(aliases=['give', 'feed_cat', 'give_nami', 'feed_nami'])
    async def feed(self, ctx, *, food):
        sender = str(ctx.message.author)[:-5]
        responses = ["*Nami takes {0} from {1}.* Thank you :)".format(
            food, sender), "*Nami denies the {0} from {1}*".format(food, sender)]
        await ctx.send(random.choice(responses))

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        channel = ctx.author.voice.channel
        await ctx.voice_client.disconnect()


def setup(client):
    client.add_cog(Communicate(client))
