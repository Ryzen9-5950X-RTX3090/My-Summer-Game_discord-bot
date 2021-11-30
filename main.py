import discord
import os
import requests
import json
import random
from replit import db


client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "pissed", "scared", "terrified", "overwhelmed", "stressed", "depressing", "horrible", "awful", "not good", "bad", "ugh", "outraged", "raged", "ticked", "not great"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are doing great!",
  "You are a great person/bot!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.key():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db ["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user} on Discord.'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('hru'):
    await message.channel.send('I am doing great, you?')

  if message.content.startswith('great'):
    await message.channel.send('That is great to hear!')

  if message.content.startswith('terrible'):
    await message.channel.send('What a shame!')

  if message.content.startswith('sup'):
    await message.channel.send('sup weirdo')

  if message.content.startswith('weirdest'):
    await message.channel.send('no u')

  if message.content.startswith('ur mom'):
    await message.channel.send('no urs')

  if message.content.startswith('bye'):
    await message.channel.send('Bye weirdo!')

  if message.content.startswith('gn'):
    await message.channel.send('gn weirdo!')

  if message.content.startswith('ttyl'):
    await message.channel.send('Ok see ya then')

  if message.content.startswith('!release-date'):
    await message.channel.send('Hello! The planned release date for My Summer Game is for Q4 of 2022!')

  if message.content.startswith('!ro.build.info'):
    await message.channel.send('Closed beta 0.4.4, built on December 1, 2021, released on December 1, 2021.')

  if message.content.startswith('!download'):
    await message.channel.send('https://github.com/Ryzen9-5950X-RTX3090/My-Summer-Game_Unity-project/releases')

  if message.content.startswith('!unity-info'):
    await message.channel.send('Unity 2D personal, version 2021.2.4f1')

  if message.content.startswith('!source-code'):
    await message.channel.send('https://github.com/Ryzen9-5950X-RTX3090/My-Summer-Game_Unity-project/')

  if message.content.startswith('!art-designers'):
    await message.channel.send('@Wolvenare#7669, @Ryzen9-5950X, 64GB RAM, RTX 3090#0001, @Nova Supreme#8855, and @becca#1828.')
    
  if message.content.startswith('spam'):
    await message.channel.send('https://giphy.com/gifs/spam-Hae1NrAQWyKA')

  if message.content.startswith('!inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  options = starter_encouragements
  if "encouragements" in db.keys():
    options = options + db["encouragements"]
  
  if message.content.startswith('!bot-info'):
    quote = get_quote()
    await message.channel.send('version 1.0, last updated on: November 30, 2021.')

  if any(word in message.content for word in sad_words):
    await message.channel.send(random.choice(options))

  if message.content.startswith("$new"):
    encouraging_message = message.content.split("$new ",1)[1]
    update encouragements(encouraging_message)
    await message.channel.send("The new encouraging message has been added to the database.")

  if message.content.startswith("$del"):
   encouragements = [] 
   if "encouragements" in db.keys():
     index = int(message.content.split("$del", 1)[1])
     delete_encouragement(index)
     encouragements = db["encouragements"]
    await message.channel.send(encouragements)

client.run(os.environ['DiscordBot_token'])