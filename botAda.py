# importe la librairie os, qui permet d'utiliser certains fonctions déjà adaptées par les systèmes d'exploitation
import os

# pouvoir utiliser l'API discord dans notre code
import discord

# on va chercher dans la librairie dotenv
# un de ses composants "load_dotenv" qui permet de charger des variables d'env
from dotenv import load_dotenv

# sert à lier le ficher .env au fichier bot
load_dotenv()

"""discord_token => variable, TOKEN => valeur de la variable
récupération du token et du nom du serveur dans les variables d'environnement pour permettre l'identification du bot"""
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# associer le bot à un client
client = discord.Client()

# décorateur qui attend le paramettre de connection
@client.event
 
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break 
    
    print(
        f'{client.user} is connected to the following guild: \n' 
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    
# Connexion au serveur Discord grâce au token d'authentification du bot
client.run(TOKEN)
