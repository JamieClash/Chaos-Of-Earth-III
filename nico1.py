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
  nico1(player1)

def nico1(player1):
  print("\nPATH SELECTED - SURVIVORS\n")
  sleep(4)
  print("~ ARRIVAL ~")
  print("The spaceship enters the exoplanet's atmosphere, and makes the landing without too much trouble. Nico opens the ship's door, and you walk out, rifle raised. You don't find any hostile aliens. You lower your gun. 'It's clear, for now.'")
  print("Nico makes his way out of the ship with his gear. 'I think the evening is coming. Do you think there are any alien settlements here?'")
  sleep(5)
  print("'Well, this place is definitely inhabitable. Let's get a move on.'")
  a=input("1.Walk into the forest. 2.Walk around the forest. 3.Walk through the plains. 4.Walk through the desert.")
  if a =="1":
    print("You and Nico sneak into the forest, careful not to make any sound.")
    print("Nico spots some smoke up ahead, and points it out to you. You nod.")
    print("Suddenly, you hear a deep screech of some sort behind you.")
    b=input("1.Run towards the smoke. 2.Stand still. 3.Walk slowly. 4.Shoot into the bushes.")
    if b =="1":
      print("You and Nico run towards the smoke, and as you approach it you identify that it is a fully functioning city, with people. Humans. Whatever is chasing you from behind is gaining. However, you and Nico can lose it by diving under a fallen tree up ahead.")
      sleep(6)
      st=time.time()
      c=input("PRESS [D] to dive!").title()
      rt = time.time()-st
      if c=="D":
        if rt<2:
          print("You successfully dive under the tree and you lose the monster's trail. You and Nico arrive at the village.")
          town(player1)
        else:
          print("You dive too late and hit your head, but Nico pulls you through just in time. You lose the creature's trail and you head into the city.")
          town(player1)
      else:
        print("You bump your head against the tree, but thankfully Nico pulls you through just in time and you head into the city.")
        town(player1)
    elif b =="2":
      print("You stand completely still, but whatever creature it was has already seen you. It pounces on you two whilst your backs are turned and it bites through your flesh easily. YOU DIED! THE END!")
      nico1(player1)
    elif b =="3":
      print("You walk extremely slowly, but whatever creature it was has already seen you. It pounces on you two whilst your backs are turned and it bites through your flesh easily. YOU DIED! THE END!")
    else:
      print("You shoot into the bushes, and a hideous beast emerges from it, the bullets barely affecting it. Nico joins in to shoot at the thing, and only then the bullets seem to be doing significant damage. The two of you keep spraying down on it until it dies. 'Mags are out. These things are tough!' Nico throws down his gun. You check your magazine, which is also empty. You drop your gun onto the ground.")
      sleep(5)
      print("You head towards the smoke, and discover that it is actually a city. With human people. Intruiged, you head into the city.")
      town(player1)
  elif a =="2":
    print("You walk around the forest, and Nico spots smoke up ahead. Some strange sounds are coming from inside the forest.")
    b=input("1.Check it out. 2.Head towards the smoke.")
    if b =="1":
      print("Slowly, you make your way into the forest to investigate the source of the sound. Suddenly, you hear something behind you, so you turn. You realize that Nico is gone. You turn back to the front, but you see nothing. You feel something grabbing your shoulder, and your vision goes dark. YOU DIED! THE END!")
      nico1(player1)
    else:
      print("You head towards the smoke, and as you approach it you can identify that it is a full on city with humans all over the place. You and Nico swap confused looks. You shrug, and enter the city.")
      town(player1)
  elif a =="3":
    print("You and Nico decide to walk through the plains. You see some sort of wall up ahead, and...electric lights!? You point it out to Nico and he widens his eyes. Suddenly, a deep screech is heard behind you.")
    b=input("1.Turn around and fight. 2.Run away. 3.Stand still.")
    if b =="2":
      print("You and Nico run towards the city, but whatever is chasing behind you is getting closer. You and Nico can lose it by diving under a fallen tree up ahead.")
      sleep(6)
      st=time.time()
      c=input("PRESS [D] to dive!").title()
      rt = time.time()-st
      if c=="D":
        if rt<2:
          print("You successfully dive under the tree and you lose the monster's trail. You and Nico arrive at the village.")
          town(player1)
        else:
          print("You dive too late and hit your head, but Nico pulls you through just in time. You lose the creature's trail and you head into the city.")
          town(player1)
      else:
        print("You bump your head against the tree, but thankfully Nico pulls you through just in time and you head into the city.")
        town(player1)
    elif b =="1":
      print("You turn around and shoot at a hideous beast standing behind you, but the bullets are barely affecting it. Nico joins in to shoot at the thing, and only then the bullets seem to be doing significant damage. The two of you keep spraying down on it until it dies. 'Mags are out. These things are tough!' Nico throws down his gun. You check your magazine, which is also empty. You drop your gun onto the ground.")
      sleep(5)
      print("You head into the city.")
      town(player1)
    else:
      print("You stand completely still, but whatever creature it was has already seen you. It pounces on you two whilst your backs are turned and it bites through your flesh easily. YOU DIED! THE END!")
      nico1(player1)
  else:
    print("You decide to head into the desert, but its conditions are hostile. You are hit by a sandstorm and you are left in the middle of the desert with little resources. YOU DIED! THE END!")
    nico1(player1)

def town(player1):
  sleep(3)
  print("\n-ONE YEAR LATER-\n")
  sleep(2)
  print("~DAY ONE~")
  print("In the past year, you and Nico have remained low profile in the city. You do not engage more than neccessary, and tried to learn more about the planet. You discover that you are on New Earth, with some of the residents having come directly from the space stations in earth, but most of them were descendants of humans brought here by aliens thousands of years ago, to join the Protocol.")
  sleep(5)
  print("What you know about the Protocol is scarce. 'Fight the Chaos'. That's what they do. You consider joining them just to find out, but you don't trust them. One day, Nico returns with an ancient paper map, showing routes on top of it.")
  sleep(3)
  print("'What's this?' You ask. Nico spreads the paper out on a table. 'The Protocol are trying to reach the Summit. I think something they want is up there. This could tell us what they're after! Why they brought humans here, to this planet!'")
  print("'Alright, what do you want us to do?'")
  print("'We climb the mountains.' 'We what?' 'Trust me! This is the key to what the Protocol are doing. Aren't you a bit interested on why humans are here for so long? And how the Protocol is everywhere in this city? And the others?'")
  sleep(5)
  d=input("1.Fine. 2.Fine.")
  print("'Fine.' You answer, and Nico nods excitedly. 'Alright! Let's go then! It's still early in the morning. Grab yourself some gear, and let's head out.'")
  print("You head over to your stuff and grab some food, water, supplies, a rifle and a knife. You have enough space for a secondary weapon.")
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
  print("You make your way outside and join Nico. He shows you a map of the region, and points out two areas on the map. 'Which way are we headed?' He asks.")
  f=input("1.The forest. 2.The Ravine.")
  if f =="1":
    forestVillage(player1)
  else:
    ravine(player1)

def forestVillage(player1):
  pass

def ravine(player1):
  pass