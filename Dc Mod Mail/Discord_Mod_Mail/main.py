import discord
from discord.ext import commands
import os
import keep_alive
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='//', intents=intents)

@Bot.event
async def on_ready():
    Bot.remove_command('help')
    
    Bot.load_extension("cogs.onMessage")
    
    await Bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(type=discord.ActivityType.playing,
                                                        name="//helps"))

# modmail
@Bot.command()
async def modmail(ctx):
    author = ctx.author
    
    embed2 = discord.Embed(title='Info',description="Our Bot Is Ready To Help Please Check Your Private Messages", colour=0xFF4654)
    embed2.set_footer(text='I Live For Service 🧐')
    await ctx.send(embed=embed2)

    embed2 = discord.Embed(title='Info',description="- Please Enter Your Requests And Recommendations Here\n"
                                                    "\n"
                                                    "- Our supporters will return to you as soon as possible.", colour=0xFF4654)
    embed2.set_footer(text='I Live For Service 🧐')
    await author.send(embed=embed2)

@Bot.command()
async def helps(ctx):
  embed = discord.Embed(
        title='Help Panel',
        description= "**------------------------ :mag: Welcome to the Help Panel :mag_right:------------------------**\n"
        "\n"
        "1- ** //modmail ** |Provides ınformation about how to submit a support ticket to mods|\n"
        "\n"
        "2- ** //close** (user name)|It helps you to delete the mail room opened by the player (Mail Room          has to be written)\n"
        "\n",
        colour=0xFF4654
    )
  embed.set_footer(text='I Live For Service 🧐')
  embed.set_author(name='Mod Mail')
  await ctx.author.send(embed=embed)
    
    
  embed2 = discord.Embed(title='Info',description="The Information You Want Is On The Road With The Pigeon",       colour=0xFF4654)
  embed2.set_footer(text='I Live For Service 🧐')
  await ctx.send(embed=embed2)







token = os.environ.get('token')
keep_alive.keep_alive()
Bot.run(token)

'''
|------------------------------------|
| *Creative By : Erdem Taha (Mr.Fx)* |
|------------------------------------|

'''
