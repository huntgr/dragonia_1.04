import random
import sys
import time
def f_ogre_loot(player):
    rand = random.randrange(0,100)
    if rand <= 5:
        player.f_sword()
        print "\nAfter defeating the Ogre you find a Sword.\n"
    elif rand > 5 and rand <= 40:
        player.f_belt()
        print "\nAfter defeating the Ogre you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player.f_offhand()
        print "\nAfter defeating the Ogre you find an Offhand.\n"
    else:
        print "\nAfter defeating the Ogre you find nothing but junk\n"
    player.f_displayStats()
    time.sleep(2)

def f_snake_loot(player):
    rand = random.randrange(0,100)
    if rand <= 5:
        player.f_sword()
        print "\nAfter defeating the Giant Snake you find a Sword.\n"
    elif rand > 5 and rand <= 40:
        player.f_belt()
        print "\nAfter defeating the Giant Snake you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player.f_offhand()
        print "\nAfter defeating the Giant Snake you find an Offhand.\n"
    else:
        print "\nAfter defeating the Giant Snake you find nothing but junk\n"
    player.f_displayStats()
    time.sleep(2)

def f_gargoyle_loot(player):
    rand = random.randrange(0,100)
    if rand >= 0 and rand <= 30:
        player.f_sword()
        print "\nYou open the tomb...."
        time.sleep(1.5)
        print "and find a Sword!\n"
    elif rand > 30 and rand <= 40:
        player.f_belt()
        print "\nYou open the tomb...."
        time.sleep(1.5)
        print "and find a Belt!\n"
    elif rand > 40 and rand <= 60:
        player.f_offhand()
        print "\nYou open the tomb...."
        time.sleep(1.5)
        print "and find an Offhand!\n"
    elif rand >= 90 and rand <= 95:
        player.f_trinket()
        print "\nYou open the tomb...."
        time.sleep(1.5)
        print "and find an interesting Trinket.  It looks like it will be useful!\n"
    elif rand == 100:
        player.f_legendary_weapon()
        print "\nYou open the tomb...."
        time.sleep(1.5)
        print """and find a Mighty Weapon that has
              not been seen for thousands of years!\n"""
    else:
        print "\nYou open the tomb...."
        time.sleep(1.5)
        print "and there's nothing inside!!\n"
    player.f_displayStats()
    time.sleep(2)

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
    time.sleep(2)
