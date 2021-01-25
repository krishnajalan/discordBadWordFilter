import requests
import json
import os
from dotenv import load_dotenv
import discord

############################ Environment Variable ########################

load_dotenv()
rapidApiToken = os.getenv("rapidApiToken")
dicordToken = os.getenv("Token")


################################ word filter ##############################
def allowStatements(string):
    try:
        string = "%20".join(string)
        url = "https://neutrinoapi-bad-word-filter.p.rapidapi.com/bad-word-filter"
        payload = f"censor-character=*&content={string}"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-key': f"{rapidApiToken}",
            'x-rapidapi-host': "neutrinoapi-bad-word-filter.p.rapidapi.com"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        data = response.json()
        return data['bad-words-total']==0
    except:
        print()
        print(data)
        print()
        return True
###########################################################################



############################## Discord Client #############################
client = discord.Client()


@client.event
async def on_ready():
    print("f{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    print(message)
    check = allowStatements(message.content.split())
    if (check!=None):
        if not check:
            await message.delete()
            await message.channel.send(f"{message.author.mention} Warning bad words used!!")


client.run(dicordToken)
############################################################################
