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
  nico2(player1)

def nico2(player1):
  print("\nPATH SELECTED - SQUAD 3-52-C\n")
  sleep(4)
  print("~ PROTOCOL ~")
  print("~DAY ONE~")
  print("You look up and see a massive spaceship hovering over yours. Nico tries to get the ship moving, but the engine has stopped. Your spaceship is slowly rising towards the spaceship, and there is nothing you can do about it.")
  print("A muffled voice tries to speak in the radio, but it doesn't come through. Nico passes out. Confused, you walk towards him, but suddenly your head feels all dizzy. You blink and drop to the ground.")
  sleep(7)
  print("Slowly, you come to. You find you and Nico in some sort of prison cell. You realize you are now inside that massive ship. You nudge Nico awake. 'Woah! Are we in their ship? What is all this?'")
  print("'I don't know. Can't be good, right? They literally just kidnapped us.' Nico nods just as three guards come in. 'Wait...are those people? Humans?' Nico asks you. You prepare to answer, but the guards open the door to your cell and drag you and Nico out. 'Where are you taking us?'")
  sleep(7)
  print("They bring you into another room. An office. A man sat at the desk. He seems intruiged.")
  print("'Ahh...The candidates. We've been expecting you!'")
  a=input("1.'Let us go!' 2.'Why are we here?' 3.'What candidates?' 4.Don't say anything.")
  if a =="1":
    print("'Let us go!' You tell the man in a shaky voice. He smirks. 'Let them go, guards.' The guards stop holding you and you are free to stand. They leave the room and lock the door behind them.")
    b=input("1.Attack the man at the desk. 2.Listen to what he has to say.")
    if b =="1":
      print("You and Nico charge at the man, but your attacks go straight through him. 'He's a hologram!' Nico gasps, and the man's voice is heard in a loudspeaker. 'Yikes. We have chosen wrong. Goodbye.'")
      print("The room fills up with some sort of gas and you try not to breathe, but eventually you breathe it in and you die. YOU DIED! THE END!")
      nico2(player1)
    else:
      print("'We, the Protocol, have been watching you. Our first ancestors were kidnapped by aliens during the building of the pyramids, and we have been living on New Earth ever since. The Protocol aims for one thing, and one thing only. To end the Chaos. That's where you two come in. We need your help.'")
      c=input("1.Attack the man. 2.Keep listening.")
      if c =="1":
        print("You and Nico charge at the man, but your attacks go straight through him. 'He's a hologram!' Nico gasps, and the man's voice is heard in a loudspeaker. 'Yikes. We have chosen wrong. Goodbye.'")
        print("The room fills up with some sort of gas and you try not to breathe, but eventually you breathe it in and you die. YOU DIED! THE END!")
        nico2(player1)
      else:
        print("You and Nico keep listening.")
        print("'On New Earth, there is a summit. The Summit of Chaos. Where Chaos rose from Order from the beginning of time. We need you to extract a substance from the summit. If you can get it, the two of you will be set free. If not, well... It won't end well for you. What's it gonna be?'")
        d=input("1.Alright. 2.Alright.")
        prepare(player1)
  elif a =="2":
    print("'Why are we here?' You ask the man. The man dismisses the guards and they leave the room, locking the door behind them.")
    b=input("1.Attack the man at the desk. 2.Listen to what he has to say.")
    if b =="1":
      print("You and Nico charge at the man, but your attacks go straight through him. 'He's a hologram!' Nico gasps, and the man's voice is heard in a loudspeaker. 'Yikes. We have chosen wrong. Goodbye.'")
      print("The room fills up with some sort of gas and you try not to breathe, but eventually you breathe it in and you die. YOU DIED! THE END!")
      nico2(player1)
    else:
      print("'We, the Protocol, have been monitoring you. Our first ancestors were kidnapped by aliens during the building of the pyramids, and we have been living on New Earth ever since. The Protocol aims for one thing, and one thing only. To end the Chaos. That's where you two come in. We need your help.'")
      c=input("1.Attack the man. 2.Keep listening.")
      if c =="1":
        print("You and Nico charge at the man, but your attacks go straight through him. 'He's a hologram!' Nico gasps, and the man's voice is heard in a loudspeaker. 'Yikes. We have chosen wrong. Goodbye.'")
        print("The room fills up with some sort of gas and you try not to breathe, but eventually you breathe it in and you die. YOU DIED! THE END!")
        nico2(player1)
      else:
        print("You and Nico keep listening.")
        print("'On New Earth, there is a summit. The Summit of Chaos. Where Chaos rose from Order from the beginning of time. We need you to extract a substance from the summit. If you can get it, the two of you will be set free. If not, well... It won't end well for you. What's it gonna be?'")
        d=input("1.Alright. 2.Alright.")
        prepare(player1)
  elif a =="3":
    print("'What candidates?' You ask the man. He dismisses the guards and they leave the room, locking the door behind them.")
    b=input("1.Attack the man at the desk. 2.Listen to what he has to say.")
    if b =="1":
      print("You and Nico charge at the man, but your attacks go straight through him. 'He's a hologram!' Nico gasps, and the man's voice is heard in a loudspeaker. 'Yikes. We have chosen wrong. Goodbye.'")
      print("The room fills up with some sort of gas and you try not to breathe, but eventually you breathe it in and you die. YOU DIED! THE END!")
      nico2(player1)
    else:
      print("'We, the Protocol, have been monitoring you. Our first ancestors were kidnapped by aliens during the building of the pyramids, and we have been living on New Earth ever since. The Protocol aims for one thing, and one thing only. To end the Chaos. That's where you two come in. We have identified you as potential candidates who can help us on our mission. We need your help.'")
      c=input("1.Attack the man. 2.Keep listening.")
      if c =="1":
        print("You and Nico charge at the man, but your attacks go straight through him. 'He's a hologram!' Nico gasps, and the man's voice is heard in a loudspeaker. 'Yikes. We have chosen wrong. Goodbye.'")
        print("The room fills up with some sort of gas and you try not to breathe, but eventually you breathe it in and you die. YOU DIED! THE END!")
        nico2(player1)
      else:
        print("You and Nico keep listening.")
        print("'On New Earth, there is a summit. The Summit of Chaos. Where Chaos rose from Order from the beginning of time. We need you to extract a substance from the summit. If you can get it, the two of you will be set free. If not, well... It won't end well for you. What's it gonna be?'")
        d=input("1.Alright. 2.Alright.")
        prepare(player1)
  else:
    print("The man nods and dismisses the guards. They leave the room and lock it behind them.")
    b=input("1.Attack the man at the desk. 2.Listen to what he has to say.")
    if b =="1":
      print("You and Nico charge at the man, but your attacks go straight through him. 'He's a hologram!' Nico gasps, and the man's voice is heard in a loudspeaker. 'Yikes. We have chosen wrong. Goodbye.'")
      print("The room fills up with some sort of gas and you try not to breathe, but eventually you breathe it in and you die. YOU DIED! THE END!")
      nico2(player1)
    else:
      print("'We, the Protocol, have been watching you. Our first ancestors were kidnapped by aliens during the building of the pyramids, and we have been living on New Earth ever since. The Protocol aims for one thing, and one thing only. To end the Chaos. That's where you two come in. We need your help.'")
      c=input("1.Attack the man. 2.Keep listening.")
      if c =="1":
        print("You and Nico charge at the man, but your attacks go straight through him. 'He's a hologram!' Nico gasps, and the man's voice is heard in a loudspeaker. 'Yikes. We have chosen wrong. Goodbye.'")
        print("The room fills up with some sort of gas and you try not to breathe, but eventually you breathe it in and you die. YOU DIED! THE END!")
        nico2(player1)
      else:
        print("You and Nico keep listening.")
        print("'On New Earth, there is a summit. The Summit of Chaos. Where Chaos rose from Order from the beginning of time. We need you to extract a substance from the summit. If you can get it, the two of you will be set free. If not, well... It won't end well for you. What's it gonna be?'")
        d=input("1.Alright. 2.Alright.")
        prepare(player1)

def prepare(player1):
  print("'Excellent choice.' The office door unlocks with a click.")
  print("'Head towards the armory, and get yourselves armed. You are Squad 3-52-C. Don't try anything, you're not gonna make it off alive if you do. Have fun!'")
  sleep(5)
  print("You and Nico head towards the armory and get a rifle and a knife. 'Hey, do you think it was the right choice, to do what they say?' You ask Nico.")
  print("Nico loads his pistol and puts it in his pocket. 'We didn't really have a choice, did we? We either do this gig for them, or we die. Whatever. Let's get this over with. It's just a mountain, right?'")
  print("'Just a mountain.' You reply.")
  sleep(5)
  print("You have enough room for a secondary weapon.")
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
  print("You follow some guards to the 'drop pad', whatever that is. A guard approaches you and Nico. 'Where are you landing?'")
  f=input("1.Volcanic badlands. 2.Glaciers. 3.A mountain range with jagged and floating peaks.")
  if f =="1":
    volcanoBadlands(player1)
  elif f =="2":
    glacierRuins(player1)
  else:
    brokenMountains(player1)

def volcanoBadlands(player1):
  pass

def glacierRuins(player1):
  pass

def brokenMountains(player1):
  pass