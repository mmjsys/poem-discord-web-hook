import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
import json
global GANJOOR_RANDOM
global WEB_HOOK
GANJOOR_RANDOM = "https://api.ganjoor.net/api/ganjoor/poem/random"
WEB_HOOK       = " web hook "
def GET_POEM_FROM_GANJOOR():
    req = requests.get(GANJOOR_RANDOM)
    return req.json()
def GET_POEM_FROM_JSON(json):
    title = json["title"]
    poem =  json["plainText"]
    return {"title":title,"poem":poem}
def MASSAGE_CONTENT(title , poem):
    massage = f"""
{title}:
{poem}

"""
    return massage
def SEND_MASSAGE(massage):
    webhook = DiscordWebhook(url=WEB_HOOK)
    embed = DiscordEmbed(title='پند ', description=str(massage))
    webhook.add_embed(embed)
    response = webhook.execute()
    return requests
while True:
      json    = GET_POEM_FROM_GANJOOR()
      poem    = GET_POEM_FROM_JSON(json)
      massage = MASSAGE_CONTENT(poem["title"],poem["poem"])
      print(SEND_MASSAGE(massage))
      time.sleep(3600)





