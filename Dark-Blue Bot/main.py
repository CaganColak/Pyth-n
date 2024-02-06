import io
import discord
from discord.ext import commands   
import random as rndm
import json
import pyshorteners
from key import token
import praw
import random
from utils.tools import *
import hashlib
import json
from discord.ext.commands import has_permissions, MissingPermissions
from gtts import gTTS


#encode şifrele
#decode çöz
colors=[0xeb4034,0x31e2e8,0x3e32e3,0xe332dd,0xe3e332]

intents = discord.Intents.default()
intents.messages = True

mainshop=[{"name":"Watch","price":100,"description":"time"},
{"name":"laptop","price":1000,"description":"work"},
{"name":"tv","price":1400,"description":"watch"},
{"name":"pc","price":2000,"description":"gaming"}
]

bot = commands.Bot(command_prefix='!', intents = intents)

def text_to_speech_and_save(text, filename="output.mp3", language='tr', speed=1.0):
    """
    Converts the given text to speech and saves it as an MP3 file.
    
    Parameters:
        text (str): The text to convert to speech.
        filename (str): The desired filename for the output MP3 file.
        language (str): The language of the text (e.g., 'en' for English, 'tr' for Turkish).
        speed (float): The speed of speech (default is 1.0). You can adjust it as needed.
    
    Returns:
        str: The filename of the saved MP3 file.
    """
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the speech as an MP3 file
    tts.save(filename)

    return filename

@bot.command()
async def Help(ctx, arg=None):
    """I think you are already know this"""
    command_names_list = [x.name for x in bot.commands]
    embed = discord.Embed(title="BabaPro bot's help")
    general_commands = "`avatar`, `ping`, `invite`"
    fun_commands = "`say`, `f`, `thiscommanddoesnothing`, `reverse`, `encodemorse`, `hotcalc`, `encode_md5`, `encode_sha256`, `hug`, `kiss`, `tts`"
    economy_commands = "`balance`, `beg`, `deposit`, `withdraw`, `rob`, `slot`, `send`, `shop`, `bag`, `buy`, `sell`, `coinflip`"
    moderation_commands = "`mute`, `unmute`, `ban`, `unban`, `kick`, `clear`"

    if arg is None:
        embed.add_field(name="general commands", value=general_commands, inline=False)
        embed.add_field(name="fun commands", value=fun_commands, inline=False)
        embed.add_field(name="economy commands", value=economy_commands, inline=False)
        embed.add_field(name="moderation commands", value=moderation_commands, inline=False)
        await ctx.send(embed=embed)
    elif arg in command_names_list:
        embed.add_field(
            name=f"!{arg}",
            value=bot.get_command(arg).help)
        await ctx.send(embed=embed)
    else:
        embed.add_field(
            name="Nope.",
            value="Don't think I got that command!"
        )
        await ctx.send(embed=embed)



@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="| !Help to help"))
	print(f'{bot.user} olarak giriş yaptık')


###General Commands###
@bot.command()
async def ping(ctx):
    """sends ping"""
    await ctx.send(f"pong! {round(bot.latency * 1000)}ms")


@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member=None):
    """Sends avatar"""
    if member is None:
        member = ctx.author
    await ctx.send("{}".format(member.avatar_url_as(size=256)))


@bot.command()
async def invite(ctx):
	"""sends invite link"""
	emb=discord.Embed(title="invite link" ,description=f"Add me with this [link]({discord.utils.oauth_url(bot.user.id)})!")
	await ctx.send(embed=emb)
      

@bot.command()
async def bruh(ctx):
	"""sends bruh gif"""
	await ctx.send("https://tenor.com/6ruK.gif")


@bot.command()
async def welcome(ctx):
	"""sends welcome gifs"""
	gifs=["https://media1.tenor.com/images/f898731211184dca06f52005d7d0a166/tenor.gif?itemid=8846380",
		"https://media.tenor.com/images/578d96612b002bd7dc9096536efcee56/tenor.gif",
		"https://media.tenor.com/images/eba043bd8859df792aaec7a185ec6cdb/tenor.gif",
		"https://media.tenor.com/images/4f276e8211aac2be5f33000e42cfa1d1/tenor.gif",
		"https://media.tenor.com/images/7ab5c8247e639abe8a5bb6de0f2bcf76/tenor.gif",
		"https://media.tenor.com/images/aef6732e83b229e0a7b80f5a177c3aee/tenor.gif"]
	await ctx.send(rndm.choice(gifs))
	
@bot.command()
async def serverinfo(ctx):
	"""sends server's info"""
	icon = str(ctx.guild.icon)
	name= ctx.guild.name
	verification= ctx.guild.verification_level	
	premiums=ctx.guild.premium_subscription_count
	channelnumber=len(ctx.guild.channels)
	voicenumber=len(ctx.guild.voice_channels)
	memberCount = str(ctx.guild.member_count)
	rolenumber=len(ctx.guild.roles)
	created=str(ctx.guild.created_at).split(".")[0]
	

	embed = discord.Embed(
      title=name + " Server Information",
      color=rndm.choice(colors)
    )

	embed.set_thumbnail(url=icon)
	embed.add_field(name="name", value=name, inline=True)	
	embed.add_field(name="verification", value=verification, inline=True)
	embed.add_field(name="premiums", value=premiums, inline=True)
	embed.add_field(name="text channels",value=channelnumber,inline=True)
	embed.add_field(name="voice channels",value=voicenumber,inline=True)
	embed.add_field(name="members",value=memberCount,inline=True)
	embed.add_field(name="roles",value=rolenumber,inline=True)
	embed.add_field(name="created at",value=created,inline=True)


	await ctx.send(embed=embed)


@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
	"""sends user's info"""
	if user is None:
		user = ctx.author      
	
	date_format = "%a, %d %b %Y %I:%M %p"
    
	joined_at=user.joined_at.strftime(date_format)
	created_at=user.created_at.strftime(date_format)
	
	embed = discord.Embed(color=rndm.choice(colors), description=user.mention)
	embed.set_author(name=str(user), icon_url=user.avatar)
	embed.set_thumbnail(url=user.avatar)
	embed.add_field(name="Joined", value=joined_at)
	members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
	embed.add_field(name="Registered", value=created_at)
	if len(user.roles) > 1:
		role_string = ' '.join([r.mention for r in user.roles][1:])
		embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
	perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
	embed.add_field(name="Guild permissions", value=perm_string, inline=False)
	embed.set_footer(text='ID: ' + str(user.id))
	return await ctx.send(embed=embed)


@bot.command()
async def servers(ctx):
	if ctx.author.id==735886435978182657:
		server_list=[]

		for i in range(0, len(bot.guilds), 10):
			embed = discord.Embed(title='Guilds', colour=0x7289DA)
			guilds = bot.guilds[i:i + 10]

		for guild in guilds:
			server_list.append(guild.name)

		embed.add_field(name="servers",value=server_list)
			

		await ctx.send(embed=embed)
###Fun Commands###
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
async def thiscommanddoesnothing(ctx):
    """It doesn't do any things (or does it? OwO)"""
    await ctx.send("Ha?")

@bot.command()
async def reverse(ctx, *, msg:str):
        """ffuts esreveR"""
        await ctx.send(msg[::-1])

@bot.command()
async def encodemorse(ctx, *, msg:str):
    """Encode something into morse code"""
    encoded_message = ""
    for char in list(msg.upper()):
        encoded_message += encode_morse[char] + " "
        await ctx.send(encoded_message)







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
async def hug(ctx, member: discord.Member = None, *, reason=None):
    """Hug someone"""
    if member is None or member == ctx.author:
        await ctx.send("You are too lonely right? \nNever mind, I am here for you dude. Let me hug you.")
    else:
        if reason is None:
            embed = discord.Embed(title=f"{ctx.author} hugged {member}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} hugged you")
        else:
            embed = discord.Embed(title=f"{ctx.author} hugged {member} for {reason}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} hugged you for {reason}")



@bot.command()
async def kiss(ctx, member: discord.Member = None, *, reason=None):
    """Kiss someone"""
    if member is None or member == ctx.author:
        await ctx.send("You are too lonely right? \nNever mind, I am here for you dude. Let me kiss you.")
    else:
        if reason is None:
            embed = discord.Embed(title=f"{ctx.author} kissed {member}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} kissed you")
        else:
            embed = discord.Embed(title=f"{ctx.author} kissed {member} for {reason}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} kissed you for {reason}")

###Hash Commands###
@bot.command(aliases=["encode-md5"])
async def encode_md5(ctx,*args):
	"""encodes text with md5"""
	original_text="".join(args)
	hash_obj = hashlib.md5(original_text.encode())
	emb= discord.Embed(title="md5 encryption",description=f"original text is: {original_text} \nresult is: {hash_obj.hexdigest()}" ,color=random.choice(colors))
	await ctx.send(embed=emb)



@bot.command(aliases=["encode-sha256"])
async def encode_sha256(ctx,*args):
	"""encodes text with sha256 """
	original_text="".join(args)
	hash_obj = hashlib.sha256(original_text.encode())
	emb= discord.Embed(title="sha256 encryption",description=f"original text is: {original_text} \nresult is: {hash_obj.hexdigest()}",color=random.choice(colors))
	await ctx.send(embed=emb)

###Economy Commands###
@bot.command(aliases=["bal"])
async def balance(ctx):
	"""sends balance info"""
	await open_account(ctx.author)

	user= ctx.author
	users = await get_bank_data()

	wallet_amt= users[str(user.id)]["wallet"]
	bank_amt= users[str(user.id)]["bank"]

	emb= discord.Embed(title=f"{ctx.author.name}'s balance",color=random.choice(colors))
	emb.add_field(name="Wallet balance",value=wallet_amt)
	emb.add_field(name="Bank balance",value=bank_amt)
	await ctx.send(embed=emb)


@bot.command()
async def beg(ctx):
	"""you beg someone"""
	await open_account(ctx.author)

	users= await get_bank_data()

	user= ctx.author


	earnings = random.randrange(101)

	await ctx.send(f"Someone gave you {earnings} coins!")

	users[str(user.id)]["wallet"] += earnings

	with open("mainbank.json","w") as f:
		json.dump(users,f)



@bot.command(aliases=["wd"])
async def withdraw(ctx,amount=None):
	"""withdraws money from bank"""
	await open_account(ctx.author)

	if amount== None:
		await ctx.send("Please enter the amount")
		return
	
	bal= await update_bank(ctx.author)

	amount= int(amount)
	if amount>bal[1]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount is must be positive!")
		return 

	await update_bank(ctx.author,amount)	
	await update_bank(ctx.author,-1*amount,"bank") 

	await ctx.send(f"You withdrew {amount} coins!")	



@bot.command(aliases=["dp"])
async def deposit(ctx,amount=None):
	"""deposits money in the bank """
	await open_account(ctx.author)

	if amount== None:
		await ctx.send("Please enter the amount")
		return
	
	bal= await update_bank(ctx.author)

	amount= int(amount)
	if amount>bal[0]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount is must be positive!")
		return 

	await update_bank(ctx.author,-1*amount)	
	await update_bank(ctx.author,amount,"bank") 

	await ctx.send(f"You you deposited {amount} coins!")	



@bot.command()
async def send(ctx,member:discord.Member,amount=None):
	"""sends money to user"""
	await open_account(ctx.author)
	await open_account(member)


	if amount== None:
		await ctx.send("Please enter the amount")
		return
	
	bal= await update_bank(ctx.author)

	if amount=="all":
		amount=bal[0]

	amount= int(amount)
	if amount>bal[1]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount is must be positive!")
		return 

	await update_bank(ctx.author,-1*amount,"bank")	
	await update_bank(member,amount,"bank") 
	await member.send(f"{ctx.author} gave you {amount} coins")
	await ctx.send(f"You gave {amount} coins!")	


@bot.command()
async def slot(ctx,amount=None): #düzenlenicek
	"""bets"""
	await open_account(ctx.author)

	if amount== None:
		await ctx.send("Please enter the amount")
		return

	bal= await update_bank(ctx.author)

	amount= int(amount)
	if amount>bal[0]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount must be positive")
		return

	emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
	a = random.choice(emojis)
	b = random.choice(emojis)
	c = random.choice(emojis)

	slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"    

	if (a == b == c):    
		await ctx.send(f"{slotmachine} All matching, you won! 🎉")
		await update_bank(ctx.author,2*amount)    

	elif (a == b) or (a == c) or (b == c):
		await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
		await update_bank(ctx.author,1.5*amount)
	else:
		await ctx.send(f"{slotmachine} No match, you lost 😢")
		await update_bank(ctx.author,-1*amount)
            

@bot.command(aliases=["coin","flip"])
async def coinflip(ctx,amount=None,side=None):
	"""coinflips"""
	await open_account(ctx.author)
	if amount== None:
		await ctx.send("Please enter the amount")
		return
	if side==None:
		await ctx.send("Please enter the side")
		return
	bal= await update_bank(ctx.author)

	amount= int(amount)
	if amount>bal[0]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount must be positive")
		return

	coinsides = ['head', 'tail']
	result=random.choice(coinsides)
	

	if side in coinsides:
		if side==result:
			await ctx.send("you win")
			await update_bank(ctx.author,1*amount)    

		else :
			await ctx.send("you lose")
			await update_bank(ctx.author,-1*amount)    

	else:
		await ctx.send("please sure to write trutly")
	

@bot.command()
async def rob(ctx,member:discord.Member):
	"""robs the user"""
	await open_account(ctx.author)
	await open_account(member)


	bal= await update_bank(member)

	
	if bal[0]<100:
		await ctx.send("It's not worth it!")
		return

	earnings = random.randrange(0,bal[0])

	await update_bank(ctx.author,earnings)	
	await update_bank(member,-1*earnings,"wallet") 

	await ctx.send(f"You robbed and got {earnings} coins!")	


@bot.command()
async def shop(ctx):
	"""sends market"""
	emb=discord.Embed(title="shop", color=random.choice(colors))
	for item in mainshop:
		name= item["name"]
		price=item["price"]
		desc=item["description"]
		emb.add_field(name=name,value=f"${price}| {desc}")

	await ctx.send(embed=emb)



@bot.command()
async def buy(ctx,item,amount=1):
	"""buys item"""
	await open_account(ctx.author)

	res = await buy_this(ctx.author,item,amount)

	if not res[0]:
		if res[1]==1:
			await ctx.send("That's object isn't there")
			return
		if res[1]==2:
			await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
			
	await ctx.send(f"You just bought {amount} {item}")



@bot.command()
async def bag(ctx):
	"""opens bag"""
	await open_account(ctx.author)
	user = ctx.author
	users= await get_bank_data()

	try:
		bag= users[str(user.id)]["bag"]
	except:
		bag=[]

	emb= discord.Embed(title="bag",color=random.choice(colors))
	for item in bag:
		name= item["item"]
		amount= item["amount"]

		emb.add_field(name=name,value=amount)

	await ctx.send(embed=emb)
	

@bot.command()
async def sell(ctx,item,amount = 1):
	"""sells item"""
	await open_account(ctx.author)

	res = await sell_this(ctx.author,item,amount)

	if not res[0]:
		if res[1]==1:
			await ctx.send("That Object isn't there!")
			return
		if res[1]==2:
			await ctx.send(f"You don't have {amount} {item} in your bag.")
			return
		if res[1]==3:
			await ctx.send(f"You don't have {item} in your bag.")
			return

	await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]



async def buy_this(user,item_name,amount):
	item_name= item_name.lower()

	name_=item_name 

	for item in mainshop:
		name= item["name"].lower()
		if name==item_name:
			name_==name
			price=item["price"]
			break

	if name_==None:
		return[False,1]

	cost=price*amount
	print(cost)
	users= await get_bank_data()	

	bal = await update_bank(user)

	if bal[0]<cost:
		return[False,2]

	try:
		index=0
		t=None
		for thing in users[str(user.id)]["bag"]:
			n= thing["item"]
			if n== item_name:
				old_amt=thing["amount"]
				new_amt=old_amt+amount
				users[str(user.id)]["bag"][index]["amount"]=new_amt
				t=1
				break
			index+=1
		if t== None:
			obj={"item":item_name,"amount":amount}
			users[str(user.id)]["bag"].append(obj)
	except:
		obj= {"item":item_name,"amount":amount}
		users[str(user.id)]["bag"]=[obj]	
	
	with open("mainbank.json","w")as f:
		json.dump(users,f)	

	await update_bank(user,cost*-1,"wallet")

	return[True,"Worked"]


async def open_account(user):
	with open("mainbank.json","r") as f:
		users = json.load(f)

	if str(user.id) in users:
		return False
	else:
		users[str(user.id)]={}
		users[str(user.id)]["wallet"] =0
		users[str(user.id)]["bank"]=0

	with open("mainbank.json","w") as f:
		json.dump(users,f)
	return True



async def get_bank_data():
	with open("mainbank.json","r") as f:
		users = json.load(f)

	return users



	
async def update_bank(user,change=0,mode="wallet"):
	users = await get_bank_data()

	users[str(user.id)][mode] += change

	with open("mainbank.json","w") as f:
		json.dump(users,f)
	
	bal= [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
	return bal

###Moderation Commands###
@bot.command()#mute
@has_permissions(manage_messages=True)
async def mute(ctx,member: discord.Member,*,reason=None):
    """mutes the user"""
    guild= ctx.guild
    mutedRole= discord.utils.get(guild.roles,name="Muted")
    
    if not mutedRole:
        mutedRole= await guild.create_role(name="Muted")
        
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False , send_messages=False, read_message_history=True, read_messages=True)
    
    await member.add_roles(mutedRole,reason=reason)
    await ctx.send(f"{member.mention} is Muted for {reason}")        
    await member.send(f"you were muted in this server {guild.name} for {reason} ")

@bot.command()#unmute
@has_permissions(manage_messages=True)
async def unmute(ctx,member:discord.Member):
    """unmutes the user"""
    guild= ctx.guild
    mutedRole = discord.utils.get(ctx.guild.roles,name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"{member.mention} is Unmuted ") 
    await member.send(f"you were Unmuted in this server {guild.name} ")

@bot.command()
@has_permissions(manage_messages=True)
async def clean(ctx, limit: int):
    """deletes messages"""
    await ctx.channel.purge(limit=limit)
    await ctx.send('Cleared by {}'.format(ctx.author.mention))
    await ctx.message.delete()





@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
    """Kicks user"""
    await user.kick(reason=reason)
    kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.channel.send(embed=kick)
    await user.send(embed=kick)






@bot.command()
@has_permissions(kick_members=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    """Bans user"""
    await user.ban(reason=reason)
    ban = discord.Embed(title=f":boot: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)


@bot.command()
@has_permissions(ban_members=True)
async def unban(ctx,user:discord.Member,*,reason="No reason provided"):
    """Unbans User"""
    banned_users= await ctx.guild.ban()
    member_name,member_disc= user.split("#")

    for banned_entry in banned_users:
        user= banned_entry.user

        if (user.name, user.discriminator)==(member_name,member_disc):
            await ctx.guild.unban(user)
            await ctx.send(user.name+" has been unbaned")
            return
    await ctx.send(user+" was not found")

@bot.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit=amount+1)

@bot.command()
async def tts(ctx, *, text: str):
    # Ensure that the user provided some text
    if text.strip():
        # Convert text to speech and save it as an MP3 file
        filename = text_to_speech_and_save(text)

        # Send the MP3 file as an attachment
        await ctx.send(file=discord.File(filename))
    else:
        await ctx.send("Please provide some text to convert to speech.")

# bot.add_command(mute)
# bot.add_command(unmute)
# bot.add_command(subreddit)
# bot.add_command(balance)
# bot.add_command(beg)
# bot.add_command(deposit)
# bot.add_command(withdraw)
# bot.add_command(rob)
# bot.add_command(slot)
# bot.add_command(clean)
# bot.add_command(send)
# bot.add_command(shop)
# bot.add_command(bag)
# bot.add_command(buy)
# bot.add_command(sell)
# bot.add_command(meme)
# bot.add_command(encode_md5)
# bot.add_command(encode_sha256)
# bot.add_command(say)
# bot.add_command(f)
# bot.add_command(coinflip)
# bot.add_command(kick)
# bot.add_command(thiscommanddoesfuckingnothing)
# bot.add_command(reverse)
# bot.add_command(encodemorse)
# bot.add_command(hotcalc)
# bot.add_command(ban)
# bot.add_command(unban)
# bot.add_command(hug)
# bot.add_command(kiss)

#fılename = text_to_soeech()
#@bot.command()
#async def send(ctx):
 # with open('voice/11.mp3', 'rb') as f:
  #      voice = discord.File(f)
  #ctx.send(file = voice)

bot.run(token) 
