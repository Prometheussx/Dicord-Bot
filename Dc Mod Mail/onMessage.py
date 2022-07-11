from discord.ext import commands
from discord import utils
import discord
import asyncio
import datetime
class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def close(self, ctx, member: discord.Member):
        if ctx.channel.category.name == "Modmail tickets":
            author = ctx.author
            channel = discord.utils.get(ctx.guild.text_channels, name="mail-logs")
            await channel.send(f"{author} Close Mail")
            await ctx.send("Deleting the channel in 10 seconds!")
            embed = discord.Embed(title='Ticket Closed',description='Your Ticket Has Been Closed By The Staff. You Can Contact Us Again For Other Questions And Requests', colour=0xe63921, timestamp=datetime.datetime.utcnow())
            embed.set_footer(text='I Live For Service 🧐')
            embed.set_author(name='Mod Mail Bot')
            await member.send(embed=embed)
            await asyncio.sleep(10)
            await ctx.channel.delete()
            
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if isinstance(message.channel, discord.DMChannel):
            guild = self.bot.get_guild(778714032243998780)
            categ = utils.get(guild.categories, name="Modmail tickets")
            if not categ:
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    guild.me: discord.PermissionOverwrite(read_messages=True)
                }
                categ = await guild.create_category(name="Modmail tickets", overwrites=overwrites)

            channel = utils.get(categ.channels, topic=str(message.author.id))
            if not channel:
                channel = await categ.create_text_channel(name=f"{message.author.name}#{message.author.discriminator}",
                                                          topic=str(message.author.id))
                await channel.send(f"New modmail created by {message.author.mention}")

            embed = discord.Embed(description=message.content, colour=0xe63921, timestamp= datetime.datetime.utcnow())
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.set_footer(text= f" Role: User")
            await channel.send(embed=embed)
        elif isinstance(message.channel, discord.TextChannel):

            if message.content.startswith(self.bot.command_prefix):
                pass
            else:
                topic = message.channel.topic
                if topic:
                    member = message.guild.get_member(int(topic))

                    roles = message.author.roles

                    top_role = roles[len(roles) - 1]
                    if member:
                        embed = discord.Embed(description=message.content, colour=0x0d730d,  timestamp=datetime.datetime.utcnow())
                        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
                        embed.set_footer(text= f" Role: {top_role}")
                        await member.send(embed=embed)


def setup(bot):
    bot.add_cog(onMessage(bot))
