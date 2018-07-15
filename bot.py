import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import collections
import pandas as pd

demons = {}
url = 'https://raw.githubusercontent.com/grimgal/einherjar-bot/master/dDemons.csv'
c = pd.read_csv(url)
count = 0
Demon = collections.namedtuple('Demon','name race grade rarity phys fire ice elec force light dark hp str mag vit agi luk s1 s2 s3 ca cr cy cp ct gr gy gp gt')
while count < 172:
    demon = Demon(name=c['Name'][count], race=c['Race'][count], grade=str(int(c['Grade'][count])), rarity='☆' * int(c['Rarity'][count]),
    phys=str(c['Phys'][count]), fire=str(c['Fire'][count]), ice=str(c['Ice'][count]),
    elec=str(c['Elec'][count]), force=str(c['Force'][count]), light=str(c['Light'][count]), dark=str(c['Dark'][count]),
    hp=c['6★ HP'][count], str=c['6★ Strength'][count], mag=c['6★ Magic'][count], vit=c['6★ Vitality'][count], agi=c['6★ Agility'][count], luk=c['6★ Luck'][count],
    s1=c['Skill 1'][count],s2=c['Skill 2'][count],s3=c['Skill 3'][count],
    ca=c['Clear Archetype'][count],cr=c['Red Archetype'][count],cy=c['Yellow Archetype'][count],cp=c['Purple Archetype'][count],ct=c['Teal Archetype'][count],
    gr=c['Red Gacha'][count],gy=c['Yellow Gacha'][count],gp=c['Purple Gacha'][count],gt=c['Teal Gacha'][count])

    demonText = "```md\n#" + demon.name + "\nRace: " + demon.race + " | Grade: " + demon.grade + " | Rarity: " + demon.rarity
    demonText = demonText + "\n\n#6☆ Max Level Stats\nHP - " + demon.hp + " | Strength - " + demon.str + " | Magic - " + demon.mag + " | Vitality - " + demon.vit
    demonText = demonText + " | Agility - " + demon.agi + " | Luck - " + demon.luk
    demonText = demonText + "\n\n#Elemental Resistances\nPhysical: " + demon.phys + " | Fire: " + demon.fire + " | Ice: " + demon.ice
    demonText = demonText + " | Electricity: " + demon.elec + " | Force: " + demon.force + " | Light: " + demon.light + " | Dark: " + demon.dark
    demonText = demonText + "\n\n#Innate Skills:\n" + demon.s1.replace('|',' | ') + "\n" + demon.s2.replace('|',' | ') + "\n" + demon.s3.replace('|',' | ')
    demonText = demonText + "\n\n#Archetype Skills:\n" + demon.ca.replace('|',' | ') + "\n" + demon.cr.replace('|',' | ') + "\n" + demon.cy.replace('|',' | ') + "\n" + demon.cp.replace('|',' | ') + "\n" + demon.ct.replace('|',' | ')
    demonText = demonText + "\n\n#Gacha Skills:\n" + demon.gr.replace('|',' | ') + "\n" + demon.gy.replace('|',' | ') + "\n" + demon.gp.replace('|',' | ') + "\n" + demon.gt.replace('|',' | ')
    demons[demon.name.lower().replace("'",'')] = demonText + "```"

    count += 1

skills = {}
url = 'https://raw.githubusercontent.com/grimgal/einherjar-bot/master/dSkills.csv'
c = pd.read_csv(url,encoding='utf-8')
count = 0
Skill = collections.namedtuple('Skill','name jp mp description owner learn')
while count < 338:
    skill = Skill(name=c['Name'][count],jp=c['JP Name'][count],mp=str(c['Cost'][count]),description=str(c['Description'][count]),owner=str(c['Learned By'][count]),learn=str(c['Transferable From'][count]))
    skills[skill.name.lower().replace("'",'')] = "```md\n#" + skill.name + " | " + skill.jp + " | " + skill.mp + " | " + skill.description + "\nDemons with skill: " + skill.owner + "\nDemons to transfer skill from: " + skill.learn + "```"
    count += 1

Client = discord.Client()
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def demon(name : str):
    name = name.lower().replace("'",'')
    try:
        selectedDemon = demons[name]
    except Exception:
        await bot.say("This demon doesn't exist in my database. If the demon name has a space in it, make sure to enclose it in quotes.")
        return
    await bot.say(selectedDemon)

@bot.command()
async def skill(name : str):
    name = name.lower().replace("'",'')
    try:
        selectedSkill = skills[name]
    except Exception:
        await bot.say("This skill doesn't exist in my database. If the skill name has a space in it, make sure to enclose it in quotes.")
        return
    await bot.say(selectedSkill)

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
