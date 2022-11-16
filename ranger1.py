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
  ranger1(player1)

def ranger1(player1):
  print("\nPATH SELECTED - RANGER 462\n")
  sleep(4)
  print("~ PROTOCOL ~")
  print("~DAY ONE~")
  print("The massive ship above you disables your ship's functions and starts beaming you up. The Ranger tells you to calm down. 'It's just the Protocol, the ones who hired me to save you.'")
  print("Your ship is now inside the massive spaceship and there are people all over the place. Humans. You gasp. There are still humans left in this universe!")
  sleep(5)
  print("The doors open and the Ranger steps out. 'Come on. it's time for our next mission.'")
  a=input("1.Follow the Ranger. 2.Stay in the ship.")
  if a =="2":
    print("You stay in the ship, unsure of whether to follow the Ranger to his next 'mission'.")
    print("'Come on! We don't have all day!'")
    b=input("1.Follow the ranger. 2.Stay in the ship.")
    if b =="2":
      print("The other people in the ship see this as a resistance to orders, and they immediately shoot you. YOU DIED! THE END!")
      ranger1(player1)

  print("You follow the Ranger and walk through the massive spaceship, offices are everywhere and people are moving in and out of all of them.")
  print("The Ranger leads you into one of these offices.")
  sleep(3)
  print("Both of you sit down at a desk. A man is sat on the other end. 'Welcome, Ranger 461 and your recruit. Are you ready for your next mission?'")
  b=input("1.Yes. 2.Yes.")
  print("'Excellent. The Protocol will task the two of you on a retrieval mission in New Earth. You are to collect a legendary substance from the Summit of Chaos, and give it to us.'")
  c=input("1.'Summit of Chaos?' 2.'What substance?' 3.'New Earth?' 4.'Why us?'")
  if c =="1":
    print("'The Summit of Chaos is where Chaos first emerged, and broke through Order. It has wrought tragedy and death wherever it goes. However, you two will handle it just fine.'")
    d=input("1.'Chaos?' 2.'Order?' 3.'What tragedy and death?'")
    if d =="1":
      print("'Chaos is all around us. It seeks disorder. Uncertainty. Probability. It causes all the terrible things that happen all around us.'")
    elif d =="2":
      print("'Order keeps things intact. Beautiful. Untouched by Chaos. Deterministic.'")
    else:
      print("All tragedy and deaths originate from Chaos. For example, famines. Wars. Death itself.")
  elif c =="2":
    print("'You may call it the elixir of life. It grants eternal life, and we need it to find a way to combat against Chaos itself.'")
    d=input("1.'Eternal life?' 2.'Combat against Chaos?'")
    if d =="1":
      print("'Yes. Immortality. The fragile lifelines of the body will be rendered gone from the consumption of the substance.'")
    else:
      print("'That is our holy mission. To bring back Order, and to remove Chaos completely. Bring everything back to the way it was. Before the Emergence.'")
  elif c =="3":
    print("'New Earth is the planet where the first aliens brought the Original Rangers. Humans live on that planet now, along with the unholy beasts.'")
    d=input("1.'Humans?' 2.'Original Rangers?' 3.'Unholy beasts?'")
    if d =="1":
      print("'Yes. Humans have been living there for thousands of years, accomplishing achievements at the same rate as the humans from your earth.'")
    elif d =="2":
      print("'They were the original Rangers, chosen by the founders of Protocol. They were part of the many humans they extracted from earth and moved to New Earth.'")
    else:
      print("'They have powerful hearing, terrible screeches and immense strength. Their hideous faces are the result of Chaos itself.'")
  else:
    print("'We saw how you and Ranger 461 survived Earth and Crivex X. The two of you are a very effective team. We need your powerful teamwork to retrieve the substance.'")
  sleep(3)
  print("'All right. You shall be known as Ranger 462 from now on. Welcome to the Protocol.'")
  sleep(3)
  print("'Rangers, head to the armory and gather your gear. You shall leave at dawn tomorrow.'")
  print("You and the Ranger are dismissed and you head over to the armory, where you got a knife and a rifle. 'Grab a secondary weapon, Ranger 462.' the Ranger tells you.")
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
  print("You and the Ranger head to your assigned quarters and have a good night's sleep.")
  print("The next morning, you and the Ranger head towards the drop pad. 'Where are we headed?' The Ranger asks you, presenting a range of landing options.")
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