import discord
import sys
import random
import os 
import json
import youtube_dl
from discord.ext import commands, tasks
from discord.utils import get 


client = commands.Bot(command_prefix = "*", help_command=None)
#                removing default help cmd     ^ ^ ^ ^ ^ ^


#FYI : 5 SPACES IN BETWEEN EACH COMMANDS OR GAY

#https://discordpy.readthedocs.io/en/stable/ <---- Official docs to help u understand some codes

#===========================================================================================  
list = ["shit", "ass", "pp", "noob", "trash", "anus", "dingus", "idiot", "dumbass", "dimwit", "retard", "dumb", "jackass", "dunce",]

killlist = ["has died to corona", "ate burgerking footlettuce burgers", "got cancelled", "made twitter mad", "got the 0 divide 1", "died from deep throating a frying pan", "has been violated", "has been staged to death penalty", "shoved his dick into a toaster",
'fell off his gaming chair and snapped his neck',
'left the stove on',
"got isekai'd",
'got vibe checked',
'snapped back to reality',
'got shot by da hood gangmembers',
'got molested by Pablo escobar',
'had too much mdma',
'drank bromine',
"Truck-kun strikes again! And isekai’ed",
'died from blueballs',
'jerked off too much',
'had a epilleptic seizure from smoothing his brain with sandpaper',
'died from stage 3 diabetes',
'died',
'Molested by a child',
'got stabbed by a swordfish',
'died from hiv',
'Reincarnated as a hilichurl',
'stuck their dick into a woodchipper and bled out.',
"went skydiving without a parachute.",
"choked on a colossal, voluptuous pair of big balls.",
"tried to express their opinion on twitter.",
"lived a long and fulfilling life, eventually succumbing to their chronic cellular deterioration and passing away serenely surrounded by loved ones.",
"tried to have sex with yo mama and suffocated in her voluminous body's embrace."]

posilist = ["https://tenor.com/view/positive-staypositive-motivation-yougothis-gif-3551207",

"https://tenor.com/view/hard-work-positive-bunny-dont-give-up-you-are-getting-stronger-gif-14030477",

"https://tenor.com/view/chibird-love-sending-extra-love-me-to-you-heart-gif-16936183",

"https://cdn.discordapp.com/attachments/875363803213205514/883900453761450024/image0.png",

"https://cdn.discordapp.com/attachments/875363803213205514/883900541929922580/Loading-Penguin-Hugs-1.png",

"https://cdn.discordapp.com/attachments/875363803213205514/883900605897273395/original.png",

"https://cdn.discordapp.com/attachments/875363803213205514/883900641553023036/image0.png",

"https://cdn.discordapp.com/attachments/820393870747238420/878758799333285899/9aaf75d501ee0d47c3165d5bf4b97a53.png",

"https://tenor.com/view/ghost-hug-positivity-its-good-gif-14571097",

"https://tenor.com/view/positive-positivity-motivation-you-got-this-stay-positive-gif-3551217",

"https://tenor.com/view/self-esteem-penguin-motivation-positive-positivity-gif-3551221",

"https://tenor.com/view/love-heart-penguin-gif-11088475",

"https://tenor.com/view/penguin-motivational-determination-gif-8004667",

"https://tenor.com/view/positive-vibes-keep-it-up-gif-11419213",

"https://tenor.com/view/chibird-bad-things-react-positively-control-gif-5430828",

"https://cdn.discordapp.com/attachments/875363803213205514/883992977356259408/chibird.png",

"https://tenor.com/view/moody-happiness-kitty-radiate-absorb-sadness-gif-4950292",

"https://tenor.com/view/bunny-positive-no-giving-up-gif-14030474",

"https://tenor.com/view/positive-positivity-stay-positive-you-can-do-it-bunny-gif-3551210",

"https://tenor.com/view/smile-positive-stay-positive-positivity-bunny-gif-3631031",

"https://tenor.com/view/positive-stay-positive-motivation-bunny-positivity-gif-3551216",

"https://tenor.com/view/cat-positivity-cute-remember-gif-14571098",

"https://tenor.com/view/positive-vibes-bunny-rabbit-good-morning-gif-14301182",

"https://tenor.com/view/stay-positive-positive-positivity-motivation-bunny-gif-3551214",

"https://tenor.com/view/positive-positivity-stay-positive-motivation-you-can-do-it-gif-3551208",

"https://tenor.com/view/happy-motivation-stay-positive-positive-positivity-gif-3551219",

"https://tenor.com/view/motivation-happy-cute-bunny-thinking-gif-12304799",

"https://tenor.com/view/bunny-positive-happy-gif-14030475",

"https://tenor.com/view/cat-bouncing-motivation-you-can-do-it-cartoon-gif-5430827",

"https://tenor.com/view/stay-positive-you-got-it-positive-positivity-motivation-gif-3551218",

"https://tenor.com/view/fairydols-gif-22167704",

"https://tenor.com/view/chibird-penguin-hug-gif-14248948",

"https://tenor.com/view/my-undying-love-and-support-hearts-gif-15474239",

"https://tenor.com/view/sunshine-someones-sunshine-olliebear-gif-22508291",

"https://tenor.com/view/chibird-gif-5430509",

"https://tenor.com/view/cheer-chibird-gif-10323275",

"https://tenor.com/view/motivational-toast-motivation-good-morning-gif-5430517",

"https://tenor.com/view/you-have-mail-youve-got-mail-gif-14006284",

"https://tenor.com/view/love-dont-worry-okay-well-work-through-this-together-cute-gif-15650807",

"https://tenor.com/view/catch-lol-sending-you-love-boing-slighshot-gif-15718106",

"https://tenor.com/view/love-all-my-love-for-you-penguin-can-of-love-gif-15717367",

"https://tenor.com/view/chibird-nice-day-gif-19690903",

"https://tenor.com/view/pocket-hedgehog-keep-up-the-good-work-gif-12865616",

"https://tenor.com/view/positive-chibird-cute-self-love-gif-20964137",

"https://tenor.com/view/snail-encouragement-you-can-do-it-you-got-this-gif-5674505"
]

#===========================================================================================





@client.event 
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game("in water (Use *help)"))
  #  ^ ^ ^ ^ ^ ^ Change text to change custom status 
  print("Bot is up and running") 




#If message comes from bot, ignore
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  await client.process_commands(message)

#idfk imma chjeck what the error is
#ok but what does is need
# go down and help me with warn command
#automod

banned_words = ["dddaadadadadad"]

@client.event
async def on_message(message):
  for word in banned_words:
    if word in message.content:   
      await message.delete()
  await client.process_commands(message)








#Help
@client.command()
async def help(ctx):
  embed = discord.Embed(title = "The available commands are:",
   description = 'The prefix is * ',
   colour = discord.Colour.green())


  embed.add_field(name = "Entertainment   ", value = "kalm, rateme, 8ball \n kill, positivity    ")
  embed.add_field(name = "Moderation", value = "kick, ban, mute, clear")
  embed.add_field(name= "Other", value = "ping, credits, borgir / bg")
  await ctx.send(embed=embed)






#kalm
@client.command()
async def kalm(ctx):
  await ctx.send(f"https://tenor.com/view/kalm-calm-panik-meme-mem-gif-19765028")




#Ping 
@client.command()
async def ping(ctx):
  await ctx.send(f"Pong! {round(client.latency * 1000)}ms(Bot's ping)")





#Credits 
@client.command(aliases = ['credit', 'Credit', 'Credits'])
async def credits(ctx): 
  await ctx.send(f"**Founders / Coders:**\nThe Duck Lord: @ARandomDuck#0001\nThe Narwhal: Electrik Narwhal#3540 \n\n**Contributors:**\nEmiya - Selected current prefix\nwan sexc - He's a chad.\nOtto - He's cool\nRex - My other half \nPlopify#7433, Lens#7359, CrackheadMungkiii#0436 - contributed on making the kill command")





#Rate me 
@client.command(aliases=['rate', 'rm'])
async def rateme(ctx):
  await ctx.send(random.choice(
    [ 
      "0/10 no iq kid "+random.choice(list)+" kid hair cut looks like a bowl of cereal kid sanded his brain to make his brain look smoother kid",
      
      "1/10 looks like a "+random.choice(list)+" probably ate "+random.choice(list)+" and the only test that ever you passed was HIV",
     "2/10 "+ random.choice(list)+" kid",
     "3/10 this guy's a " + random.choice(list),
     "4/10 "+ random.choice(list) +" but ok",
     "5/10 average",
      "6/10 not "+ random.choice(list)+" guy ngl",
      "7/10 pretty good",
      "8/10 good guy",
      "9/10 pro",
      "10/10 god"
     ]))





#8ball 
@client.command(aliases=['8ball', '8b'])
async def _8ball(ctx):
  responses = ["It is decidedly so.",
   "Without a doubt",
   "Yes definitely.",
   "You may rely on it.",
   "As I see it, yes.",
   "Most likely.",
   "Probably.",
   "Yes.",
   "Signs point to yes.",
   "Hell no.",
   "Um probably not",
   "You won't like the answer.",
   "Yeah no.",
   "I don't think so.",
   "Don't count on it.",
   "My reply is no.",
   "My sources say no.",
   "Very doubtful"]
  await ctx.send(random.choice(responses))





#Purge / Clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  amount = amount + 1
  await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error1(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Please specify an amount.')
  elif isinstance(error, commands.MissingPermissions):
    await ctx.send("Nice try kid but you don't have the required permissions")
#Purge end





#Super secret hentai command (confidential)
@client.command(aliases=['298547'])
async def _djsbfiousdhfasdhsfisdfhjoisdhjfsiodfhsiodhfshfhIofshbfijsbdfijbobfjsdfnjsdfbskfsfkjbgshjngfkhnfkhfglkhdfgkfdhglfdklghdfhgjfdkgdfhgjkdfhgldujgridnjgdfng(ctx):
  await ctx.send("Sauce ;)\n\nhttps://cdn.discordapp.com/attachments/876405142323331082/883220258264088596/image0.jpg\n\nhttps://nhentai.net/g/298547")









#DONT DELETE DOWN HERE

#Ghost ping (confidential)
#@client.command()
#async def ghostping(ctx,user_id, self :int):
 # user = ctx.guild.get_member(user_id)
  #mention = f'<@!{user.id}>'
  #await ctx.send(user)
  #if mention in ctx.author:
   # await ctx.send((mention), ctx.channel.purge(2))


#user = ctx.guild.get_member(user_id)

#DONT DELETE UP HERE^^^^^^^



#Kick / Ban 
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f"Successfully kicked {member.mention}")

@kick.error
async def kick_error1(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Nice try kid but you don't have the required permissions")

@kick.error
async def kick_error2(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please specify who")
    
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send("Ban successfully executed")

@ban.error
async def ban_error1(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Nice try kid but you don't have the required permissions")

@ban.error
async def ban_error2(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please specify who")





#Unban 
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if(user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention} successfully.")

  




#Mute 
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member, *, reason="unspecified"):
  if member.top_role >= ctx.author.top_role: 
        await ctx.send("You can't mute people with higher roles than you peasant.")
        return

  guild = ctx.guild
  mutedrole = discord.utils.get(guild.roles, name = "Muted")

  if not mutedrole: 
    mutedrole = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedrole, send_messages=False, read_message_history=True,read_messages=True)

  await member.add_roles(mutedrole, reason=reason)
  await ctx.send(f"Muted {member.mention} successfully for reason: {reason}")


@mute.error
async def mute_error1(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please specify who.")

  elif isinstance(error, commands.MissingPermissions):
    await ctx.send("Nice try kid but you don't have the required permissions")





#Unmute
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member):
  mutedrole = discord.utils.get(ctx.guild.roles, name = "Muted")


  await member.remove_roles(mutedrole)
  await ctx.send(f"Successfully unmuted {member.mention}")

@unmute.error
async def unmute_error1(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Nice try kid but you don't have the required permissions")



#i need help
def save_warn(ctx, member: discord.Member):
    with open('warns.json', 'r') as f:
         warns = json.load(f)

         warns[str(member.id)] += 1

    with open('warns.json', 'w') as f:
         json.dump(warns, f)

def remove_warn(ctx, member: discord.Member, amount: int):
    with open('warns.json', 'r') as f:
         warns = json.load(f)

         warns[str(member.id)] -= amount

    with open('warns.json', 'w') as f:
         json.dump(warns, f)
    
def warns_check(member: discord.Member):
    with open('warns.json', 'r') as f:
         warns = json.load(f)

         warns[str(member.id)]
    return warns

#Warn 

#down here is the problem
@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason):
      save_warn(ctx, member)
      warned=discord.messag("warned " + f"{member.mention} ")
      await ctx.send(warned)


@client.command()
@commands.has_permissions(kick_members=True)
async def warnings(ctx, member: discord.Member):
      warns = warns_check(member)
      await ctx.send(f"{member.name} has {warns} warnings.")

@client.command()
@commands.has_permissions(kick_members=True)
async def rmwarn(ctx, member: discord.Member, amount: int):
      remove_warn(ctx, member, amount)
      await ctx.send(f"Removed {amount} warnings from {member.name}.")

@warn.error
async def warn_error1(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please specify a user.")






#Kill command 
@client.command()
async def kill(ctx, user:discord.User):
  await ctx.send(f"{user.mention} "+(random.choice(killlist))) 





#Positivity command
@client.command(aliases = ["positive"])
async def positivity(ctx):
  await ctx.send(random.choice(posilist))





#killtest (basically mentioning author and the mentioned user at the same time)
@client.command(pass_context = True)
async def killtest(ctx, user:discord.User):
  await ctx.send(ctx.message.author.mention+" killed "+ f"{user.mention} ")

@killtest.error
async def kill_error1(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please specify a user")



#Is god check
def isgod(ctx):
    with open('gods.txt') as f:
        if str(ctx.author.id) in f.read():
            return ctx.author.id        
#Godlist
@client.command(aliases=["gods"])
@commands.check(isgod)
async def godlist(ctx):
  await ctx.send("You are a certified god.")

@godlist.error
async def gl_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("You are not a god, sorry.")

#Ascend a god
@client.command()
@commands.check(isgod)
async def ascend(ctx, user:discord.Member=None):
    if user == None:
        await ctx.send("You need to tell us who to ascend.")
        return


    def is_god(user_id): 
        with open('gods.txt', 'r') as f:
            if str(user_id) in f.read():
                return True
            else:
                return False

    def ascend_god(user_id):
        with open('gods.txt', 'a') as f: 
            f.write(f"\n{str(user_id)}\n")
            f.close()

    # Now we put those functions to use #
    if is_god(user.id) == True:
        await ctx.send(f"{user.mention} has already ascended")
    else:
        ascend_god(user.id)
        await ctx.send(f"The light is flickering, the floor is shaking, the sky is dark, the council has spoken a god has awoken. All hail {user.mention}")



#random sauce
@client.command(aliases=["rs"])
@commands.check(isgod)
async def randomsauce(ctx):
  await ctx.send(f"https://nhentai.net/g/{random.randint(1, 273999)}" )

@randomsauce.error
async def rs_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("Only gods can use this command.")




#Join VC
@client.command()
async def join(ctx):
  vc = ctx.author.voice.channel
  if ctx.author.voice is None:
    return await ctx.send("Connect to a VC first")

  if ctx.author.voice is not None:
    await vc.connect()
    await ctx.send(f"Joined voice channel")

  else:
    await ctx.send("You are not in a voice cha")



#I need help on this one

#Leave VC
@client.command(aliases=["dc"])
async def disconnect(ctx):
  vc = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if vc.is_connected:
    await vc.disconnect()
    await ctx.send("Disconnected")

#try putting the vc connect above the if statement 

#can i change something if doesnt work ill reverse it

@client.command(aaliases=["bg"])
async def borgir(ctx):
  await ctx.send("https://tenor.com/view/borgir-abdu-rozik-burger-kid-gif-22116968")




 
   
           
       




#DO NOT DELETE THIS CODE DOWN HERE

#@client.command(pass_context = True)
#async def hello(ctx):
    #await ctx.send("Hi "+ctx.message.author.mention)

#DO NOT DELETE


#do not delete this code below

#ctx.message.author.mention (mentioning author)
#"+ f"{user.mention} " (mention the user that was mentioned)






#Do not touch ANY code below, it is mandatory to make the bot work.

client.run(os.getenv('Token'))


