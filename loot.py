def _ogre_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player._sword()
        print "\nAfter defeating the Ogre you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player._belt()
        print "\nAfter defeating the Ogre you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player._offhand()
        print "\nAfter defeating the Ogre you find an Offhand.\n"
    else:
        print "\nAfter defeating the Ogre you find nothing but junk\n"
    player._displayStats()

def _snake_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player._sword()
        print "\nAfter defeating the Giant Snake you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player._belt()
        print "\nAfter defeating the Giant Snake you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player._offhand()
        print "\nAfter defeating the Giant Snake you find an Offhand.\n"
    else:
        print "\nAfter defeating the Giant Snake you find nothing but junk\n"
    player._displayStats()

def _gargoyle_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player._sword()
        print "\nAfter defeating the Gargoyle you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player._belt()
        print "\nAfter defeating the Gargoyle you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player._offhand()
        print "\nAfter defeating the Gargoyle you find an Offhand.\n"
    elif rand >= 90 and rand <= 95:
        player._trinket()
        print "\nAfter defeating the Gargoyle you find an extremely rare Trinket.\n"
    elif rand == 100:
        player._legendary_weapon()
        print "\nAfter defeating the Gargoyle you find a Weapon that hasn't been seen for thousands of years.\n"
    else:
        print "\nAfter defeating the Gargoyle you find nothing but junk\n"
    player._displayStats()

def _dragon_loot(player):
    rand = random.randrange(0,100)
    if rand <= 10:
        player._sword()
        print "\nAfter defeating the Dragon you find a Sword.\n"
    elif rand > 10 and rand <= 40:
        player._belt()
        print "\nAfter defeating the Dragon you find a Belt.\n"
    elif rand > 40 and rand <= 60:
        player._offhand()
        print "\nAfter defeating the Dragon you find an Offhand.\n"
    elif rand > 70 and rand <= 95:
        player._trinket()
        print "\nAfter defeating the Dragon you find an extremely rare Trinket.\n"
    elif rand > 95 and rand <= 100:
        player._legendary_weapon()
        print "\nAfter defeating the Dragon you find a Weapon that hasn't been seen for thousands of years.\n"
    else:
        print "\nAfter defeating the Dragon you find nothing but junk\n"
    player._displayStats()
