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

  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!release-date'):
    await message.channel.send('Hello! The planned release date for My Summer Game is for Q4 of 2022!')

client.run(os.environ['DiscordBot_token'])