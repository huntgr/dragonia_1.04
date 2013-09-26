def _abilities():
    print "Your abilities are: "
    player._abilities()
    sys.stdout.flush()

def _damage(chosen_ability):
     global _exit
     print ""
     #player._ability0()
     eval("player."+chosen_ability)
     enemy.health -= player.damage
     enemy._ability0()
     if(player.shield):
         if(player.shield < enemy.damage):
             enemy.damage -= player.shield
             player.shield = 0
         else:
             player.shield -= enemy.damage
             enemy.damage = 0
     player.health -= enemy.damage
     player._health()
     enemy._health()
     print ""
     if enemy.health <= 0 and player.health > 0:
         print "\nThe enemy has been defeated! WELL DONE!  You rest for a bit and regain some health"
         print "..."
         print "......"
         player.health = player.health + enemy.stamina*2
         if player.health > (player.stamina*10):
             player.health = player.stamina*10
         player._health()
         player.xp += enemy.xp
         if player.xp >= player.lvl * player.lvl * 65:
             player._level()
             player._displayStats()
             player._health()
             player._abilities()
             time.sleep(2)
         if enemy.name == 'ogre':
             _ogre_loot(player)
         elif enemy.name == 'snake':
             _snake_loot(player)
         elif enemy.name == 'gargoyle':
             _gargoyle_loot(player)
         elif enemy.name == 'dragon':
             _dragon_loot(player)
         else:
             print "something bad happened"
         time.sleep(2)
     elif player.health <= 0:
         print "\nYou have been slain! Better luck next time"
         print "...GAMEOVER..."
         _reset()
         _exit = True
    
def _attack(enemy):
    print "\nWhat would you like to use?"
    player._abilities()
    inpute = raw_input(">>> ")
    if int(inpute) == 1:
        _damage("_ability0()")
    elif int(inpute) == 2:
        _damage("_ability1()")
    sys.stdout.flush()
            
def _dance():
    print "\nYour character breaks into dance. 'This is awkward'"
    sys.stdout.flush()

def _reset():
    global chosen
    global _exit
    global no_enemy
    global enemies
    chosen = False
    no_enemy = True
    enemies = ['ogre','giant snake','ogre','giant snake','ogre','giant snake','gargoyle','dragon']
    _exit = False
