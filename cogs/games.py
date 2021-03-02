import discord
from discord.ext import commands
from random import choice

class Games(commands.Cog):
	"""Some games to play with others in a discord server or the bot"""

	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def coin_flip(self, ctx, opponent, side):
		outcome = {0:"tails", 1:"heads"}
		side1 = pop(choice(outcome))
		player1 = random.choice()
		# TODO allow player to pick side


def setup(client):
	client.add_cog(Games(client))
