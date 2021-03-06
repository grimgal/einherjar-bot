import discord
# from discord.ext.commands import Bot
from discord.ext import commands
import os
import collections
import difflib
import pandas as pd
from texttable import Texttable

def aether_types(s, i):
    # Yellow/Purple/Blue/Red
    if s == "Entity" or s == "Zealot" or s == "Enigma" or s == "UMA" or s == "Rumor" or s == "Hero" or s == "Fiend":
        if i == 1:
            return "Light"
        if i == 2:
            return "Dark"
        if i == 3:
            return "Lawful"
        if i == 4:
            return "Chaotic"
    elif s == "Dragon" or s == "Kishin" or s == "Lady" or s == "Fury":
        # Chaotic Good (Red + Yellow)
            if i == 1 or i == 3:
                return "Chaotic"
            if i == 2 or i == 4:
                return "Light"
    elif s == "Haunt" or s == "Tyrant" or s == "Foul":
        # Chaotic Evil (Red + Purple)
            if i == 1 or i == 3:
                return "Chaotic"
            if i == 2 or i == 4:
                return "Dark"
    elif s == "Avian" or s == "Megami" or s == "Herald":
        # Lawful Good (Blue + Yellow)
            if i == 1 or i == 3:
                return "Lawful"
            if i == 2 or i == 4:
                return "Light"
    elif s == "Vile":
        # Lawful Evil (Blue + Purple)
            if i == 1 or i == 3:
                return "Lawful"
            if i == 2 or i == 4:
                return "Dark"
    elif s == "Wilder" or s == "Jaki":
        # Neutral Evil (Green + Purple)
            if i == 1 or i == 3:
                return "Neutral"
            if i == 2 or i == 4:
                return "Dark"
    elif s == "Genma" or s == "Holy" or s == "Avatar" or s == "Deity":
        # Neutral Good (Green + Yellow)
            if i == 1 or i == 3:
                return "Neutral"
            if i == 2 or i == 4:
                return "Light"
    elif s == "Night" or s == "Femme" or s == "Brute" or s == "Fallen":
        # Neutral Chaotic (Green + Red)
            if i == 1 or i == 3:
                return "Neutral"
            if i == 2 or i == 4:
                return "Chaotic"
    elif s == "Yoma" or s == "Divine":
        # Neutral Lawful (Green + Blue)
            if i == 1 or i == 3:
                return "Neutral"
            if i == 2 or i == 4:
                return "Lawful"
    elif s == "Fairy" or s == "Beast" or s == "Snake":
        # Neutral (Green)
            return "Neutral"
    return ""

def aether(s, r, i):
    # Yellow/Purple/Blue/Red
    if s == "Entity" or s == "Zealot" or s == "Enigma" or s == "UMA" or s == "Rumor" or s == "Hero" or s == "Fiend":
        if r == 5:
            return "15 Large " + aether_types(s, i) + " Aether"
        elif r == 4:
            return "5 Large " + aether_types(s, i) + " Aether"
        elif r == 3:
            return "10 Medium " + aether_types(s, i) + " Aether"
        elif r == 2:
            return "5 Medium " + aether_types(s, i) + " Aether"
        elif r == 1:
            return "5 Small " + aether_types(s, i) + " Aether"
    elif s == "Dragon" or s == "Kishin" or s == "Lady" or s == "Fury" or s == "Haunt" or s == "Tyrant" or s == "Foul" or s == "Avian" or s == "Megami" or s == "Herald" or s == "Vile" or s == "Wilder" \
    or s == "Genma" or s == "Holy" or s == "Avatar" or s == "Deity" or s == "Night" or s == "Femme" or s == "Brute" or s == "Fallen" or s == "Yoma" or s == "Divine":
        # Chaotic Good (Red + Yellow)
        if r == 5:
            if i == 1 or i == 2:
                return "20 Medium " + aether_types(s, i) + " Aether"
            if i == 3 or i == 4:
                return "15 Large " + aether_types(s, i) + " Aether"
        elif r == 4:
            if i == 1 or i == 2:
                return "15 Medium " + aether_types(s, i) + " Aether"
            if i == 3 or i == 4:
                return "5 Large " + aether_types(s, i) + " Aether"
        elif r == 3:
            if i == 1 or i == 2:
                return "5 Small " + aether_types(s, i) + " Aether"
            if i == 3 or i == 4:
                return "10 Medium " + aether_types(s, i) + " Aether"
        elif r == 2:
            if i == 1 or i == 2:
                return "10 Medium " + aether_types(s, i) + " Aether"
            if i == 3 or i == 4:
                return "5 Medium " + aether_types(s, i) + " Aether"
        elif r == 1:
            if i == 1 or i == 2:
                return "10 Small " + aether_types(s, i) + " Aether"
    elif s == "Fairy" or s == "Beast" or s == "Snake":
        # Neutral (Green)
        if r == 5:
            if i == 1:
                return "40 Medium " + aether_types(s, i) + " Aether"
            if i == 2:
                return "30 Large " + aether_types(s, i) + " Aether"
        elif r == 4:
            if i == 1:
                return "30 Medium " + aether_types(s, i) + " Aether"
            if i == 2:
                return "10 Large " + aether_types(s, i) + " Aether"
        elif r == 3:
            if i == 1:
                return "10 Small " + aether_types(s, i) + " Aether"
            if i == 2:
                return "20 Medium " + aether_types(s, i) + " Aether"
        elif r == 2:
            if i == 1:
                return "20 Small " + aether_types(s, i) + " Aether"
            if i == 2:
                return "10 Medium " + aether_types(s, i) + " Aether"
        elif r == 1:
            if i == 1 or i == 2:
                return "20 Small " + aether_types(s, i) + " Aether"
    return ""

# Returns any localized names
def demon_name(name):
    name = name.lower().replace("'", '')
    if name == "suzaku":
        name = "feng huang"
    elif name == "seiryu" or name == "qing long" or name == "seiryuu":
        name = "long"
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
def get_skill_list(skill, arch=''):
    skills = skill.split('|')
    count = 0
    for item in skills:
        skills[count] = item.strip()
        count += 1

    if len(skills) < 4:
        if len(arch) > 3:
            return [skills[0], '', '', '']
        return [skills[0], '', '']
    if len(arch) > 3:
        return [arch, skills[0], skills[2], skills[3]]
    return [skills[0], skills[2], skills[3]]


def largest_character_count(s):
    ln = 0
    for item in s:
        if len(item) > ln:
            ln = len(item)
    return ln


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
                table.add_row(get_skill_list(d.ct, "Elementalist (Teal)"))
            r = r + table.draw().strip() + "\n"
            count += 1
    elif t == 3:
        count = 0
        while count < 4:
            table = Texttable()
            table.set_deco(Texttable.VLINES)
            table.set_cols_align(["l", "c", "c", "l"])
            table.set_cols_width([19, largest_character_count([d.gr.split('|')[0], d.gy.split('|')[0], d.gp.split('|')[0], d.gt.split('|')[0]]), 7, 150])

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
Demon = collections.namedtuple('Demon', 'name race grade rarity ai phys fire ice elec force light dark hp str mag vit agi luk s1 s2 s3 ca cr cy cp ct gr gy gp gt patk pdef matk mdef aether1 aether2 aether3 aether4')
# demons row count - 1
while count < 189:
    demon = Demon(name=c['Name'][count], race=c['Race'][count], grade=str(int(c['Grade'][count])), rarity='☆' * int(c['Rarity'][count]), ai=str(c['AI'][count]),
    phys=str(c['Phys'][count]), fire=str(c['Fire'][count]), ice=str(c['Ice'][count]),
    elec=str(c['Elec'][count]), force=str(c['Force'][count]), light=str(c['Light'][count]), dark=str(c['Dark'][count]),
    hp=str(c['6★ HP'][count]).strip(), str=str(c['6★ Strength'][count]).strip(), mag=str(c['6★ Magic'][count]).strip(),
    vit=str(c['6★ Vitality'][count]).strip(), agi=str(c['6★ Agility'][count]).strip(), luk=str(c['6★ Luck'][count]).strip(),
    s1=c['Skill 1'][count], s2=c['Skill 2'][count], s3=c['Skill 3'][count],
    ca=c['Clear Archetype'][count], cr=c['Red Archetype'][count], cy=c['Yellow Archetype'][count], cp=c['Purple Archetype'][count], ct=c['Teal Archetype'][count],
    gr=c['Red Gacha'][count], gy=c['Yellow Gacha'][count], gp=c['Purple Gacha'][count], gt=c['Teal Gacha'][count],
    patk = str(int(c['PATK'][count])), pdef = str(int(c['PDEF'][count])), matk = str(int(c['MATK'][count])), mdef = str(int(c['MDEF'][count])),
    aether1=aether(c['Race'][count],int(c['Rarity'][count]),1), aether2=aether(c['Race'][count],int(c['Rarity'][count]),2), aether3=aether(c['Race'][count],int(c['Rarity'][count]),3),
    aether4=aether(c['Race'][count],int(c['Rarity'][count]),4))

    infoTable = Texttable()
    infoTable.set_cols_align(["c", "c", "c"])
    infoTable.add_rows([["Race", "Grade", "Rarity"],
                        [demon.race, demon.grade, demon.rarity]])

    statsTable = Texttable()
    statsTable.set_deco(Texttable.VLINES)
    statsTable.set_cols_width([len(demon.hp),len(demon.str),len(demon.mag),len(demon.vit),len(demon.agi),len(demon.luk)])
    statsTable.set_cols_align(["c", "c", "c", "c", "c", "c"])
    statsTable.add_rows([["HP","Strength","Magic","Vitality","Agility","Luck"],
    [demon.hp,demon.str,demon.mag,demon.vit,demon.agi,demon.luk]])

    resistsTable = Texttable()
    # resistsTable.set_deco()
    resistsTable.set_cols_align(["c", "c", "c", "c", "c", "c", "c"])
    resistsTable.add_rows([["Physical","Fire","Ice","Electricity","Force","Light","Dark"],
    [demon.phys,demon.fire,demon.ice,demon.elec,demon.force,demon.light,demon.dark]])

    innateSkills = get_skills(demon, 1)
    archSkills = get_skills(demon, 2)
    gachaSkills = get_skills(demon, 3)

    # demonText = "```md\n#" + demon.name + "\n" + infoTable.draw()
    # demonText = demonText + "\n\n#Elemental Resistances\nPhysical: " + demon.phys + " | Fire: " + demon.fire + " | Ice: " + demon.ice + " | Electricity: " + demon.elec + " | Force: " + demon.force + " | Light: " + demon.light + " | Dark: " + demon.dark
    demonText = "```md\n#" + demon.name + "\nRace: " + demon.race + " | Grade: " + demon.grade + " | Rarity: " + demon.rarity
    # demonText = demonText + "\n\n#6☆ Max Level Stats\nHP - " + demon.hp + " | Strength - " + demon.str + " | Magic - " + demon.mag + " | Vitality - " + demon.vit + " | Agility - " + demon.agi + " | Luck - " + demon.luk
    demonText = demonText + "\n\n#6☆ Max Level Stats\n" + statsTable.draw()
    demonText = demonText + "\n\n#Elemental Resistances\n" + resistsTable.draw()
    demonText = demonText + "\n\n#Innate Skills\n" + innateSkills
    demonText = demonText + "\n#Archetype Skills\n" + archSkills
    demonText = demonText + "\n#Gacha Skills\n" + gachaSkills
    # demonText = demonText + "\n\n#Innate Skills:"\
    # + "\nSkill 1 | " + demon.s1.replace('|',' | ') + "\nSkill 2 | " + demon.s2.replace('|',' | ') + "\nSkill 3 | " + demon.s3.replace('|',' | ')
    # demonText = demonText + "\n\n#Archetype Skills:\nCommon (Clear)      | " + demon.ca.replace('|',' | ')\
    # + "\nAragami (Red)       | " + demon.cr.replace('|',' | ') + "\nProtector (Yellow)  | " + demon.cy.replace('|',' | ')\
    # + "\nPsychic (Purple)    | " + demon.cp.replace('|',' | ') + "\nElementalist (Teal) | " + demon.ct.replace('|',' | ')
    # demonText = demonText + "\n\n#Gacha Skills:"\
    # + "\nAragami (Red)       | " + demon.gr.replace('|',' | ') + "\nProtector (Yellow)  | " + demon.gy.replace('|',' | ')\
    # + "\nPsychic (Purple)    | " + demon.gp.replace('|',' | ') + "\nElementalist (Teal) | " + demon.gt.replace('|',' | ')
    demons[demon.name.lower().replace("'", '')] = demonText + "```"
    demons_mobile[demon.name.lower().replace("'", '')] = demon
    #if len(demonText) > 1900:
    #    print(len(demonText))

    demon_names.append(demon.name)
    count += 1

# Read and store raw demon data from csv
skills = {}
skills_mobile = {}
skill_names = []
url = 'https://raw.githubusercontent.com/grimgal/einherjar-bot/master/dSkills.csv'
c = pd.read_csv(url, encoding='utf-8')
count = 0
Skill = collections.namedtuple('Skill', 'name jp mp description owner learn element target sp')

# skills row count - 1
while count < 363:
    if isinstance(c['Transferable From'][count], float):
        skill = Skill(name=str(c['Name'][count]), jp=str(c['JP Name'][count]), mp=str(c['Cost'][count]), description=str(c['Description'][count]),
                      owner=str(c['Learned By'][count]), learn='N/A', element=c['Element'][count], target=c['Target'][count], sp=str(c['Skill Points'][count]))
    else:
        skill = Skill(name=str(c['Name'][count]), jp=str(c['JP Name'][count]), mp=str(c['Cost'][count]), description=str(c['Description'][count]),
                      owner=str(c['Learned By'][count]), learn=c['Transferable From'][count], element=c['Element'][count], target=c['Target'][count], sp=str(int(c['Skill Points'][count])))
        
    skills[skill.name.lower().replace("'", '')] = "```md\n#" + skill.name + " | " + skill.jp + " | " + skill.mp + " | " + skill.description\
    + "\n\nDemons with skill: " + skill.owner + "\nDemons to transfer skill from: " + skill.learn + "```"
    skills_mobile[skill.name.lower().replace("'", '')] = skill

    skill_names.append(skill.name)
    count += 1

Client = discord.Client()
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_server_join(server):
    await client.send_message(client.get_channel('demon-and-skill-info'), "Bot is online!")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


# Get demon info
@bot.command()
async def demon(name: str):
    name = demon_name(name)
    try:
        demon = demons[name]
    except Exception:
        maybe = difflib.get_close_matches(name, demon_names)
        if len(maybe) > 0:
            demon = demons[maybe[0].lower().replace("'", '')]
            # await bot.say("This demon doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
        else:
            await bot.say("This demon doesn't exist in my database. If the demon name has a space in it, make sure to enclose it in quotes.")
            return

    await bot.say(demon)


# Get skill info
@bot.command()
async def skill(name: str):
    name = name.lower().replace("'", '')
    try:
        skill = skills[name]
    except Exception:
        maybe = difflib.get_close_matches(name, skill_names)
        if len(maybe) > 0:
            # await bot.say("This skill doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
            skill = skills[maybe[0].lower().replace("'", '')]
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
            demon = demons_mobile[maybe[0].lower().replace("'", '')]
            # await bot.say("This demon doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
        else:
            await bot.say("This demon doesn't exist in my database. If the demon name has a space in it, make sure to enclose it in quotes.")
            return
    web_name = demon.name.replace(' ', '%20')
    em = discord.Embed(title=demon.name, description="Race: " + demon.race + " | Grade: " + demon.grade + " | Rarity: " + demon.rarity + " | AI: " + demon.ai,
                       color=0xFFBF00)
    em.set_thumbnail(url="https://raw.githubusercontent.com/grimgal/einherjar-bot/master/icons/" + web_name + ".jpg")
    em.add_field(name="Elemental Resistances", value="Phys: " + demon.phys + "\nFire: " + demon.fire + "\nIce: " + demon.ice
                 + "\nElec: " + demon.elec + "\nForce: " + demon.force + "\nLight: " + demon.light + "\nDark: " + demon.dark)
    em.add_field(name="6☆ Max Level Stats", value="HP - " + demon.hp + "\nStrength - " + demon.str + "\nMagic - " + demon.mag
                  + "\nVitality - " + demon.vit + "\nAgility - " + demon.agi + "\nLuck - " + demon.luk)

    em.add_field(name="6☆ Combat Stats", value="PATK - " + demon.patk + "\nPDEF- " + demon.pdef + "\nMATK - " + demon.matk + "\nMDEF - " + demon.mdef + "\n---\n" + demon.aether1
    + "\n" + demon.aether2 + "\n" + demon.aether3 + "\n" + demon.aether4)

    em.add_field(name="Base Skills", value="Transferable Skill - " + demon.s1.split('|')[0] + "\nInnate Skill 1 - " + demon.s2.split('|')[0] + "\nInnate Skill 2 - " + demon.s3.split('|')[0])
    em.add_field(name="Archetype Skills", value="Common (Clear) - " + demon.ca.split('|')[0]
                 + "\nAragami (Red) - " + demon.cr.split('|')[0] + "\nProtector (Yellow) - " + demon.cy.split('|')[0]
                 + "\nPsychic (Purple) - " + demon.cp.split('|')[0] + "\nElementalist (Teal) - " + demon.ct.split('|')[0])
    em.add_field(name="\nGacha Skills", value="Aragami (Red) - " + demon.gr.split('|')[0] + "\nProtector (Yellow) - " + demon.gy.split('|')[0]
                 + "\nPsychic (Purple) - " + demon.gp.split('|')[0] + "\nElementalist (Teal) - " + demon.gt.split('|')[0])
    await bot.say(embed=em)


# ,inline=False
# Get skill info (mobile)
@bot.command()
async def s(name: str):
    name = name.lower().replace("'", '')
    try:
        skill = skills_mobile[name]
    except Exception:
        maybe = difflib.get_close_matches(name, skill_names)
        if len(maybe) > 0:
            # await bot.say("This skill doesn't exist in my database. Did you mean:\n```fix\n" + ", ".join(maybe) + "```")
            skill = skills_mobile[maybe[0].lower().replace("'", '')]
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

    em = discord.Embed(description="JP Name: " + skill.jp + "\nMP Cost: " + skill.mp + "\nSkill Points: " + skill.sp + "\nDescription: " + skill.description, color=0xFFBF00)
    em.set_author(name=skill.name, icon_url="https://raw.githubusercontent.com/grimgal/einherjar-bot/master/icons/skills/" + icon_name)
    if icon_name == "passive.png":
        em.set_footer(text=skill.target)
    else:
        em.set_footer(icon_url="https://raw.githubusercontent.com/grimgal/einherjar-bot/master/icons/skills/" + icon_target, text=skill.target)
    em.add_field(name="Demons with skill", value=skill.owner)
    em.add_field(name="Demons to transfer skill from", value=skill.learn)
    await bot.say(embed=em)

TOKEN = os.getenv('TOKEN')

bot.run(TOKEN)
