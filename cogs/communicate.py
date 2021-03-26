import discord
from discord.ext import commands
import random


class Communicate(commands.Cog):
    """Some funny communication commands with the bot and other members of the server"""

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['hey_miku', 'hi_miku', 'greet_cat'])
    async def greet_miku(self, ctx):
        sender = str(ctx.message.author)[:-5]

        responses = ['Ossu!', 'Moshi Moshi :3', '*Purrs*', '*Jumps* oh hello master {} X3'.format(
            sender), 'Kon\'nichiwa', 'Ohayou gozaimasu o.0', ':cat:']
        await ctx.send(random.choice(responses))

    @commands.command(aliases=['party_time'])
    async def party(self, ctx):
        sender = str(ctx.message.author)[:-5]

        responses = ['P P Partee time!', 'UwU time for party', 'Bois will now commence in darnce or die']
        await ctx.send(random.choice(responses))

    @commands.command(aliases=['night_miku', 'goodnight_miku', 'night_cat'])
    async def night(self, ctx):
        sender = str(ctx.message.author)[:-5]

        responses = ['Night {} :3'.format(
            sender), 'Nightttt! *Falls aslweep* -.-']
        await ctx.send(random.choice(responses))

    @commands.command(aliases=['murder', 'assassinate', 'scratch'])
    async def kill(self, ctx, target):
        sender = str(ctx.message.author)[:-5]

        if target == "<@!253640969122086922>":
            await ctx.send("Miku pees on {0}. NO NO! I would never huwt my swexy muscley master Dinker >.<".format(sender))

        elif target == "<@!814909398031794256>":
            await ctx.send("AHHH I WONT DO THAT >0<")

        else:
            responses = ['*Miku obeys master {0}, proceeds to scratch {1} down to the bone.* \n*{1} is dead.* \nMiku crawls back and sits on {0}\'s lap.*'.format(sender, target),
                         '*Strikes {0}* nyanyanaynyanya. \n*Poops on {0} and walks away*'.format(
                             target),
                         'UwU...... 0w0 HAKAAAAIIIIIIIIIII.\n*{0} Dies.*'.format(target)]
            await ctx.send(random.choice(responses))

    @commands.command(aliases=['pet', 'poke', 'kiss', 'stroke_cat', 'pet_cat', 'poke_cat', 'kiss_cat', 'make_happy'])
    async def stroke(self, ctx):
        sender = str(ctx.message.author)[:-5]
        responses = ['*Purrs*', 'UwU Harder please *Blushes*', '*Dabs, proceeds to then yeet.*', '*Runs away*', 'WTF?', 'Hey i have a boyfriend >.<', '*Blushes*',
                     'Licks {}\'s, buthole'.format(sender), "You perv eeeeek!", "EW! Get away from me >.<", "Hewp me someone, {} is trying to touch me.".format(sender)]
        await ctx.send(random.choice(responses))

    @commands.command()
    async def summon(self, ctx):
        sender = str(ctx.message.author)[:-5]
        responses = [
        "Come on {0} it's time, {1} wants to play some games UwU.".format(ctx.message.guild.default_role, sender), 
        "What's good {0} it's time for hardcore gaming and cheek slappin. >.<".format(ctx.message.guild.default_role), 
        "{0} has requested that {1} must attend the ceremonial gathering of the bois. UwU".format(sender, ctx.message.guild.default_role)]

        await ctx.send(random.choice(responses))

    @commands.command(aliases=['give', 'feed_cat', 'give_miku', 'feed_miku'])
    async def feed(self, ctx, *, food):
        sender = str(ctx.message.author)[:-5]
        responses = ["*Miku takes {0} from {1}.* Thank you :3".format(
            food, sender), "*Miku denies the {0} from {1}*, get that away from me >.<".format(food, sender)]
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
