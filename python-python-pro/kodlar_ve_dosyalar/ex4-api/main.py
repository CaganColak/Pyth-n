import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_pokemon_image_url():
    total_pokemon = 500
    random_pokemon_id = random.randint(0, total_pokemon) 
    url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}'
    res = requests.get(url)
    data = res.json()
    return data['name']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program get_duck_image_url() fonksiyonunu çağırır'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('poke')
async def duck(ctx):
    '''poke komutunu çağırdığımızda, program get_pokemon_image_url() fonksiyonunu çağırır'''
    pokemon = get_pokemon_image_url()
    await ctx.send(pokemon)


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)


bot.run("")