import discord
import os
from keep_alive import keep_alive
from discord.ext import discordEvents

bot = new.discordClient()
bot = commands.Bot("/")

@bot.event
aysnc def on_ready():
  await bot.change_presence(type = ["Online"], status_type = ["Playing"], description = ["/help"]
  print(f"logged in as {}".formatBotUsername)

bot.run(os.config.json(data="token"))
