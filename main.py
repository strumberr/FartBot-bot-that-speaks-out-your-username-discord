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

bot = commands.Bot(command_prefix = "")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.members = True

async def on_message(message):
    print(message.author.id)

@bot.command(name = "a")
async def join(ctx):
    channel = ctx.author.voice.channel
    author = ctx.message.author
    user_name = author.name
    await channel.connect()
    random_number = random.randint(0,700000000000000)
    random_number_to_string = str(random_number)
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    username_to_string = str(user_name)
    mytext = username_to_string + "breaking news"
    language = 'en'
    name_file_random = random_number
    myobj = gTTS(text=mytext, lang=language, slow=True)
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