import discord
def sendembed(link,name,faction,maineffect,echoeffect,m,f,w,handcmc,reservecmc,imgurl):
    maineffect = maineffect.replace("{J}", "On Enter: ")
    if faction == 'Lyra':
        r = 238
        g = 123
        b = 165
    if faction == 'Axiom':
        r = 112
        g = 67
        b = 51
    if faction == 'Bravos':
        r = 117
        g = 56
        b = 49
    if faction == 'Muna':
        r = 97
        g = 150
        b = 89
    if faction == 'Ordis':
        r = 7
        g = 120
        b = 160
    if faction == 'Yzmir':
        r = 175
        g = 92
        b = 198
    embed = discord.Embed(url=link,title=name)
    embed.set_author(name="AlteredBot")
    embed.add_field(name="Faction:",value=faction)
    if len(maineffect)>0:
        embed.add_field(name="Main Effect:",value=maineffect)
    if len(echoeffect)>0:
        embed.add_field(name="Echo Effect:",value=echoeffect)
    if len(m)>0 or len(f)>0 or len(w)>0:
        embed.add_field(name="Statistics F/M/O:",value=f+"/"+m+"/"+w)
    if len(handcmc)>0 or len(reservecmc)>0:
        embed.add_field(name="Mana Cost H/R:",value=handcmc+"/"+reservecmc)
    embed.set_thumbnail(url=str(imgurl))
    embed.color = discord.Color.from_rgb(r,g,b)
    return embed
