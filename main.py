import os
import discord
import random
from discord.ext import commands
import time
import secrets
import keep_alive
from discord.ext import commands
# Import the required module for text 
# to speech conversion
from gtts import gTTS
token = os.getenv('token')
import urllib.parse
import requests






bot = commands.Bot(command_prefix="")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.members = True


@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="!help"))







@bot.command(name = "!conversation")
async def conversation(ctx): 
  await ctx.send("say hello!")

  def check(m):
        return m.content == "hello" and m.channel == ctx.channel
  
  msg = await bot.wait_for("message", check=check)
  author_to_string = str(msg.author)
  author = author_to_string[:-5]
  await ctx.send(f"stfu {author}. Go talk to a real person")




@bot.command(name = "!speak")
async def speak(ctx):
    channel = ctx.author.voice.channel
    author = ctx.message.author
    user_name = author.name
    await channel.connect()
    random_number = random.randint(0,700000000000000)
    random_number_to_string = str(random_number)
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    username_to_string = str(user_name)
    message_content = ctx.message.content[6:50]
    mytext = username_to_string + "says, " + message_content
    language = 'en'
    name_file_random = random_number
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("mp3_files/%s.mp3" % name_file_random)
    audio_source = discord.FFmpegPCMAudio('fart1.mp3')
    audio_source2 = discord.FFmpegPCMAudio('fart2.mp3')
    audio_source3 = discord.FFmpegPCMAudio('fart3.mp3')
    audio_voice = discord.FFmpegPCMAudio("mp3_files/" + random_number_to_string + ".mp3")
    random_audio = [audio_source, audio_source2, audio_source3]
    choose_random_audio = secrets.choice(random_audio)
    if not voice_client.is_playing():
        voice_client.play(audio_voice, after=None)
        time.sleep(2)
        os.remove("mp3_files/" + random_number_to_string + ".mp3")
        time.sleep(4)
        await ctx.voice_client.disconnect()





@bot.command(name = "!fart")
async def fart(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('fart1.mp3')
    audio_source2 = discord.FFmpegPCMAudio('fart2.mp3')
    audio_source3 = discord.FFmpegPCMAudio('fart3.mp3')
    random_audio = [audio_source, audio_source2, audio_source3]
    choose_random_audio = secrets.choice(random_audio)
    if not voice_client.is_playing():
        voice_client.play(choose_random_audio, after=None)
        time.sleep(6)
        await ctx.voice_client.disconnect()



@bot.command(name = "!help")
async def help(ctx):
  embedVar = discord.Embed(title="FartBot", description="This is a bot that does various stupid things like:", color=0x00ff00)
  embedVar.add_field(name="!speak", value="'Ex: !speak hello' will join your voice channel and speak out what you said, in this case 'hello'", inline=False)
  embedVar.add_field(name="!fart", value="The bot will join your voice channel and play random fart sounds", inline=False)
  embedVar.add_field(name="**Add your own fart**", value="If you want to add your own fart, open this link and send the name of the youtube video (NOT LINK) '(WORK IN PROGRESS)''", inline=False)
  await ctx.send(embed=embedVar)
  






#@bot.command(name = "!conversation.fartbot")
#async def greet(ctx):
#    msg = "{0.author.mention}"
#    await ctx.send(f"Hello {msg.author}!")
#
#    def check(m):
#        return m.content == "hello"
#
#    msg2 = await bot.wait_for("message", check=check)
#    await ctx.send(f"Hello {msg2.author}!")




print("running...")

keep_alive.keep_alive()
bot.run(token)