#╔═══╦╗─╔╦══╦═══╦════╦══lll═╦═══╦════╦═╗╔═╗
#║╔═╗║║─║╠╣╠╣╔══╣╔╗╔╗║╔═╗║╔═╗║╔╗╔╗╠╗╚╝╔╝
#║║─║║║─║║║║║╚══╬╝║║╚╣║─║║╚═╝╠╝║║╚╝╚╗╔╝
#║║─║║║─║║║║║╔══╝─║║─║╚═╝║╔╗╔╝─║║──╔╝╚╗
#║╚═╝║╚═╝╠╣╠╣╚══╗─║║─║╔═╗║║║╚╗─║║─╔╝╔╗╚╗
#╚══╗╠═══╩══╩═══╝─╚╝─╚╝─╚╩╝╚═╝─╚╝─╚═╝╚═╝
#───╚╝SEFLBOT

#------------------MODULE--------------------
import discord
from discord.ext import commands
from discord.utils import get
import colorama
from colorama import Fore
import requests
import google
import sys
import asyncio
import json
import googleapiclient
from webserver import keep_alive
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
import os
import re
import typing
import random
import time
import pafy
import youtube_dl
import importlib

def get_prefix(quiet,message):
    with open("quiet/setting/prefixes.json", "r") as f:
      prefixes = json.load(f)

    return prefixes

quiet = discord.Client()
quiet = commands.Bot(command_prefix=get_prefix, selfbot=True)
for filename in os.listdir("quiet/allcmd"):
    if filename.endswith(".py"):
        module_name = filename[:-3]
        module = importlib.import_module(f"{module_name}")
        for name, obj in vars(module).items():
            if isinstance(obj, discord.ext.commands.core.Command):
                quiet.add_command(obj)


print(f'''
{Fore.BLUE}
░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░

{Fore.GREEN}The program has successfully logged into the your account

{Fore.BLUE}Prefix: !!

Project Dev: QuietArtx
''')

keep_alive()
quiet.run(os.getenv("TOKEN"), bot=False)
#============================================
#----------------DATABASE--------------------
#============================================
