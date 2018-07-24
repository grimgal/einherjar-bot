import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import collections
import difflib
import math
import pandas as pd
from texttable import Texttable

# Returns any localized names
def demon_name(name):
    name = name.lower().replace("'",'')
    if name == "suzaku":
        name = "feng huang"
    elif name == "seiryu" or name == "long" or name == "seiryuu":
        name = "qing long"
    elif name == "kohryu":
        name = "huang long"
    elif name == "koutei":
        name = "huang di"
    elif name == "seitei tensei":
        name = "wu kong"
    elif name == "hokuto seikun":
        name = "beiji-wang"
    elif name == "byakko":
        name = "baihu"

    return name

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

def largest_character_count (s):
    l = 0
    for item in s:
        if len(item) > l:
            l = len(item)
    return l

# Returns skill table
def get_skills(d, t):
    r = ""
    if t == 1:
        count = 1
        while count < 4:
            table = Texttable()
            table.set_deco(Texttable.VLINES)
            table.set_cols_align(["l", "c", "c", "l"])
            table.set_cols_width([7, largest_character_count([d.s1.split('|')[0], d.s2.split('|')[0], d.s3.split('|')[0]]), 7,150])

            if count == 1:
                table.add_row(get_skill_list(d.s1, "Skill 1"))
            elif count == 2:
                table.add_row(get_skill_list(d.s2, "Skill 2"))
            elif count == 3:
                table.add_row(get_skill_list(d.s3, "Skill 3"))
            r = r + table.draw().strip() + "\n"
            count += 1
    elif t == 2:
        count = 0
        while count < 5:
            table = Texttable()
            table.set_deco(Texttable.VLINES)
            table.set_cols_align(["l", "c", "c", "l"])
            table.set_cols_width([19, largest_character_count([d.ca.split('|')[0], d.cr.split('|')[0], d.cy.split('|')[0], d.cp.split('|')[0], d.ct.split('|')[0]]), 7, 150])

            if count == 0:
                table.add_row(get_skill_list(d.ca, "Common (Clear)"))
            elif count == 1:
                table.add_row(get_skill_list(d.cr, "Aragami (Red)"))
            elif count == 2:
                table.add_row(get_skill_list(d.cy, "Protector (Yellow)"))
            elif count == 3:
                table.add_row(get_skill_list(d.cp, "Psychic (Purple)"))
            elif count == 4:
                print(d.ct)
                table.add_row(get_skill_list(d.ct, "Elementalist (Teal)"))
            r = r + table.draw().strip() + "\n"
            count += 1
    elif t == 3:
        count = 0
        while count < 4:
            table = Texttable()
            table.set_deco(Texttable.VLINES)
            table.set_cols_align(["l", "c", "c", "l"])
            table.set_cols_width([19, largest_character_count([d.gr.split('|')[0], d.gy.split('|')[0], d.gp.split('|')[0], d.gt.split('|')[0]]), 7,150])

            if count == 0:
                table.add_row(get_skill_list(d.gr, "Aragami (Red)"))
            elif count == 1:
                table.add_row(get_skill_list(d.gy, "Protector (Yellow)"))
            elif count == 2:
                table.add_row(get_skill_list(d.gp, "Psychic (Purple)"))
            elif count == 3:
                table.add_row(get_skill_list(d.gt, "Elementalist (Teal)"))
            r = r + table.draw().strip() + "\n"
            count += 1

    return r

# Read and store raw demon data from csv
demons = {}
demons_mobile = {}
demon_names = []
url = 'https://raw.githubusercontent.com/grimgal/einherjar-bot/master/dDemons.csv'
c = pd.read_csv(url)
count = 0
Demon = collections.namedtuple('Demon','name race grade rarity phys fire ice elec force light dark hp str mag vit agi luk s1 s2 s3 ca cr cy cp ct gr gy gp gt')
while count < 179:
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
    statsTable.set_deco(Texttable.VLINES)
    statsTable.set_cols_width([len(demon.hp),len(demon.str),len(demon.mag),len(demon.vit),len(demon.agi),len(demon.luk)])
    statsTable.set_cols_align(["c", "c", "c", "c", "c", "c"])
    statsTable.add_rows([["HP","Strength","Magic","Vitality","Agility","Luck"],
    [demon.hp,demon.str,demon.mag,demon.vit,demon.agi,demon.luk]])

    resistsTable = Texttable()
    #resistsTable.set_deco()
    resistsTable.set_cols_align(["c", "c", "c", "c", "c", "c", "c"])
    resistsTable.add_rows([["Physical","Fire","Ice","Electricity","Force","Light","Dark"],
    [demon.phys,demon.fire,demon.ice,demon.elec,demon.force,demon.light,demon.dark]])

    innateSkills = get_skills(demon, 1)
    archSkills = get_skills(demon, 2)
    gachaSkills = get_skills(demon, 3)

    #demonText = "```md\n#" + demon.name + "\n" + infoTable.draw()
    #demonText = demonText + "\n\n#Elemental Resistances\nPhysical: " + demon.phys + " | Fire: " + demon.fire + " | Ice: " + demon.ice + " | Electricity: " + demon.elec + " | Force: " + demon.force + " | Light: " + demon.light + " | Dark: " + demon.dark
    demonText = "```md\n#" + demon.name + "\nRace: " + demon.race + " | Grade: " + demon.grade + " | Rarity: " + demon.rarity
    #demonText = demonText + "\n\n#6☆ Max Level Stats\nHP - " + demon.hp + " | Strength - " + demon.str + " | Magic - " + demon.mag + " | Vitality - " + demon.vit + " | Agility - " + demon.agi + " | Luck - " + demon.luk
    demonText = demonText + "\n\n#6☆ Max Level Stats\n" + statsTable.draw()
    demonText = demonText + "\n\n#Elemental Resistances\n" + resistsTable.draw()
    demonText = demonText + "\n\n#Innate Skills\n" + innateSkills
    demonText = demonText + "\n#Archetype Skills\n" + archSkills
    demonText = demonText + "\n#Gacha Skills\n" + gachaSkills
    #demonText = demonText + "\n\n#Innate Skills:"\
    #+ "\nSkill 1 | " + demon.s1.replace('|',' | ') + "\nSkill 2 | " + demon.s2.replace('|',' | ') + "\nSkill 3 | " + demon.s3.replace('|',' | ')
    #demonText = demonText + "\n\n#Archetype Skills:\nCommon (Clear)      | " + demon.ca.replace('|',' | ')\
    #+ "\nAragami (Red)       | " + demon.cr.replace('|',' | ') + "\nProtector (Yellow)  | " + demon.cy.replace('|',' | ')\
    #+ "\nPsychic (Purple)    | " + demon.cp.replace('|',' | ') + "\nElementalist (Teal) | " + demon.ct.replace('|',' | ')
    #demonText = demonText + "\n\n#Gacha Skills:"\
    #+ "\nAragami (Red)       | " + demon.gr.replace('|',' | ') + "\nProtector (Yellow)  | " + demon.gy.replace('|',' | ')\
    #+ "\nPsychic (Purple)    | " + demon.gp.replace('|',' | ') + "\nElementalist (Teal) | " + demon.gt.replace('|',' | ')
    demons[demon.name.lower().replace("'",'')] = demonText + "```"
    demons_mobile[demon.name.lower().replace("'",'')] = demon
    if len(demonText) > 1900:
        print(len(demonText))

    demon_names.append(demon.name)
    count += 1

# Read and store raw demon data from csv
skills = {}
skills_mobile = {}
skill_names = []
url = 'https://raw.githubusercontent.com/grimgal/einherjar-bot/master/dSkills.csv'
c = pd.read_csv(url,encoding='utf-8')
count = 0
Skill = collections.namedtuple('Skill','name jp mp description owner learn element target')
while count < 343:
    if isinstance(c['Transferable From'][count], float):
        skill = Skill(name=c['Name'][count],jp=c['JP Name'][count],mp=str(c['Cost'][count]),description=str(c['Description'][count]),\
                      owner=str(c['Learned By'][count]),learn='N/A',element=c['Element'][count],target=c['Target'][count])
    else:
        skill = Skill(name=c['Name'][count],jp=c['JP Name'][count],mp=str(c['Cost'][count]),description=str(c['Description'][count]),\
                      owner=str(c['Learned By'][count]),learn=c['Transferable From'][count],element=c['Element'][count],target=c['Target'][count])

    skills[skill.name.lower().replace("'",'')] = "```md\n#" + skill.name + " | " + skill.jp + " | " + skill.mp + " | " + skill.description\
    + "\n\nDemons with skill: " + skill.owner + "\nDemons to transfer skill from: " + skill.learn + "```"
    skills_mobile[skill.name.lower().replace("'",'')] = skill

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

# Get demon info
@bot.command()
async def demon(name : str):
    name = demon_name(name)
    try:
        demon = demons[name]
    except Exception:
        maybe = difflib.get_close_matches(name, demon_names)
        if len(maybe) > 0:
            demon = demons[maybe[0]]
            pass
            #await bot.say("This demon doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
        else:
            await bot.say("This demon doesn't exist in my database. If the demon name has a space in it, make sure to enclose it in quotes.")
            return

    await bot.say(demon)

# Get skill info
@bot.command()
async def skill(name : str):
    name = name.lower().replace("'",'')
    try:
        skill = skills[name]
    except Exception:
        maybe = difflib.get_close_matches(name, skill_names)
        if len(maybe) > 0:
            #await bot.say("This skill doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
            skill = skills[maybe[0]]
            pass
        else:
            await bot.say("This skill doesn't exist in my database. If the skill name has a space in it, make sure to enclose it in quotes.")
            return

    await bot.say(skill)

# Get demon info (mobile)
@bot.command()
async def d(name):
    name = demon_name(name)

    try:
        demon = demons_mobile[name]
    except Exception:
        maybe = difflib.get_close_matches(name, demon_names)
        if len(maybe) > 0:
            demon = demons_mobile[maybe[0]]
            pass
            #await bot.say("This demon doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
        else:
            await bot.say("This demon doesn't exist in my database. If the demon name has a space in it, make sure to enclose it in quotes.")
            return

    web_name = demon.name.replace(' ','%20')
    em = discord.Embed(title=demon.name,description="Race: " + demon.race + " | Grade: " + demon.grade + " | Rarity: " + demon.rarity,\
                       color=0xFFBF00)
    em.set_thumbnail(url="https://raw.githubusercontent.com/grimgal/einherjar-bot/master/icons/" + web_name + ".jpg")
    em.add_field(name="Elemental Resistances",value="Phys: " + demon.phys + "\nFire: " + demon.fire + "\nIce: " + demon.ice\
                 + "\nElec: " + demon.elec + "\nForce: " + demon.force + "\nLight: " + demon.light + "\nDark: " + demon.dark)
    em.add_field(name="6☆ Max Level Stats",value="HP - " + demon.hp + "\nStrength - " + demon.str + "\nMagic - " + demon.mag\
                  + "\nVitality - " + demon.vit + "\nAgility - " + demon.agi + "\nLuck - " + demon.luk)
    em.add_field(name="Base Skills",value="Transferable Skill - " + demon.s1.split('|')[0] + "\nInnate Skill 1 - " +  demon.s2.split('|')[0] + "\nInnate Skill 2 - " + demon.s3.split('|')[0],\
                 inline=False)
    em.add_field(name="Archetype Skills",value="Common (Clear) - " + demon.ca.split('|')[0]\
                 + "\nAragami (Red) - " + demon.cr.split('|')[0] + "\nProtector (Yellow) - " + demon.cy.split('|')[0]\
                 + "\nPsychic (Purple) - " + demon.cp.split('|')[0] + "\nElementalist (Teal) - " + demon.ct.split('|')[0])
    em.add_field(name="\nGacha Skills",value="Aragami (Red) - " + demon.gr.split('|')[0] + "\nProtector (Yellow) - " + demon.gy.split('|')[0]\
                 + "\nPsychic (Purple) - " + demon.gp.split('|')[0] + "\nElementalist (Teal) - " + demon.gt.split('|')[0])
    await bot.say(embed=em)

# Get skill info (mobile)
@bot.command()
async def s(name : str):
    name = name.lower().replace("'",'')
    try:
        skill = skills_mobile[name]
    except Exception:
        maybe = difflib.get_close_matches(name, skill_names)
        if len(maybe) > 0:
            #await bot.say("This skill doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
            skill = skills_mobile[maybe[0]]
            pass
        else:
            await bot.say("This skill doesn't exist in my database. If the skill name has a space in it, make sure to enclose it in quotes.")
            return


    icon_name = skill.element + ".png"
    icon_target = skill.target
    if icon_name == "fire.png":
        icon_name = "fira.png"

    if icon_target == "Single Enemy" or icon_target == "Single Party Member":
        icon_target = "Single.png"
    elif icon_target == "All Enemies" or icon_target == "All Party Members":
        icon_target = "All.png"
    elif icon_target == "Random Enemy/ies":
        icon_target = "Random.png"

    em = discord.Embed(description="JP Name: " + skill.jp + "\nMP Cost: " + skill.mp + "\nDescription: " + skill.description,color=0xFFBF00)
    em.set_author(name=skill.name,icon_url="https://raw.githubusercontent.com/grimgal/einherjar-bot/master/icons/skills/" + icon_name)
    if icon_name == "passive.png":
        em.set_footer(text=skill.target)
    else:
        em.set_footer(icon_url="https://raw.githubusercontent.com/grimgal/einherjar-bot/master/icons/skills/" + icon_target,text=skill.target)
    em.add_field(name="Demons with skill",value=skill.owner)
    em.add_field(name="Demons to transfer skill from",value=skill.learn)
    await bot.say(embed=em)

TOKEN = os.getenv('TOKEN')

bot.run(TOKEN)
