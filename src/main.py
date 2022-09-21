from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 483204256397262858  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(com):
    await com.send(com.author)
    
@bot.command()
async def d6(com):
    await com.send(random.randrange(1,6))

@bot.event
async def on_message(com):
    if "Salut tout le monde" in com.content:
        await com.channel.send("Salut tout seul " + str(com.author.mention))
    await bot.process_commands(com)
    
@bot.command()
async def ban(com, member : discord.Member, reason=None):
    if reason == None:
        await com.send(f"Oh oh {com.author.mention} don't provide a reason!")
    else:
        message = f"You have been banned from {com.guild.name} for {reason}"
        await member.send(message)
        await member.ban(reason=reason)
        
        
token = "MTAyMjE5MzI1ODM5MjIwNzQ2MA.GhECsQ.d6Mg0kmSUtj1nFWxn6TvOkHk8r-OldobKRcTuU"
bot.run(token)  # Starts the bot