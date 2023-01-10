@client.command(name='changeprefix', help='Change the bot prefix')
async def changeprefix(ctx, prefix: str):
    if len(prefix) != 1:
        await ctx.send("Prefix should be only one character.")
        return
    elif any(c.name == prefix for c in client.commands):
        await ctx.send(f"{prefix} is already used as command name")
        return
    else:
        client.command_prefix = prefix
        await ctx.send(f"Prefix changed to {prefix}")
