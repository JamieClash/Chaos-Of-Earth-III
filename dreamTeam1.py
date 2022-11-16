import time 
import player
from time import sleep

global eternalFlame
eternalFlame = False
global pistol
pistol = False
global bow
bow = False
global dagger2
dagger2 = False
global axe
axe = False
global stickyBombs
stickyBombs = False

def die(player1):
  dreamTeam1(player1)

def dreamTeam1(player1):
  print("\nPATH SELECTED - DUO OF THE CENTURY\n")
  sleep(4)
  print("~ ARRIVAL ~")
  print("You take a deep breath as the spaceship enters the exoplanet's atmosphere. Jess had identified this planet a week ago, and the planet's readings suggests that it is indeed inhabitable.")
  sleep(3)
  print("The spaceship lands safely, and the two of you step out into the planet, taking in the beautiful landscape all around you. You squint, and see a dramatic mountain range far ahead, with a summit reaching into the clouds. Jess nudges you, and points out smoke in the distance. 'Could be a fire,' she whipsers.")
  a=input("1.Check out the smoke. 2.Don't check out the smoke.")
  if a =="1":
    print("You decide to check out the smoke. You make your way through the forest and your jaw drops when you see the source of the smoke. 'It's a city! With humans!' 'What!??' Jess, too spots the city, and gasps in awe. 'Let's head towards it! We can-'")
  else:
    print("You don't want to check ou the smoke, but Jess drags you along anyways. You make your way through the forest, and your jaw drops when you see the source of the smoke. 'It's a city! With humans!' 'What!??' Jess, too spots the city, and gasps in awe. 'Let's head towards it! We can-'") 

  print("Something screeches nearby, and several twigs snap. 'What is that?' Jess whispers.")  
  b=input("1.Run to the city. 2.Sneak towards the city. 3.Throw something away to distract whatever it is. 4.Stand still.")
  if b =="1":
    print("You and Jess break into a sprint towards the city, and some horrifying creature starts chasing after you. However, if you successfully slide under an upcoming log, you'll lose its trail.")
    sleep(5)
    st=time.time()
    c=input("PRESS [S] to slide!").upper()
    rt=time.time()
    if c=="S":
      if rt<2:
        print("You slide under the log, successfully evading the monster's trail. You make it into the city, panting.")
        town(player1)
      else:
        print("You slid too late, but thankfully Jess helps pull you under just in time. You take a heavy breath and continue towards the city.")
        town(player1)
    else:
      print("You failed to slide, bumping your head against the log. Thankfully, Jess helps pull you under just in time. You take a heavy breath and continue towards the city.")
      town(player1)
  elif b =="2":
    print("You start sneaking towards the city, careful not to make any noise. Heavy footsteps announce the departure of the creature, and you and Jess sprint towards the city before it comes back.")
    town(player1)
  elif b =="3":
    print("You throw an object into the trees, prompting a screech from the creature again. You and Jess break into a run, and a horrifying monster emerges from the bushes and starts chasing you. However, if you successfully slide under an upcoming log, you'll lose its trail.")
    sleep(5)
    st=time.time()
    c=input("PRESS [S] to slide!").upper()
    rt=time.time()
    if c=="S":
      if rt<2:
        print("You slide under the log, successfully evading the monster's trail. You make it into the city, panting.")
        town(player1)
      else:
        print("You slid too late, but thankfully Jess helps pull you under just in time. You take a heavy breath and continue towards the city.")
        town(player1)
    else:
      print("You failed to slide, bumping your head against the log. Thankfully, Jess helps pull you under just in time. You take a heavy breath and continue towards the city.")
      town(player1)
  else:
    print("You and Jess stay completely still, and heavy foosteps announce the departure of the creature after a few minutes. You and Jess sprint towards the city in case it comes back.")
    town(player1)


def town(player1):
  sleep(3)
  print("You and Jess are welcomed by the residents of the city, and across the next few months you learn about how people have been brought here by aliens thousands of years ago, and the 'chosen ones' were brought to the Protocol, where they could fight against the 'Chaos'. Whatever that is.")
  sleep(5)
  print("~DAY ONE~")
  print("One particular day, Jess enters your room, holding some kind of ancient map. 'I've found us a way, no, ways, we could use to reach the summit! We can finally see if all the myths are true: Immortality lies at the Summit of Chaos.'")
  print("You stifle a laugh. 'We're NOT going mythbusting, Jess.' 'Yes, we are! It'll be a breeze. I doubt there will even be as many monsters as the run we did in the Ravine. C'mon!'")
  d=input("1.Fine. 2.Fine.")
  print("'Fine. Good to take on that immortality myth, I guess. Who knows, maybe it IS real.' 'That's the spirit! Go get yourself a secondary weapon from the armory. We'll leave at dawn tomorrow.'")
  sleep(3)
  print("You sigh, and head off to the armory.")
  e=input("1.Get a bow. 2.Get a pistol. 3.Get a second dagger. 4.Get an axe.")
  if e =="1":
    bow = True
    print("You add a bow to your arsenal as a {secondary weapon}.")
  elif e=="2":
    pistol = True
    print("You add a pistol to your arsenal as a {secondary weapon}.")
  elif e=="3":
    dagger2 = True
    print("You add a second dagger to your arsenal as a {secondary weapon}.")
  else:
    axe = True
    print("You add an axe to your arsenal as a {secondary weapon}.")
  sleep(3)
  print("You go back home to have a good night's sleep, and the next day, you and Jess are fully equipped and ready to take on the Summit of Chaos. You take a look at Jess's ancient map. 'Hmm... let's see...'")
  f=input("1.Go through the Jungle. 2.Go through the red desert. 3.Go through a monster city.")
  if f =="1":
    jungleRuins(player1)
  elif f =="2":
    redDesert(player1)
  else:
    monsterCity(player1)

def jungleRuins(player1):
  pass

def redDesert(player1):
  pass

def monsterCity(player1):
  pass