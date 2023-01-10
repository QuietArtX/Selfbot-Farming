import discord
import time
import requests
from discord.ext import commands
from quiet.setting.prefixes import get_prefix

quiet = discord.Client()
quiet = commands.Bot(command_prefix = get_prefix, self_bot=True, help_command=None, shorten=None, case_insensitive=True)

@quiet.command()
async def uptime(ctx):
    await ctx.message.delete()
    current_time = time.time()
    uptime = int(current_time - start_time)
    uptime_minutes, uptime_seconds = divmod(uptime, 60)
    uptime_hours, uptime_minutes = divmod(uptime_minutes, 60)
    uptime_days, uptime_hours = divmod(uptime_hours, 24)
    message = f'```\nI have been running for:\n  ▸'
    if uptime_days > 0:
        message += f'{uptime_days} Days, '
    if uptime_hours > 0:
        message += f'{uptime_hours} Hours, '
    if uptime_minutes > 0:
        message += f'{uptime_minutes} Minutes, '
    message += f'{uptime_seconds} Seconds.\n```'
    await ctx.send(message)
