import time 
import player
from time import sleep

global grenades
grenades = False
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

#hired by protocol
def die(player1):
  ranger2(player1)
  
def ranger2(player1):
  print("\nPATH SELECTED - LOOSE CANNON\n")
  sleep(4)
  print("~ PROTOCOL ~")
  print("~DAY ONE~")
  print("You look up, and find the source of the massive shadow. A massive spaceship, bigger than yours at least a hundred times.")
  print("You remain calm when the radio picks up a signal, and someone speaks through it.")
  sleep(3)
  print("'You must be Ranger 461's candidate! Let us beam you up.'")
  a=input("1.Let them do it. 2.Say no. 3.Shoot at the massive ship. 4.Drive the ship away.")
  if a =="1":
    print("You stand by and wait as the massive ship beams your ship into it. You are briefly blinded by a white light, and your eyes slowly adjust and you find yourself in a hangar, filled with many other ships of your size. Your ship doors open, and you are greeted by some humans.")
    sleep(5)
    ship(player1)
  elif a =="2":
    print("Someone chuckles in the radio, and they beam you up anyways. You are briefly blinded by a white light, and your eyes slowly adjust and you find yourself in a hangar, filled with many other ships of your size. Your ship doors open, and you are greeted by some humans.")
    sleep(5)
    ship(player1)
  elif a =="3":
    print("You open fire onto the massive ship, but it has some kind of shield protecting it. No damage is done, but the massive ship returns fire. Your ship is destroyed immediately and you float into eternal space.")
    ranger2(player1)
  else:
    print("You try to drive the ship away, but the controls aren't working. The massive ship proceeds to beam you up. You are briefly blinded by a white light, and your eyes slowly adjust and you find yourself in a hangar, filled with many other ships of your size. Your ship doors open, and you are greeted by some humans.")
    sleep(5)
    ship(player1)

def ship(player1):
  print("They gesture towards a hallway when you step out into the hangar. You look around, taking in the scene completely.")
  b=input("1.Follow them through the hallway. 2.Get back into the ship. 3.Run away. 4.Attack them.")
  if b =="1":
    print("You follow them through the hallway, and they drop you off in an office, where a man sat on a desk. Those who escorted you to this room leave, and lock the door behind them.")
    sleep(3)
    ship2(player1)
  elif b =="2":
    print("You walk back into the ship, but the doors are closed. You have no choice but to follow them now.")
    print("You follow them through the hallway, and they drop you off in an office, where a man sat on a desk. Those who escorted you to this room leave, and lock the door behind them.")
    sleep(3)
    ship2(player1)
  elif  b =="3":
    print("You attempt to run away, but you don't know where you're running to, and you accidentally enter an airlock. Whilst trying to lock the door, you accidentally open it and launch yourself into space. YOU DIED! THE END!")
    ranger2(player1)
  else:
    print("You try to attack the people, but a laser emerges from the walls and fries you alive. YOU DIED! THE END!")
    ranger2(player1)

def ship2(player1):
  print("'Welcome! We've been expecting you.'")
  print("'You abandoned Ranger 461 in your mission in Crivex X, but you survived in your own way. We plan to hire you for a mission in New Earth.'")
  c=input("1.Accept. 2.Accept.")
  print("'Excellent. Your mission is to climb to the Summit of Chaos, and to retrieve the legendary substance from it. Any questions?'")
  d=input("1.'New Earth?' 2.'Summit of Chaos?' 3.'Legendary substance?'")
  if d =="1":
    print("'New Earth is the planet where the first aliens brought the Original Rangers. Humans live on that planet now, along with the unholy beasts. Monsters, those are.'")
  elif d =="2":
    print("'The Summit of Chaos is where Chaos first emerged, and broke through Order. It has wrought tragedy and death wherever it goes. However, you two will handle it just fine.'")
  else:
    print("You might call it the elixir of life. It grants immortal life, protecting its user from the Chaos of death. And we, the Protocol, plan to use it in our mission to defeat Chaos and bring back Order.")
  print("'Head to the armory and gather your gear. You shall leave at dawn tomorrow.'")
  print("You are dismissed and you head over to the armory, where you got a knife and a rifle. You have enough space for a secondary weapon.")
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
  print("You head to your assigned quarters and have a good night's sleep.")
  print("The next morning, you head towards the drop pad. 'Where are you headed?' The pilot asks you, presenting a range of landing options.")
  f=input("1.Desert. 2.Badlands. 3.Snowy Tundra. 4.Plains.")
  if f =="1":
    desert(player1)
  elif f =="2":
    volcanoBadlands(player1)
  elif f =="3":
    tundra(player1)
  else:
    plains(player1)

def desert(player1):
  pass

def volcanoBadlands(player1):
  pass

def tundra(player1):
  pass

def plains(player1):
  pass