import discord
import discord.ext.commands
from discord.utils import get
import colorama
from colorama import Fore
import requests
import sys
import asyncio
import json
from webserver import keep_alive
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
import os
import re
import typing
import time

def get_prefix(bot,message):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)

    return prefixes 

start_time = time.time()

quiet = commands.Bot(command_prefix = !!, self_bot=True)

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
