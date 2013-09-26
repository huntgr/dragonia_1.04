import random,sys,time
from classes import *
from loot import *
from creatures import *
from _globals import *
from commands import *
    
while running != False:
    print "\nPlease choose your class: Mage (1), Warrior (2), Cleric(3), Warlock(4)"
    while chosen != True:
        _exit = False
        try:
            _class = raw_input(">>> ")
            if int(_class) is 1:
                print "Enter your adventurer's name"
                my_name = raw_input(">>> ")
                player = mage(my_name)
                chosen = True
            elif int(_class) is 2:
                print "Enter your adventurer's name"
                my_name = raw_input(">>> ")
                player = warrior(my_name)
                chosen = True
            elif int(_class) is 3:
                print "Enter your adventurer's name"
                my_name = raw_input(">>> ")
                player = cleric(my_name)
                chosen = True
            elif int(_class) is 4:
                print "Enter your adventurer's name"
                my_name = raw_input(">>> ")
                player = warlock(my_name)
                chosen = True
            elif int(_class) is 5:
                running = False
                chosen = True
            else:
                print "incorrect input"
        except ValueError:
            count += 1
            
    if running == False:
        break
    print ('\nWelcome ' + player.cls + ' '+ player.name +' lets begin our journey through Dragonia.  Good luck.')
    print "\nThe following commands are allowed: attack, dance, abilities, and exit.  More to come!\n"
    player._displayStats()
    print ""
    player._abilities()
    print ""
    _reset()
    time.sleep(3)
    while _exit == False:
        try:
            if no_enemy == True:
                if enemies == []:
                    print "You efforts have been valient, victory is yours!"
                    _reset()
                    break      
                else:
                    enemies_left = len(enemies)
                    if enemies_left == 1:
                        pick_enemy = 0
                    else:
                        pick_enemy = random.randrange(0,enemies_left)
                    if enemies[pick_enemy] == 'ogre':
                        enemy = ogre()
                    elif enemies[pick_enemy] == 'giant snake':
                        enemy = giant_snake()
                    elif enemies[pick_enemy] == 'gargoyle':
                        enemy = gargoyle()
                    elif enemies[pick_enemy] == 'dragon':
                        enemy = dragon()
                    enemy._display()
                    no_enemy = False
            inpt = raw_input(">>> ")
            if inpt == 'attack':
                _attack(enemy)
                if enemy.health <= 0 and player.health > 0:
                    no_enemy = True
                    if enemies != []:
                        enemies.pop(pick_enemy)
            elif inpt == 'abilities':
                _abilities()
            elif inpt == 'dance':
                _dance()
            elif inpt == 'exit':
                _exit = True
                running = False
            else:
                val = random.randrange(0,12)
                print "{0}".format(error_messages[val])
        except:
            count += 1
