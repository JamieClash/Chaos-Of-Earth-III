from time import sleep
import time 
import player

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
  alone3(player1)

def alone3(player1):
  print("\nPATH SELECTED - HERO OF THE VILLAGE\n")
  sleep(4)
  print("~DAY ONE~")
  print("The spaceship finally finds an exoplanet after weeks of aimless travel, but you let out a sigh of relief when the ship lands and you take in its beautiful scenery. 'Hey! Stay with me!' The new leader, Mike, shouts as the villagers try to navigate themselves around the planet.")
  sleep(3)
  print("'There's smoke over there!' Someone yells back. Mike checks the direction and spots the smoke. 'Alright! Let's head towards it. Hopefully they're not more aliens. Guns at the ready!'")
  print("You bring out your rifle and follow the rest of the villagers towards the smoke.")
  print("'That's a city!? What is this place?' Mike exclaims, looking ahead, past the trees, where skyscrapers lay. 'Let's head on over! We'll-'")
  sleep(5)
  print("A deep screech stops him in his speech. Something rustles in the bushes.")
  a=input("1.Run. 2.Sneak slowly. 3.Stay completely still. 4.Throw something away to distract it.")
  if a =="1":
    print("'RUN!!!!' Everyone breaks into a run, and horrifying monsters leap out of the bushes, and start chasing after all of you.")
    print("You need to jump over a fallen log up ahead.")
    sleep(5)
    st=time.time()
    b=input("PRESS [J] to jump!").title()
    rt=time.time()-st
    if b=="J":
      if rt < 2:
        print("You jump over the log, and follow everyone else towards the city, where the city gates are opened for you all.")
      else:
        print("You jumped too slowly, and trip over. Someone helps pull you up and you keep on running towards the city.")
    else:
      print("You trip over the log. Someone helps pull you up and you keep on running towards the city.")

    town(player1)
  elif a=="2":
    print("You all start sneaking quietly towards the city. The noises have stopped, but they may still be there.")
    b=input("1.RUN. 2.Keep going. 3.Throw something away to distract them, if they're there. 4.Stop moving.")
    if b =="1":
      print("'RUN!!!!' Everyone breaks into a run, and horrifying monsters leap out of the bushes, and start chasing after all of you.")
      print("You need to jump over a fallen log up ahead.")
      sleep(5)
      st=time.time()
      c=input("PRESS [J] to jump!").title()
      rt=time.time()-st
      if c=="J":
        if rt < 2:
          print("You jump over the log, and follow everyone else towards the city, where the city gates are opened for you all.")
        else:
          print("You jumped too slowly, and trip over. Someone helps pull you up and you keep on running towards the city.")
      else:
        print("You trip over the log. Someone helps pull you up and you keep on running towards the city.")
      town(player1)
    elif b =="2":
      print("You keep on sneaking towards the city, and you trigger no other screeches from the nearby area. You keep on sneaking just in case.")
      town(player1)
    elif b =="3":
      print("You throw an object far away, which triggers some deep screeches, and heavy foosteps leading away from the area.")
      print("'RUN!!!!' Everyone breaks into a run, and horrifying monsters leap out of the bushes, and start chasing after all of you.")
      print("You need to jump over a fallen log up ahead.")
      sleep(5)
      st=time.time()
      c=input("PRESS [J] to jump!").title()
      rt=time.time()-st
      if b=="J":
        if rt < 2:
          print("You jump over the log, and follow everyone else towards the city, where the city gates are opened for you all.")
        else:
          print("You jumped too slowly, and trip over. Someone helps pull you up and you keep on running towards the city.")
      else:
        print("You trip over the log. Someone helps pull you up and you keep on running towards the city.")
      town(player1)
    else:
      print("You stop moving, and after a minute or so, heavy footsteps announce the departure of whatever creature that was hiding in the bushes. You wait for an extra minute just to be sure, and start walking towards the city.")
      town(player1)
      
  elif a =="3":
    print("You all stand completely still, until the sounds stop. However, they may still be here.")
    b=input("1.RUN. 2.Start moving slowly. 3.Throw something away to distract them, if they're there. 4.Continue standing still.")
    if b =="1":
      print("'RUN!!!!' Everyone breaks into a run, and horrifying monsters leap out of the bushes, and start chasing after all of you.")
      print("You need to jump over a fallen log up ahead.")
      sleep(5)
      st=time.time()
      c=input("PRESS [J] to jump!").title()
      rt=time.time()-st
      if c=="J":
        if rt < 2:
          print("You jump over the log, and follow everyone else towards the city, where the city gates are opened for you all.")
        else:
          print("You jumped too slowly, and trip over. Someone helps pull you up and you keep on running towards the city.")
      else:
        print("You trip over the log. Someone helps pull you up and you keep on running towards the city.")
      town(player1)
    elif b =="2":
      print("You start sneaking towards the city, and you trigger no other screeches from the nearby area. You continue sneaking all the way to the city.")
      town(player1)
    elif b =="3":
      print("You throw an object far away, which triggers some deep screeches, and heavy foosteps leading away from the area.")
      print("'RUN!!!!' Everyone breaks into a run, and horrifying monsters leap out of the bushes, and start chasing after all of you.")
      print("You need to jump over a fallen log up ahead.")
      sleep(5)
      st=time.time()
      c=input("PRESS [J] to jump!").title()
      rt=time.time()-st
      if b=="J":
        if rt < 2:
          print("You jump over the log, and follow everyone else towards the city, where the city gates are opened for you all.")
        else:
          print("You jumped too slowly, and trip over. Someone helps pull you up and you keep on running towards the city.")
      else:
        print("You trip over the log. Someone helps pull you up and you keep on running towards the city.")
      town(player1)
    else:
      print("You continue standing still, and after a minute or so, heavy footsteps announce the departure of whatever creature that was hiding in the bushes. You wait for an extra minute just to be sure, and start walking towards the city.")
      town(player1)
  else:
    print("You throw an object far away, which triggers some deep screeches, and heavy foosteps leading away from the area.")
    print("'RUN!!!!' Everyone breaks into a run, and horrifying monsters leap out of the bushes, and start chasing after all of you.")
    print("You need to jump over a fallen log up ahead.")
    sleep(5)
    st=time.time()
    b=input("PRESS [J] to jump!").title()
    rt=time.time()-st
    if b=="J":
      if rt < 2:
        print("You jump over the log, and follow everyone else towards the city, where the city gates are opened for you all.")
      else:
        print("You jumped too slowly, and trip over. Someone helps pull you up and you keep on running towards the city.")
    else:
      print("You trip over the log. Someone helps pull you up and you keep on running towards the city.")

    town(player1)


def town(player1):
  sleep(3)
  print("You make it to the city, and all of you are immediately greeted by the locals, who are, surprisingly, human. They explain that they've been here since aliens chose a lot of people to join their Protocol a few thousand years ago, to fight against Chaos. You shrug it off, but some random woman brings you towards a building, where another woman sat. 'Please, take a seat.'")
  sleep(5)
  print("You take a seat, confused. The woman starts speaking. 'The Protocol have been observing you. Since Earth, and then...Crivex X... We've seen a lot of potential from you, and we would like to offer you a challenge. To reach the summit of the mountain range near here.'")
  print("'Why would I do that? I-'")
  sleep(3)
  print("'Immortality. Eternal life. That is what awaits you, should you choose to accept our challenge.' She says.")
  print("'You can't just GIVE immortality, that stuff isn't real.'")
  print("'It is very real, my friend, and no one has ever survived the journey. But it will be worth it. After all, after all you've been through, climbing a mountain isn't that big of a challenge for you, is it?'")
  d=input("1.Accept. 2.Accept.")
  print("'Excellent! Head over to the armory over there and get yourself geared up! You shall leave tomorrow at dawn.'")
  print("You sigh. What have you gotten yourself into? You find the way to the armory, and take a look around.")
  print("You have enough room for a secondary weapon.")
  sleep(4)
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
  print("You make your way to the village's assigned residential building and have a good night's sleep.")
  print("The next day, you get yourself some extra food, and squint at the rising sun. 'Right...Which way to go?'")
  f=input("1.The mines. 2.A derelict village in the distance. 3.A functioning village in the distance.")
  if f =="1":
    mines(player1)
  elif f =="2":
    abandonedVillage(player1)
  else:
    plainsVillage(player1)

def mines(player1):
  pass

def abandonedVillage(player1):
  pass

def plainsVillage(player1):
  pass