import random
import sys
import time
def f_ogre_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player.f_sword()
        print "\nAfter defeating the Ogre you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player.f_belt()
        print "\nAfter defeating the Ogre you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player.f_offhand()
        print "\nAfter defeating the Ogre you find an Offhand.\n"
    else:
        print "\nAfter defeating the Ogre you find nothing but junk\n"
    player.f_displayStats()

def f_snake_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player.f_sword()
        print "\nAfter defeating the Giant Snake you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player.f_belt()
        print "\nAfter defeating the Giant Snake you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player.f_offhand()
        print "\nAfter defeating the Giant Snake you find an Offhand.\n"
    else:
        print "\nAfter defeating the Giant Snake you find nothing but junk\n"
    player.f_displayStats()

def f_gargoyle_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player.f_sword()
        print "\nAfter defeating the Gargoyle you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player.f_belt()
        print "\nAfter defeating the Gargoyle you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player.f_offhand()
        print "\nAfter defeating the Gargoyle you find an Offhand.\n"
    elif rand >= 90 and rand <= 95:
        player.f_trinket()
        print "\nAfter defeating the Gargoyle you find an extremely rare Trinket.\n"
    elif rand == 100:
        player.f_legendary_weapon()
        print "\nAfter defeating the Gargoyle you find a Weapon that hasn't been seen for thousands of years.\n"
    else:
        print "\nAfter defeating the Gargoyle you find nothing but junk\n"
    player.f_displayStats()

def f_dragon_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player.f_sword()
        print "\nAfter defeating the Dragon you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player.f_belt()
        print "\nAfter defeating the Dragon you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player.f_offhand()
        print "\nAfter defeating the Dragon you find an Offhand.\n"
    elif rand > 70 and rand <= 95:
        player.f_trinket()
        print "\nAfter defeating the Dragon you find an extremely rare Trinket.\n"
    elif rand > 95 and rand <= 100:
        player.f_legendary_weapon()
        print "\nAfter defeating the Dragon you find a Weapon that hasn't been seen for thousands of years.\n"
    else:
        print "\nAfter defeating the Dragon you find nothing but junk\n"
    player.f_displayStats()
