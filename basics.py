import discord
import requests
from discord.types import embed

from embedsender import sendembed
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
faction = ""
maineffect = ""
echoeffect = ""
name = ""
m = ""
f = ""
w = ""
handcmc = ""
reservecmc = ""
imgurl = ""
def sendapirequest(crdname, rarity,colorbent):
    global faction
    global maineffect
    global echoeffect
    global name
    global m
    global f
    global w
    global handcmc
    global reservecmc
    global imgurl
    response = requests.get(
        "https://api.altered.gg/public/cards?rarity=" + str(rarity) + "&query=" + str(crdname) + "&locale=en")
    data = response.json()
    if colorbent:
        print("Card is colorbent")
        dcrdname = data["hydra:member"][1]["reference"]
        faction = (str(data["hydra:member"][1]["mainFaction"]["name"]))
        maineffect = (data["hydra:member"][1]["mainEffect"])
        echoeffect = (data["hydra:member"][1]["echoEffect"])
        name=(data["hydra:member"][1]["name"])
        m = (data["hydra:member"][1]["elements"]["MOUNTAIN_POWER"])
        f = (data["hydra:member"][1]["elements"]["FOREST_POWER"])
        w = (data["hydra:member"][1]["elements"]["OCEAN_POWER"])
        handcmc = (data["hydra:member"][1]["elements"]["MAIN_COST"])
        reservecmc = (data["hydra:member"][1]["elements"]["RECALL_COST"])
        imgurl = (data["hydra:member"][1]["assets"]["WEB"][0])
    else:
        print("Card is  not colorbent")
        dcrdname = data["hydra:member"][0]["reference"]
        faction = (data["hydra:member"][0]["mainFaction"]["name"])
        maineffect = (data["hydra:member"][0]["mainEffect"])
        echoeffect = (data["hydra:member"][0]["echoEffect"])
        name=(data["hydra:member"][0]["name"])
        m = (data["hydra:member"][0]["elements"]["MOUNTAIN_POWER"])
        f = (data["hydra:member"][0]["elements"]["FOREST_POWER"])
        w = (data["hydra:member"][0]["elements"]["OCEAN_POWER"])
        handcmc = (data["hydra:member"][0]["elements"]["MAIN_COST"])
        reservecmc = (data["hydra:member"][0]["elements"]["RECALL_COST"])
        imgurl = (data["hydra:member"][0]["assets"]["WEB"][0])
    return str(dcrdname)


client.event
async def on_ready(client):
    print('Logged in as')
    print(client.user.name)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '[' and ']' in str(message.content):
        print(message.content)
        if '{' and '}' in str(message.content):
            print("args detected")
            fbbr = '{'
            ebbr = '}'
            fbmsg= message.content
            bflist = fbmsg[fbmsg.find(fbbr) + len(fbbr):fbmsg.rfind(ebbr)]
            args=list(bflist)
            if 'R' in args or 'r' in args:
                rarity = 'rare'
                dontrun = False
                if 'B' in args or 'b' in args:
                    return
                else:
                    colorbent = False
                if 'C' in args or 'c' in args:
                    await message.channel.send("Please only enter one rarity, Thank you!")
                    print("More than one rarity detected canceling job")
                    dontrun = True
            if 'C' in args or 'c' in args:
                rarity = 'common'
                colorbent = False
                dontrun = False
                if 'B' in args or 'b' in args:
                    await message.channel.send("Please only enter one rarity, Thank you!")
                    print("More than one rarity detected canceling job")
                    dontrun = True
            if 'B' in args or 'b' in args:
                colorbent = True
                dontrun = False
                if 'R' in args or 'r' in args:
                    return
                else:
                    rarity = 'rare'
            fbr = '}'
            ebr = ']'
            msg = message.content
            crdname = msg[msg.find(fbr) + len(fbr):msg.rfind(ebr)]
            if dontrun == False:
                link = "https://www.altered.gg/en-us/cards/" + sendapirequest(crdname, rarity, colorbent)
                await message.channel.send(embed=sendembed(link,name,faction,maineffect,echoeffect,m,f,w,handcmc,reservecmc,imgurl))
        else:
            print("no args detected")
            fbr = '['
            ebr = ']'
            msg = message.content
            crdname=msg[msg.find(fbr)+len(fbr):msg.rfind(ebr)]
            rarity = "common"
            colorbent = False
            link = "https://www.altered.gg/en-us/cards/" + sendapirequest(crdname, rarity, colorbent)
            await message.channel.send(embed=sendembed(link, name, faction, maineffect, echoeffect, m, f, w, handcmc, reservecmc, imgurl))

client.run('DISCORDTOKENHERE')
#print(sendapirequest('anubis', 'rare')+'isthecard')
