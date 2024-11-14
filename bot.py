import discord
import os
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

    
@bot.event
async def on_ready():
    print(f'{bot.user} giriş yaptı')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    mem_name = os.listdir('images')
    mem_namee = random.choice(mem_name)
    with open(f'images/{mem_namee}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def afis(ctx):
    afis_isim = os.listdir('afisler')
    afisss= random.choice(afis_isim)
    with open(f'afisler/{afisss}' , 'rb' ) as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def esya(ctx):
    esya_isim = os.listdir('esyalar')
    esyaaa= random.choice(esya_isim)
    with open(f'esyalar/{esyaaa}' , 'rb' ) as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
bot.run("")






