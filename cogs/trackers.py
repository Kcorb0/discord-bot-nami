import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import random
import requests


class CryptoTracker:
	"""Track information on any coin available from coindesk.com"""

	def __init__(self, coin):
		self.coin = coin

	def c_info(self):
		html_text = requests.get('https://www.coindesk.com/price/{}'.format(self.coin)).text
		soup = BeautifulSoup(html_text, 'lxml')
		cats = soup.find('div', class_='coin-info-list')

		c_price = cats.find('div', class_='price-large').text
		c_change = cats.find('span', class_='percent-value-text').text
		c_cap = cats.find('div', class_='price-medium').text
		c_vol = cats.find_all('div', class_='price-medium')[1].text

		return [c_price.replace(',', ""), c_change+"%", c_cap.replace(',', ""), c_vol.replace(',', "")]
		
	def c_price(self):
		# Returns the current market price of coin
		price = self.c_info()[0]
		gbp = "£" + str(round(float(price[1:])*.72, 2))

		return f"{price} ({gbp})"

	def c_change(self):
		# Returns 24/hr change of the coin
		return self.c_info()[1]

	def c_cap(self):
		# Returns the current market cap of coin
		return self.c_info()[2].replace(',', "")

	def c_vol(self):
		# Returns the 24hr volume
		return self.c_info()[3].replace(',', "")
	

class LolTracker:
	"""Finds player info from lolprofile"""

	def __init__(self, player):
		self.player = player

	def lol_rank(self):
		html_text = requests.get('https://lolprofile.net/summoner/euw/{}#update'.format(self.player)).text
		soup = BeautifulSoup(html_text, 'lxml')
		rank = soup.find('div', class_='s-c cf tab1').find('div', class_='s-cl').find('span', class_='tier').text
		return str(rank)

	def lol_games(self):
		html_text = requests.get('https://lolprofile.net/summoner/euw/{}#update'.format(self.player)).text
		soup = BeautifulSoup(html_text, 'lxml')
		wins = (soup.find('div', class_='s-rs-info').find('span', class_='win-txt').text).split(" ")[0]
		loss = (soup.find('div', class_='s-rs-info').find('span', class_='lose-txt').text).split(" ")[0]

		return f"Wins: {wins} Losses: {loss} Total: {int(loss)+int(wins)}"


class TrackCommands(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def c_info(self, ctx, coin):
		info = CryptoTracker(coin.lower()).c_info()
		try:
			await ctx.send(f"{info[0]}\n{info[1]}\n{info[2]}\n{info[3]}")
		except:
			await ctx.send("I can't find that coin >.0")

	@commands.command()
	async def c_price(self, ctx, coin):
		try:
			await ctx.send("Price for {} right now is: {}".format(coin.capitalize(), CryptoTracker(coin.lower()).c_price()))
		except:
			await ctx.send("I can't find that coin >.0")

	@commands.command()
	async def c_change(self, ctx, coin):
		try:
			await ctx.send("The 24hr change for {} is: {}".format(coin.capitalize(), CryptoTracker(coin.lower()).c_change()))
		except:
			await ctx.send("I can't find that coin >.0")

	@commands.command()
	async def c_cap(self, ctx, coin):
		try:
			await ctx.send("The current market cap for {} is: {}".format(coin.capitalize(), CryptoTracker(coin.lower()).c_cap()))
		except:
			await ctx.send("I can't find that coin >.0")

	@commands.command()
	async def c_vol(self, ctx, coin):
		try:
			await ctx.send("The past 24hr volume for {} is: {}".format(coin.capitalize(), CryptoTracker(coin.lower()).c_cap()))
		except:
			await ctx.send("I can't find that coin >.0")

	@commands.command()
	async def lol_rank(self, ctx, player):
		try:
			await ctx.send("Getting rank for {} ^.^\nRank: {}".format(player, LolTracker(player.lower()).lol_rank()))
		except:
			await ctx.send("I can't find that player >.<")

	@commands.command()
	async def lol_games(self, ctx, player):
		try:
			await ctx.send(f"Getting total games played for {player} ^.^")
			await ctx.send(LolTracker(player.lower()).lol_games())
			await ctx.send("Woweeeee, and you are still silver XD oooofies")
		except:
			await ctx.send("I can't find that player >.<")


def setup(client):
	client.add_cog(TrackCommands(client))

if __name__ == "__main__":
	print(LolTracker('JNKYY').lol_rank())
	print(LolTracker('JNKYY').lol_games())
