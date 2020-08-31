import os
# importe la librairie os, qui permet d'utiliser certains fonctions déjà adaptées par les systèmes d'exploitation

import discord
# pouvoir utiliser l'API discord dans notre code

from dotenv import load_dotenv
# on va chercher dans la librairie dotenv
# un de ses composants "load_dotenv" qui permet de charger des variables d'env

load_dotenv()
# sert à lier le ficher .env au fichier bot
TOKEN = os.getenv('DISCORD_TOKEN')
# discord_token => variable, TOKEN => valeur de la variable
# générer un token pour permettre l'identification du bot

client = discord.Client()
# associer le bot à un client

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
