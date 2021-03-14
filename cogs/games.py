import discord
from discord.ext import commands
from random import choice


class Games(commands.Cog):
    """Some games to play with others in a discord server or the bot"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coin_flip(self, ctx, opponent, side, amnt=1):
        sender = str(ctx.message.author)[:-5]

        sides = ["heads", "tails"]
        player1 = sides.pop(sides.index(side))
        player2 = sides[0]

        flip = choice(["heads", "tails"])

        await ctx.send(f"{sender} challenges {opponent} to a coinflip taking {side}.")
        await ctx.send(f"*Miku flips coin*, it lands on {flip}.")

        if player1 == flip:
            await ctx.send(f"{sender} wins >.<")
        else:
            await ctx.send(f"{opponent} wins >.<")


def setup(client):
    client.add_cog(Games(client))
