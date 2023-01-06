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
import importlib
from Quiet import uptime

quiet = discord.Client()

command_files = [file for file in os.listdir('Quiet') if file.endswith('.py')]

# Import and load each command file
for file in command_files:
    importlib.import_module('uptime')
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
