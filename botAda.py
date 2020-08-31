# importe la librairie os, qui permet d'utiliser certains fonctions déjà adaptées par les systèmes d'exploitation
import os

# pouvoir utiliser l'API discord dans notre code
import discord

# on va chercher dans la librairie dotenv
# un de ses composants "load_dotenv" qui permet de charger des variables d'env
from dotenv import load_dotenv

# sert à lier le ficher .env au fichier bot
load_dotenv()

# discord_token => variable, TOKEN => valeur de la variable
# générer un token pour permettre l'identification du bot
TOKEN = os.getenv('DISCORD_TOKEN')

# associer le bot à un client
client = discord.Client()

# décorateur qui attend le paramettre de connection
@client.event
# function qui dit au décorateur de se connecter au serveur Discord
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
