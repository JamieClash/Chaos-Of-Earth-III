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
  dreamTeam3(player1)

def dreamTeam3(player1):
  print("\nPATH SELECTED - IN ANOTHER WORLD\n")
  sleep(4)
  print("~DAY ONE~")
  print("You've finally arrived at the exoplanet you saw a few days back. You get yourself a safe landing, and you get out of your spaceship, looking around for any immediate threats. You look back at the ship, reminiscing your good friend, who helped you escape Earth and most of Crivex X. You take a deep breath and head into the forest.")
  sleep(5)
  print("Suddenly, you hear a twig snap behind you, and a deep screech.")
  a=input("1.Stand still. 2.Move more slowly. 3.Make a run for it. 4.Throw something away to distract whatever it is.")
  if a =="1":
    print("You stand completely still, and you hear heavy foosteps that belong to some sort of creature. You remain still for a few more minutes, when the creature's footsteps announce its departure.")
    b=input("1.Run. 2.Start moving slowly. 3.Continue standing still.")
    if b =="1":
      print("You make a run for it, and a hideous monster emerges from the trees, chasing after you. You see a narrow gap up ahead that you can squeeze through and lose the monster.")
      sleep(5)
      st=time.time()
      c=input("PRESS [S] to squeeze through!").title()
      rt = time.time()-st
      if c =="S":
        if rt<2:
          print("You squeeze through the gap perfectly, and leave the creature in the dust. You gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
          town(player1)
        else:
          print("You barely manage to make it through after timing it incorrectly, but you gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
          town(player1)
      else:
        print("You miss the gap the first time, but you scrmable your way into fitting through the gap just in time as the monster runs into the barrier and gives up its prey. You turn around, and you gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
      town(player1)
    elif b =="2":
      print("You start moving slowly, and you spot a smoke up ahead. You make your way towards it without making any sound. You arrive, and you gasp in awe as you find yourself staring at a functional city, filled to the brim with humans. You make your way into it.")
      town(player1)
    else:
      print("You continue to stand still, and you confirm that there is nothing left after a few more minutes. You see a smoke up ahead and head towards it. You arrive, and you gasp in awe as you find yourself staring at a functional city, filled to the brim with humans. You take a deep breath and enter.")
      town(player1)
      
  elif a =="2":
    print("You start moving slowly, and you spot smoke up ahead. Please don't be more aliens. You hope.")
    b=input("1.Run to the smoke. 2.Keep sneaking towards it. 3.Stop and listen for the creature's footsteps.")
    if b =="1":
      print("You make a run for it, and a hideous monster emerges from the trees, chasing after you. You see a narrow gap up ahead that you can squeeze through and lose the monster.")
      sleep(5)
      st=time.time()
      c=input("PRESS [S] to squeeze through!").title()
      rt = time.time()-st
      if c =="S":
        if rt<2:
          print("You squeeze through the gap perfectly, and leave the creature in the dust. You gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
          town(player1)
        else:
          print("You barely manage to make it through after timing it incorrectly, but you gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
          town(player1)
      else:
        print("You miss the gap the first time, but you scrmable your way into fitting through the gap just in time as the monster runs into the barrier and gives up its prey. You turn around, and you gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
      town(player1)
    elif b =="2":
      print("You continue moving slowly towards the smoke. You don't make any sound. You arrive, and you gasp in awe as you find yourself staring at a functional city, filled to the brim with humans. You make your way into it.")
      town(player1)
    else:
      print("You stop moving, and you confirm that there is nothing left after a standing for a few minutes. You continue heading towards the smoke. You arrive, and you gasp in awe as you find yourself staring at a functional city, filled to the brim with humans. You take a deep breath and enter.")
      town(player1)
      
  elif a =="3":
    print("You make a run for it, and a hideous monster emerges from the trees, chasing after you. You see a narrow gap up ahead that you can squeeze through and lose the monster.")
    sleep(5)
    st=time.time()
    b=input("PRESS [S] to squeeze through!").title()
    rt = time.time()-st
    if b =="S":
      if rt<2:
        print("You squeeze through the gap perfectly, and leave the creature in the dust. You gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
        town(player1)
      else:
        print("You barely manage to make it through after timing it incorrectly, but you gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
        town(player1)
    else:
      print("You miss the gap the first time, but you scrmable your way into fitting through the gap just in time as the monster runs into the barrier and gives up its prey. You turn around, and you gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
      town(player1)
  else:
    print("You throw an object into the trees, triggering a response from some sort of creature. You identify some sort of smoke up ahead, and you decide to make a run for it.")
    print("A hideous monster emerges from the trees, chasing after you. You see a narrow gap up ahead that you can squeeze through and lose the monster.")
    sleep(5)
    st=time.time()
    b=input("PRESS [S] to squeeze through!").title()
    rt = time.time()-st
    if b =="S":
      if rt<2:
        print("You squeeze through the gap perfectly, and leave the creature in the dust. You gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
        town(player1)
      else:
        print("You barely manage to make it through after timing it incorrectly, but you gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
        town(player1)
    else:
      print("You miss the gap the first time, but you scrmable your way into fitting through the gap just in time as the monster runs into the barrier and gives up its prey. You turn around, and you gasp in awe as you take in the scenery you see before you - a beautiful, functioning city, filled with people. Humans. You head into the town.")
      town(player1)


def town(player1):
  sleep(5)
  print("You are immediately greeted by the people of the city. They ask you if you're from another city, which makes you wonder how many cities there are in this place, but you just nod and keep on walking around. Someone pulls you into a building.")
  sleep(3)
  print("You struggle, but you stop when you realize that you are not being attacked. You find a woman sitting behind a desk that says 'Protocol'. 'Who are you?' You ask.")
  print("'Jess, isn't it? I am here on behalf of Protocol, to hire you to retrieve something from the Summit of Chaos.''")
  sleep(3)
  print("'I'm not getting hired by no one. How do you know my name!?'")
  print("'We've been following your progress, Jess. Since Earth to Crivex X to here, new Earth. We know what you are capable of. Take on this mission, and should you succeed, your fallen friend may return from the clutches of death.'")
  print("'What?' You ask.")
  print("The woman hands you a file and a guard opens the door behind you. 'Everything you need is in that file. Head over to the armory, get yourself some gear. We expect excellence from you.'")
  sleep(5)
  d=input("1.Accept the job. 2.Accept the job.")
  print("You head on over to the armory after reading the file. You seem to need to travel to the highest summit in a nearby mountain range and gather some sort of crystal, capable of granting immortality. You are unsure of that information, but it IS a chance to bring back your fallen friend, whose body is still in Crivex X. You take a deep breath, and walk through the doors of the armory.")
  sleep(5)
  print("You find a few things that you may find helpful, but you can only carry one.")
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
  print("After that, you head to a Protocol residential building and have a good night's sleep after a much needed shower.")
  sleep(3)
  print("The next day, you bring out your map and prepare to choose a route for your journey. 'Hmm...Where should I go?'")
  f=input("1.Abandoned Monster village. 2.Desert Monster village.")
  if f =="1":
    abandonedVillage(player1)
  else:
    desertVillage(player1)

def abandonedVillage(player1):
  pass

def desertVillage(player1):
  pass