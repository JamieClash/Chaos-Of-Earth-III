import time 
from time import sleep
import player

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

#hired by protocol
def die(player1):
  alone1(player1)

def alone1(player1):
  print("\nPATH SELECTED - LONE WOLF\n")
  sleep(4)
  print("~ DAY ONE ~")
  print("You slow down your spaceship when you approach the planet, and you land without any problems. You bring out your rifle, scanning the environment around you. You find an abandoned village a few minutes from your landing area.")
  sleep(3)
  print("Why is there a village in this exoplanet? You ask yourself. More aliens? You hear rustling in some bushes nearby.")
  a=input("1.'Who's there!?'. 2.'Come out!'. 3.Shoot. 4.Say nothing.")
  if a =="3":
    print("You take a shot into the bush, and you hear a pained scream of a child. A bloody limb falls from the cover of the bushes and before you can react, a sniper shot bursts through your heart and your world goes black. YOU DIED! THE END!")
    alone1(player1)
  elif a=="1":
    print("'Who's there!?' You yell out to the bush.")
  elif a =="2":
    print("'Come out!' You shout at the bush.")
  print("A child slowly emerges from the bush. You frown. A human child. How are there humans-")
  print("You are interrupted by an adult male, also human. He regards you with interest and lowers his sniper rifle.")
  sleep(3)
  print("You didn't know what to expect, but you did not expect him to start speaking English.")
  print("'You must be the one. Come with us.'")
  print("You prepare to reply, but suddenly you hear a deep screech of some sort.")
  b=input("1.Run. 2.Slowly turn around. 3.Fight whatever creature it is. 4.Don't move.")
  if b =="2":
    print("You slowly turn around, but you step on a twig accidentally. The sound alerts some sort of disfigured creature which launches itself right on top of you before you have even finished turning. The beast feasts on your flesh. YOU DIED! THE END!")
    alone1(player1)
  elif b =="4":
    print("You don't move, and neither do the humans. You hear heavy footsteps announce the departure of the unknown creature. You and the other two relax. 'Follow me.' The man says. Since you'd rather not have another alien encounter, you follow him.")
    print("He brings you to some sort of city, host of at least a couple thousand people.")
    sleep(5)
    town(player1)
  elif b =="1":
    print("You immediately break into a run, and the man picks up the child and follows suit. 'Turn left here!'")
    sleep(4)
    st=time.time()
    qte=input("PRESS [L] to turn left!").upper()
    rt=time.time()-st
    if qte=="L":
      if rt <2:
        print("You turn left, and you keep on following the man's instructions until you arrive in some sort of city, inhabited by at least a couple thousand people.")
        sleep(3)
        town(player1)
      else:
        print("You trip over a rock, but the man helps you up and eventually you reach some sort of city, with at least a couple thousand people inside.")
        sleep(3)
        town(player1)
    else:
      print("You trip over a rock, but the man helps you up and eventually you reach some sort of city, with at least a couple thousand people inside.")
      sleep(3)
      town(player1)
  else:
    print("You stand your ground, preparing to fight whatever creature it is, but nothing emerges from the bushes. You remain silent like the others and nothing comes. 'Follow me.' The man says. Since you'd rather not have another alien encounter, you follow him.")
    print("He brings you to some sort of city, host of at least a couple thousand people.")
    sleep(5)
    town(player1)

def town(player1):
  print("You let out a gasp of awe, looking around the place. Humans are everywhere. 'Where am I?' You ask the man. The man replies, 'Earth. New Earth. We named it after the old one.'")
  print("'How did you make so much progress? It's only been two years since the outbreak-' 'Humans have been living here for thousands of years, since the Rituans brought their chosen ones here from the pyramid days.' 'You-'")
  sleep(5)
  print("The man interrupts you. 'The Protocol would like to meet you. They are in this building right here. Have a nice day.' And with that, the man took his child and left. You shake your head, and enter the building. You are greeted by a woman.")
  sleep(5)
  print("'Welcome to New Earth! We've been expecting you.'")
  print("'You have?'")
  print("'Yes. We have been looking for a candidate to reach the Summit of Chaos and unlock its hidden secrets!'")
  print("You laugh. 'I'm not doing anything. I-'")
  print("'Immortality. Life eternal. Freedom from all this Chaos.' the woman states.")
  print("'What?' You ask.")
  print("'That is what you'll achieve if you make this journey. We know what you are capable of. We know how you survived in Crivex X.'")
  print("That intruiges you. How did they know about Crivex X?")
  sleep(5)
  c=input("1.Accept. 2.Accept.")
  print("'Excellent. Gather some supplies from the armory, and make your way up the mountains! Good luck!'")
  print("You take a deep breath and head over to the armory.")
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

  print("After that, you go to the community shelter and have a good night's sleep.")
  sleep(3)
  print("The next day, you prepare to set off to the mountains, where the summit lay.")
  e=input("1.Go through the desert. 2.Go through the sea.")
  if e =="1":
    pyramid(player1)
  else:
    pirates(player1)

def pyramid(player1):
  pass

def pirates(player1):
  pass