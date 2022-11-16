import time 
import player
from time import sleep

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
  stranger2(player1)

def stranger2(player1):
  print("\nPATH SELECTED - SQUAD 3-36-A\n")
  sleep(4)
  print("~ PROTOCOL ~")
  print("~DAY ONE~")
  print("You widen your eyes as the massive spaceship above you approaches your ship. Cara tries to get the ship running, but the engine is down for some reason.'What do we do?' She asks.")
  a=input("1.Activate emergency thrusters. 2.Get into the escape pod. 3.Accept your fate.")
  if a =="1":
    print("You head over to the engines console to activate the emergency thrusters, but it is unresponsive.")
  elif a =="2":
    print("You and Cara run over to the escape pod and try to get it running, but it doesn't seem to have any power. You make your way back to the front of the ship.")
  print("The massive ship comes to a stop and starts to beam your ship up into it.")
  sleep(3)
  print("You and Cara gasp as your ship enters the massive ship. It is brightly lit in white light, and there are many spaceships littered across the area. This must be some sort of hangar.")
  sleep(3)
  print("A few guards start heading towards you and Cara and your ship door suddenly opens. The guards keep walking towards you. They may be armed.")
  b=input("1.Make a run for it. 2.Try to close the door. 3.Attack the guards.")
  if b =="3":
    print("You and Cara charge at the guards, but unfortunately they ARE armed and they shoot you both in the head before you can even punch them. YOU DIED! THE END!")
    stranger2(player1)
  elif b =="1":
    print("You and Cara try to run away, but the guards catch up easily as you have no idea where to run. They grab the two of you and drag you off.")
    office(player1)
  else:
    print("You try to close the ship's door, but once again the ship doesn't seem to have any power. The guards grab you and drag you away.")
    office(player1)

def office(player1):
  print("The guards bring you and Cara into some sort of office. A man in a suit sat at the other side of the desk in the room. 'Take a seat.'")
  print("Since the guards are still here, you do as the man says. The man dismisses the guards and tells them to lock the door behind them. You hear a click on the door to confirm that it is locked.")
  sleep(3)
  c=input("1.Attack the man. 2.Do not attack the man.")
  if c =="1":
    print("You and Cara attack the man, but your punch goes straight through the man's form as if he isn't there. 'What the hell!?' Cara frowns at the man. 'I'm a hologram. And a test. A test that you just failed.' The man announces.")
    sleep(3)
    print("The man's form vanishes and suddenly your bodies are covered in lasers. All the guns fire at the same time. YOU DIED! THE END!")
    stranger2(player1)
  else:
    print("The man continues, 'I am representing the Protocol here. Protocol wishes to hire the two of you for a retrieval mission; There is a legendary substance that lies in the Summit of Chaos in New Earth. We need you to get it for us.'")
    sleep(5)
    print("'We're not doing anything for- ' Cara starts to shout but you calm her down. 'Please, continue.'")
    print("The man nods. 'If you agree to help us, your lives will be spared.'")
    d=input("1.Accept. 2.Accept")
    print("'Excellent! You will be SQUAD 3-36-A.' The door behind you unlocks with a click. The man smiles. 'Get to the armory and get some gear. You leave tomorrow at dawn.'")
    print("The guards return to the office and escort the two of you to the armory.")
    sleep(3)
    print("You and Cara each pick up a rifle and a knife, but you have room for one secondary weapon.")
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
    print("You and Cara head over to your assigned quarters for the night.")
    sleep(3)
    print("After a good night's sleep, you and Cara head over to the Drop Pad.")
    print("The man walks over and beams at you. 'Good luck! The Protocol's battle against Chaos starts with you!'")
    print("You frown. 'Battle agsint-' The guard interrupts you. 'Where are you landing?'")
    sleep(3)
    print("He reveals to you a map with various paths leading towards the Summit of Chaos.")
    print("'Hmmm....'")
    f=input("1.Drop onto the desert riddled with chasms. 2.Drop into a mountain range with floating peaks. 3.Drop into a dried up ocean.")
    if f =="1":
      brokenDesert(player1)
    elif f =="2":
      brokenMountains(player1)
    else:
      brokenOcean(player1)

def brokenDesert(player1):
  pass

def brokenMountains(player1):
  pass

def brokenOcean(player1):
  pass