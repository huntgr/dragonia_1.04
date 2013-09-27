import random
import sys
import time
class cyclops:
    def __init__(self):
        self.name = 'cyclops'
        self.health = 500
        self.stamina = 50
        self.damage = 0
        self.miss = 25
        self.last = -1
        self.dict = ['SMASHES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 175
    def f_ability0(self):
        ability = random.randrange(0,1)
        if ability == 0:
            damage = random.randrange(30,45)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The cyclops MISSES you completely!"
        elif crit >=9:
            crit = damage*2
            self.damage = crit
            print "The cyclops CRITS you for {0} damage".format(self.damage)
        else:
            self.damage = damage
            print "The cyclops {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The cyclops has {0} health remaining".format(self.health)
    def f_display(self):
        print """You enter a room filled with a foul stench.
            A cyclops smells your flesh...
            'ME HUNGRY' ME EAT YOU NOW'
            Prepare yourself for a fight!"""
        print """
            _......._
        .-'.'.'.'.'.'.`-.
      .'.'.'.'.'.'.'.'.'.`.
     /.'.'               '.\
     |.'    _.--...--._     |
     \    `._.-.....-._.'   /
     |     _..- .-. -.._   |
  .-.'    `.   ((@))  .'   '.-.
 ( ^ \      `--.   .-'     / ^ )
  \  /         .   .       \  /
  /          .'     '.  .-    \
 ( _.\    \ (_`-._.-'_)    /._\)
  `-' \   ' .--.          / `-'
      |  / /|_| `-._.'\   |
      |   |       |_| |   /-.._
  _..-\   `.--.______.'  |
       \       .....     |
        `.  .'      `.  /
          \           .'
           `-..___..-`
           """
        
class ogre:
    def __init__(self):
        self.name = 'ogre'
        self.health = 300
        self.stamina = 30
        self.damage = 0
        self.miss = 20
        self.dict = ['SMASHES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 75
    def f_ability0(self):
        damage = random.randrange(17,30)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The ogre MISSES you completely!"
        elif crit ==10:
            crit = damage*2
            self.damage = crit
            print "The ogre CRITS you for {0} damage".format(self.damage)
        else:
            self.damage = damage
            print "The ogre {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The ogre has {0} health remaining".format(self.health)
    def f_display(self):
        print """An ogre is sleeping in the next room.
        He appears to be surrounded by bones from those
        who have attempted to kill him before."""
        print '''
                      |\  ,,,,,  /|
                      | \/_   _\/ |
               /\     (_    "    _)
               \ \      (  ,--, )
               / /    ,,,\__-__/,,,
               \ \   ,,,,""""""",,,,  ,,,,
               /_/   |  |"""""""(  ) ,(  )
              [!!!]-'  / """"""" \  \ / /
               |!|----' """"""""" `,___/
                        ;;;;;;;;;
                        """""""""
                        """" """"
                        """   """
                       _"",   ,""_
                      (___)   (___)

                '''
        
class gargoyle:
    def __init__(self):
        self.name = 'gargoyle'
        self.health = 450
        self.stamina = 45
        self.damage = 0
        self.miss = 5
        self.dict = ['DECIMATES','HITS','CRUSHES','OBLITERATES','SCRAPES','BARELY HITS','CRITS','misses']
        self.target = 'unknown'
        self.xp = 150
    def f_ability0(self):
        damage = random.randrange(30,45)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The Gargoyle MISSES you completely!"
        elif crit ==10:
            crit = damage*1.5
            self.damage = crit
            print "The Gargoyle CRITS you for {0} damage".format(self.damage)
        else:
            self.damage = damage
            print "The Gargoyle {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The Gargoyle has {0} health remaining".format(self.health)
    def f_display(self):
        print """You enter the next room and a
        Gargoyle guards a tomb.  I wonder whats inside?"""
        print """
               /|    /(_)\    |\                
             /' `\   \`,'/   /' `\              
           /' / | `\_/\~/\_/' | \ `\          
          O  |   \/'   V   `\/   |  O        
         O   |,-,|   ,_;_,   |,-,|   O       
        oO    \  \\ '\ I /` //  /    Oo     
        oO     \ \`\  \ /  /'/ /     Oo     
         O    /~\ \,\  |  /,/ /~\    O       
    ______O  /__/ /__| I |__\ \__\  O____    
    |      \|  '''  ''' ```  ```  |/     
        """

class dragon:
    def __init__(self):
        self.name = 'dragon'
        self.health = 1000
        self.stamina = 100
        self.damage = 0
        self.miss = 7
        self.dict = ['HITS','BITES','BURNS','DEVOURES','BREATHES FIRE','CRITS','MISSES']
        self.target = 'unknown'
        self.xp = 1000
    def f_ability0(self):
        damage = random.randrange(1,80)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The Dragon MISSES you completely!"
        elif crit ==10:
            crit = damage*2.5
            self.damage = crit
            print "The Dragon CRITS you for {0}".format(self.damage)
        else:
            self.damage = damage
            print "The Dragon {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The Dragon has {0} health remaining".format(self.health)
    def f_display(self):
        print """You happen upon a dragon's lair.
        The gold and spoils he is guarding are beyond
        your wildest dreams.  If you can manage to defeat him..."""
        print """
                                             ..
                                     ,o""'o
                                  ,o$"     o
                               ,o$$$                                 
                             ,o$$$'
                           ,o$"o$'
                         ,o$$"$"'   
                      ,o$"$o"$"'    
                   ,oo$"$"$"$"$$`                      ,oooo$$$$$$$$oooooo.  
                ,o$$$"$"$"$"$"$"o$`..             ,$o$"$$"$"'            `oo.o
             ,oo$$$o"$"$"$"$  $"$$$"$`o        ,o$$"o$$$o$'                 `o
          ,o$"$"$o$"$"$"$  $"$$o$$o $$o`o   ,$$$$$o$"$$o'                    $
        ,o"$$"'  `$"$o$" o$o$o"  $$$o$o$oo"$$$o$"$$"$o"'                     $
     ,o$"'        `"$ "$$o$$" $"$o$o$$"$o$$o$o$o"$"$"`""o                   ' 
   ,o$'          o$ `"$"$o "$o$$o$$$"$$$o"$o$$o"$$$    `$$  
  ,o'           (     `" o$"$o"$o$$$"$o$"$"$o$"$$"$ooo|  `` 
 $"$             `    (   `"o$$"$o$o$$ "o$o"   $o$o"$"$    )
(  `                   `    `o$"$$o$" "o$$     "o /|"$o"
 `                           `$o$$$$"" o$      "o$\|"$o'
                              `$o"$"$ $ "       `"$"$o$
                               "$$"$$ "oo         ,$""$ 
                               $"$o$$""o"          ,o$"$
                               $$"$$"$ "o           `,",
                     ,oo$oo$$$$$$"$o$$$ ""o           
                  ,o$$"o"o$o$$o$$$"$o$$oo"oo
                ,$"oo"$$$$o$$$$"$$$o"o$o"o"$o o
               ,$$$""$$o$,      `$$$$"$$$o""$o $o               
               $o$o$"$,          `$o$"$o$o"$$o$ $$o             
              $$$o"o$$           ,$$$$o$$o"$"$$ $o$$oo      ,   
              "$o$$$ $`.        ,"$$o$"o$""$$$$ `"$o$$oo    `o
              `$o$o$"$o$o`.  ,.$$"$o$$"$$"o$$$$   `$o$$ooo    $$ooooooo
                `$o$"$o"$"$$"$$"$"$$o$$o"$$o"        `"$o$o            `"o
                   `$$"$"$o$$o$"$$"$ $$$  $ "           `$"$o            `o
                      `$$"o$o"$o"$o$ "  o $$$o            `$$"o          ,$
                         (" ""$""'     o"" "o$o             `$$ooo     ,o$$
                              $$'""o   (   "$o$$$"o            `$o$$$o$"$'
                                ) ) )           )  ) )            ` "'
        """
class giant_snake:
    def __init__(self):
        self.name = 'snake'
        self.health = 250
        self.stamina = 25
        self.damage = 0
        self.miss = 15
        self.dict = ['HITS','BITES','KNICKS','DEVOURES','POISONS','CRITS','MISSES']
        self.target = 'unknown'
        self.xp = 65
    def f_ability0(self):
        damage = random.randrange(20,30)
        crit = random.randrange(1,10)
        miss = random.randrange(1,100)
        if miss <= self.miss:
            self.damage = 0
            print "The giant snake MISSES you completely!"
        elif crit ==10:
            crit = damage*2.5
            self.damage = crit
            print "The giant snake CRITS you for {0}".format(self.damage)
        else:
            self.damage = damage
            print "The giant snake {0} for {1} damage".format(self.dict[random.randrange(0,6)],self.damage)
    def f_health(self):
        print "The giant snake has {0} health remaining".format(self.health)
    def f_display(self):
        print """You enter the next room and startle
            a Giant Snake.  He attacks!"""
        print '''
           ---_ ...... _/_ -    
          /  .      ./ .'*\ \    
          : '         /__-'   \. 
         /                      )
       _/                  >   .' 
     /   .   .       _.-" /  .'   
     \           __/"     /.'/|   
       \ '--  .-" /     //' |\|  
        \|  \ | /     //_ _ |/|
         `.  \:     //|_ _ _|\|
         | \/.    //  | _ _ |/| 
          \_ | \/ /    \ _ _ \\\ 
              \__/      \ _ _ \|\
        '''
