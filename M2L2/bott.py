import discord
from discord.ext import commands
import random
from bot_logic import *
import requests


description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

oneri =["Plastik bardak ve şişe gibi tek kullanımlık ürünleri kullanmaktan kaçının",
        "Kağıt tüketimini azaltmak için e-okuyuculara geçiş yapın",
        "Mümkün olduğunca az ambalajlı market ürünlerini ve atıştırmalıkları tercih edin, yiyecekleri ağırlıklarına göre (ambalajsız) satın alın ve yeniden kullanılabilir poşetlere geçmeye çalışın",
        "Geri dönüştürmeye çalışın. Geri dönüştürülebilir ürünler için bir çöp kutusu ayırın ve dolduğunda geri dönüşüm istasyonuna taşıyın"]

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def oneri(ctx):
    """Adds two numbers together."""
    await ctx.send(random.choice(oneri))

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def avatar(self, ctx, *,  avamember:discord.Member):
    """sends users avatar"""
    userAvatarUrl = avamember.avatar_url

@bot.command()
async def say(ctx, *, message:str):
    """Make the bot say whatever you want it to say"""
    try:
        await ctx.message.delete()
    except:
        pass
    await ctx.send(message)

@bot.command()
async def f(ctx, *, text: commands.clean_content = None):
    """ Press F to pay respect """
    hearts = ['❤', '💛', '💚', '💙', '💜']
    reason = f"for **{text}** " if text else ""
    await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")

@bot.command()
async def reverse(ctx, *, msg:str):
        """ffuts esreveR"""
        await ctx.send(msg[::-1])


@bot.command(aliases=['howhot', 'hot'])
async def hotcalc(ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")

@bot.command()
async def hug(ctx,member=None,*, reason=None):
    """Hug someone"""
    if member==None or member== ctx.author:
        await ctx.send("You are too lonely right? \n nevermind I am here for you dude let me hug you")
    else:
        if reason==None:
            embed=discord.Embed(title=f"{ctx.author} hugged {member}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} hugged you")            

        else:
            embed=discord.Embed(title=f"{ctx.author} hugged {member} for {reason}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} hugged you for {reason}")


@bot.command()
async def kiss(ctx,member=None,*, reason=None):
    """kiss someone"""
    if member==None or member== ctx.author:
        await ctx.send("You are too lonely right? \n nevermind I am here for you dude let me kiss you")
    else:
        if reason==None:
            embed=discord.Embed(title=f"{ctx.author} kissed {member}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} kissed you")            
            
        else:
            embed=discord.Embed(title=f"{ctx.author} kissed {member} for {reason}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} kissed you for {reason}")  

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
@cool.command(name='user')
async def _user(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the user is cool.')


bot.run('MTExMjA2OTUwMzE2MTk5OTQwMA.GKCM2x.2JNkAcatVvvsK-f-ZfC-fjsyscfeTEIBC_u-1o')