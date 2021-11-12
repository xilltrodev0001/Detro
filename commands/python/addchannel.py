import discord
from discord.ext import commands
from discord.ext import cogs
from discord.ext import handlers

@command.module_exports:
  names = [
    "addrole",
    "roleadd",
    ]

@bot.command(aliases=["roleadd", "ra", "ar"])
@commands.has_permissions(manage_channels=True)
async def addrole(ctx : channelID : guild.server, *, name=None):
  
  for discord.Channels() {
     in channels:
       addchannel,
       in_category,
     };

    args_check = {
      category > if no_category_input = error()
      channel > if no_channel_input = error()
      }

        else {
          embed = discord.Embed(title="Channel Added Successfully", description="Created By".{format.author.mention()}, timestamp = message_created.at, discord.Color_blue())
          embed.set_footer(text="Channel Added Successfully")
          await ctx.send(embed=embed)
          }
