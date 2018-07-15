import discord
from discord.ext.commands import Bot
from discord.ext import commands

import asyncio
import os
import csv
import collections

demons = {}
skills = {}
with open('dDemons.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    l = list(reader)
    l.pop(0)
    Demon = collections.namedtuple('Demon','name race grade rarity phys fire ice elec force light dark hp str mag vit agi luk s1 s2 s3 ca cr cy cp ct gr gy gp gt')
    for item in l:
        if len(item[0]) < 50:
            for i, entry in enumerate(item):
                item[i] = entry.replace('|',' | ')

            demon = Demon(name=item[0], race=item[1], grade=item[2], rarity='☆' * int(item[3]),
            phys=item[10],fire=item[11],ice=item[12],elec=item[13],force=item[14],light=item[15],dark=item[16],
            hp=item[4],str=item[5],mag=item[6],vit=item[7],agi=item[8],luk=item[9],
            s1=item[17],s2=item[18],s3=item[19],
            ca=item[20],cr=item[21],cy=item[22],cp=item[23],ct=item[24],
            gr=item[25],gy=item[26],gp=item[27],gt=item[28])

            demonText = "```md\n#" + demon.name + "\nRace: " + demon.race + " | Grade: " + demon.grade + " | Rarity: " + demon.rarity
            demonText = demonText + "\n\n#6☆ Max Level Stats\nHP - " + demon.hp + " | Strength - " + demon.str + " | Magic - " + demon.mag + " | Vitality - " + demon.vit
            demonText = demonText + " | Agility - " + demon.agi + " | Luck - " + demon.luk
            demonText = demonText + "\n\n#Elemental Resistances\nPhysical: " + demon.phys + " | Fire: " + demon.fire + " | Ice: " + demon.ice
            demonText = demonText + " | Electricity: " + demon.elec + " | Force: " + demon.force + " | Light: " + demon.light + " | Dark: " + demon.dark
            demonText = demonText + "\n\n#Innate Skills:\n" + demon.s1 + "\n" + demon.s2 + "\n" + demon.s3
            demonText = demonText + "\n\n#Archetype Skills:\n" + demon.ca + "\n" + demon.cr + "\n" + demon.cy + "\n" + demon.cp + "\n" + demon.ct
            demonText = demonText + "\n\n#Gacha Skills:\n" + demon.gr + "\n" + demon.gy + "\n" + demon.gp + "\n" + demon.gt

            demons[demon.name.lower()] = demonText + "```"

print('Finished reading demons.')

with open('dSkills.csv') as csvfile:
    reader = csv.reader(csvfile)
    l = list(reader)
    l.pop(0)
    Skill = collections.namedtuple('Skill','name jp mp description owner learn')
    for item in l:
        for i, entry in enumerate(item):
            item[i] = entry.replace('|',' | ')

        skill = Skill(name=item[1],jp=item[2],mp=item[3],description=item[4],owner=item[6],learn=item[7])
        skills[skill.name.lower()] = "```md\n#" + skill.name + " | " + skill.jp + " | " + skill.mp + " | " + skill.description + "\nDemons with skill: " + skill.owner + "\nDemons to transfer skill from: " + skill.learn + "```"

print('Finished reading skills.')

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
    name = name.lower()
    try:
        selectedDemon = demons[name]
    except Exception:
        await bot.say("This demon doesn't exist in my database. If the demon name has a space in it, make sure to enclose it in quotes.")
        return
    await bot.say(selectedDemon)

@bot.command()
async def skill(name : str):
    name = name.lower()
    try:
        selectedSkill = skills[name]
    except Exception:
        await bot.say("This skill doesn't exist in my database. If the skill name has a space in it, make sure to enclose it in quotes.")
        return
    await bot.say(selectedSkill)

bot.run(os.environ['TOKEN'])
