import discord
from discord.ext import commands
from discord.utils import get
from config import *
client = commands.Bot(command_prefix=CMD_PREFIX, description=DESCRIPTION)


## INDICATOR + STATUS
@client.event
async def on_ready():
    print("beatBot! up to bop")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("the cutest girl in hell by Colliding With Mars"), afk=False)
    


## TEST: !ping <string>
@client.command(name='ping',help=': Pings bot') # You make make the command respond to other commands too
async def ping(ctx, a_variable): # A variable is a parameter you use in the command
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms. Your input was {a_variable}")


## CLEAR: !clear <number+1> or !c <number+1>
@client.command(aliases = ['c'],name='clear', help=': Clear messages')
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=2): #2
    await ctx.channel.purge(limit = amount)


# ABRUPT END PROGRAM
@client.command(aliases=['a2'])
async def A2(message):
    await message.channel.send(f"{message.author.mention}\nIf you need any info on music theory, you know where to find me!")





## MENU K
@client.command(aliases=['k1'])
async def K1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        MENU\n\
Select another option!\n\n\
        H1. What is Music Theory?\n\
        H2. What does Music Theory consist of?\n\
        H3. Why do we learn Music Theory?\n\
        L3. Conclusion\n\
        A2. End")





### INTRO: !start
## QUESTION A
@client.command(name='start', help=': Bot introduces itself')
async def start(ctx):
    await ctx.send(f"Hi, {ctx.author.mention}. I'm beatBot! I'm assuming you are intrigued by the most wonderful, global language that\
        is music? (Enter a letter and its number)\n\n\
            A1. Yes, I'm curious :D\n\
            A2. End")





## QUESTION B (user chose A1)
@client.command(aliases=['a1'])
async def A1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
Awesome!\n\
Let's begin. You may type 'B1' to continue into the introduction, or select any other options below.\n\n\
            B1. What is Music Theory?\n\
            B2. What does Music Theory consist of?\n\
            B3. Why do we learn Music Theory?\n\
            A2. End")












########################################### vv STORYLINE vv ##########################################################################################

## QUESTION C (user chose b1)
@client.command(aliases=['b1','B2','b2','B3','b3'])
async def B1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
Before we begin, quick intro; music theory is a tool that allows us to learn more about the language of music and to create music ourselves. It also helps us to break down the different parts that make up a tune, so we can better understand why it sounds amazing to our ears.\n\n\
            C1. Phone: 'RING RING! RING RING!'\n\
            A2. End")





## QUESTION D (user chose C1)
@client.command(aliases=['c1'])
async def C1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
Wait- Your phone is ringing. Pick up the call?\n\n\
        D1. Yes\n\
        D2. No\n\
        A2. End")





## QUESTION E (user chose d1)
@client.command(aliases=['d1'])
async def D1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"You accept the call. An unfamiliar voice can be heard from the other end.\n\
???: Hello, {message.author.mention}. I don't have much time before the line cuts. This is urgent.\n\n\
        E1. 'Who are you, and how do you know my name?!'\n\
        E2. 'I'm listening'\n\
        A2. End")

## user chooses d2
@client.command(aliases=['d2'])
async def D2(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
The phone remains ringing. Come on, you have to pick it up! Your nyan cat ringtone is killing my eardrums, and I don't even have ears.\n\n\
        D1. You give in and pick up the call\n\
        A2. End")





## QUESTION F (user chose e1)
@client.command(aliases=['e1'])
async def E1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
???: That's not important. I am contacting you via space control- at least what's left of it. I need you to compose some sort of song to drive them away. They seem to hate that.\n\n\
        F1. 'Who's them? I need answers'\n\
        F2. 'No problem, I'll help you out'\n\
        A2. End")

## user chose e2
@client.command(aliases=['e2'])
async def E2(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
???: I am contacting you via space control- at least what's left of it. I need you to compose some sort of song to drive them away. They seem to hate that for some unknown reason.\n\n\
        F1. 'Who's them? I need answers.'\n\
        F2. 'No problem, I'll help you out.'\n\
        A2. End")





## QUESTION G (user chose f1)
@client.command(aliases=['f1'])
async def F1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
???: You're really chatty, aren't you? Listen, this spacecraft is no record studio. We need you to do this for us, whoever you are.\n\
        F2. 'Alright fine. Consider it done.'\n\
        A2. End")



## QUESTION H (user chose f2)
@client.command(aliases=['f2'])
async def F2(message):
    if message.author == client.user:
        return
    await message.channel.send(f"???: Thank y-\n\
Strange, a convenient line cut-off. Welp anyways, looks like you're given an important task, {message.author.mention}. Let's get right to it! Choose an option to begin studying what you need to know, so we can save this mysterious caller.\n\n\
        H1. What is Music Theory?\n\
        H2. What does Music Theory consist of?\n\
        H3. Why do we learn Music Theory?\n\
        A2. End")

########################################### ^^ STORY ^^ ##########################################################################################




















########################################### vv WHAT IS MT? vv ##########################################################################################

## QUESTION I
@client.command(aliases=['h1'])
async def H1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHAT IS MUSIC THEORY?\n\
Music theory is a practice musicians use to understand and communicate the language of music. An example would be if you wanted to understand Michael who speaks a foreign language. Tell me, what tool do use to decipher what Michael is trying to say?\n\n\
        I1. Notebook and pen (for him to write on)\n\
        I2. Your mom (because)\n\
        I3. Google Translate\n\
        K1. MENU\n\
        A2. End")



## QUESTION I1
@client.command(aliases=['i1'])
async def I1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"\t\tWHAT IS MUSIC THEORY?\n\
That would work only if Michael can converse a bit of English as well. Having him write French words on paper wouldn't help at all! Rack that noggin of yours, {message.author.mention}\n\n\
        I1. Notebook and pen (for him to write on)\n\
        I2. Your mom (because)\n\
        I3. Google Translate\n\
        K1. MENU\n\
        A2. End")



## QUESTION I2
@client.command(aliases=['i2'])
async def I2(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHAT IS MUSIC THEORY?\n\
If my mom possessed an enormous database of all the languages in the world, this answer would be correct. Unfortunately, she is no Artificially Intelligent work of art like me. #respectstomomtho. Try again!\n\n\
        I1. Notebook and pen (for him to write on)\n\
        I2. Your mom (because)\n\
        I3. Google Translate\n\
        K1. MENU\n\
        A2. End")



## QUESTION I3
@client.command(aliases=['i3'])
async def I3(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHAT IS MUSIC THEORY?\n\
That's right! In order to understand what our buddy Michael is saying, we can use the power of Google Translate to translate from French to English. In a musical context, Music Theory acts as Google Translate, while Michael acts as a piece of music we are trying to understand. Music Theory also helps to break down the different components of a tune so it can be easily analysed.\n\n\
        K1. MENU\n\
        A2. End")


########################################### ^^ WHAT IS MT? ^^ ##########################################################################################




















########################################### vv CONSIST IN MT? vv ##########################################################################################

## QUESTION J
@client.command(aliases=['h2'])
async def H2(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHAT DOES MUSIC THEORY CONSIST OF?\n\
Music is made up of 3 basic, yet important ingredients; harmony, melody and rhythm. Select which ingredient you would like to learn more about.\n\n\
        J1. Harmony\n\
        J2. Melody\n\
        J3. Rhythm\n\
        A2. End")



## QUESTION I (harmony)
@client.command(aliases=['j1'])
async def JI1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHAT DOES MUSIC THEORY CONSIST OF?\n\
Harmony is when multiple notes or voices play simultaneously to produce a new sound. The combined sounds in harmonies complement one another and sound pleasing. Relate this to letters that make up a word. Try forming a word out of this anogram of letters: R, P, E, A\n\n\
        - Enter '!<word>'\n\
        A2. End")



@client.command(aliases=['rape'])
async def RAPE(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
dang. are you good..? please try again.")

@client.command(aliases=['pear','reap','REAP'])
async def PEAR(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHAT DOES MUSIC THEORY CONSIST OF?\n\
Nice! Using these individual letters, you formed a totally new thing which is the word {message}! This is similar to notes creating a harmony, hence forming a totally new sound.\n\
Additionally, combining vocals also creates harmony, like the combined voices of a choir. The multiple voices that make up a choir blend to make a harmonious sound.\n\n\
        K1. MENU\n\
        H2. Back\n\
        A2. End")



## QUESTION I (melody)
@client.command(aliases=['j2'])
async def J2(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHAT DOES MUSIC THEORY CONSIST OF?\n\
Melody is a group of notes arranged into a musical phrase. A song’s melody is often the most memorable and recognizable part. Pitch and rhythm plays a part together in making a beautiful melody.\n\
Think of the most memorable company melodies off the top of your head. My favourite is the McDonalds' jingle. Bada bap bap baa!\n\n\
        K1. MENU\n\
        H2. Back\n\
        A2. End")



## QUESTION I (rhythm)
@client.command(aliases=['j3'])
async def J3(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHAT DOES MUSIC THEORY CONSIST OF?\n\
Rhythm has more than one meaning:\n\
Firstly, it can mean a movement of notes and rests (silences) in time that sound in intervals.\n\
Secondly, rhythm describes a pattern of strong and weak notes that repeat throughout a song. These patterns can be created with drums, percussion, instruments, and vocals!\n\n\
        K1. MENU\n\
        H2. Back\n\
        A2. End")

########################################### vv CONSIST IN MT? vv ##########################################################################################




















########################################### vv BENEFITS OF MT? vv ##########################################################################################

## QUESTION L
@client.command(aliases=['h3'])
async def H3(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHY DO WE LEARN MUSIC THEORY?\n\
Stating the obvious, knowing how music works will make the music production process easier and help you become an effective music producer.\n\
There wayy more benefits to learning Music Theory. Would you like to know them?\n\n\
        L1. Yes!\n\
        L2. I'll pass\n\
        A2. End")



## L1
@client.command(aliases=['l1'])
async def L1(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHY DO WE LEARN MUSIC THEORY?\n\
Alright, ready?? *inhale\n\
• Help you achieve expression and evoke emotion\n\
• Improve your critical listening skills\n\
• Speed up your workflow\n\
• Make it easy to communicate with other musicians\n\
• Deepen your appreciation for music\n\
• Help you discover new creative possibilities\n\n\
        K1. MENU\n\
        A2. End")



## L2
@client.command(aliases=['l2'])
async def L2(message):
    if message.author == client.user:
        return
    await message.channel.send(f"{message.author.mention}\n\
        WHY DO WE LEARN MUSIC THEORY?\n\
Suit yourself!\n\n\
        K1. MENU\n\
        A2. End")

########################################### ^^ BENEFITS OF MT? ^^ ##########################################################################################




















########################################### ^^ CONCLUSION ^^ ##########################################################################################

@client.command(aliases=['l3'])
async def L3(message):
    if message.author == client.user:
        return
    await message.channel.send(f"Alright, you now have the basic knowledge on the creation of music. Try out some sofwares and programs to create a tune, so you can help Mystery Caller from whatever disaster they got themselves into. You got this, {message.author.mention}!\n\
These are the basics of Music Theory that can help you kickstart the rest of your musical journey. beatBot hopes that you have learnt plenty from my sharings today. If you listen hard enough, you will realise that music is all around us! In parks, shopping malls, and in your own schools! (the ding dong of your school bells for example). Don't stop exploring, and save more people like Mystery Caller by introducing them to the wonders of Music Theory!")






client.run(TOKEN)