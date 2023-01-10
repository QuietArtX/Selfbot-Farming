import discord
from discord.ext import commands

quiet = discord.Client()
quiet = commands.Bot(command_prefix="!!", self_bot=True, help_command=None)

@quiet.command()
async def sui(ctx):
     await ctx.send("SUUUUUU")
