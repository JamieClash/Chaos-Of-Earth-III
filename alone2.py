import time 
from time import sleep
import player

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
  alone2(player1)

def alone2(player1):
  print("\nPATH SELECTED - THE MENTOR\n")
  sleep(4)
  print("~ ARRIVAL ~")
  print("The spaceship carrying the survivors of Crivex X finally arrives on the exoplanet your new apprentice, Haley, spotted on the starmap several weeks back.")
  print("The new village leader, Mike, leads you and the villagers towards a smoke signal he saw in the distance. There are strange sounds coming from the trees around you, but nothing comes out. Haley stays close to you.")
  sleep(5)
  print("'A City! With people! Humans!' Mike shouts, pointing to, what indeed is, a city in the distance. You all start heading towards it, but deep screeches are heard around you.")
  a=input("1.RUN! 2.Stay still. 3.Shoot warning shots into the trees. 4.Walk more silently.")
  if a =="3":
    print("You and some others shoot into the trees, warning the creatures hidden within, but all it does is summon at least five horrifying looking monsters towards your location. They overpower your guns easily and feast upon your flesh. YOU DIED! THE END!")
    alone2(player1)
  elif a=="4":
    print("You walk more silently, but the creatures still manage to find you. They overpower the gunfire and feast upon your flesh. YOU DIED! THE END!")
    alone2(player1)
  elif a =="2":
    print("Everyone stays still, and eventually heavy footsteps announce the departure of the unknown creatures.")
    b=input("1.RUN! 2.STAY.STILL. 3.Start moving quietly. 4.Throw an object elsewhere to distract them, if they're still there.")
    if b =="1":
      print("You break into a run, and half a dozen horrifying creatures emerge from the trees and start chasing you all.")
      print("You need to duck under an incoming branch.")
      sleep(5)
      st=time.time()
      c=input("PRESS [D] to duck!").upper()
      rt= time.time()-st
      if c =="D":
        if rt<2:
          print("You successfully duck under the branch, and follow the rest of the villagers to the city.")
        else:
          print("You dodged too slowly, and you hit your head against the branch. Haley pulls you up and you continue to run towards the city.")
      else:    
        print("You missed the dodge, and you hit your head against the branch. Haley pulls you up and you continue to run towards the city.")
      town(player1)
    elif b =="2":
      print("You stay still for some more time, and you take a step to double check. Nothing happens. You start walking faster and break into a run. The villagers follow suit as nothing comes out.")
      town(player1)
    elif b =="3":
      print("You start moving quietly, which doesn't trigger any response from the creatures. Slowly, you sneak towards the city.")
      town(player1)
    else:
      print("You throw an object elsewhere to distract them, and it works. You hear beasts thrashing towards the direction where you threw the object.")
      print("You all break into a run, and half a dozen horrifying creatures emerge from the trees and start chasing you all.")
      print("You need to duck under an incoming branch.")
      sleep(5)
      st=time.time()
      c=input("PRESS [D] to duck!").upper()
      rt= time.time()-st
      if c =="D":
        if rt<2:
          print("You successfully duck under the branch, and follow the rest of the villagers to the city.")
        else:
          print("You dodged too slowly, and you hit your head against the branch. Haley pulls you up and you continue to run towards the city.")
      else:    
        print("You missed the dodge, and you hit your head against the branch. Haley pulls you up and you continue to run towards the city.")
      town(player1)
  else:
    print("You all break into a run, and half a dozen horrifying creatures emerge from the trees and start chasing you all.")
    print("You need to duck under an incoming branch.")
    sleep(5)
    st=time.time()
    b=input("PRESS [D] to duck!").upper()
    rt= time.time()-st
    if b =="D":
      if rt<2:
        print("You successfully duck under the branch, and follow the rest of the villagers to the city.")
      else:
        print("You dodged too slowly, and you hit your head against the branch. Haley pulls you up and you continue to run towards the city.")
    else:    
      print("You missed the dodge, and you hit your head against the branch. Haley pulls you up and you continue to run towards the city.")
    town(player1)

def town(player1):
  sleep(3)
  print("You arrive at the city, and are greeted by many humans. You look around the place and find at least a couple thousand people here. You continue to look around in awe and take in the beautiful landscape surrounding the city.")
  sleep(4)
  print("The city inhabitants direct you and the villagers to a residential building and Mike thanks them. Haley points to some sort of a temple in the distance, surrounded by spikes on a hill. 'Can we raid that?' 'Sure.' You say.")
  sleep(5)
  print("\n-FIVE YEARS LATER-\n")
  sleep(2)
  print("~DAY ONE~")
  print("Haley bursts into your room, carrying some sort of ancient scroll. You sigh. 'Where do you find this stuff? Just because people have been living here for a couple thousand years doesn't mean their scrolls are everywhere! Did you get that from the Protocol? They are obsessed with stopping some 'Chaos' thing-'")
  print("'Check this out!' Haley shows you the scroll.")
  print("'Reach the summit...embrace, fight, or to escape the Chaos...eternal life...Haley, really, where did you find this?'")
  print("'Don't worry about it! Come on! We have to go! For my sixteenth birthday!'")
  print("You take a deep breath.")
  sleep(5)
  d=input("1.Okay. 2.Okay.")
  print("'Okay. Grab your gun. We leave tomorrow. Still remember how to use it?'")
  print("'Pfft. Yeah. We literally went to that pyramid last month. Full of Monsters.'")
  print("'Alright. Let me head over to the armory and get some stuff.' 'Cool.'")
  print("You head out to the armory.")
  sleep(5)
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

  sleep(4)
  print("You have a good night's sleep and set off the next day. Haley brings out an ancient map. 'These two paths seem to make the most sense. Which one should we take?'")
  f=input("1.Dense jungle. 2.Red Desert.")
  if f =="1":
    jungleRuins(player1)
  else:
    redDesert(player1)

def jungleRuins(player1):
  pass

def redDesert(player1):
  pass
  