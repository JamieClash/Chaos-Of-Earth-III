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

def die(player1):
  stranger1(player1)

def stranger1(player1):
  print("\nPATH SELECTED - VICTIMS OF HELL\n")
  sleep(4)
  print("~ ARRIVAL ~")
  print("~DAY ONE~")
  print("After a few weeks of aimless flight, the spaceship has identified a potential inhabitable planet up ahead in your course. 'Cara! I think we finally got a planet!'")
  sleep(3)
  print("'Coming!' Cara puts down the book, which she had been reading a lot since she found it in the ship a week ago in storage. 'Learn anything new about that Mountain of Immortality or whatever?' You tease. Cara giggles. 'It's the Summit of Chaos. The elixir of life is up there. I wonder who wrote the book and left it here though...'")
  sleep(5)
  print("Cara looks towards the window and widens her eyes. 'WATCH OUT!'")
  print("You regain the controls to the ship as you approach the asteroid belt.")
  sleep(5)
  st = time.time()
  a=input("PRESS [D] to dodge an upcoming asteroid!").title()
  rt = time.time()-st
  if a =="D":
    if rt<2:
      print("You barely manage to dodge the asteroid.")
    else:
      print("You dodged too late, and the asteroid smashes against your ship, damaging it.")
  else:
    print("You fail to dodge the asteroid, and it smashes against your ship, damaging it.")

  print("You are just recovering from the first asteroid, but you look ahead and see three more asteroids coming your way.")
  b=input("1.Let Cara drive. 2.You can drive past these. 3.Try to steer out of the belt.")
  if b =="1":
    print("'Cara! You steer! I'll get the emergency thrusters going!' You yell, and immediately get off the seat, heading towards the engines console.")
    sleep(3)
    print("Cara takes control of the ship and she makes a big turn, shaking everything inside the ship. You get the engines console up.")
    c=input("1.Flick the white lever. 2.Swipe up in the touch pad. 3.Swipe down in the touch pad. 4.Press the blue button.")
    if c =="1":
      print("You flick the white lever, and the whole ship shudders. The engines turn off and the console loses control over the ship. Cara screams as an asteroid hurls towards your ship and crashes through the window. The vacuum of space sucks you two out of your ship and you die. THE END!")
    elif c =="4":
      print("You press the blue button, and the ship's front windows start opening. You and Cara are sucked out into space and slam right into an asteroid. YOU DIED! THE END!")
    else:
      print("You swipe on the touch pad, and the emergency thrusters activate immediately. The ship suddenly jerks out of the path of an incoming asteroid and flies straight up.")
      print("Cara breathes heavily as she steers the ship at such a high speed, and after what seems like forever, Cara gets the two of you out of the asteroid belt. You pant heavily.")
      survived(player1)
  elif b =="2":
    print("You continue to take control of the steering, and you call out to Cara to get the emergency thrusters in action. You barely steer away from a massive asteroid, and Cara calls out from the engines console. 'What do I do?'")
    c=input("1.Flick the white lever. 2.Swipe up in the touch pad. 3.Swipe down in the touch pad. 4.Press the blue button.")
    if c =="1":
      print("You tell Cara to flick the white lever, and the whole ship shudders. The engines turn off and the console loses control over the ship. Cara screams as an asteroid hurls towards your ship and crashes through the window. The vacuum of space sucks you two out of your ship and you die. THE END!")
    elif c =="4":
      print("You tell Cara to press the blue button, and the ship's front windows start opening. You and Cara are sucked out into space and slam right into an asteroid. YOU DIED! THE END!")
    else:
      print("You tell Cara to swipe on the touch pad, and the emergency thrusters activate immediately. The ship suddenly jerks out of the path of an incoming asteroid and flies straight up.")
      print("You take a deep breath as the ship accelerates upwards and you make sudden turns to avoid the incoming asteroids. After what seems like forever, you finally make it out of the belt. You sigh.")
      survived(player1)
  else:
    print("You try to steer your way out of the asteroid belt, but there are too many asteroids. One slams into your ship's front window and the two of you are sucked out into space. YOU DIED! THE END!")



def survived(player1):
  sleep(3)
  print("'That was close.' You say. 'Yeah...'")
  print("Cara gasps at something through the wide window. You walk up to her and peer through the window yourself.")
  print("You see a magnificent spacescape, with bright and colorful stars far in the distance. But you see what has caught Cara's eye. It's right in front of you.")
  sleep(5)
  print("'The Exoplanet, New Earth.' She says quietly. You frown. 'Isn't that where the Summit of Cookies-'")
  print("'-Chaos. Summit of Chaos...' Her voice falters.")
  print("'It's all real?' You ask Cara, who still seems to be lost in wonder of discovering the planet from her book.")
  print("Cara finally draws her eyes away from the window. 'We have to find out. Please.'")
  d=input("1.Alright. 2.Fine.")
  print("Cara lightens up and thanks you. 'Get your gear together, then! We've got an exoplanet to explore!'")
  sleep(3)
  print("You head over to the armory to gather some weapons. You get a rifle and a knife, but you have room for a secondary weapon. What will you get?")
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
  print("You head to your quarters and have a good night's sleep.")
  print("The next day, you head towards the steering console and find that Cara is already driving you towards New Earth. 'I've identified the Summit! There are two places I think our ship will remain untouched in. Where should we land?'")
  f=input("1.Flower forest. 2.Hills.")
  if f =="1":
    flowerForest(player1)
  else:
    hillsVillage(player1)


def flowerForest(player1):
  pass

def hillsVillage(player1):
  pass