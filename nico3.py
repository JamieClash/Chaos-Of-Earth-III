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
  nico3(player1)

def nico3(player1):
  print("\nPATH SELECTED - WAR HEROES\n")
  sleep(4)
  print("~ ARRIVAL ~")
  print("~DAY ONE~")
  print("Your spaceship finally lands after a long journey. Mike, the new leader of the village, leads you and the villagers out of the spaceship, armed with rifles. 'Scan the area, guys! We need to make sure there aren't aliens trying to kill us in this one!'")
  print("All of you start looking around for signs of life, but suddenly Nico spots a smoke in the distance. 'Smoke! We should head towards it. Be careful, there-'")
  sleep(5)
  print("Something snaps a branch in the trees, stopping everyone in their tracks.")
  a=input("1.Run to the smoke. 2.Stand still. 3.Walk to the smoke slowly. 4.Shoot into the trees.")
  if a =="1":
    print("You and everyone else starts running towards the smoke, and several hideous beasts emerge from the trees, close on your tail. There is a crack up ahead which can trip you.")
    sleep(5)
    st=time.time()
    b=input("PRESS [J] to jump over the crack!").title()
    rt = time.time()-st
    if b =="J":
      if rt<2:
        print("You jump over the crack and approach the smoke.")
      else:
        print("You jumped too late, and you tripped over the crack. Nico helps you up and you keep running towards the smoke.")
    else:
      print("You forget to jump, and you trip over. Nico helps you back up quickly and you continue running towards the smoke.")
    town(player1)
  elif a =="2":
    print("All of you stand completely still and make as little noise as possible. After a minute or so, you don't hear anything move in the trees.")
    b=input("1.Run to the smoke. 2.Walk slowly towards the smoke. 3.Continue standing. 4.Throw something into the trees to check if something's there.")
    if b =="1":
      print("You and everyone else starts running towards the smoke, and several hideous beasts emerge from the trees, close on your tail. There is a crack up ahead which can trip you.")
      sleep(5)
      st=time.time()
      c=input("PRESS [J] to jump over the crack!").title()
      rt = time.time()-st
      if c =="J":
        if rt<2:
          print("You jump over the crack and approach the smoke.")
        else:
          print("You jumped too late, and you tripped over the crack. Nico helps you up and you keep running towards the smoke.")
      else:
        print("You forget to jump, and you trip over. Nico helps you back up quickly and you continue running towards the smoke.")
      print("All of you squeeze through a crack that the creatures couldn't go through, towards the smoke. You let out a breath of relief.")
      town(player1)
    elif b =="2":
      print("You start walking slowly towards the smoke, and nothing comes out of the trees. You approach the smoke.")
      town(player1)
    elif b =="3":
      print("You stand for a bit more time, and finally many sets of heavy footsteps announce the departure of a large group of unknown creatures. Slowly, everyone heads towards the smoke.")
      town(player1)
    else:
      print("You throw something into the trees, which triggers many deep screeches from a large number of creatures. 'RUN!'")
      print("You and everyone else starts running towards the smoke, and several hideous beasts emerge from the trees, close on your tail. There is a crack up ahead which can trip you.")
      sleep(5)
      st=time.time()
      c=input("PRESS [J] to jump over the crack!").title()
      rt = time.time()-st
      if c =="J":
        if rt<2:
          print("You jump over the crack and approach the smoke.")
        else:
          print("You jumped too late, and you tripped over the crack. Nico helps you up and you keep running towards the smoke.")
      else:
        print("You forget to jump, and you trip over. Nico helps you back up quickly and you continue running towards the smoke.")
      print("All of you squeeze through a crack that the creatures couldn't go through, towards the smoke. You let out a breath of relief.")
      town(player1)
  elif a =="3":
    print("You all start heading towards the smoke slowly and quietly. Nothing emerges from the trees.")
    b=input("1.Start running to the smoke. 2.Keep moving slowly.")
    if b =="1":
      print("You and everyone else starts running towards the smoke, and several hideous beasts emerge from the trees, close on your tail. There is a crack up ahead which can trip you.")
      sleep(5)
      st=time.time()
      c=input("PRESS [J] to jump over the crack!").title()
      rt = time.time()-st
      if c =="J":
        if rt<2:
          print("You jump over the crack and approach the smoke.")
        else:
          print("You jumped too late, and you tripped over the crack. Nico helps you up and you keep running towards the smoke.")
      else:
        print("You forget to jump, and you trip over. Nico helps you back up quickly and you continue running towards the smoke.")
      print("All of you squeeze through a crack that the creatures couldn't go through, towards the smoke. You let out a breath of relief.")
      town(player1)
    else:
      print("You keep moving slowly, and approach the smoke without triggering any creatures or aliens from the trees.")
      town(player1)
  else:
    print("You shoot into the trees, which trigger a dozen hideous monsters to jump out of the trees' cover and attack you. The bullets aren't doing significant damage to the beasts, and all of you are overrun by them before you could even start running. YOU DIED! THE END!")
    nico3(player1)

def town(player1):
  sleep(3)
  print("'A city!' Mike yells out as you arrive at the source of the smoke. You check behind you, and there is nothing following you. Good.")
  print("You and the villagers arrive at the city, and everyone gasps when they discover that their inhabitants are...human. The city people take you and the villagers in, and assign you all a building dedicated to your village's residence.")
  sleep(5)
  print("'What on earth is this?' You ask Nico. He shrugs. He prepares to reply, but someone grabs him and takes him towards a building. Someone else does the same to you.")
  sleep(3)
  print("The people who grabbed you deposit you into the building and swiftly leave. You and Nico reorient yourselves and see a woman sitting at a desk. 'Hello. I am here on behalf of the Protocol to hire you for a job.'")
  sleep(3)
  print("'We don't need your job! We just got here-'")
  print("The woman ignores you and continues speaking.")
  print("'We've seen your records, what you've done. In Earth, and in Crivex X. You are to reach the Summit of Chaos and retrieve a substance from it, and give it to us. Failure to do so will result in your untimely deaths.'")
  print("Nico looks at you. You look back at Nico.")
  d=input("1.Agree. 2.Agree.")
  print("'Excellent! Make your way to the armory and grab yourselves some gear. Don't try anything. You'll end up dead before anyone in this city believes your stories.'")
  sleep(3)
  print("You and Nico head over to the armory, and pick up a rifle and a knife. Nico whispers, 'How do we get out of this situation?' You sigh. 'We can't. They have all the firepower, all the people. We have to do what they want.' Nico nods. 'Right. Get yourself a secondary weapon. I think they're waiting for us.'")
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
  sleep(3)
  print("You and Nico head out of the armory and the Protocol's guards escort you to outside the city. They hand you a map and leave.")
  print("'Oh boy. Woah, look at this! There's so many ways to go! Which way do we take?'")
  f=input("1.Plains. 2.Red Desert. 3.Flower forest.")
  if f =="1":
    plainsVillage(player1)
  elif f =="2":
    redDesert(player1)
  else:
    flowerForest(player1)

def plainsVillage(player1):
  pass

def redDesert(player1):
  pass

def flowerForest(player1):
  pass
