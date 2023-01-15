import os
import requests
import discord

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_message(message):
  if message.author.bot:
    return
  else:
    headers = {
        'Authorization': 'Bearer ' + os.environ["notify_url"],
    }
    files = {
        'message': (None, "<" + message.author.name + ">" + message.content),
    }
    response = requests.post('https://notify-api.line.me/api/notify',
                             headers=headers,
                             files=files)


TOKEN = os.environ["discord_token"]

bot.run(TOKEN)
