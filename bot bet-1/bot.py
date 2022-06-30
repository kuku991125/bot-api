import discord

bot = discord.Client()

@bot.event
async def on_ready():
    print('Login As：', bot.user)
    game = discord.Game('lol')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "test" or message.content == "Test":
        await message.channel.send('Hi')

    if message.content.startswith('!'):
      tmp = message.content.split(" ",2)
      if len(tmp) == 1:
        await message.channel.send("?")
      else:
        await message.channel.send(tmp[1])

bot.run("OTgyNjA0OTIyMDA2Njc1NDU3.Goae5a.4yb4f8i6AigOQJ9gOxgr_Cb9MU9r--hX2eVfXA")    
