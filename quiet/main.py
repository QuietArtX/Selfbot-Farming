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
import json
import os
from webserver import keep_alive
import re
import importlib
from allcmd.uptime import uptime

def get_prefix(quiet,message):
    with open("quiet/setting/prefixes.json", "r") as f:
      prefixes = json.load(f)

    return prefixes 

quiet = discord.Client()
quiet = commands.Bot(command_prefix=get_prefix, selfbot=True, help_command=None)
for filename in os.listdir("quiet/allcmd"):
    if filename.endswith(".py"):
        module_name = filename[:-3]
        module = importlib.import_module(f"allcmd.{module_name}")
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
