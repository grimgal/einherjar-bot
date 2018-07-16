import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import collections
import difflib
import math
import pandas as pd
from texttable import Texttable

# Returns list used for skill tables
def get_skill_list(skill, arch = ''):
    skills = skill.split('|')
    count = 0
    for item in skills:
        skills[count] = item.strip()
        count += 1

    if len(skills) < 4:
        if len(arch) > 3:
            return [skills[0],'','','']
        return [skills[0],'','']
    if len(arch) > 3:
        return [arch, skills[0], skills[2], skills[3]]
    return [skills[0],skills[2],skills[3]]

# Read and store raw demon data from csv
demons = {}
demon_names = []
url = 'https://raw.githubusercontent.com/grimgal/einherjar-bot/master/dDemons.csv'
c = pd.read_csv(url)
count = 0
Demon = collections.namedtuple('Demon','name race grade rarity phys fire ice elec force light dark hp str mag vit agi luk s1 s2 s3 ca cr cy cp ct gr gy gp gt')
while count < 172:
    demon = Demon(name=c['Name'][count], race=c['Race'][count], grade=str(int(c['Grade'][count])), rarity='☆' * int(c['Rarity'][count]),
    phys=str(c['Phys'][count]), fire=str(c['Fire'][count]), ice=str(c['Ice'][count]),
    elec=str(c['Elec'][count]), force=str(c['Force'][count]), light=str(c['Light'][count]), dark=str(c['Dark'][count]),
    hp=c['6★ HP'][count].strip(), str=c['6★ Strength'][count].strip(), mag=c['6★ Magic'][count].strip(),
    vit=c['6★ Vitality'][count].strip(), agi=c['6★ Agility'][count].strip(), luk=c['6★ Luck'][count].strip(),
    s1=c['Skill 1'][count],s2=c['Skill 2'][count],s3=c['Skill 3'][count],
    ca=c['Clear Archetype'][count],cr=c['Red Archetype'][count],cy=c['Yellow Archetype'][count],cp=c['Purple Archetype'][count],ct=c['Teal Archetype'][count],
    gr=c['Red Gacha'][count],gy=c['Yellow Gacha'][count],gp=c['Purple Gacha'][count],gt=c['Teal Gacha'][count])

    infoTable = Texttable()
    infoTable.set_cols_align(["c","c","c"])
    infoTable.add_rows([["Race","Grade","Rarity"],
                        [demon.race,demon.grade,demon.rarity]])

    statsTable = Texttable()
    statsTable.set_cols_align(["c", "c", "c", "c", "c", "c"])
    statsTable.add_rows([["HP","Strength","Magic","Vitality","Agility","Luck"],
    [demon.hp,demon.str,demon.mag,demon.vit,demon.agi,demon.luk]])

    resistsTable = Texttable()
    resistsTable.set_cols_align(["c", "c", "c", "c", "c", "c", "c"])
    resistsTable.add_rows([["Physical","Fire","Ice","Electricity","Force","Light","Dark"],
    [demon.phys,demon.fire,demon.ice,demon.elec,demon.force,demon.light,demon.dark]])

    #skillsTable = Texttable()
    #skillsTable.set_cols_align(["c", "c", "c"])
    #skillsTable.add_rows([["Skill Name","MP Cost","Description"],get_skill_list(demon.s2),get_skill_list(demon.s1),get_skill_list(demon.s3)])
    #archtypeTable = Texttable()
    #archtypeTable.set_cols_align(["c", "c", "c", "c"])
    #archtypeTable.add_rows([["Archetype","Skill Name","MP Cost","Description"],get_skill_list(demon.ca,"Common"),get_skill_list(demon.cr,"Aragami"),get_skill_list(demon.cy,"Protector"),get_skill_list(demon.cp,"Psychic"),get_skill_list(demon.ct,"Elementalist")])
    #gachaTable = Texttable()
    #gachaTable.set_cols_align(["c", "c", "c", "c"])
    #gachaTable.add_rows([["Archetype","Skill Name","MP Cost","Description"],get_skill_list(demon.gr,"Aragami"),get_skill_list(demon.gy,"Protector"),get_skill_list(demon.gp,"Psychic"),get_skill_list(demon.gt,"Elementalist")])

    #demonText = "```md\n#" + demon.name + "\n" + infoTable.draw()
    #demonText = demonText + "\n\n#6☆ Max Level Stats\n" + statsTable.draw()
    demonText = "```md\n#" + demon.name + "\nRace: " + demon.race + " | Grade: " + demon.grade + " | Rarity: " + demon.rarity
    demonText = demonText + "\n\n#6☆ Max Level Stats\nHP - " + demon.hp + " | Strength - " + demon.str + " | Magic - " + demon.mag + " | Vitality - " + demon.vit + " | Agility - " + demon.agi + " | Luck - " + demon.luk
    demonText = demonText + "\n\n#Elemental Resistances\n" + resistsTable.draw()
    demonText = demonText + "\n\n#Innate Skills:"\
    + "\nSkill 1 | " + demon.s1.replace('|',' | ') + "\nSkill 2 | " + demon.s2.replace('|',' | ') + "\nSkill 3 | " + demon.s3.replace('|',' | ')
    demonText = demonText + "\n\n#Archetype Skills:\nCommon (Clear)      | " + demon.ca.replace('|',' | ')\
    + "\nAragami (Red)       | " + demon.cr.replace('|',' | ') + "\nProtector (Yellow)  | " + demon.cy.replace('|',' | ')\
    + "\nPsychic (Purple)    | " + demon.cp.replace('|',' | ') + "\nElementalist (Teal) | " + demon.ct.replace('|',' | ')

    demonText = demonText + "\n\n#Gacha Skills:"\
    + "\nAragami (Red)       | " + demon.gr.replace('|',' | ') + "\nProtector (Yellow)  | " + demon.gy.replace('|',' | ')\
    + "\nPsychic (Purple)    | " + demon.gp.replace('|',' | ') + "\nElementalist (Teal) | " + demon.gt.replace('|',' | ')

    #demonText = demonText + "\n\n#6☆ Max Level Stats\nHP - " + demon.hp + " | Strength - " + demon.str + " | Magic - " + demon.mag + " | Vitality - " + demon.vit + " | Agility - " + demon.agi + " | Luck - " + demon.luk
    #demonText = demonText + "\n\n#Elemental Resistances\nPhysical: " + demon.phys + " | Fire: " + demon.fire + " | Ice: " + demon.ice + " | Electricity: " + demon.elec + " | Force: " + demon.force + " | Light: " + demon.light + " | Dark: " + demon.dark
    demons[demon.name.lower().replace("'",'')] = demonText + "```"
    demon_names.append(demon.name)
    count += 1

# Read and store raw demon data from csv
skills = {}
skill_names = []
url = 'https://raw.githubusercontent.com/grimgal/einherjar-bot/master/dSkills.csv'
c = pd.read_csv(url,encoding='utf-8')
count = 0
Skill = collections.namedtuple('Skill','name jp mp description owner learn')
while count < 338:
    skill = Skill(name=c['Name'][count],jp=c['JP Name'][count],mp=str(c['Cost'][count]),description=str(c['Description'][count]),owner=str(c['Learned By'][count]),learn=c['Transferable From'][count])
    if isinstance(skill.learn, float):
        skill = Skill(name=c['Name'][count],jp=c['JP Name'][count],mp=str(c['Cost'][count]),description=str(c['Description'][count]),owner=str(c['Learned By'][count]),learn='N/A')

    skills[skill.name.lower().replace("'",'')] = "```md\n#" + skill.name + " | " + skill.jp + " | " + skill.mp + " | " + skill.description\
    + "\n\nDemons with skill: " + skill.owner + "\nDemons to transfer skill from: " + skill.learn + "```"
    skill_names.append(skill.name)
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
        maybe = difflib.get_close_matches(name, demon_names)
        if len(maybe) > 0:
            await bot.say("This demon doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
        else:
            await bot.say("This demon doesn't exist in my database. If the demon name has a space in it, make sure to enclose it in quotes.")
        return

    await bot.say(selectedDemon)

@bot.command()
async def skill(name : str):
    name = name.lower().replace("'",'')
    try:
        selectedSkill = skills[name]
    except Exception:
        maybe = difflib.get_close_matches(name, skill_names)
        if len(maybe) > 0:
            await bot.say("This skill doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
        else:
            await bot.say("This skill doesn't exist in my database. If the skill name has a space in it, make sure to enclose it in quotes.")
        return

    await bot.say(selectedSkill)

TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
