import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="-")
@bot.event
async def on_ready():
  print('we heve logged in as {0.user}.format(client')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswich('hi'):   
    await message.channel.send('hello')



bot.run('OTgyNjA0OTIyMDA2Njc1NDU3.GKSeKF.de3Vy4MHEyYURqbPotDgKM52ruoKzrfGU28g4Y')