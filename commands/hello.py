import discord
from discord.ext import commands

quiet = commands.Bot(command_prefix='!!', self_bot=True)

@quiet.command()
async def hello(ctx):
    await ctx.send('Hello!')
