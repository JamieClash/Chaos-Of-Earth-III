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
  ranger3(player1)

def ranger3(player1):
  print("\nPATH SELECTED - ABANDON SQUAD\n")
  sleep(4)
  print("~ PROTOCOL ~")
  print("~DAY ONE~")
  print("You look up, and find a massive spaceship hovering above you. It starts to beam your ship into it, and it seems like there is nothing you can do.")
  sleep(5)
  st= time.time()
  a=input("PRESS [B] to try to break free!").title()
  rt=time.time()-st
  if a=="B":
    print("You try to break free from the beam, but it is too powerful. You are beamed up anyways.")
  else:
    print("You click the wrong button and nothing happens. You take a deep breath as you are beamed up.")
  sleep(3)
  print("The interior of the ship is filled with bright white light, and once your eyes adapt to the light, you find yourself in a massive hangar, filled to the brim with all sorts of spaceships.")
  sleep(3)
  print("Your spaceship doors open, and you see several armed guards on the other side. 'Please, come with us, candidate.'")
  b=input("1.Go with them. 2.Close the spaceship doors. 3.Attack the guards. 4.Try to run away.")
  if b=="1":
    print("You comply and follow the guards.")
    speak(player1)
  elif b =="2":
    print("You try to shut the spaceship doors, but the controls aren't working. The guards enter your ship and grab you. 'Hey! Let me go!' The guards ignore you and drag you off.")
    speak(player1)
  elif b =="4":
    print("You try to run away, but the guards grab you easily and carry you off.")
    speak(player1)
  else:
    print("You attack the armmed guards, and while you are punching one of them, the other draws their gun and shoots you in the head. YOU DIED! THE END!")
    ranger3(player1)

def speak(player1):
  sleep(3)
  print("They bring you to some sort of fancy office. A man in a black suit sits at the only desk in the room. He gestures for you to sit on one of the chairs.")
  c=input("1.Sit on the left chair. 2.Sit on the middle chair.  3.Sit on the right chair.")
  if c =="1" or c =="3":
    print("'I understand that you are...uneasy, to say the least.' The man stirs his mug of coffee.")
  else:
    print("'Straight to it! Confident. Just what we need.'")
  print("'Ranger 461 believed that you were worth hiring, which is why you are still alive. I believe we can help each other.' He says.")
  d=input("1.'I will never help you!' 2.'How can I help?' 3.'Let me go!'")
  if d =="1":
    print("'I'll never help you!' You shout, and the man nods. 'I see.' He brings out a gun and shoots you in the head. YOU DIED! THE END!")
    ranger3(player1)
  elif d =="2":
    print("'How can we help each other?' You ask.")
    print("The man nods. 'I work for the Protocol. So did the Ranger. We need something from the Summit of Chaos on New Earth, and your survival skills in Earth and Crivex X suggests that you are a prime candidate to retrieve it from the summit.'")
    print("'And I need to live.' You say. The man beams. 'You do! So what's it gonna be?'")
    e=input("1.Accept. 2.Refuse.")
    if e =="1":
      print("'Excellent. Head over to the armory and get yourself some gear. You leave at first light tomorrow.'")
      armory(player1)
    else:
      print("The man nods. He pulls out a gun and shoots you in the head. THE END! YOU DIED!")
      ranger3(player1)
  else:
    print("'Let me go!' You yell at the man. He smirks.'I will...if you retrieve something for me.'")
    e=input("1.'Fine.' 2.'Go to hell!'")
    if e =="1":
      print("'Fine. What do you want?'")
      print("The man smiles. 'I work for the Protocol. So did the Ranger. We need something from the Summit of Chaos on New Earth, and your survival skills in Earth and Crivex X suggests that you are a prime candidate to retrieve it from the summit.'")
      f=input("1.Accept. 2.Refuse.")
      if f =="1":
        print("'Excellent. Head over to the armory and get yourself some gear. You leave at first light tomorrow.'")
        armory(player1)
      else:
        print("The man nods. He pulls out a gun and shoots you in the head. THE END! YOU DIED!")
        ranger3(player1)
      
    else:
      print("'Go to hell!' You shout at the man. The man sighs. 'Such wasted potential...' He pulls out a gun and shoots you in the head. YOU DIED! THE END!")
      ranger3(player1)

def armory(player1):
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