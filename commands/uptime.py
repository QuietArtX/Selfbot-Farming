import discord
from discord.ext import commands

@quiet.command()
async def uptime(ctx):
    await ctx.message.delete()
    current_time = time.time()
    uptime = int(current_time - start_time)
    uptime_minutes, uptime_seconds = divmod(uptime, 60)
    uptime_hours, uptime_minutes = divmod(uptime_minutes, 60)
    uptime_days, uptime_hours = divmod(uptime_hours, 24)
    message = f'I have been running for '
    if uptime_days > 0:
        message += f'{uptime_days} days, '
    if uptime_hours > 0:
        message += f'{uptime_hours} hours, '
    if uptime_minutes > 0:
        message += f'{uptime_minutes} minutes, '
    message += f'and {uptime_seconds} seconds.'
    await ctx.send(message)
