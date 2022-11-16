import time 
import player
from time import sleep

global grenades
grenades = False
global amuletOfLife
amuletOfLife = False
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
  dreamTeam2(player1)

def dreamTeam2(player1):
  print("\nPATH SELECTED - SQUAD 4-96-D\n")
  sleep(4)
  print("~ PROTOCOL ~")
  print("~DAY ONE~")
  print("You look up at the shadow and find an absolutely massive spaceship hovering over you. Jess reaches for the gun, but she passes out. Confused, you, too reach for the gun. Everything suddenly starts spinning, and you pass out too.")
  sleep(5)
  print("You wake up in some sort of brightly lit room. You don't see Jess anywhere. You look down and discover that your clothes have been changed. 'What on earth-'")
  print("A human person opens the door, and grabs you. 'Come with me.'")
  sleep(5)
  st=time.time()
  a=input("PRESS [B] to break free!").upper()
  rt=time.time()-st
  if a =="B":
    if rt<2:
      print("You break free from the person's grasp, and disarm them in the blink of an eye.")
      b=input("1.Threaten them. 2.Knock them out. 3.Run away. 4.Kill them.")
      if b =="1":
        print("You point the gun at the guard's head, and threaten to shoot. Other guards arrive and a man laughs. 'You are exactly what I hoped for. Come, guards, drop your weapons. I want a chat with our friend here.' Intruiged, you follow the man. You hand over the gun, since you definitely can't fight past them.")
      elif b =="2":
        print("You knock the guard out, and several other guards show up. A man laughs. 'You are exactly what I hoped for. Come, guards, drop your weapons. I want a chat with our friend here.' Intruiged, you follow the man. You hand over the gun, since you definitely can't fight past them.")
      elif b =="3":
        print("You attempt to run away, but you run straight into a bunch of guards. They grab you and drag you into some sort of an office, where a man sat at a desk, menacingly.")
      else:
        print("You shoot the guard in the head, which triggers the nearby guards to arrive. You put up a good fight, but there are too many of them. As you are bleeing out, a man stands over you. 'Ah, shame. You had so much potential. Get the girl. Kill her.'")
        print("YOU DIED! THE END!")
        dreamTeam2(player1)
    else:
      print("You try to struggle, but the guard keeps dragging you. You arrive in an office, where a man sat at a desk, menacingly.")
  else:
    print("You miss your window of opportunity and the guard drags you into some sort of office, where a man sat at a desk menacingly.")

  print("'There you are. You know, we're very excited to have you here! Your experience, your potential for greatness- We've seen your work! On Earth, Crivex X- you and Jess are quite the duo!'")
  sleep(5)
  print("'I won't do anything you want. Might as well kill me.'")
  print("'No, no, no. You have this all wrong! We want to hire you... To extract a legendary substance...capable of granting immortality, and maybe an end to all this, ah...Chaos.'")
  print("Another guard brings Jess into the room. She seems fine, despite having a scowl on her face.")
  print("'Will you accept our offer?' The man smiles.")
  c=input("1.Accept. 2.Accept.")
  print("'Excellent! Rangers - assign them to Squad 4-96-D, and standard-issue rifles. Bring them to the armory for their secondary weapon of choice.'")
  sleep(3)
  print("The guards grab you and escort you to the armory, where they gave you a rifle and a knife. They give you a selection of secondary weapons to choose from.")
  d=input("1.Get a bow. 2.Get a pistol. 3.Get a second dagger. 4.Get an axe.")
  if d =="1":
    bow = True
    print("You add a bow to your arsenal as a {secondary weapon}.")
  elif d=="2":
    pistol = True
    print("You add a pistol to your arsenal as a {secondary weapon}.")
  elif d=="3":
    dagger2 = True
    print("You add a second dagger to your arsenal as a {secondary weapon}.")
  else:
    axe = True
    print("You add an axe to your arsenal as a {secondary weapon}.")
  sleep(3)
  print("They assign you to your quarters for the night, and you will leave first thing tomorrow morning.")
  print("Jess sighs. 'Do you think they're telling the truth? About the immortality?'")
  print("'I don't know. We definitely can't overpower them though, and they'll probably be watching us the entire time. We'll find out one way or another.'")
  print("'Goodnight.' 'Goodnight.'")
  sleep(5)
  print("'Alright, Squad 4-96-D, you have three landing locations to choose from, whichever may suit your needs the most to reach the Summit. Are you ready?'")
  e=input("1.Yes. 2.Yes.")
  print("'That's what I like to hear! Alright, where are you landing?'")
  print("You look at Jess. She shrugs. 'This planet looks beautiful, but I have no idea where we are going. You pick.'")
  f=input("1.Volcanic badlands. 2.Glaciers. 3.Mountain range.")
  if f =="1":
    volcanoBadlands(player1)
  elif f =="2":
    glacierRuins(player1)
  else:
    mountains(player1)

def volcanoBadlands(player1):
  pass

def glacierRuins(player1):
  pass

def mountains(player1):
  pass