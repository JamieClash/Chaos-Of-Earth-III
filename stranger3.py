import time 
import player
from time import sleep

global khopesh
khopesh = False
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
  stranger3(player1)

def stranger3(player1):
  print("\nPATH SELECTED - SAVIORS OF THE VILLAGE\n")
  sleep(4)
  print("~ ARRIVAL ~")
  print("The ship enters the atmosphere of the exoplanet, and nothing sets on fire.")
  print("Good. After months of drifting in space, lots of the villagers have lost hope. You may have as well.")
  print("But thankfully, Cara spotted the exoplanet out of the corner of her eye about two weeks back, and the systems confirm that it is inhabitable. Everyone rejoiced that day.")
  sleep(3)
  print("The spaceship lands with a shattering thud, and the doors slowly open. The new village leader, Mike, hands you, Cara and several others some rifles. 'Let's clear the area. Can't have these guys dying on us.' You and Cara nod, and you head out into the exoplanet.")
  sleep(3)
  print("It reminds you of earth. A lot. But the biomes scattered across the surface are no joke. Deserts are right next to towering snowy mountains, chasms and ravines bordering a peaceful forest... and the Summit, the peak far off in the distance, so tall that it reaches into the clouds and goes even higher.")
  print("Cara nudges you to stay on task. You nod and continue clearing the landing area.")
  print("Suddenly, you hear a noise behind you in some bushes. Some sort of deep screeching.")
  a=input("1.Don't move. 2.Run. 3.Move slowly. 4.Shoot into the bushes.")
  if a =="4":
    print("You shoot into the bushes, which triggers shrieks from all around you and the villagers. Suddenly, hideous monsters emerge from the trees and massacre all of you. YOU DIED! THE END!")
    stranger3(player1)
  elif a =="3":
    print("You signal for the villagers to move slowly. Mike spots a smoke on the other side of the forest and points it out to you. You nod and everyone slowly heads towards the smoke.")
    sleep(5)
    st = time.time()
    b=input("PRESS [A] to avoid snapping a twig!").title()
    rt = time.time()-st
    if b=="A" and rt<2:
      print("You avoid snapping the twig and continue heading towards the smoke.")
    else:
      print("You snap the twig, which makes a sharp, crunched sound. Nothing reacts to it. 'Whew.' Everyone continues heading towards the smoke.")
    town(player1)
  elif a =="1":
    print("You don't move, and so do the rest of the village. Mike spots a smoke up ahead, and points it out to everyone. You haven't heard another shriek, but you're not sure if it's still there.")
    b=input("1.Run. 2.Start moving slowly. 3.Stay still. 4.Throw something into the distance to distract it.")
    if b =="1":
      print("'RUN!' You yell, and everyone breaks into a run just as hideous monsters emerge from the trees and chase right behind you all.")
      print("You see a tight opening up ahead that can lose the monsters behind you.")
      sleep(6)
      st=time.time()
      c=input("PRESS [S] to squeeze through the opening!").title()
      rt = time.time()-st
      if c =="S" and rt<2:
        print("You squeeze right through and lose the monsters' trail. You and the others head towards the smoke.")
      else:
        print("You failed to go through, but thankfully Cara grabs your arm through the opening and pulls you through just as the monsters arrive. You pant heavily. 'That was close.' You rejoin the others and head towards the smoke.")
      town(player1)
    elif b =="2":
      print("You start moving slowly towards the smoke.")
      sleep(3)
      st = time.time()
      c=input("PRESS [A] to avoid snapping a twig!").title()
      rt = time.time()-st
      if c=="A" and rt<2:
        print("You avoid snapping the twig and continue heading towards the smoke.")
      else:
        print("You snap the twig, which makes a sharp, crunched sound. Nothing reacts to it. 'Whew.' Everyone continues heading towards the smoke.")
      town(player1)
    elif b =="3":
      print("You continue to remain still and heavy footsteps announce the departure of whatever that was there.")
      print("You head towards the smoke.")
      town(player1)
    else:
      print("You throw something into the distance, which draws the attention of whatever that was there. You start heading to the smoke slowly, but suddenly hideous monsters emerge from the trees.")
      print("'RUN!!!' You yell, and everyone breaks into a run as the monsters chase behind you.")
      sleep(5)
      st=time.time()
      c=input("PRESS [S] to squeeze through the opening!").title()
      rt = time.time()-st
      if c =="S" and rt<2:
        print("You squeeze right through and lose the monsters' trail. You and the others head towards the smoke.")
      else:
        print("You failed to go through, but thankfully Cara grabs your arm through the opening and pulls you through just as the monsters arrive. You pant heavily. 'That was close.' You rejoin the others and head towards the smoke.")
      town(player1)
  else:
    print("'RUN!' You yell, and everyone breaks into a run just as hideous monsters emerge from the trees and chase right behind you all.")
    print("'Smoke! There!' Mike yells out, pointing out a smoke up ahead on the other side of the forest.")
    print("Everyone starts heading towards the smoke, but one of the monsters stand in the way.")
    b=input("1.Curve around it. 2.Shoot it. 3.Stab it.")
    if b =="1":
      print("You try to curve around it, but it stands in your way, preventing you from passing. It roars loudly.")
      c=input("1.Shoot it. 2.Stab it.")
      if c =="1":
        print("You shoot at the monster, but your bullets have barely any effect on it. It grabs you in the neck and breaks it in one hand. YOU DIED! THE END!")
        stranger3(player1)
      else:
        print("You stab the monster in the torso with a knife, which pierces through seamlessly and causes it to start bleeding. The monster cries in pain, allowing you to run around it and towards the smoke.")
      town(player1)
    elif b =="2":
      print("You shoot at the monster, but your bullets have barely any effect on it. It grabs you in the neck and breaks it in one hand. YOU DIED! THE END!")
      stranger3(player1)
    else:
      print("You stab the monster in the torso with a knife, which pierces through seamlessly and causes it to start bleeding. The monster cries in pain, allowing you to run around it and towards the smoke.")
      town(player1)
      
def town(player1):
  print("You finally arrive at the source of the smoke. Your jaw drops. 'This is a city!'")
  print("In front of you, a beautiful collection of paths, houses and even buildings can be seen, bustling with... humans!")
  print("'There are humans here!?' Cara exclaims, and she follows the rest of the villagers who have started entering the village.")
  sleep(3)
  print("Mike makes his way to the front of the group and is greeted by some sort of mayor of the city. They start talking, but you and Cara are captivated by the scenery around you. 'I never thought I'd see a city again. One still standing, I mean.' Cara nods. 'Excellent!' Mike shouts. 'We get to stay!' Everyone cheers.")
  sleep(6)
  print("\n-ONE YEAR LATER-\n")
  print("~DAY ONE~")
  print("You attended the usual Protocol talk. 'Fight against Chaos, blah blah blah, bring back Order, blah blah blah.'")
  print("But today something else happens.")
  sleep(4)
  print("The Protocol recruiter walks towards you and hands you a map with some papers. 'You said you wanted proof of our battle? Here it is. You shall see with your own eyes.'")
  print("You take the sheets and the recruiter leaves. You stare down at the papers you have been handed.")
  sleep(3)
  print("You make your way back home and Cara greets you. You bring her over to the table and show her the sheets.")
  print("'Climb the Summit of Chaos... Find the elixir of life? The key to Eternal life.' Cara frowns. 'What is all this?'")
  print("'The Protocol. I said that I didn't believe them, and now they've given me this.' You say. 'Should we do it?' Cara asks. 'This mundane life isn't fitting us very well is it?' You grimace.")
  d=input("1.Let's do it. 2.Let's do it.")
  print("'Let's do it. We'll leave tomorrow at dawn. I'll go get some gear.'")
  print("Cara nods. 'Tomorrow at dawn.'")
  sleep(3)
  print("You make your way to the armory, pick up two rifles and two knives. You have enough room for a secondary weapon.")
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
  print("You make your way back home and have a good night's sleep.")
  print("The next day, you and Cara make your way to the outskirts of town and Cara brings up the map and shows it to you. 'There's a few different routes on this map... which one should we take?'")
  f=input("1.The desert. 2.The sea. 3.The mines.")
  if f =="1":
    pyramid(player1)
  elif f =="2":
    pirates(player1)
  else:
    mines(player1)

def pyramid(player1):
  pass

def pirates(player1):
  pass

def mines(player1):
  pass