import random
import sys
import time
from _globals import *
from loot import *
from commands import *
from classes import *
from creatures import *

g_chosen = False
g_exit = False
g_running = True
g_count = 0
g_no_enemy = True
g_enemies = ['ogre','giant snake','ogre','cyclops','giant snake','ogre','giant snake','gargoyle','dragon']
g_error_messages = ["Robin...no.","You think I'm going to listen to you?","um...what?","Yeah no clue what you're telling me to do.","Stop touching me there.","Will you attack already?","Glares at you.","Siiiiigh.", "You want me to do WHAT?","Sorry I don't roll that way","I would if I could.","NO..NO NO NO NO..NONONONONONONON!"]

def main():
    global g_exit
    global g_chosen
    global g_running
    global g_count
    global g_no_enemy
    global g_enemies
    global g_error_messages
    
    while g_running != False:
        print "Welcome to Dragonia."
        print "\nPlease choose your class: Mage (1), Warrior (2), Cleric(3), Warlock(4)"
        f_reset()
        #player.dead = 0
        g_chosen = False
        g_chosen = False
        g_no_enemy = True
        g_enemies = ['ogre','giant snake','ogre','cyclops','giant snake','ogre','giant snake','gargoyle','dragon']
        #print g_enemies
        #print g_enemies
        while g_chosen != True:
            g_exit = False
            
            try:
                my_class = raw_input(">>> ")
                if int(my_class) is 1:
                    print "Enter your adventurer's name"
                    my_name = raw_input(">>> ")
                    player = mage(my_name)
                    g_chosen = True
                elif int(my_class) is 2:
                    print "Enter your adventurer's name"
                    my_name = raw_input(">>> ")
                    player = warrior(my_name)
                    g_chosen = True
                elif int(my_class) is 3:
                    print "Enter your adventurer's name"
                    my_name = raw_input(">>> ")
                    player = cleric(my_name)
                    g_chosen = True
                elif int(my_class) is 4:
                    print "Enter your adventurer's name"
                    my_name = raw_input(">>> ")
                    player = warlock(my_name)
                    g_chosen = True
                elif int(my_class) is 5:
                    g_running = False
                    g_chosen = True
                else:
                    print "incorrect input"
            except ValueError:
                #g_count += 1
                print "error"
                
        if g_running == False:
            break
        print ('\nWelcome ' + player.cls + ' '+ player.name +' lets begin our journey through Dragonia.  Good luck.')
        print "\nThe following commands are allowed: attack, dance, abilities, and exit.  More to come!\n"
        player.f_displayStats()
        print ""
        player.f_abilities()
        print ""
        f_reset()
        time.sleep(3)
        while g_exit == False:
            try:
                if g_no_enemy == True:
                    if g_enemies == []:
                        print "You efforts have been valient, victory is yours!"
                        f_reset()
                        g_exit = True
                        player.dead = 1
                        break      
                    else:
                        enemies_left = len(g_enemies)
                        if enemies_left == 1:
                            pick_enemy = 0
                        else:
                            pick_enemy = random.randrange(0,enemies_left)
                        if g_enemies[pick_enemy] == 'ogre':
                            enemy = ogre()
                        elif g_enemies[pick_enemy] == 'giant snake':
                            enemy = giant_snake()
                        elif g_enemies[pick_enemy] == 'gargoyle':
                            enemy = gargoyle()
                        elif g_enemies[pick_enemy] == 'dragon':
                            enemy = dragon()
                        elif g_enemies[pick_enemy] == 'cyclops':
                            enemy = cyclops()
                        enemy.f_display()
                        g_no_enemy = False
                if player.dead == 1:
                    break
                inpt = raw_input(">>> ")
                if inpt == 'attack':
                    f_attack(player,enemy)
                    if enemy.health <= 0 and player.health > 0:
                        g_no_enemy = True
                        if g_enemies != []:
                            g_enemies.pop(pick_enemy)
                elif inpt == 'abilities':
                    #f_abilities(player)
                    print "Your abilities are: "
                    player.f_abilities()
                elif inpt == 'dance':
                    f_dance()
                elif inpt == 'exit':
                    g_exit = True
                    g_running = False
                else:
                    val = random.randrange(0,12)
                    print "{0}".format(g_error_messages[val])
            except ValueError:
                #g_count += 1
                print "something"

if __name__ == "__main__":
    main()
