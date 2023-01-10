@client.event
async def on_ready():
    # Load the prefix from the prefix file if exists
    if os.path.exists("quiet/setting/prefixes.json"):
        with open("prefixes.json", "r") as f:
            prefix = f.read()
        client.command_prefix = prefix

    with open("prefixes.json", "w") as f:
            f.write(client.command_prefix)
