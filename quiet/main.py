#╔═══╦╗─╔╦══╦═══╦════╦═══╦═══╦════╦═╗╔═╗
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
    with open("quiet/setting/prefixes.json", "r") as f:
      prefixes = json.load(f)

    return prefixes 

start_time = time.time()
quiet = discord.Client()
quiet = commands.Bot(command_prefix = get_prefix, self_bot=True, help_command=None, shorten=None, case_insensitive=True)

giveaway_entries = []
API_KEY = "28bf153817808a7c28697f2b4bbbff39"
owners = [989430735561715712, 1048214159877226547]
channel_ids = [1062228651233513552, 1060875376009695266, 1060875376009695265]

@quiet.event
async def on_message(message):
    if message.author != quiet.user:
        if message.content.startswith("!mycommand"):
            # Do something
            await message.channel.send("Hello, this is your command")

#--------------------------------------------
#--------------------------------------------

#============================================
#---------------HELP COMMNAND----------------
#============================================
@quiet.command(name='help')
async def help(ctx):
    await ctx.message.delete()
    await ctx.send(f"```\n𝗛𝗘𝗟𝗣 𝗖𝗢𝗠𝗠𝗔𝗡𝗗\n\nPrefix : ▸ {ctx.prefix} ( you can change your prefix by cmd )\n\n𝗔𝗗𝗠𝗜𝗡\nkick, ban, gban, purge\n\n𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦\nprefix, status\n\n𝗙𝗨𝗡\npagi, siang, malam, salam, hack\n\n𝗨𝗧𝗜𝗟𝗟𝗦\nvoice, farming, gleave, ping, nick\n\nType !!cmd(usage) For More Information\n\nExample !!cmdadmin !!cmdsetting\n```", delete_after=15)
#--------------------------------------------
#--------------------------------------------

@quiet.command(aliases=['cmdban', 'cmdkick', 'cmdgban'])
async def cmdadmin(ctx):
    await ctx.message.delete()
    await ctx.send(f"```𝗔𝗗𝗠𝗜𝗡\nRequires discord server admin permission\n\n𝗨𝗦𝗔𝗚𝗘\n• {ctx.prefix}kick <member> = kick user form server\n• {ctx.prefix}ban <member> = ban user from server\n• {ctx.prefix}gban <member> = global ban users from server the admin is in\n• {ctx.prefix}purge <limit> = delete message by limit\n\nNOTE : Requires admin permission to run this command```")

@quiet.command(aliases=['cmdprefix', 'cmdstatus'])
async def cmdsetting(ctx):
    await ctx.message.delete()
    await ctx.send(f"```𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦\nFor Settings your selfbot\n\n𝗣𝗥𝗘𝗙𝗜𝗫\n• {ctx.prefix}cprefix <newprefix> = Change your self prefix with cmd\n\n𝗦𝗧𝗔𝗧𝗨𝗦\n• {ctx.prefix}game <usage> = For Playing Activity Status\n• {ctx.prefix}stream <usage> = For Streaming Activity Status\n• {ctx.prefix}listen <usage> = For Listening Activity Status\n• {ctx.prefix}watch <usage> = For Watching Activity Status\n• {ctx.prefix}rstatus = Remove your Activity Status\n\nfor example type : {ctx.prefix}stream NAME USAGE | YOUR NICK, and cek your Activity```")
    
@quiet.command(aliases=['cmdpagi', 'cmdsiang', 'cmdsore', 'cmdmalam', 'cmdsalam'])
async def cmdfun (ctx):
    await ctx.message.delete()
    await ctx.send(f"```𝗙𝗨𝗡\n To have fun with your server friends\n\n𝗨𝗦𝗔𝗚𝗘\n• {ctx.prefix}pg = good morning greetings\n• {ctx.prefix}sg = good afternoon\n• {ctx.prefix}mlm = good night\n• {ctx.prefix}hack = fake hacker\n• {ctx.prefix}p = Assalamualaikum\n• {ctx.prefix}l = Waalaikumsallam\n\nSelfbot By QuietArtx```")
    
@quiet.command(aliases=['cmdvoice', 'cmdfarming', 'cmdping', 'cmdgleave', 'cmdnick'])
async def cmduttils(ctx):
    await ctx.message.delete()
    await ctx.send(f"```𝗨𝗧𝗜𝗟𝗟𝗦\nVery useful command for you\n\n𝗩𝗢𝗜𝗖𝗘\n• {ctx.prefix}join <channelid> = For join Voice Channel without without you joining\n• {ctx.prefix}leave = exit the voice channel\n\n𝗙𝗔𝗥𝗠𝗜𝗡𝗚\nfarming work Unbeliavaboat global, for OwO is coming\n• {ctx.prefix}unb <cmdwork> <delaytime> = For Farming Work Unbeliavaboat\n• {ctx.prefix}unstop = Stop the Farming\n\n𝗢𝗧𝗛𝗘𝗥\n• {ctx.prefix}gleave <serverid> = leave from server only with server id\n• {ctx.prefix}ping = For check your latency ping\n• {ctx.prefix}cnick = Change Your Nickname```")
#============================================
#-------------------END----------------------
#============================================


#============================================
#-------------------ADMIN--------------------
#============================================
@quiet.command(name='purge', description='Menghapus Chat')
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("> You require the manage messages permission to use this command! ")

@quiet.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="Beban"
    await ctx.guild.kick(member)
    await ctx.send(f'> User **{member.mention}** Has Been Kicked From This Server\nReason : **{reason}**')
    
@quiet.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.ban(reason = message)
    await ctx.send(f"> You Got Banned **{member}** From Server!!")

@quiet.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'> Unbanned **{user.mention}** From This Server')
            return
 
@quiet.command()
async def gban(ctx, x: int):
    await ctx.message.delete()
    user, l = await quiet.fetch_user(x), []
    msg = await ctx.send(f"Banning {user}")
   
    for g in quiet.guilds:
        # ban user with given object
        await g.ban(discord.Object(id=x))
        await asyncio.sleep(1)
        l.append(g.name)

    await msg.edit(content=f"Global Banned!! **{user}** from **{', '.join(l)}**")
#============================================
#-------------------END----------------------
#============================================


#============================================
#------------------SETTINGS------------------
#============================================
@quiet.command()
async def cprefix(ctx, *, prefix):
    await ctx.message.delete()

    with open("quiet/setting/prefixes.json", "r") as f:
      prefixes = json.load(f)

    prefixes = prefix

    with open("quiet/setting/prefixes.json", "w") as f:
      json.dump(prefixes,f)
    await ctx.send(f"> Prefix Has Been Changed To **{prefix}**")


@quiet.event
async def on_message(msg):

     try:

         if msg.mention[1] == quiet.user:

              with open("quiet/setting/prefixes.json", "r") as f:
                 prefixes = json.load(f)

              pre = prefixes
       
              await msg.channel.send(f"My Prefix Is **{pre}**")

     except:
         pass

     await quiet.process_commands(msg)

@quiet.command()
async def game(ctx, *, message):
   await ctx.message.delete()
   await quiet.change_presence(activity=discord(type=discord.ActivityType.playing, name=message))
   await ctx.send("> Status Activity Has Been Change To **Game!!**")

@quiet.command()
async def stream(ctx, *, message):
  await ctx.message.delete()
  activity = discord.Streaming(name=message, url="https://www.youtube.com/watch?v=kVH3qI_MAlY", type=1)
  await quiet.change_presence(status=discord.Status.do_not_disturb, activity=activity)
  await ctx.send("> Status Activity Has Been Change To **Streaming**")

@quiet.command()
async def listen(ctx, *, message):
   await ctx.message.delete()
   await quiet.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))
   await ctx.send("> Status Activity Has Been Change To **Listening!!**")

@quiet.command()
async def watch(ctx, *, message):
   await ctx.message.delete()
   await quiet.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message))
   await ctx.send("> Status Activity Has Been Change To **Watching!!**")
   
@quiet.command()
async def rstatus(ctx):
    await ctx.message.delete()
    await quiet.change_presence(activity=None)
    await ctx.send("> Status Activity has been **Removed**")
#============================================
#-------------------END----------------------
#============================================


#============================================
#-------------------FUN----------------------
#============================================
@quiet.command()
async def start_giveaway(ctx, message_id: int):
    # Get all the channels in the server
    channels = quiet.get_all_channels()
    
    # Find the channel where the message was sent
    channel = None
    for c in channels:
        if c.id == ctx.channel.id:
            channel = c
            break
    
    # Get the message object using the message ID
    async for message in channel.history(limit=3):
        if message.id == message_id:
            # Get the reactions on the message
            reactions = message.reactions
            for reaction in reactions:
                if str(reaction.emoji) == "🎉":
                    # Get the users who reacted to the message
                    users = await reaction.users().flatten()
                    # Add the users to the giveaway entries list
                    for user in users:
                        giveaway_entries.append(user)

@quiet.command()
async def end_giveaway(ctx):
    # Check if the giveaway entries list is empty
    if not giveaway_entries:
        await ctx.send("There are no entries for this giveaway.")
    else:
        # Select a random user from the giveaway entries list
        winner = random.choice(giveaway_entries)
        await ctx.send(f"The winner of the giveaway is {winner.mention}!")

def is_owner():
    async def predicate(ctx):
        return ctx.author.id in owners
    return commands.check(predicate)

@quiet.command()
@is_owner()
async def dino(ctx):
    await ctx.message.delete()
    message = await ctx.send("DIN DINNN DINOSAURUS!....")
    a_int = 1
    a_ttl = range(45)
    a_chars = [
        "🏃                        🦖",
        "🏃                       🦖",
        "🏃                      🦖",
        "🏃                     🦖",
        "🏃     LARII          🦖",
        "🏃                   🦖",
        "🏃                  🦖",
        "🏃                 🦖",
        "🏃                🦖",
        "🏃               🦖",
        "🏃              🦖",
        "🏃             🦖",
        "🏃            🦖",
        "🏃           🦖",
        "🏃WOARGH!   🦖",
        "🏃           🦖",
        "🏃            🦖",
        "🏃             🦖",
        "🏃              🦖",
        "🏃               🦖",
        "🏃                🦖",
        "🏃                 🦖",
        "🏃                  🦖",
        "🏃                   🦖",
        "🏃                    🦖",
        "🏃                     🦖",
        "🏃  Huh-Huh           🦖",
        "🏃                   🦖",
        "🏃                  🦖",
        "🏃                 🦖",
        "🏃                🦖",
        "🏃               🦖",
        "🏃              🦖",
        "🏃             🦖",
        "🏃            🦖",
        "🏃           🦖",
        "🏃          🦖",
        "🏃         🦖",
        "DIA SEMAKIN MENDEKAT!!!",
        "🏃       🦖",
        "🏃      🦖",
        "🏃     🦖",
        "🏃    🦖",
        "Dahlah Pasrah Aja",
        "🧎🦖",
        "-TAMAT-",
    ]
    for i in a_ttl:
        await asyncio.sleep(a_int)
        await message.edit(content=a_chars[i % 45])
    

@quiet.command()
async def bulan(ctx):
    await ctx.message.delete()
    message = await ctx.send("**Moon...**")
    animation_interval = 0.5
    animation_ttl = range(16)
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit(content=animation_chars[i % 32])

@quiet.command()
async def flipcoin(ctx):
    # Flip a coin and get the result
    result = 'heads' if random.randint(0, 1) == 0 else 'tails'
    # Send the appropriate coin flip image to the current channel
    if result == 'heads':
        await ctx.send('https://cdn.discordapp.com/attachments/1061025685419851849/1061166940393054278/heads.png')
    else:
        await ctx.send('https://cdn.discordapp.com/attachments/1061025685419851849/1061166940757970997/tails.png')

@quiet.command()
async def cat(ctx):
     await ctx.message.delete()
     r = requests.get('http://aws.random.cat/meow')
     cat_image_url = r.json()['file']
     await ctx.send(cat_image_url)

@quiet.command()
async def ml(ctx):
      await ctx.message.delete()
      await ctx.send("```\nNickname : **Mystic Excaliburnn.**\nID : **498484453 (8010)**\nRole : **Mid/Exp**\nSquad : **None**\n```")

@quiet.command()
async def countdown(ctx, t: int):
    await ctx.send(f"Counting down from {t}s")

    while t > 0:
        t -= 1
        # Sleep for 1 second
        await asyncio.sleep(1)

    await ctx.send("Countdown end reached")

@quiet.command()
async def pg(ctx):
    await ctx.message.delete()
    await ctx.send("> Selamat Pagi Everyonee\n> Jangan Lupa Sarapan\n> Semangat!! <a:GhostLove:849875645680451604>")

@quiet.command()
async def sg(ctx):
    await ctx.message.delete()
    await ctx.send("> Selamat Siaang Everyonee!!")

@quiet.command()
async def mlm(ctx):
    await ctx.message.delete()
    await ctx.send("> Good Nights Pepss! Kamu Jangan Begadang Yaa! Ga Baik Buat Kesehatan")
  
@quiet.command()
async def p(ctx):
    await ctx.message.delete()
    await ctx.send("> **Assalamu\'alaikum..**")

@quiet.command()
async def l(ctx):
    await ctx.message.delete()
    await ctx.send("> **Wa\'alaikumsallam**")
    
@quiet.command()
async def hack(ctx):
    await ctx.message.delete()
    await ctx.send("Installing...", delete_after=5)
    await asyncio.sleep(5)
    await ctx.send("Installing Files To Hacked Private Server...", delete_after=4)
    await asyncio.sleep(4)
    await ctx.send("Target Selected..", delete_after=3)
    await ctx.send("Installing... 0%\n▒▒▒▒▒▒▒▒▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 10%\n█▒▒▒▒▒▒▒▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 20%\n██▒▒▒▒▒▒▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 30%\n███▒▒▒▒▒▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 40%\n████▒▒▒▒▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 50%\n█████▒▒▒▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 60%\n██████▒▒▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 70%\n███████▒▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 80%\n████████▒▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 90%\n█████████▒", delete_after=2)
    await asyncio.sleep(2)
    await ctx.send("Installing... 100%\n█████Installed█████", delete_after=3)
    await asyncio.sleep(3)
    await ctx.send("Target files Uploading...\n\nDirecting To Remote  server to hack..", delete_after=3)
    await asyncio.sleep(3)
    await ctx.send("Connecting nd getting combined token from discord.com", delete_after=3)
    await asyncio.sleep(3)
    await ctx.send("100%\n█████████HACKED███████████ `\n\n\n  TERMINAL: \nDownloading Bruteforce-Discord-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Discord-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for discord: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: `", delete_after=3)
    await asyncio.sleep(3)
    await ctx.send("**Akun Diretas**\n\n> Mengumpulkan semua data\n\n> Sedang login kedalam Discord....", delete_after=5)
    await asyncio.sleep(5)
    await ctx.send("**Login Succes...**", delete_after=4)
    await asyncio.sleep(4)
    await ctx.send("Check Your DM!!", delete_after=6)
#============================================
#-------------------END----------------------
#============================================


#============================================
#------------------UTILLS--------------------
#============================================
@quiet.event
async def on_ready():
    with open("quiet/setting/data.json", "r") as f:
        data = json.load(f)
    if data["guild"] == None or data["channel"] == None:
        pass
    else:
        try:
            voice_channel = discord.utils.get(bot.get_guild(int(data["guild"])).channels, id = int(data["channel"]))
            
            await voice_channel.connect()
            print(f"{Fore.GREEN}[-]{Fore.WHITE} Connected to {Fore.CYAN}{voice_channel} {Fore.WHITE}in {Fore.CYAN}{voice_channel.guild}{Fore.WHITE}.")
        except:
            print(f"{Fore.RED} [ - ] Error Occured. Please reconnect using commands.")

@quiet.command()
async def join(ctx, voice_channel : discord.VoiceChannel):
    await ctx.message.delete()
    await voice_channel.connect()
    data = {"guild":str(ctx.guild.id),"channel":str(voice_channel.id)}
    with open("quiet/setting/data.json", "w") as f:
        json.dump(data, f)
    await ctx.guild.change_voice_state(channel=voice_channel, self_mute=False, self_deaf=False)
    await ctx.send("> Join to Voice Channel **Successful**")
    print(f"{Fore.GREEN}[-]{Fore.WHITE} Connected to {Fore.CYAN}{voice_channel} {Fore.WHITE}in {Fore.CYAN}{voice_channel.guild}{Fore.WHITE}.")

@quiet.command()
async def leave(ctx):
    await ctx.message.delete()
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    with open("quiet/setting/data.json", "w") as f:
        json.dump({"guild":None,"channel":None}, f)
    await ctx.send("> Leave From Voice Channel **Sucsessful**")
    print(f"{Fore.RED}[-]{Fore.WHITE} Disconnected from {Fore.CYAN}{voice_client.channel}{Fore.WHITE} in {Fore.CYAN}{ctx.message.guild}{Fore.WHITE}.")

@quiet.command()
async def play(ctx, url):
    audio_player = discord.PCMVolumeTransformer(discord.AudioSource(url))
    ctx.voice_client.play(audio_player, after=lambda e: print('Player error: %s' % e) if e else None)


@quiet.event
async def on_message(message):

     try:

        if message.content == '!deafen':
             voice_state = message.author.voice
             if voice_state is not None and voice_state.deaf:
                 await message.channel.send('I am already deafened!')
             else:
                 await message.author.edit(self_deaf=True)
                 await message.channel.send('I am now deafened!')
     except:
        pass

     await quiet.process_commands(message)

@quiet.command()  
async def unb(ctx, message, *, amount: typing.Optional[int] = 0):
	await ctx.message.delete()
	await ctx.send('Farming **Work** Unbeliavabot **Enabled**!\n> Bypass Global = ON')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(2)
			await ctx.send(message, delete_after=2)
			await asyncio.sleep(amount)
      
@quiet.command()
async def unstop(ctx):
	await ctx.message.delete()
	await ctx.send('> Farming **Work** Unbeliavaboat is **Disabled**')
	global dmcs
	dmcs = False

@quiet.command()
async def sleave(ctx, guild_id):
    await ctx.message.delete()
    await quiet.get_guild(int(guild_id)).leave()
    await ctx.send("> **Jurus Ninjaaaa..**")
    await asyncio.sleep(3)
    await ctx.send(f"```Berhasil Keluar Dari Server\nID SERVER {guild_id}```")

@quiet.command()
async def ping(ctx):
    await ctx.message.delete()
    start = time.perf_counter()
    message = await ctx.send("> Resolving...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content=f"```\nPong!: {round(quiet.latency * 1000)}ms\nTotal latency: {duration:.0f}ms\n```")

@quiet.command()
async def cnick(ctx, *, name: str=None):
    await ctx.message.delete()
    if name is None:
        await ctx.send(f"```Usage: {ctx.prefix}cnick <new name>```")
    elif len(name) < 1:
        await ctx.send("Name need to have atleast 1 characters")
    else:
        try:
            await ctx.author.edit(nick=name)
            await ctx.send(f"> Nickname Has Been Change to **{name}**")
        except Exception as e:
            await ctx.send(f"Error: {e}")
            
            
def is_me(m):
    return m.author == bot.user
@quiet.command()
async def urpurge(ctx, amount:int=None):
    await ctx.message.delete()
    try:
        if amount is None:
            await ctx.send("Invalid amount")
        else:
            deleted = await ctx.channel.purge(limit=amount, before=ctx.message, check=is_me)
            asd = await ctx.send('Deleted {} message(s)'.format(len(deleted)))
            await asyncio.sleep(3)
            await asd.delete()
    except:
        try:
            await asyncio.sleep(1)
            c = 0
            async for message in ctx.message.channel.history(limit=amount):
                if message.author == quiet.user:
                    c += 1
                    await message.delete()
                else:
                    pass
            asd = await ctx.send('Deleted {} message(s)'.format((c)))
            await asyncio.sleep(3)
            await asd.delete()
        except Exception as e:
            await ctx.send(f"Error: {e}")

@quiet.command()
async def userinfo(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.author
    mutual_servers = []
    for server in quiet.guilds:
        if server.get_member(member.id):
            mutual_servers.append(server.name)
    message = f"**〝 USER INFO 〞**\n"
    message += f"> ▸ Name: **{member.nick}#{member.discriminator}**\n"
    message += f"> ▸ ID: **{member.id}**\n"
    message += f"> ▸ Status: **{member.status}**\n"
    if mutual_servers:
        message += f'> ▸ Mutual Server:\n'
        for server in mutual_servers:
            message += f'```\n▸{server}\n```'
    message += f"> ▸ Joined At **{member.joined_at}**\n"
    message += f"> ▸ Created At: **{member.created_at}**\n"
    message += f"> ▸ Avatar: ||{member.avatar_url}||"
    await ctx.send(message)
    
@quiet.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    await ctx.send("*Getting ServerInfo...*", delete_after=3)
    await asyncio.sleep(3)
    guild = ctx.guild
    online = len([m.status for m in guild.members if m.status == discord.Status.online or m.status == discord.Status.idle])
    offline = len([m.status for m in guild.members if m.status == discord.Status.offline])
    total_users = online + offline
    member = ctx.author

    name = guild.name
    id = guild.id
    member_count = len(guild.members)
    owner = guild.owner
    owner_id = guild.owner_id
    icon_url = guild.icon_url
    created = guild.created_at
    level = guild.premium_tier
    tboost = guild.premium_subscription_count
    

    user_name = member.name
    user_id = member.id
    user_highest_role = member.top_role.name

    message = (f"> **〝 SERVER INFO 〞**\n"
               f"> ▸ Server name: **{name}**\n"
               f"> ▸ Server ID: **{id}**\n"
               f"> ▸ Level Boost: **{level}\n"
               f"> ▸ Total Boost: **{tboost}**\n"
               f"> ▸ All Members: **{total_users}**\n"
               f"> ▸ Owner: **{owner}**\n"
               f"> ▸ Owner ID: **{owner_id}**\n"
               f"> ▸ Created At: **{created}**\n"
               f"> ▸ Icon: ||{icon_url}||")
    await ctx.send(message)

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
    
@quiet.command()
async def weather(ctx, *, city: str=None):
    await ctx.message.delete()
    if city is None:
       await ctx.send("Enter City/Country Name!")
    # Get the current weather data for the city
    weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric").json()
    
    # Check if the city was found
    if weather_data["cod"] == "404":
        await ctx.send("```\nKota/Negara tidak ditemukan!.\n```")
    else:
        # Get the current temperature, humidity, and weather description
        #weather.main Group of weather parameters
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_code = weather_data["weather"][0]["id"]
        description = weather_data["weather"][0]["description"]
        wind_speed_mps = weather_data["wind"]["speed"]
        wind_speed_kph = wind_speed_mps * 3.6
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        day_of_week = now.strftime("%A")
        
        # Get the appropriate icon based on the weather code
        if weather_code >= 200 and weather_code <= 232:
            icon = ":cloud_lightning:"
            weather_condition = "thunderstorm"
            description = "**Hujan Badai disertai Gerimis Lebat**"
        elif weather_code >= 300 and weather_code <= 321:
            icon = ":cloud_rain:"
            weather_condition = "drizzle"
            description = "**Gerimis**"
        elif weather_code >= 500 and weather_code <= 531:
            icon = ":cloud_rain:"
            weather_condition = "rainy"
            description = "**Hujan Deras**"
        elif weather_code >= 600 and weather_code <= 622:
            icon = ":cloud_snow:"
            weather_condition= "snow"
            description = "**Salju Ringan**"
        elif weather_code >= 700 and weather_code <= 781:
            icon = ":fog:"
            weather_condition = "fog"
            description = "**Berkabut**"
        elif weather_code == 800:
            icon = ":sunny:"
            description = "**Awan Yang Cerah**"
        elif weather_code == 801:
            icon = ":partly_sunny:"
            description = "**Berawan**"
        elif weather_code >= 802 and weather_code <= 804:
            icon = ":cloud:"
            description = "**Berawan**"
        else:
            icon = ":sunny:"
            weather_condition = "clear"

        # Send the weather data to the user
        await ctx.send(f"❏ 𝐂𝐔𝐑𝐑𝐄𝐍𝐓𝐋𝐘 𝐖𝐄𝐀𝐓𝐇𝐄𝐑\n> **{city}**\n> {icon} {temperature}°C | Kelembapan : **{humidity}%** | {description}\n> Kecepatan Angin: **{wind_speed_mps}**m/s\n> **{day_of_week}**, {date_time}")

@quiet.command()
async def search(ctx, *, query):
    await ctx.message.delete()
    service = googleapiclient.discovery.build('customsearch', 'v1', developerKey='AIzaSyBN9SQQJg9sQxr3U8QUeMlosDmdVbBLff0')
    results = service.cse().list(q=query, cx='9678f11e344024890').execute()
    message = f'> SEARCH RESULT FOR **〝 "{query}" 〞**:\n\n'
    for result in results['items']:
        message += f' **{result["title"]}**\n> {result["link"]}\n\n'
    # Send the message to the current channel
    await ctx.send(message)
#===========================================
#-------------------END----------------------
#======================================


#============================================
#----------------DATABASE--------------------
#=========================================
print(f'''
{Fore.BLUE}
░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░

{Fore.GREEN}The program has successfully logged into the your account {quiet.user}

{Fore.BLUE}Prefix: {prefix}

Project Dev: QuietArtx
''')

keep_alive()
quiet.run(os.getenv("TOKEN"), bot=False)
#============================================
#----------------DATABASE--------------------
#============================================
