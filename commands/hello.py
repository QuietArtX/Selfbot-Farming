import discord
from discord.ext import commands

quiet = commands.Bot(command_prefix='!!')

@quiet.command()
async def hello(ctx):
    await ctx.send('Hello!')
