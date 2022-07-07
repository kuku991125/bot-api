from discord.ext import commands
bot = commands.Bot(command_prefix="-")
@bot.event
async def on_message(message):
    
    if message.author == bot.user:
        return
   
    if message.content.startswith('說'):
     
      tmp = message.content.split(" ",2)
      
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])


