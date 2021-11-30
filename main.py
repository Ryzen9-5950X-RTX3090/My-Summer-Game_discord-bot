import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user} on Discord.'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('Hello!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hru'):
    await message.channel.send('I am doing great, you?')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('great'):
    await message.channel.send('That is great to hear!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('terrible'):
    await message.channel.send('What a shame!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('sup'):
    await message.channel.send('sup weirdo')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('weirdest'):
    await message.channel.send('no u')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('ur mom'):
    await message.channel.send('no urs')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('bye'):
    await message.channel.send('Bye weirdo!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('gn'):
    await message.channel.send('gn weirdo!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('ttyl'):
    await message.channel.send('Ok see ya then')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!release-date'):
    await message.channel.send('Hello! The planned release date for My Summer Game is for Q4 of 2022!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!ro.build.info'):
    await message.channel.send('Closed beta 0.4.4, built on December 1, 2021, released on December 1, 2021.')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!download'):
    await message.channel.send('https://github.com/Ryzen9-5950X-RTX3090/My-Summer-Game_Unity-project/releases')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!unity-info'):
    await message.channel.send('Unity 2D personal, version 2021.2.4f1')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!source-code'):
    await message.channel.send('https://github.com/Ryzen9-5950X-RTX3090/My-Summer-Game_Unity-project/')

client.run(os.environ['DiscordBot_token'])