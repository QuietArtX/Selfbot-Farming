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

try:
    import shutil
except:
    os.system("pip install shutil")
    import shutil

try:
    from colorama import init, Fore, Back, Style
except:
    os.system("pip install colorama")
    from colorama import init, Fore, Back, Style
#---------------------END--------------------

#--------------SETUP TOKEN-------------------
#       Input your token in secret
#--------------------------------------------
prefix = "!!"
username = "yourusername#1234"

def getstatus(m):
    if str(m.status) == "do.not.disturb":
        return "do not disturb"
    return m.status

def get_prefix(quiet,message):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)

    return prefixes 

start_time = time.time()

quiet = commands.Bot(command_prefix = get_prefix, self_bot=True, help_commandn=None, shorten=None)
command_files = [file for file in os.listdir('commands') if file.endswith('.py')]

for file in command_files:
    importlib.import_module(f'commands.{file[:-3]}')
