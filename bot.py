import os

import ctx as ctx
from discord.ext import commands
import discord

def run(msg,role):
    if role == "main":
        ping = 939298116786585600
    if role == "awa":
        ping = 939298067390271598
    if role == "manos":
        ping = 939297929527693333


    try:
        TOKEN = os.getenv('DISCORD_TOKEN')
        GUILD = 'Bdo Market Alarm'

        client = discord.Client()

        @client.event
        async def on_ready():
            for guild in client.guilds:
                if guild.name == GUILD:
                    break
            print(guild.roles)

            channel = client.get_channel(938387578313392168)
            await channel.send(msg+" <@&{}>".format(ping))


            await client.close()

        client.run(TOKEN)
    except RuntimeError:
        pass


# run("Manos pen gonna be sold in XX:XXX:XXX (just a test mssg lol)","manos")