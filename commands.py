import random
import sys
import time
from loot import *
from classes import *

def abilities(player):
    print "Your abilities are: "
    player.f_abilities()
    sys.stdout.flush()

def f_damage(chosen_ability,enemy,player):
     global g_exit
     global g_chosen
     global g_running
     global g_count
     global g_no_enemy
     global g_enemies
     global g_error_messages
     print ""
     #player._ability0()
     eval("player."+chosen_ability)
     time.sleep(0.5)
     enemy.health -= player.damage
     enemy.f_ability0()
     time.sleep(0.5)
     if(player.shield):
         if(player.shield < enemy.damage):
             enemy.damage -= player.shield
             player.shield = 0
         else:
             player.shield -= enemy.damage
             enemy.damage = 0
     player.health -= enemy.damage
     player.f_health()
     time.sleep(0.5)
     enemy.f_health()
     time.sleep(0.5)
     print ""
     if enemy.health <= 0 and player.health > 0:
         print "\nThe enemy has been defeated! WELL DONE!  You rest for a bit and regain some health"
         print "..."
         print "......"
         player.health = player.health + enemy.stamina*2
         if player.health > (player.stamina*10):
             player.health = player.stamina*10
         player.f_health()
         time.sleep(0.5)
         player.xp += enemy.xp
         if player.xp >= player.lvl * player.lvl * 65:
             player.f_level()
             time.sleep(0.75)
             player.f_displayStats()
             time.sleep(0.75)
             player.f_health()
             time.sleep(0.75)
             player.f_abilities()
             time.sleep(1)
         if enemy.name == 'ogre':
             f_ogre_loot(player)
         elif enemy.name == 'snake':
             f_snake_loot(player)
         elif enemy.name == 'gargoyle':
             f_gargoyle_loot(player)
         elif enemy.name == 'dragon':
             f_dragon_loot(player)
         elif enemy.name == 'cyclops':
             f_cyclops_loot(player)
         else:
             print "something bad happened"
         time.sleep(1)
     elif player.health <= 0:
         print "\nYou have been slain! Better luck next time"
         print "...GAMEOVER..."
         player.dead = 1
         f_reset()
         g_exit = True
    
def f_attack(player,enemy):
    print "\nWhat would you like to use?"
    player.f_abilities()
    inpute = raw_input(">>> ")
    if int(inpute) == 1:
        f_damage("f_ability0()",enemy,player)
    elif int(inpute) == 2:
        f_damage("f_ability1()",enemy,player)
    elif int(inpute) == 3:
        f_damage("f_ability2()",enemy,player)
    sys.stdout.flush()
            
def f_dance():
    print "\nYour character breaks into dance. 'This is awkward'"
    sys.stdout.flush()

def f_reset():
    global g_exit
    global g_chosen
    global g_running
    global g_count
    global g_no_enemy
    global g_enemies
    global g_error_messages
    g_chosen = False
    g_no_enemy = True
    g_enemies = ['ogre','giant snake','ogre','giant snake','ogre','giant snake','gargoyle','dragon']
    g_exit = False
