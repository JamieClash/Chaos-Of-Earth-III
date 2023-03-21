from time import sleep
import time
from alone1 import alone1
from alone2 import alone2
from alone3 import alone3
from dreamTeam1 import dreamTeam1
from dreamTeam2 import dreamTeam2
from dreamTeam3 import dreamTeam3
from nico1 import nico1
from nico2 import nico2
from nico3 import nico3
from ranger1 import ranger1
from ranger2 import ranger2
from ranger3 import ranger3
from stranger1 import stranger1
from stranger2 import stranger2
from stranger3 import stranger3
from player import *

def setup():
  skill()
  print("\nPick the path you left Crivex X with:")
  print("1.Alone")
  print("2.Dream Team")
  print("3.Stranger")
  print("4.Ranger")
  print("5.Nico")
  path = input("> ")
  if path =="1":
    print("1.Sole survivor")
    print("2.Apprentice")
    print("3.Survived with village")
    p=input(">")
    if p=="1":
      alone1(player1)
    elif p =="2":
      alone2(player1)
    else:
      alone3(player1)
  elif path =="2":
    print("1.Sole survivors")
    print("2.Ominous shadow")
    print("3.Jess")
    p=input(">")
    if p=="1":
      dreamTeam1(player1)
    elif p =="2":
      dreamTeam2(player1)
    else:
      dreamTeam3(player1)
  elif path =="3":
    print("1.Sole survivors")
    print("2.Ominous shadow")
    print("3.Survived with village")
    p=input(">")
    if p=="1":
      stranger1(player1)
    elif p =="2":
      stranger2(player1)
    else:
      stranger3(player1)
  elif path =="4":
    print("1.Sole survivors")
    print("2.Failure to follow instructions")
    print("3.Sole survivor")
    p=input(">")
    if p=="1":
      ranger1(player1)
    elif p =="2":
      ranger2(player1)
    else:
      ranger3(player1)
  else:
    print("1.Sole survivors")
    print("2.Ominous shadow")
    print("3.Survived with village")
    p=input(">")
    if p=="1":
      nico1(player1)
    elif p =="2":
      nico2(player1)
    else:
      nico3(player1)

def tutorial():
  print("\nWelcome to the QTE tutorial.")
  print("\nA quick time event requires you to press a certain key within a time frame. Let's test it out:")
  sleep(2)
  while True:
    sleep(2)
    start_time = time.time()
    qte=input("PRESS [F]!").upper()
    response_time = time.time() - start_time
    if response_time < 1:
      if qte=="F":
        print("Well done!")
        break
      else:
        print("You didn't quite get that. Let's try again!")
    else:
      print("You didn't quite get that. Let's try again!")
  print("\nSome rare events may require key presses within a specific time frame, such as between 1 and 2 seconds. Beware of these. Good luck!")
  sleep(3)
  

def skill():
  print("\nThere are three types of paths you can choose to unlock useful skills to use in your game. Here are the following paths and their skills. Skills in square brackets are a secondary skill extended from the first skill. The first skill must be acquired first.\n")
  sleep(5)
  print("STEALTH PATH")
  print("- Silent Arrows [Craft gun supressors]")
  print("- Undetectable in hiding spots [Undetectable while sneaking around]\n")
  print("SURVIVAL PATH")
  print("- Climb mountains [Climb snowy and icy mountains]")
  print("- Temperature endurance [Quick traversal speeds on all surfaces]\n")
  print("COMBAT PATH")
  print("- Reliably win against one Monster [Reliably win against two Monsters]")
  print("- Dodge Monster attacks [Lethal counter attack while dodging]\n")
  choice = input("What is your path? [stealth/survival/combat]").lower()
  global player1
  if choice =="stealth":
    player1 = player("stealth")
  elif choice =="survival":
    player1 = player("survival")
  else:
    player1 = player("combat")
  player1.newSkill()

player.startGame()
time.sleep(1)
print("Welcome to Chaos of Earth III, the third game in the Chaos of Earth franchise.\n")
tut = input("Would you like to run the quick time event tutorial? [Yes/No]").title()
if tut == "No":
  setup()
else:
  tutorial()
  setup()