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
import importlib
import os

quiet = discord.Client()

# Get a list of all Python files in the commands folder
command_files = [file for file in os.listdir('commands') if file.endswith('.py')]

# Import and load each command file
for file in command_files:
    importlib.import_module(f'commands.{file[:-3]}')

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
quiet.run('OTg5NDMwNzM1NTYxNzE1NzEy.GARrM7.R5J-0gcPwPxkj9GL74eCp892IPjSVL-qxgOVBU')
#============================================
#----------------DATABASE--------------------
#============================================
