import discord
from discord.ext import commands
import time
import os
import json

def get_prefix(quiet,message):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)

quiet = commands.Bot(command_prefix = get_prefix, self_bot=True)

@quiet.command()
async def uptime(ctx):
    await ctx.message.delete()
    current_time = time.time()
    uptime = int(current_time - start_time)
    uptime_minutes, uptime_seconds = divmod(uptime, 60)
    uptime_hours, uptime_minutes = divmod(uptime_minutes, 60)
    uptime_days, uptime_hours = divmod(uptime_hours, 24)
    message = f'``` I have been running for :'
    if uptime_days > 0:
        message += f'{uptime_days} Days, '
    if uptime_hours > 0:
        message += f'{uptime_hours} Hours, '
    if uptime_minutes > 0:
        message += f'{uptime_minutes} Minutes, '
    message += f'{uptime_seconds} Seconds. ```'
    await ctx.send(message)