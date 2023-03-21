#ALL SKILL TIER 1
import time
from time import sleep
from player import *

def die(player1):
  pass

def pirates(player1):#Used in 2 scenes. Formatted for ALONE.
  print("The sea is pretty uneventful. You used one of the rental boats by the docks, you just hope that you'd be alive to return it.")
  sleep(3)
  print("You hear a deep sound behind you.")
  a=input("1.Drive faster. 2.Turn around. 3.Duck. 4.Guns-a-blazing.")
  if a =="1":
    print("You drive faster, making a turn just as a cannonball misses your head and smashes hard into the water next to you.")
    print("You glance behind you and see a massive pirate ship. They do not look friendly.")
    print("You turn the boat around just as another cannonball smashes into the water.")
    b=input("1.Turn left. 2.Turn right. 3.Go forwards. 4.Stop the boat.")
    if b =="1":
      print("You turn left, dodging an incoming cannonball completely.")
      print("The ship is gaining on you, and the ocean is as open as ever. You need to find somewhere to outmaneuver their bigger ship.")
      sleep(4)
      print("A cannonball whizzes past your side, and smashes into the water in front of you.")
      print("The water sprays on your face.")
      print("You quickly glance back and find that the ship is really gaining on you.")
      c=input("1.Head to the beach. 2.Head to the rocky shore. 3.Head towards the massive cave embedded in a mountain. 4.Head towards the mountains.")
      if c =="1":
        print("You decide to head towards the beach.")
        sleep(3)
        print("As you approach the beach, you slow down to avoid crashing at the shore.")
        print("However, when you glance behind, the monsters have no intention of stopping.")
        print("They crash into your boat, overturning it and you are launched into the sky, before hitting your head violently against a tree.")
        print("Your head splits open and you can't stop the blood.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You decide to head towards the rocky shore, hoping that the piartes would give up the chase knowing how dangerous the shore could be.")
        print("You slow down as you arrive near the shore, but the pirates have no intention of stopping. They crash into your boat, and you are knocked off the side of it, smashing your head against one of the rocks close to the water surface.")
        print("YOU DIED! THE END!")
      elif c =="3":
        print("You decide to head towards the massive caves.")
        sleep(3)
        print("The pirates are dangerously close to you now, and the caves are still quite far away.")
        d=input("1.Do a sharp U turn and double back. 2.Abandon ship. 3.Try to jump onto their ship. 4.Guns out.")
        if d =="1":
          print("You quickly do a sharp U turn, and the pirates cruise right past you.")
          print("You take this opportunity to drive faster, allowing you some more time to get away from the pirates.")
          sleep(3)
          print("But where to?")
          e=input("1.Through the caves. 2.Into the open sea. 3.To the other set of mountains. 4.To the shore.")
          if e =="1":
            print("You decide to drive your boat through the caves. You hope you can lose them in here.")
            sleep(3)
            print("After a few minutes, the deep sounds of the pirate ship returns.")
            f=input("1.Go forwards. 2.Go left. 3.Go right. 4.Turn off the engine and venture on foot.")
            if f =="1":
              print("You decide to go forwards.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            elif f == "2":
              print("You decide to go left.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You decide to go right.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            else:
              print("You quickly turn off the engine and leave the boat.")
              sleep(5)
              print("You hear the ship drive off in a nearby cave after a while. It looks like you've finally lost them.")
              print("You look around. The dark caves branch off everywhere.")
              print("'Just excellent.' You mutter to yourself.")
              player1.newSkill()
              nextChapter(player1)#####################
          elif e =="2":
            print("You venture into the open sea, which was a grave mistake.")
            print("The long range makes it easier for the pirates to use their cannons, and they hit you in one shot. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start heading towards the other set of mountains, but the pirates are still gaining on you.")
            sleep(3)
            print("A cannonball flies past your side and crashes into the water.")
            print("You notice that there is a gunpowder barrel next to one of the cannons on the ship.")
            f=input("1.Shoot it now. 2.Shoot it after a cannonball. 3.Shoot it after two cannonballs. 4.Shoot it after three cannonballs.")
            if f =="1":
              print("You turn around to shoot the barrel, only to be hit in the head with a cannonball.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You decide to dodge the next cannonball before shooting the barrel.")
              sleep(4)
              print("You successfully dodged the shot.")
              print("You turn around to shoot the barrel, only to be hit in the head with a cannonball.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You dodge two cannonballs in a row, and turn around to make the shot.")
              sleep(4)
              print("Your bullet connects with the gunpowder barrel, and the whole ship blows up before you.")
              print("You smile to yourself and arrive at the base of the mountains.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You decide to dodge the next three cannonballs before shooting the barrel.")
              sleep(4)
              print("You failed to dodge the third cannonball, and you are hit right in the head.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start heading towards the shore, but the shore was farther than you anticipated. The pirate ship saw you and shot your boat down with a cannon, and proceeded to run their ship over you.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to abandon ship, but as you jump out of your boat, the pirate ship crashes right into your boat and you. Your back is broken and you can't do anything as you slowly sink into the bottom of the ocean.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("As the ship gets closer and closer, you ready yourself to jump onto their ship.")
          print("Their ship crashes into your boat, and you take this chance to leap towards their ship, and you manage to hold on to the ledge of the deck.")
          e=input("1.Climb up. 2.Climb somewhere else to climb up to the deck. 3.Wait it out. 4.Let go.")
          if e =="1":
            print("You decide to climb up the deck, only to be surrounded by the pirates on board immediately. They slit your throat with a cutlass.")
            print("YOU DIED! THE END!")
          elif e =="2":
            print("You climb the ledge around the deck, until you find a quieter place to climb up.")
            sleep(4)
            print("You climb onto the deck, and quickly duck behind a barrel to avoid being seen.")
            print("You make a quick peek and identify eight pirates on the ship.")
            print("Who should you shoot at?")
            f=input("1.The three at the cannons. 2.The captain. 3.The one driving. 4.The three on standby with cutlasses.")
            if f =="1":
              print("You spray at the three monsters at the cannons.")
              print("One of your stray bullets pierce into a barrel of gunpowder, which causes a massive chain reaction that blows up the entire ship.")
              sleep(7)
              print("You blink hard, and look around yourself.")
              print("You were washed onto the shore atop a piece of the wreck. There are no monsters in sight.")
              print("You see the mountains ahead of you. You better keep moving.")
              player1.newSkill()
              nextChapter(player1)#####################
            elif f =="2":
              print("You shoot the captain right in the head, causing them to drop their revolver into the sea.")
              print("The crew now realizes that you're here, but you've got the ranged weapon. They only have cutlasses.")
              sleep(6)
              print("It was a massacre. The pirates' bodies litter the deck. You head over to the wheel, only to realize you don't know how to operate it.")
              print("You take one of the dinghies and head to shore, where the mountains await you.")
              player1.newSkill()
              nextChapter(player1)#####################
            elif f =="3":
              print("You shoot the driver dead, which alerts the captain and the crew.")
              print("The captain quickly swings around and draws a revolver, which he uses to embed a bullet into your head.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to shoot the three with the cutlasses, killing all of them.")
              sleep(3)
              print("However, the captain turns around and reveals that he has a revolver. He shoots you in the head before you could even react. YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You hold on to the ledge, and wait it out.")
            sleep(7)
            print("The pirates seem to have given up on searching for your body, and the ship starts moving once again.")
            f=input("1. Stay. 2.Climb onto the deck. 3.Drop into the water.")
            if f =="1":
              print("You stay hanging on the edge of the ship, but one of the pirates saw you while peering over the edge.")
              print("They stabbed you in the head with a cutlass. YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You climb onto the deck, only to face seven monsters wielding cutlasses.")
              sleep(3)
              print("The eighth pirate, the captain, quick draws their revolver and you are shot in the head.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You drop into the water, only occasionally swimming up to the surface to breathe.")
              sleep(6)
              print("After a long time of paranoid swimming, you made it to the shore.")
              print("The mountains lie up ahead. You better start moving.")
              player1.newSkill()
              nextChapter(player1)#####################
          else:
            print("You let go of the ledge, crashing into the water underneath you.")
            sleep(3)
            print("The ship cruises directly onto you.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You get your guns out, but unfortunately, their ship has caught up and they crash right into your face. YOU DIED! THE END!")
          die(player1)
      else:
        print("You decide to head towards the mountains.")
        sleep(5)
        print("The pirates are dangerously close to you now, and the mountains are still quite far away.")
        d=input("1.Do a sharp U turn and double back. 2.Abandon ship. 3.Try to jump onto their ship. 4.Guns out.")
        if d =="1":
          print("You quickly do a sharp U turn, and the pirates cruise right past you.")
          print("You take this opportunity to drive faster, allowing you some more time to get away from the pirates.")
          sleep(3)
          print("But where to?")
          e=input("1.Through the caves. 2.Into the open sea. 3.To the other set of mountains. 4.To the shore.")
          if e =="1":
            print("You decide to drive your boat through the caves. You hope you can lose them in here.")
            sleep(3)
            print("After a few minutes, the deep sounds of the pirate ship returns.")
            f=input("1.Go forwards. 2.Go left. 3.Go right. 4.Turn off the engine and venture on foot.")
            if f =="1":
              print("You decide to go forwards.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            elif f == "2":
              print("You decide to go left.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You decide to go right.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            else:
              print("You quickly turn off the engine and leave the boat.")
              sleep(5)
              print("You hear the ship drive off in a nearby cave after a while. It looks like you've finally lost them.")
              print("You look around. The dark caves branch off everywhere.")
              print("'Just excellent.' You mutter to yourself.")
              player1.newSkill()
              nextChapter(player1)#####################
          elif e =="2":
            print("You venture into the open sea, which was a grave mistake.")
            print("The long range makes it easier for the pirates to use their cannons, and they hit you in one shot. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start heading towards the other set of mountains, but the pirates are still gaining on you.")
            sleep(3)
            print("A cannonball flies past your side and crashes into the water.")
            print("You notice that there is a gunpowder barrel next to one of the cannons on the ship.")
            f=input("1.Shoot it now. 2.Shoot it after a cannonball. 3.Shoot it after two cannonballs. 4.Shoot it after three cannonballs.")
            if f =="1":
              print("You turn around to shoot the barrel, only to be hit in the head with a cannonball.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You decide to dodge the next cannonball before shooting the barrel.")
              sleep(4)
              print("You successfully dodged the shot.")
              print("You turn around to shoot the barrel, only to be hit in the head with a cannonball.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You dodge two cannonballs in a row, and turn around to make the shot.")
              sleep(4)
              print("Your bullet connects with the gunpowder barrel, and the whole ship blows up before you.")
              print("You smile to yourself and arrive at the base of the mountains.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You decide to dodge the next three cannonballs before shooting the barrel.")
              sleep(4)
              print("You failed to dodge the third cannonball, and you are hit right in the head.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start heading towards the shore, but the shore was farther than you anticipated. The pirate ship saw you and shot your boat down with a cannon, and proceeded to run their ship over you.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to abandon ship, but as you jump out of your boat, the pirate ship crashes right into your boat and you. Your back is broken and you can't do anything as you slowly sink into the bottom of the ocean.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("As the ship gets closer and closer, you ready yourself to jump onto their ship.")
          print("Their ship crashes into your boat, and you take this chance to leap towards their ship, and you manage to hold on to the ledge of the deck.")
          e=input("1.Climb up. 2.Climb somewhere else to climb up to the deck. 3.Wait it out. 4.Let go.")
          if e =="1":
            print("You decide to climb up the deck, only to be surrounded by the pirates on board immediately. They slit your throat with a cutlass.")
            print("YOU DIED! THE END!")
          elif e =="2":
            print("You climb the ledge around the deck, until you find a quieter place to climb up.")
            sleep(4)
            print("You climb onto the deck, and quickly duck behind a barrel to avoid being seen.")
            print("You make a quick peek and identify eight pirates on the ship.")
            print("Who should you shoot at?")
            f=input("1.The three at the cannons. 2.The captain. 3.The one driving. 4.The three on standby with cutlasses.")
            if f =="1":
              print("You spray at the three monsters at the cannons.")
              print("One of your stray bullets pierce into a barrel of gunpowder, which causes a massive chain reaction that blows up the entire ship.")
              sleep(7)
              print("You blink hard, and look around yourself.")
              print("You were washed onto the shore atop a piece of the wreck. There are no monsters in sight.")
              print("You see the mountains ahead of you. You better keep moving.")
              player1.newSkill()
              nextChapter(player1)#####################
            elif f =="2":
              print("You shoot the captain right in the head, causing them to drop their revolver into the sea.")
              print("The crew now realizes that you're here, but you've got the ranged weapon. They only have cutlasses.")
              sleep(6)
              print("It was a massacre. The pirates' bodies litter the deck. You head over to the wheel, only to realize you don't know how to operate it.")
              print("You take one of the dinghies and head to shore, where the mountains await you.")
              player1.newSkill()
              nextChapter(player1)#####################
            elif f =="3":
              print("You shoot the driver dead, which alerts the captain and the crew.")
              print("The captain quickly swings around and draws a revolver, which he uses to embed a bullet into your head.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to shoot the three with the cutlasses, killing all of them.")
              sleep(3)
              print("However, the captain turns around and reveals that he has a revolver. He shoots you in the head before you could even react. YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You hold on to the ledge, and wait it out.")
            sleep(7)
            print("The pirates seem to have given up on searching for your body, and the ship starts moving once again.")
            f=input("1. Stay. 2.Climb onto the deck. 3.Drop into the water.")
            if f =="1":
              print("You stay hanging on the edge of the ship, but one of the pirates saw you while peering over the edge.")
              print("They stabbed you in the head with a cutlass. YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You climb onto the deck, only to face seven monsters wielding cutlasses.")
              sleep(3)
              print("The eighth pirate, the captain, quick draws their revolver and you are shot in the head.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You drop into the water, only occasionally swimming up to the surface to breathe.")
              sleep(6)
              print("After a long time of paranoid swimming, you made it to the shore.")
              print("The mountains lie up ahead. You better start moving.")
              player1.newSkill()
              nextChapter(player1)#####################
          else:
            print("You let go of the ledge, crashing into the water underneath you.")
            sleep(3)
            print("The ship cruises directly onto you.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You get your guns out, but unfortunately, their ship has caught up and they crash right into your face. YOU DIED! THE END!")
          die(player1)
    elif b =="2":
      print("You turn right, but the cannonball connects with the ship's side and knocks you overboard.")
      sleep(4)
      print("The ship stops, as if the monsters aboard are looking for you.")
      sleep(3)
      print("You carefully swim towards the back of the ship while they are still looking at the shipwreck.")
      print("You find a ladder and climb on. You see a monster above you.")
      sleep(6)
      st=time.time()
      c=input("PRESS [P] to pull them overboard!").title()
      rt=time.time() - st
      if c =="P" and rt<2:
        print("You pull the monster overboard and successfully make it onto the deck.")
        sleep(4)
        print("You find a cutlass lying against a wall and pick it up.")
        print("Four monsters have seen you. There are eight on the ship.")
        d=input("1.Take the fight. 2.Run down to the hull. 3.Take the high ground. 4.Cut the rope next to you.")
        if d =="1":
          print("You decide to take the fight against the four monsters.")
          sleep(3)
          print("It did not end well.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You decide to make a run for the hull, where you find barrels of gunpowder all over the place.")
          e=input("1.Run back the way you came. 2.Run to the other end of the hull. 3.Take the fight. 4.Shoot the barrels.")
          if e=="1":
            print("You decide to run back the way you came, only to run back towards the four monsters chasing you.")
            print("You stood no chance. YOU DIED! THE END!")
            die(player1)
          elif e =="2":
            print("You quickly run towards the other side of the hull.")
            print("There is no way out on this side either.")
            f=input("1.Run back to the other end of the hull. 2.Shoot the barrels. 3.Stay here.")
            if f =="1":
              print("You decide to run back to the other end of the hull.")
              sleep(3)
              print("The pirates met you on the other side, and you were not ready for it.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You shoot the gunpowder barrels and they explode just as the monster pirates arrive at the other end of the hull.")
              print("A massive violent explosion takes out all of the pirates, as well as the ship.")
              sleep(5)
              print("You blink hard and find yourself on the shore. The wreck of the ship is floating off in the distance.")
              print("You turn around and look at the mountains ahead of you.")
              print("You better keep moving.")
              player1.newSkill()
              nextChapter(player1)##########
            else:
              print("You stay here on this end of the hull, and prepare to face the incoming pirates.")
              sleep(3)
              print("They've alerted the rest of the pirates and they all come down to the hull to fight you.")
              print("You were able to shoot most of the pirates, but the captain was armed with a revolver and shoots you right in the head.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e == "3":
            print("You decide to take the fight here.")
            sleep(3)
            print("You managed to kill off two of the monsters, however the remaining two overpowered you and ran their cutlasses right through you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to shoot the barrels.")
            sleep(3)
            print("They all explode violently right next to you, charring you and burning you to death.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="3":
          print("You decide to run up to the high ground.")
          print("You died at a higher altitude.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You cut the rope next to you, despite having no idea what it does.")
          print("A sail becomes loose and falls directly on the four pirates. They are crushed by the large poles that held it up.")
          sleep(4)
          print("You relocate into a hidden position. The remaining pirates are looking for you.")
          e=input("1.Announce yourself. 2.Hide next to the barrels. 3.Hide in the hull. 4.Stay where you are hidden.")
          if e =="1":
            print("You announce yourself to the remaining monsters.")
            sleep(3)
            print("The captain shoots you in the head with a revolver.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e == "2":
            print("You decide to hide next to the barrels.")
            sleep(3)
            print("A monster sees you hiding, and manages to alert the others of your location before you kill them.")
            print("You found out the hard way that you were hiding behind gunpowder barrels.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You decide to hide in the hull. You find lots of gunpowder barrels there.")
            f=input("1.Announce yourself. 2.Hide here. 3.Go back up to the deck.")
            if f =="1":
              print("You yell out and announce yourself to the pirates, and immediately run to the other end of the hull.")
              print("Just as the monsters run down to the hull, you shoot at the barrels.")
              sleep(3)
              print("A massive violent explosion takes out all of the pirates, as well as the ship.")
              sleep(5)
              print("You blink hard and find yourself on the shore. The wreck of the ship is floating off in the distance.")
              print("You turn around and look at the mountains ahead of you.")
              print("You better keep moving.")
              player1.newSkill()
              nextChapter(player1)##########
            elif f =="2":
              print("You decide to hide in here, however with time, you realize that nothing is going to happen down here, and you still have nowhere to go.")
              sleep(3)
              print("You head towards the exit of the hull, just to run into five pirates.")
              print("You were severely outnumbered. YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go back up onto the deck, only to run directly into a group of five pirates on the way up.")
              print("You were caught off guard and outnumbered, so your head was removed from your torso.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to stay exactly where you are.")
            sleep(3)
            print("Two monsters walk by you and you were unable to take out both of them before the others arrived.")
            print("YOU DIED! THE END!")
            die(player1)
      else:
        print("You failed to pull them overboard and they stabbed you in the head with a cutlass. YOU DIED! THE END!")
        die(player1)
    elif b =="3":
      print("You go forwards, only to have the cannonball smash into the back of your skull.")
      print("YOU DIED! THE END!")
      die(player1)
    else:
      print("You immediately stop the boat, and another cannonball flies right over your head. You quickly start driving again.")
      print("You quickly glance back and find that the ship isgaining on you.")
      print("You need to outmaneuver the pirates somehow.")
      c=input("1.Head to the beach. 2.Head to the rocky shore. 3.Head towards the massive cave embedded in a mountain. 4.Head towards the mountains.")
      if c =="1":
        print("You decide to head towards the beach.")
        sleep(3)
        print("As you approach the beach, you slow down to avoid crashing at the shore.")
        print("However, when you glance behind, the monsters have no intention of stopping.")
        print("They crash into your boat, overturning it and you are launched into the sky, before hitting your head violently against a tree.")
        print("Your head splits open and you can't stop the blood.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You decide to head towards the rocky shore, hoping that the piartes would give up the chase knowing how dangerous the shore could be.")
        print("You slow down as you arrive near the shore, but the pirates have no intention of stopping. They crash into your boat, and you are knocked off the side of it, smashing your head against one of the rocks close to the water surface.")
        print("YOU DIED! THE END!")
      elif c =="3":
        print("You decide to head towards the massive caves.")
        sleep(3)
        print("The pirates are dangerously close to you now, and the caves are still quite far away.")
        d=input("1.Do a sharp U turn and double back. 2.Abandon ship. 3.Try to jump onto their ship. 4.Guns out.")
        if d =="1":
          print("You quickly do a sharp U turn, and the pirates cruise right past you.")
          print("You take this opportunity to drive faster, allowing you some more time to get away from the pirates.")
          sleep(3)
          print("But where to?")
          e=input("1.Through the caves. 2.Into the open sea. 3.To the other set of mountains. 4.To the shore.")
          if e =="1":
            print("You decide to drive your boat through the caves. You hope you can lose them in here.")
            sleep(3)
            print("After a few minutes, the deep sounds of the pirate ship returns.")
            f=input("1.Go forwards. 2.Go left. 3.Go right. 4.Turn off the engine and venture on foot.")
            if f =="1":
              print("You decide to go forwards.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            elif f == "2":
              print("You decide to go left.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You decide to go right.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            else:
              print("You quickly turn off the engine and leave the boat.")
              sleep(5)
              print("You hear the ship drive off in a nearby cave after a while. It looks like you've finally lost them.")
              print("You look around. The dark caves branch off everywhere.")
              print("'Just excellent.' You mutter to yourself.")
              player1.newSkill()
              nextChapter(player1)#####################
          elif e =="2":
            print("You venture into the open sea, which was a grave mistake.")
            print("The long range makes it easier for the pirates to use their cannons, and they hit you in one shot. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start heading towards the other set of mountains, but the pirates are still gaining on you.")
            sleep(3)
            print("A cannonball flies past your side and crashes into the water.")
            print("You notice that there is a gunpowder barrel next to one of the cannons on the ship.")
            f=input("1.Shoot it now. 2.Shoot it after a cannonball. 3.Shoot it after two cannonballs. 4.Shoot it after three cannonballs.")
            if f =="1":
              print("You turn around to shoot the barrel, only to be hit in the head with a cannonball.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You decide to dodge the next cannonball before shooting the barrel.")
              sleep(4)
              print("You successfully dodged the shot.")
              print("You turn around to shoot the barrel, only to be hit in the head with a cannonball.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You dodge two cannonballs in a row, and turn around to make the shot.")
              sleep(4)
              print("Your bullet connects with the gunpowder barrel, and the whole ship blows up before you.")
              print("You smile to yourself and arrive at the base of the mountains.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You decide to dodge the next three cannonballs before shooting the barrel.")
              sleep(4)
              print("You failed to dodge the third cannonball, and you are hit right in the head.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start heading towards the shore, but the shore was farther than you anticipated. The pirate ship saw you and shot your boat down with a cannon, and proceeded to run their ship over you.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to abandon ship, but as you jump out of your boat, the pirate ship crashes right into your boat and you. Your back is broken and you can't do anything as you slowly sink into the bottom of the ocean.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("As the ship gets closer and closer, you ready yourself to jump onto their ship.")
          print("Their ship crashes into your boat, and you take this chance to leap towards their ship, and you manage to hold on to the ledge of the deck.")
          e=input("1.Climb up. 2.Climb somewhere else to climb up to the deck. 3.Wait it out. 4.Let go.")
          if e =="1":
            print("You decide to climb up the deck, only to be surrounded by the pirates on board immediately. They slit your throat with a cutlass.")
            print("YOU DIED! THE END!")
          elif e =="2":
            print("You climb the ledge around the deck, until you find a quieter place to climb up.")
            sleep(4)
            print("You climb onto the deck, and quickly duck behind a barrel to avoid being seen.")
            print("You make a quick peek and identify eight pirates on the ship.")
            print("Who should you shoot at?")
            f=input("1.The three at the cannons. 2.The captain. 3.The one driving. 4.The three on standby with cutlasses.")
            if f =="1":
              print("You spray at the three monsters at the cannons.")
              print("One of your stray bullets pierce into a barrel of gunpowder, which causes a massive chain reaction that blows up the entire ship.")
              sleep(7)
              print("You blink hard, and look around yourself.")
              print("You were washed onto the shore atop a piece of the wreck. There are no monsters in sight.")
              print("You see the mountains ahead of you. You better keep moving.")
              player1.newSkill()
              nextChapter(player1)#####################
            elif f =="2":
              print("You shoot the captain right in the head, causing them to drop their revolver into the sea.")
              print("The crew now realizes that you're here, but you've got the ranged weapon. They only have cutlasses.")
              sleep(6)
              print("It was a massacre. The pirates' bodies litter the deck. You head over to the wheel, only to realize you don't know how to operate it.")
              print("You take one of the dinghies and head to shore, where the mountains await you.")
              player1.newSkill()
              nextChapter(player1)#####################
            elif f =="3":
              print("You shoot the driver dead, which alerts the captain and the crew.")
              print("The captain quickly swings around and draws a revolver, which he uses to embed a bullet into your head.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to shoot the three with the cutlasses, killing all of them.")
              sleep(3)
              print("However, the captain turns around and reveals that he has a revolver. He shoots you in the head before you could even react. YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You hold on to the ledge, and wait it out.")
            sleep(7)
            print("The pirates seem to have given up on searching for your body, and the ship starts moving once again.")
            f=input("1. Stay. 2.Climb onto the deck. 3.Drop into the water.")
            if f =="1":
              print("You stay hanging on the edge of the ship, but one of the pirates saw you while peering over the edge.")
              print("They stabbed you in the head with a cutlass. YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You climb onto the deck, only to face seven monsters wielding cutlasses.")
              sleep(3)
              print("The eighth pirate, the captain, quick draws their revolver and you are shot in the head.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You drop into the water, only occasionally swimming up to the surface to breathe.")
              sleep(6)
              print("After a long time of paranoid swimming, you made it to the shore.")
              print("The mountains lie up ahead. You better start moving.")
              player1.newSkill()
              nextChapter(player1)#####################
          else:
            print("You let go of the ledge, crashing into the water underneath you.")
            sleep(3)
            print("The ship cruises directly onto you.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You get your guns out, but unfortunately, their ship has caught up and they crash right into your face. YOU DIED! THE END!")
          die(player1)
      else:
        print("You decide to head towards the mountains.")
        sleep(5)
        print("The pirates are dangerously close to you now, and the mountains are still quite far away.")
        d=input("1.Do a sharp U turn and double back. 2.Abandon ship. 3.Try to jump onto their ship. 4.Guns out.")
        if d =="1":
          print("You quickly do a sharp U turn, and the pirates cruise right past you.")
          print("You take this opportunity to drive faster, allowing you some more time to get away from the pirates.")
          sleep(3)
          print("But where to?")
          e=input("1.Through the caves. 2.Into the open sea. 3.To the other set of mountains. 4.To the shore.")
          if e =="1":
            print("You decide to drive your boat through the caves. You hope you can lose them in here.")
            sleep(3)
            print("After a few minutes, the deep sounds of the pirate ship returns.")
            f=input("1.Go forwards. 2.Go left. 3.Go right. 4.Turn off the engine and venture on foot.")
            if f =="1":
              print("You decide to go forwards.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            elif f == "2":
              print("You decide to go left.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You decide to go right.")
              sleep(3)
              print("The pirates saw you and shot you in the back of the head. YOU DIED! THE END!")
              die(player1)
            else:
              print("You quickly turn off the engine and leave the boat.")
              sleep(5)
              print("You hear the ship drive off in a nearby cave after a while. It looks like you've finally lost them.")
              print("You look around. The dark caves branch off everywhere.")
              print("'Just excellent.' You mutter to yourself.")
              player1.newSkill()
              nextChapter(player1)#####################
          elif e =="2":
            print("You venture into the open sea, which was a grave mistake.")
            print("The long range makes it easier for the pirates to use their cannons, and they hit you in one shot. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start heading towards the other set of mountains, but the pirates are still gaining on you.")
            sleep(3)
            print("A cannonball flies past your side and crashes into the water.")
            print("You notice that there is a gunpowder barrel next to one of the cannons on the ship.")
            f=input("1.Shoot it now. 2.Shoot it after a cannonball. 3.Shoot it after two cannonballs. 4.Shoot it after three cannonballs.")
            if f =="1":
              print("You turn around to shoot the barrel, only to be hit in the head with a cannonball.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You decide to dodge the next cannonball before shooting the barrel.")
              sleep(4)
              print("You successfully dodged the shot.")
              print("You turn around to shoot the barrel, only to be hit in the head with a cannonball.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You dodge two cannonballs in a row, and turn around to make the shot.")
              sleep(4)
              print("Your bullet connects with the gunpowder barrel, and the whole ship blows up before you.")
              print("You smile to yourself and arrive at the base of the mountains.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You decide to dodge the next three cannonballs before shooting the barrel.")
              sleep(4)
              print("You failed to dodge the third cannonball, and you are hit right in the head.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start heading towards the shore, but the shore was farther than you anticipated. The pirate ship saw you and shot your boat down with a cannon, and proceeded to run their ship over you.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to abandon ship, but as you jump out of your boat, the pirate ship crashes right into your boat and you. Your back is broken and you can't do anything as you slowly sink into the bottom of the ocean.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("As the ship gets closer and closer, you ready yourself to jump onto their ship.")
          print("Their ship crashes into your boat, and you take this chance to leap towards their ship, and you manage to hold on to the ledge of the deck.")
          e=input("1.Climb up. 2.Climb somewhere else to climb up to the deck. 3.Wait it out. 4.Let go.")
          if e =="1":
            print("You decide to climb up the deck, only to be surrounded by the pirates on board immediately. They slit your throat with a cutlass.")
            print("YOU DIED! THE END!")
          elif e =="2":
            print("You climb the ledge around the deck, until you find a quieter place to climb up.")
            sleep(4)
            print("You climb onto the deck, and quickly duck behind a barrel to avoid being seen.")
            print("You make a quick peek and identify eight pirates on the ship.")
            print("Who should you shoot at?")
            f=input("1.The three at the cannons. 2.The captain. 3.The one driving. 4.The three on standby with cutlasses.")
            if f =="1":
              print("You spray at the three monsters at the cannons.")
              print("One of your stray bullets pierce into a barrel of gunpowder, which causes a massive chain reaction that blows up the entire ship.")
              sleep(7)
              print("You blink hard, and look around yourself.")
              print("You were washed onto the shore atop a piece of the wreck. There are no monsters in sight.")
              print("You see the mountains ahead of you. You better keep moving.")
              player1.newSkill()
              nextChapter(player1)#####################
            elif f =="2":
              print("You shoot the captain right in the head, causing them to drop their revolver into the sea.")
              print("The crew now realizes that you're here, but you've got the ranged weapon. They only have cutlasses.")
              sleep(6)
              print("It was a massacre. The pirates' bodies litter the deck. You head over to the wheel, only to realize you don't know how to operate it.")
              print("You take one of the dinghies and head to shore, where the mountains await you.")
              player1.newSkill()
              nextChapter(player1)#####################
            elif f =="3":
              print("You shoot the driver dead, which alerts the captain and the crew.")
              print("The captain quickly swings around and draws a revolver, which he uses to embed a bullet into your head.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to shoot the three with the cutlasses, killing all of them.")
              sleep(3)
              print("However, the captain turns around and reveals that he has a revolver. He shoots you in the head before you could even react. YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You hold on to the ledge, and wait it out.")
            sleep(7)
            print("The pirates seem to have given up on searching for your body, and the ship starts moving once again.")
            f=input("1. Stay. 2.Climb onto the deck. 3.Drop into the water.")
            if f =="1":
              print("You stay hanging on the edge of the ship, but one of the pirates saw you while peering over the edge.")
              print("They stabbed you in the head with a cutlass. YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You climb onto the deck, only to face seven monsters wielding cutlasses.")
              sleep(3)
              print("The eighth pirate, the captain, quick draws their revolver and you are shot in the head.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You drop into the water, only occasionally swimming up to the surface to breathe.")
              sleep(6)
              print("After a long time of paranoid swimming, you made it to the shore.")
              print("The mountains lie up ahead. You better start moving.")
              player1.newSkill()
              nextChapter(player1)#####################
          else:
            print("You let go of the ledge, crashing into the water underneath you.")
            sleep(3)
            print("The ship cruises directly onto you.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You get your guns out, but unfortunately, their ship has caught up and they crash right into your face. YOU DIED! THE END!")
          die(player1)
      
  elif a =="2":
    print("You turn around, only to see the cannonball hurling straight towards your face.")
    print("YOU DIED! THE END!")
    die(player1)
  elif a =="3":
    print("You duck, just as a cannonball cruises over your head.")
    print("You quickly turn around and see the massive pirate ship behind you.")
    sleep(4)
    print("A cannonball crashes into your boat, causing it to leak. You will capsize soon.")
    b=input("1.Jump overboard. 2.Stay on board.")
    if b =="1":
      print("You hurl yourself overboard.")
      sleep(4)
      print("The ship stops, as if the monsters aboard are looking for you.")
      sleep(3)
      print("You carefully swim towards the back of the ship while they are still looking at the shipwreck.")
      print("You find a ladder and climb on. You see a monster above you.")
      sleep(6)
      st=time.time()
      c=input("PRESS [P] to pull them overboard!").title()
      rt=time.time() - st
      if c =="P" and rt<2:
        print("You pull the monster overboard and successfully make it onto the deck.")
        sleep(4)
        print("You find a cutlass lying against a wall and pick it up.")
        print("Four monsters have seen you. There are eight on the ship.")
        d=input("1.Take the fight. 2.Run down to the hull. 3.Take the high ground. 4.Cut the rope next to you.")
        if d =="1":
          print("You decide to take the fight against the four monsters.")
          sleep(3)
          print("It did not end well.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You decide to make a run for the hull, where you find barrels of gunpowder all over the place.")
          e=input("1.Run back the way you came. 2.Run to the other end of the hull. 3.Take the fight. 4.Shoot the barrels.")
          if e=="1":
            print("You decide to run back the way you came, only to run back towards the four monsters chasing you.")
            print("You stood no chance. YOU DIED! THE END!")
            die(player1)
          elif e =="2":
            print("You quickly run towards the other side of the hull.")
            print("There is no way out on this side either.")
            f=input("1.Run back to the other end of the hull. 2.Shoot the barrels. 3.Stay here.")
            if f =="1":
              print("You decide to run back to the other end of the hull.")
              sleep(3)
              print("The pirates met you on the other side, and you were not ready for it.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You shoot the gunpowder barrels and they explode just as the monster pirates arrive at the other end of the hull.")
              print("A massive violent explosion takes out all of the pirates, as well as the ship.")
              sleep(5)
              print("You blink hard and find yourself on the shore. The wreck of the ship is floating off in the distance.")
              print("You turn around and look at the mountains ahead of you.")
              print("You better keep moving.")
              player1.newSkill()
              nextChapter(player1)##########
            else:
              print("You stay here on this end of the hull, and prepare to face the incoming pirates.")
              sleep(3)
              print("They've alerted the rest of the pirates and they all come down to the hull to fight you.")
              print("You were able to shoot most of the pirates, but the captain was armed with a revolver and shoots you right in the head.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e == "3":
            print("You decide to take the fight here.")
            sleep(3)
            print("You managed to kill off two of the monsters, however the remaining two overpowered you and ran their cutlasses right through you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to shoot the barrels.")
            sleep(3)
            print("They all explode violently right next to you, charring you and burning you to death.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="3":
          print("You decide to run up to the high ground.")
          print("You died at a higher altitude.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You cut the rope next to you, despite having no idea what it does.")
          print("A sail becomes loose and falls directly on the four pirates. They are crushed by the large poles that held it up.")
          sleep(4)
          print("You relocate into a hidden position. The remaining pirates are looking for you.")
          e=input("1.Announce yourself. 2.Hide next to the barrels. 3.Hide in the hull. 4.Stay where you are hidden.")
          if e =="1":
            print("You announce yourself to the remaining monsters.")
            sleep(3)
            print("The captain shoots you in the head with a revolver.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e == "2":
            print("You decide to hide next to the barrels.")
            sleep(3)
            print("A monster sees you hiding, and manages to alert the others of your location before you kill them.")
            print("You found out the hard way that you were hiding behind gunpowder barrels.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You decide to hide in the hull. You find lots of gunpowder barrels there.")
            f=input("1.Announce yourself. 2.Hide here. 3.Go back up to the deck.")
            if f =="1":
              print("You yell out and announce yourself to the pirates, and immediately run to the other end of the hull.")
              print("Just as the monsters run down to the hull, you shoot at the barrels.")
              sleep(3)
              print("A massive violent explosion takes out all of the pirates, as well as the ship.")
              sleep(5)
              print("You blink hard and find yourself on the shore. The wreck of the ship is floating off in the distance.")
              print("You turn around and look at the mountains ahead of you.")
              print("You better keep moving.")
              player1.newSkill()
              nextChapter(player1)##########
            elif f =="2":
              print("You decide to hide in here, however with time, you realize that nothing is going to happen down here, and you still have nowhere to go.")
              sleep(3)
              print("You head towards the exit of the hull, just to run into five pirates.")
              print("You were severely outnumbered. YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go back up onto the deck, only to run directly into a group of five pirates on the way up.")
              print("You were caught off guard and outnumbered, so your head was removed from your torso.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to stay exactly where you are.")
            sleep(3)
            print("Two monsters walk by you and you were unable to take out both of them before the others arrived.")
            print("YOU DIED! THE END!")
            die(player1)
      else:
        print("You failed to pull them overboard and they stabbed you in the head with a cutlass. YOU DIED! THE END!")
        die(player1)
    else:
      print("You stay on board, but what can you do against an endless stream of cannonballs?")
      print("YOU DIED! THE END!")
      die(player1)
  else:
    print("You quickly duck down to grab your rifle, just as a cannonball hurls over your head and smashes into the water.")
    print("You peek out with your rifle, and see a massive pirate ship with several cannons, heading straight to you.")
    sleep(3)
    print("You peek, and make a few shots at the monsters on the ship. None of them seem fazed by the shots.")
    print("Another cannon is shot and this time it connects with your ship. Water is filling up your boat.")
    b=input("1.Jump overboard. 2.Continue shooting.")
    if b =="1":
      print("You hurl yourself overboard.")
      sleep(4)
      print("The ship stops, as if the monsters aboard are looking for you.")
      sleep(3)
      print("You carefully swim towards the back of the ship while they are still looking at the shipwreck.")
      print("You find a ladder and climb on. You see a monster above you.")
      sleep(6)
      st=time.time()
      c=input("PRESS [P] to pull them overboard!").title()
      rt=time.time() - st
      if c =="P" and rt<2:
        print("You pull the monster overboard and successfully make it onto the deck.")
        sleep(4)
        print("You find a cutlass lying against a wall and pick it up.")
        print("Four monsters have seen you. There are eight on the ship.")
        d=input("1.Take the fight. 2.Run down to the hull. 3.Take the high ground. 4.Cut the rope next to you.")
        if d =="1":
          print("You decide to take the fight against the four monsters.")
          sleep(3)
          print("It did not end well.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You decide to make a run for the hull, where you find barrels of gunpowder all over the place.")
          e=input("1.Run back the way you came. 2.Run to the other end of the hull. 3.Take the fight. 4.Shoot the barrels.")
          if e=="1":
            print("You decide to run back the way you came, only to run back towards the four monsters chasing you.")
            print("You stood no chance. YOU DIED! THE END!")
            die(player1)
          elif e =="2":
            print("You quickly run towards the other side of the hull.")
            print("There is no way out on this side either.")
            f=input("1.Run back to the other end of the hull. 2.Shoot the barrels. 3.Stay here.")
            if f =="1":
              print("You decide to run back to the other end of the hull.")
              sleep(3)
              print("The pirates met you on the other side, and you were not ready for it.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You shoot the gunpowder barrels and they explode just as the monster pirates arrive at the other end of the hull.")
              print("A massive violent explosion takes out all of the pirates, as well as the ship.")
              sleep(5)
              print("You blink hard and find yourself on the shore. The wreck of the ship is floating off in the distance.")
              print("You turn around and look at the mountains ahead of you.")
              print("You better keep moving.")
              player1.newSkill()
              nextChapter(player1)##########
            else:
              print("You stay here on this end of the hull, and prepare to face the incoming pirates.")
              sleep(3)
              print("They've alerted the rest of the pirates and they all come down to the hull to fight you.")
              print("You were able to shoot most of the pirates, but the captain was armed with a revolver and shoots you right in the head.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e == "3":
            print("You decide to take the fight here.")
            sleep(3)
            print("You managed to kill off two of the monsters, however the remaining two overpowered you and ran their cutlasses right through you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to shoot the barrels.")
            sleep(3)
            print("They all explode violently right next to you, charring you and burning you to death.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="3":
          print("You decide to run up to the high ground.")
          print("You died at a higher altitude.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You cut the rope next to you, despite having no idea what it does.")
          print("A sail becomes loose and falls directly on the four pirates. They are crushed by the large poles that held it up.")
          sleep(4)
          print("You relocate into a hidden position. The remaining pirates are looking for you.")
          e=input("1.Announce yourself. 2.Hide next to the barrels. 3.Hide in the hull. 4.Stay where you are hidden.")
          if e =="1":
            print("You announce yourself to the remaining monsters.")
            sleep(3)
            print("The captain shoots you in the head with a revolver.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e == "2":
            print("You decide to hide next to the barrels.")
            sleep(3)
            print("A monster sees you hiding, and manages to alert the others of your location before you kill them.")
            print("You found out the hard way that you were hiding behind gunpowder barrels.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You decide to hide in the hull. You find lots of gunpowder barrels there.")
            f=input("1.Announce yourself. 2.Hide here. 3.Go back up to the deck.")
            if f =="1":
              print("You yell out and announce yourself to the pirates, and immediately run to the other end of the hull.")
              print("Just as the monsters run down to the hull, you shoot at the barrels.")
              sleep(3)
              print("A massive violent explosion takes out all of the pirates, as well as the ship.")
              sleep(5)
              print("You blink hard and find yourself on the shore. The wreck of the ship is floating off in the distance.")
              print("You turn around and look at the mountains ahead of you.")
              print("You better keep moving.")
              player1.newSkill()
              nextChapter(player1)##########
            elif f =="2":
              print("You decide to hide in here, however with time, you realize that nothing is going to happen down here, and you still have nowhere to go.")
              sleep(3)
              print("You head towards the exit of the hull, just to run into five pirates.")
              print("You were severely outnumbered. YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go back up onto the deck, only to run directly into a group of five pirates on the way up.")
              print("You were caught off guard and outnumbered, so your head was removed from your torso.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to stay exactly where you are.")
            sleep(3)
            print("Two monsters walk by you and you were unable to take out both of them before the others arrived.")
            print("YOU DIED! THE END!")
            die(player1)
      else:
        print("You failed to pull them overboard and they stabbed you in the head with a cutlass. YOU DIED! THE END!")
        die(player1)
    else:
      print("You stay on board to shoot, like the madman you are, and surprisingly, your guns did not prevail against the cannons and the sinking boat.")
      print("YOU DIED! THE END!")
      die(player1)

def mines(player1):#Used in two scenes. Formatted for ALONE. 
  print("You decide to head down the old mines.")
  sleep(3)
  print("You kick down the doors down to the mine, and slowly head down.")
  print("The mines should be hooked up with a massive cave system that branches out to the top of the highest mountain.")
  print("You look at the cobwebs under the eroding infrastructure.")
  print("This mine probably hasn't been used for a long time.")
  sleep(5)
  print("After travelling down the main path for a while, you reach your first split in the path.")
  a=input("1.Go left. 2.Go right. 3.Go forwards. 4.Go down.")
  if a =="1":
    print("You decide to go left.")
    print("Halfway down the path, you feel a strange tremble above you.")
    print("You look up, only to find the tunnel collapsing onto you, crushing every bone in your body and cracking your skull open.")
    print("YOU DIED! THE END!")
    die(player1)
  elif a =="2":
    print("You decide to head right.")
    sleep(3)
    print("The path feels strangely... eerie.")
    print("You feel that it's too silent.")
    b=input("1.Turn back, and head left. 2.Turn back, and head forwards. 3.Turn back, and head down. 4.Keep going.")
    if b =="1":
      print("You decide to turn back and head left.")
      print("Halfway down the left path, you feel a strange tremble above you.")
      print("You look up, only to find the tunnel collapsing onto you, crushing every bone in your body and cracking your skull open.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="2":
      print("You turned back, and headed forwards.")
      print("The path opens up into a massive cave, about a kilometer across in diameter.")
      print("You see some sort of settlement up ahead, with smoke emerging from one of the huts.")
      sleep(3)
      print("You decide to head closer for a better look.")
      sleep(3)
      print("Now that you are closer to it, you identify signs that someone has been here quite recently.")
      c=input("1.Run back to where you came from. 2.Hide somewhere. 3.Sneak deeper into the settlements. 4.Travel around the rim of the cave.")
      if c =="1":
        print("You decide to run back the way you came from. Big mistake.")
        print("A monster emerges from one of the huts and shoots you in the back of the head with a pistol.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You try to look for somewhere to hide, but the racket you cause while doing so is incredibly noticeable, and you have been noticed.")
        print("You were shot in the back of the head. YOU DIED! THE END!")
        die(player1)
      elif c =="3":
        print("You decide to sneak deeper into the settlements. You hear something moving just around the corner.")
        d=input("1.Take the fight! 2.Stay where you are. 3.Slowly sneak away. 4.Cause a distraction.")
        if d =="1":
          print("You decide to take the fight.")
          if player1.c2 == True or player1.c3 == True:
            print("You strike first, knocking the shotgun out of their hands and onto the ground.")
            print("They move to strike, but you anticipated their move and dodged, following up with a strong stab into their stomach with your knife. You cut their stomach open with the knife and their organs come pouring out of their bloody torse. You dump the limp body onto the ground and take a peek in the corridor they just came through.")
            print("Looks like it leads somewhere.")
            sleep(3)
            print("Suddenly, the whole corridor shudders.")
            sleep(3)
            print("The ground behind you starts cracking, and you start running.")
            print("Lava starts spewing out from the cracks behind you, and the cracks are getting wider and wider.")
            print("You see a junction up ahead. All of them seem fine for now.")
            sleep(6)
            st=time.time()
            e=input("1.Go left! 2.Go right! 3.Go straight!")
            rt=time.time()-st
            if rt>2:
              print("You couldn't make a decision in time and the lava caught up with you.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              if e =="1":
                print("You decided to go left.")
                sleep(3)
                print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
                print("Which way do you go?")
                f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
                if f =="1":
                  print("You decide to go left.")
                  print("The lava raining from the ceiling made you regret your decision.")
                  print("You totally regretted it as you screamed when the lava melted through you.")
                  print("YOU DIED! THE END!")
                  die(player1)
                elif f =="2":
                  print("You decide to go second left.")
                  print("You were spared from a horrible death from the lava.")
                  sleep(4)
                  print("Instead, you were crushed by falling debris.")
                  print("YOU DIED! THE END!")
                  die(player1)
                elif f =="3":
                  print("You decide to go right.")
                  sleep(3)
                  print("The corridor eventually led to a collapsed dead end.")
                  print("You were roasted alive. YOU DIED! THE END!")
                  die(player1)
                else:
                  print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                  print("Your destination is upwards. You head up.")
                  player1.newSkill()
                  nextChapter(player1)#####################
              elif e =="2":
                print("You decided to go right, but unfortunately for you, it was a dead end.")
                print("Your screams were pretty intense when your legs were burning off.")
                print("YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go straight ahead.")
                sleep(3)
                print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
                print("Your screams filled the caves as you died.")
                print("YOU DIED! THE END!")
                die(player1)
          else:
            print("You tried to overpower the monster, but they were stronger and faster.")
            print("Amongst the chaos, your face was blown off by their shotgun.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You stay exactly where you are.")
          if player1.t3 == True:
            print("The monsters walked right past you and you quickly move into the corridor they just came from.")
            print("You follow your way down the corridor, but suddenly the whole place starts shaking.")
            sleep(3)
            print("The ground behind you starts cracking, and you start running.")
            print("Lava starts spewing out from the cracks behind you, and the cracks are getting wider and wider.")
            print("You see a junction up ahead. All of them seem fine for now.")
            sleep(6)
            st=time.time()
            e=input("1.Go left! 2.Go right! 3.Go straight!")
            rt=time.time()-st
            if rt>2:
              print("You couldn't make a decision in time and the lava caught up with you.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              if e =="1":
                print("You decided to go left.")
                sleep(3)
                print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
                print("Which way do you go?")
                f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
                if f =="1":
                  print("You decide to go left.")
                  print("The lava raining from the ceiling made you regret your decision.")
                  print("You totally regretted it as you screamed when the lava melted through you.")
                  print("YOU DIED! THE END!")
                  die(player1)
                elif f =="2":
                  print("You decide to go second left.")
                  print("You were spared from a horrible death from the lava.")
                  sleep(4)
                  print("Instead, you were crushed by falling debris.")
                  print("YOU DIED! THE END!")
                  die(player1)
                elif f =="3":
                  print("You decide to go right.")
                  sleep(3)
                  print("The corridor eventually led to a collapsed dead end.")
                  print("You were roasted alive. YOU DIED! THE END!")
                  die(player1)
                else:
                  print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                  print("Your destination is upwards. You head up.")
                  player1.newSkill()
                  nextChapter(player1)#####################
              elif e =="2":
                print("You decided to go right, but unfortunately for you, it was a dead end.")
                print("Your screams were pretty intense when your legs were burning off.")
                print("YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go straight ahead.")
                sleep(3)
                print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
                print("Your screams filled the caves as you died.")
                print("YOU DIED! THE END!")
                die(player1)
          else:
            print("You tried to remain hidden, but one of them felt your movement.")
            print("You were greeted with a shotgun to the face. YOU DIED! THE END!")
            die(player1)
        elif d =="3":
          print("You decide to slowly sneak away from the corridor they are coming from, but unluckily for you, you turned around just as they left the corridor and into view of you.")
          print("Your back was destroyed into atoms after their bullets were done with you.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to cause a distraction by throwing something to the other side of the corridor exit, but someone saw the rock come from your side.")
          print("They suddenly peeked through the corridor exit and killed you with a good shotgun shot to the head.")
          print("YOU DIED! THE END!")
          die(player1)
      else:
        print("You decide to head to the rim of the cave for safer travel.")
        sleep(3)
        print("Suddenly, you hear a group of aliens heading your way in a connecting cave.")
        d=input("1.Run back the way you came. 2.Ambush them. 3.Hide behind a barrel. 4.Hide behind a pile of rocks.")
        if d =="1":
          print("You decide to run back the way you came, only to be seen doing so.")
          print("Your neck seemed to have stopped working.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You try to ambush the group, only to be killed brutally due to the difference in numbers.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to hide behind a barrel.")
          print("One of the monsters sit on the barrel you are hiding behind.")
          sleep(5)
          print("They turned around and starts to bring out their weapon, but you managed to shoot them to death, however, the other monsters have also been alerted.")
          print("You found out the hard way that you were hiding behind a barrel of gunpowder.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You quickly hide behind a pile of rocks, and the monsters simply walk right by without seeing you.")
          print("You decide to head down the corridor they came from.")
          sleep(3)
          print("Suddenly, the whole corridor shudders.")
          sleep(3)
          print("The ground behind you starts cracking, and you start running.")
          print("Lava starts spewing out from the cracks behind you, and the cracks are getting wider and wider.")
          print("You see a junction up ahead. All of them seem fine for now.")
          sleep(6)
          st=time.time()
          e=input("1.Go left! 2.Go right! 3.Go straight!")
          rt=time.time()-st
          if rt>2:
            print("You couldn't make a decision in time and the lava caught up with you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            if e =="1":
              print("You decided to go left.")
              sleep(3)
              print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
              print("Which way do you go?")
              f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
              if f =="1":
                print("You decide to go left.")
                print("The lava raining from the ceiling made you regret your decision.")
                print("You totally regretted it as you screamed when the lava melted through you.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You decide to go second left.")
                print("You were spared from a horrible death from the lava.")
                sleep(4)
                print("Instead, you were crushed by falling debris.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to go right.")
                sleep(3)
                print("The corridor eventually led to a collapsed dead end.")
                print("You were roasted alive. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                print("Your destination is upwards. You head up.")
                player1.newSkill()
                nextChapter(player1)#####################
            elif e =="2":
              print("You decided to go right, but unfortunately for you, it was a dead end.")
              print("Your screams were pretty intense when your legs were burning off.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go straight ahead.")
              sleep(3)
              print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
              print("Your screams filled the caves as you died.")
              print("YOU DIED! THE END!")
              die(player1)
    elif b =="3":
      print("You head back to the area from earlier and head down. You turn on a flashlight to aid your descent.")
      sleep(4)
      print("You reach the bottom of the ladder and turn around.")
      print("The area opens up into a lot of paths.")
      c=input("1.Go far left. 2.Go second left. 3.Go third left. 4.Go far right. 5.Go second right. 6.Go third right.")
      if c =="1":
        print("You decide to go through the path in the far left.")
        sleep(3)
        print("Something about the air is bothering you. You start walking faster.")
        sleep(3)
        print("You've been holding your breath for the past ten seconds. Where's the other end of the corridor?")
        sleep(3)
        print("Scratching the floor in your final moments didn't help. You suffocated in the thick air of the caverns.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You decide to head down the second left corridor. Something about it seems good.")
        sleep(3)
        print("The air is getting thicker. You've got to get to the other side. You start walking faster.")
        sleep(5)
        print("The air is unbreathable now. You start running down the corridor.")
        sleep(4)
        print("You gasp and quickly gulp down as much oxygen as you can once you make it to the end of the corridor.")
        print("After recovering enough oxygen, you take a good look at your surroundings.")
        print("'Woah...' You are in a massive cavern, with a massive hole down the middle.")
        print("You can't see the other end of the hole.")
        sleep(3)
        print("Suddenly, the whole cavern shakes.")
        d=input("1.Run to the other side of the cavern. 2.Run back the way you came.")
        if d =="1":
          print("You start running to the other side of the cavern, and the cave walls and floor behind you start cracking and shooting lava out of them. You make your way to the other end of the cavern and enter the corridor there.")
          sleep(6)
          print("Up ahead, you see an incoming junction.")
          st=time.time()
          e=input("1.Go left! 2.Go right! 3.Go straight!")
          rt=time.time()-st
          if rt>2:
            print("You couldn't make a decision in time and the lava caught up with you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            if e =="1":
              print("You decided to go left.")
              sleep(3)
              print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
              print("Which way do you go?")
              f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
              if f =="1":
                print("You decide to go left.")
                print("The lava raining from the ceiling made you regret your decision.")
                print("You totally regretted it as you screamed when the lava melted through you.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You decide to go second left.")
                print("You were spared from a horrible death from the lava.")
                sleep(4)
                print("Instead, you were crushed by falling debris.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to go right.")
                sleep(3)
                print("The corridor eventually led to a collapsed dead end.")
                print("You were roasted alive. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                print("Your destination is upwards. You head up.")
                player1.newSkill()
                nextChapter(player1)#####################
            elif e =="2":
              print("You decided to go right, but unfortunately for you, it was a dead end.")
              print("Your screams were pretty intense when your legs were burning off.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go straight ahead.")
              sleep(3)
              print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
              print("Your screams filled the caves as you died.")
              print("YOU DIED! THE END!")
              die(player1)
        else:
          print("You decide to head back the way you came, only to have the walls crack and release lava through them.")
          print("You made a good human kebab.")
          print("YOU DIED! THE END!")
          die(player1)
      elif c =="3":
        print("You decide to head down the third left corridor. You stepped on a weird rock. 'Huh.'")
        print("It starts beeping.")
        print("Before you could run away, the whole corridor falls down onto you. YOU DIED! THE END!")
        die(player1)
      elif c =="4":
        print("You decide to head down the far right corridor. You managed to go ten steps before it collapsed onto you.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="5":
        print("You decided to head down the second right tunnel. Seems legit, right?")
        sleep(4)
        print("The stalactite that pierced through your back was pretty legit. Too bad you are stuck there now. Forever.")
        print("YOU DIED! THE END!")
        die(player1)
      else:
        print("You decide to head down the third right corridor. The corridor seems a bit shaky, but it's barely holding on.")
        sleep(3)
        print("You managed to make it to the other end of the corridor without a hitch.")
        print("'Woah.' You say, after discovering that the corridor opened up into a massive cavern with a huge hole down the middle.")
        print("You can't see the bottom of the hole from here.")
        sleep(3)
        print("Suddenly, the whole cavern shakes.")
        d=input("1.Run to the other side of the cavern. 2.Run back the way you came.")
        if d =="1":
          print("You start running to the other side of the cavern, and the cave walls and floor behind you start cracking and shooting lava out of them. You make your way to the other end of the cavern and enter the corridor there.")
          sleep(6)
          print("Up ahead, you see an incoming junction.")
          st=time.time()
          e=input("1.Go left! 2.Go right! 3.Go straight!")
          rt=time.time()-st
          if rt>2:
            print("You couldn't make a decision in time and the lava caught up with you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            if e =="1":
              print("You decided to go left.")
              sleep(3)
              print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
              print("Which way do you go?")
              f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
              if f =="1":
                print("You decide to go left.")
                print("The lava raining from the ceiling made you regret your decision.")
                print("You totally regretted it as you screamed when the lava melted through you.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You decide to go second left.")
                print("You were spared from a horrible death from the lava.")
                sleep(4)
                print("Instead, you were crushed by falling debris.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to go right.")
                sleep(3)
                print("The corridor eventually led to a collapsed dead end.")
                print("You were roasted alive. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                print("Your destination is upwards. You head up.")
                player1.newSkill()
                nextChapter(player1)#####################
            elif e =="2":
              print("You decided to go right, but unfortunately for you, it was a dead end.")
              print("Your screams were pretty intense when your legs were burning off.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go straight ahead.")
              sleep(3)
              print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
              print("Your screams filled the caves as you died.")
              print("YOU DIED! THE END!")
              die(player1)
        else:
          print("You decide to head back the way you came, only to have the walls crack and release lava through them.")
          print("You made a good human kebab.")
          print("YOU DIED! THE END!")
          die(player1)
    else:
      print("You decide to keep going.")
      print("Suddenly, a monster emerges from ahead, and two more monsters appear from the walls in both sides. You are surrounded.")
      print("You stood no chance.")
      print("YOU DIED! THE END!")
      die(player1)
  elif a =="3":
    print("You head forwards, and the path eventually opens up into a massive cave.")
    print("The walls of the cave are approximately one kilometer across, and in the middle is some sort of settlement with smoke coming off of the top of one of the huts.")
    b=input("1.Approach the settlements. 2.Turn back, and head left. 3.Turn back, and head right. 4.Turn back, and head down.")
    if b =="1":
      print("You decide to approach the settlemnts. Now that you are closer to it, you identify signs that someone has been here quite recently.")
      c=input("1.Run back to where you came from. 2.Hide somewhere. 3.Sneak deeper into the settlements. 4.Travel around the rim of the cave.")
      if c =="1":
        print("You decide to run back the way you came from. Big mistake.")
        print("A monster emerges from one of the huts and shoots you in the back of the head with a pistol.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You try to look for somewhere to hide, but the racket you cause while doing so is incredibly noticeable, and you have been noticed.")
        print("You were shot in the back of the head. YOU DIED! THE END!")
        die(player1)
      elif c =="3":
        print("You decide to sneak deeper into the settlements. You hear something moving just around the corner.")
        d=input("1.Take the fight! 2.Stay where you are. 3.Slowly sneak away. 4.Cause a distraction.")
        if d =="1":
          print("You decide to take the fight.")
          if player1.c2 == True or player1.c3 == True:
            print("You strike first, knocking the shotgun out of their hands and onto the ground.")
            print("They move to strike, but you anticipated their move and dodged, following up with a strong stab into their stomach with your knife. You cut their stomach open with the knife and their organs come pouring out of their bloody torse. You dump the limp body onto the ground and take a peek in the corridor they just came through.")
            print("Looks like it leads somewhere.")
            sleep(3)
            print("Suddenly, the whole corridor shudders.")
            sleep(3)
            print("The ground behind you starts cracking, and you start running.")
            print("Lava starts spewing out from the cracks behind you, and the cracks are getting wider and wider.")
            print("You see a junction up ahead. All of them seem fine for now.")
            sleep(6)
            st=time.time()
            e=input("1.Go left! 2.Go right! 3.Go straight!")
            rt=time.time()-st
            if rt>2:
              print("You couldn't make a decision in time and the lava caught up with you.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              if e =="1":
                print("You decided to go left.")
                sleep(3)
                print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
                print("Which way do you go?")
                f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
                if f =="1":
                  print("You decide to go left.")
                  print("The lava raining from the ceiling made you regret your decision.")
                  print("You totally regretted it as you screamed when the lava melted through you.")
                  print("YOU DIED! THE END!")
                  die(player1)
                elif f =="2":
                  print("You decide to go second left.")
                  print("You were spared from a horrible death from the lava.")
                  sleep(4)
                  print("Instead, you were crushed by falling debris.")
                  print("YOU DIED! THE END!")
                  die(player1)
                elif f =="3":
                  print("You decide to go right.")
                  sleep(3)
                  print("The corridor eventually led to a collapsed dead end.")
                  print("You were roasted alive. YOU DIED! THE END!")
                  die(player1)
                else:
                  print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                  print("Your destination is upwards. You head up.")
                  player1.newSkill()
                  nextChapter(player1)#####################
              elif e =="2":
                print("You decided to go right, but unfortunately for you, it was a dead end.")
                print("Your screams were pretty intense when your legs were burning off.")
                print("YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go straight ahead.")
                sleep(3)
                print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
                print("Your screams filled the caves as you died.")
                print("YOU DIED! THE END!")
                die(player1)
          else:
            print("You tried to overpower the monster, but they were stronger and faster.")
            print("Amongst the chaos, your face was blown off by their shotgun.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You stay exactly where you are.")
          if player1.t3 == True:
            print("The monsters walked right past you and you quickly move into the corridor they just came from.")
            print("You follow your way down the corridor, but suddenly the whole place starts shaking.")
            sleep(3)
            print("The ground behind you starts cracking, and you start running.")
            print("Lava starts spewing out from the cracks behind you, and the cracks are getting wider and wider.")
            print("You see a junction up ahead. All of them seem fine for now.")
            sleep(6)
            st=time.time()
            e=input("1.Go left! 2.Go right! 3.Go straight!")
            rt=time.time()-st
            if rt>2:
              print("You couldn't make a decision in time and the lava caught up with you.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              if e =="1":
                print("You decided to go left.")
                sleep(3)
                print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
                print("Which way do you go?")
                f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
                if f =="1":
                  print("You decide to go left.")
                  print("The lava raining from the ceiling made you regret your decision.")
                  print("You totally regretted it as you screamed when the lava melted through you.")
                  print("YOU DIED! THE END!")
                  die(player1)
                elif f =="2":
                  print("You decide to go second left.")
                  print("You were spared from a horrible death from the lava.")
                  sleep(4)
                  print("Instead, you were crushed by falling debris.")
                  print("YOU DIED! THE END!")
                  die(player1)
                elif f =="3":
                  print("You decide to go right.")
                  sleep(3)
                  print("The corridor eventually led to a collapsed dead end.")
                  print("You were roasted alive. YOU DIED! THE END!")
                  die(player1)
                else:
                  print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                  print("Your destination is upwards. You head up.")
                  player1.newSkill()
                  nextChapter(player1)#####################
              elif e =="2":
                print("You decided to go right, but unfortunately for you, it was a dead end.")
                print("Your screams were pretty intense when your legs were burning off.")
                print("YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go straight ahead.")
                sleep(3)
                print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
                print("Your screams filled the caves as you died.")
                print("YOU DIED! THE END!")
                die(player1)
          else:
            print("You tried to remain hidden, but one of them felt your movement.")
            print("You were greeted with a shotgun to the face. YOU DIED! THE END!")
            die(player1)
        elif d =="3":
          print("You decide to slowly sneak away from the corridor they are coming from, but unluckily for you, you turned around just as they left the corridor and into view of you.")
          print("Your back was destroyed into atoms after their bullets were done with you.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to cause a distraction by throwing something to the other side of the corridor exit, but someone saw the rock come from your side.")
          print("They suddenly peeked through the corridor exit and killed you with a good shotgun shot to the head.")
          print("YOU DIED! THE END!")
          die(player1)
      else:
        print("You decide to head to the rim of the cave for safer travel.")
        sleep(3)
        print("Suddenly, you hear a group of aliens heading your way in a connecting cave.")
        d=input("1.Run back the way you came. 2.Ambush them. 3.Hide behind a barrel. 4.Hide behind a pile of rocks.")
        if d =="1":
          print("You decide to run back the way you came, only to be seen doing so.")
          print("Your neck seemed to have stopped working.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You try to ambush the group, only to be killed brutally due to the difference in numbers.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to hide behind a barrel.")
          print("One of the monsters sit on the barrel you are hiding behind.")
          sleep(5)
          print("They turned around and starts to bring out their weapon, but you managed to shoot them to death, however, the other monsters have also been alerted.")
          print("You found out the hard way that you were hiding behind a barrel of gunpowder.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You quickly hide behind a pile of rocks, and the monsters simply walk right by without seeing you.")
          print("You decide to head down the corridor they came from.")
          sleep(3)
          print("Suddenly, the whole corridor shudders.")
          sleep(3)
          print("The ground behind you starts cracking, and you start running.")
          print("Lava starts spewing out from the cracks behind you, and the cracks are getting wider and wider.")
          print("You see a junction up ahead. All of them seem fine for now.")
          sleep(6)
          st=time.time()
          e=input("1.Go left! 2.Go right! 3.Go straight!")
          rt=time.time()-st
          if rt>2:
            print("You couldn't make a decision in time and the lava caught up with you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            if e =="1":
              print("You decided to go left.")
              sleep(3)
              print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
              print("Which way do you go?")
              f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
              if f =="1":
                print("You decide to go left.")
                print("The lava raining from the ceiling made you regret your decision.")
                print("You totally regretted it as you screamed when the lava melted through you.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You decide to go second left.")
                print("You were spared from a horrible death from the lava.")
                sleep(4)
                print("Instead, you were crushed by falling debris.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to go right.")
                sleep(3)
                print("The corridor eventually led to a collapsed dead end.")
                print("You were roasted alive. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                print("Your destination is upwards. You head up.")
                player1.newSkill()
                nextChapter(player1)#####################
            elif e =="2":
              print("You decided to go right, but unfortunately for you, it was a dead end.")
              print("Your screams were pretty intense when your legs were burning off.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go straight ahead.")
              sleep(3)
              print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
              print("Your screams filled the caves as you died.")
              print("YOU DIED! THE END!")
              die(player1)
    elif b =="2":
      print("You turned back and head left.")
      print("Halfway down the left path, you feel a strange tremble above you.")
      print("You look up, only to find the tunnel collapsing onto you, crushing every bone in your body and cracking your skull open.")
      print("YOU DIED! THE END!")
    elif b =="3":
      print("You turned back and headed right.")
      sleep(3)
      print("You were ambushed by three monsters, and they feasted upon your flesh.")
      print("YOU DIED! THE END!")
      die(player1)
    else:
      print("You decide to turn back and head down. You turn on a flashlight to aid your descent.")
      sleep(4)
      print("You reach the bottom of the ladder and turn around.")
      print("The area opens up into a lot of paths.")
      c=input("1.Go far left. 2.Go second left. 3.Go third left. 4.Go far right. 5.Go second right. 6.Go third right.")
      if c =="1":
        print("You decide to go through the path in the far left.")
        sleep(3)
        print("Something about the air is bothering you. You start walking faster.")
        sleep(3)
        print("You've been holding your breath for the past ten seconds. Where's the other end of the corridor?")
        sleep(3)
        print("Scratching the floor in your final moments didn't help. You suffocated in the thick air of the caverns.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You decide to head down the second left corridor. Something about it seems good.")
        sleep(3)
        print("The air is getting thicker. You've got to get to the other side. You start walking faster.")
        sleep(5)
        print("The air is unbreathable now. You start running down the corridor.")
        sleep(4)
        print("You gasp and quickly gulp down as much oxygen as you can once you make it to the end of the corridor.")
        print("After recovering enough oxygen, you take a good look at your surroundings.")
        print("'Woah...' You are in a massive cavern, with a massive hole down the middle.")
        print("You can't see the other end of the hole.")
        sleep(3)
        print("Suddenly, the whole cavern shakes.")
        d=input("1.Run to the other side of the cavern. 2.Run back the way you came.")
        if d =="1":
          print("You start running to the other side of the cavern, and the cave walls and floor behind you start cracking and shooting lava out of them. You make your way to the other end of the cavern and enter the corridor there.")
          sleep(6)
          print("Up ahead, you see an incoming junction.")
          st=time.time()
          e=input("1.Go left! 2.Go right! 3.Go straight!")
          rt=time.time()-st
          if rt>2:
            print("You couldn't make a decision in time and the lava caught up with you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            if e =="1":
              print("You decided to go left.")
              sleep(3)
              print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
              print("Which way do you go?")
              f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
              if f =="1":
                print("You decide to go left.")
                print("The lava raining from the ceiling made you regret your decision.")
                print("You totally regretted it as you screamed when the lava melted through you.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You decide to go second left.")
                print("You were spared from a horrible death from the lava.")
                sleep(4)
                print("Instead, you were crushed by falling debris.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to go right.")
                sleep(3)
                print("The corridor eventually led to a collapsed dead end.")
                print("You were roasted alive. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                print("Your destination is upwards. You head up.")
                player1.newSkill()
                nextChapter(player1)#####################
            elif e =="2":
              print("You decided to go right, but unfortunately for you, it was a dead end.")
              print("Your screams were pretty intense when your legs were burning off.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go straight ahead.")
              sleep(3)
              print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
              print("Your screams filled the caves as you died.")
              print("YOU DIED! THE END!")
              die(player1)
        else:
          print("You decide to head back the way you came, only to have the walls crack and release lava through them.")
          print("You made a good human kebab.")
          print("YOU DIED! THE END!")
          die(player1)
      elif c =="3":
        print("You decide to head down the third left corridor. You stepped on a weird rock. 'Huh.'")
        print("It starts beeping.")
        print("Before you could run away, the whole corridor falls down onto you. YOU DIED! THE END!")
        die(player1)
      elif c =="4":
        print("You decide to head down the far right corridor. You managed to go ten steps before it collapsed onto you.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="5":
        print("You decided to head down the second right tunnel. Seems legit, right?")
        sleep(4)
        print("The stalactite that pierced through your back was pretty legit. Too bad you are stuck there now. Forever.")
        print("YOU DIED! THE END!")
        die(player1)
      else:
        print("You decide to head down the third right corridor. The corridor seems a bit shaky, but it's barely holding on.")
        sleep(3)
        print("You managed to make it to the other end of the corridor without a hitch.")
        print("'Woah.' You say, after discovering that the corridor opened up into a massive cavern with a huge hole down the middle.")
        print("You can't see the bottom of the hole from here.")
        sleep(3)
        print("Suddenly, the whole cavern shakes.")
        d=input("1.Run to the other side of the cavern. 2.Run back the way you came.")
        if d =="1":
          print("You start running to the other side of the cavern, and the cave walls and floor behind you start cracking and shooting lava out of them. You make your way to the other end of the cavern and enter the corridor there.")
          sleep(6)
          print("Up ahead, you see an incoming junction.")
          st=time.time()
          e=input("1.Go left! 2.Go right! 3.Go straight!")
          rt=time.time()-st
          if rt>2:
            print("You couldn't make a decision in time and the lava caught up with you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            if e =="1":
              print("You decided to go left.")
              sleep(3)
              print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
              print("Which way do you go?")
              f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
              if f =="1":
                print("You decide to go left.")
                print("The lava raining from the ceiling made you regret your decision.")
                print("You totally regretted it as you screamed when the lava melted through you.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You decide to go second left.")
                print("You were spared from a horrible death from the lava.")
                sleep(4)
                print("Instead, you were crushed by falling debris.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to go right.")
                sleep(3)
                print("The corridor eventually led to a collapsed dead end.")
                print("You were roasted alive. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                print("Your destination is upwards. You head up.")
                player1.newSkill()
                nextChapter(player1)#####################
            elif e =="2":
              print("You decided to go right, but unfortunately for you, it was a dead end.")
              print("Your screams were pretty intense when your legs were burning off.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go straight ahead.")
              sleep(3)
              print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
              print("Your screams filled the caves as you died.")
              print("YOU DIED! THE END!")
              die(player1)
        else:
          print("You decide to head back the way you came, only to have the walls crack and release lava through them.")
          print("You made a good human kebab.")
          print("YOU DIED! THE END!")
          die(player1)
  else:
    print("You decide to head down the ladder.")
    sleep(5)
    print("You are unable to see below you, so you grab your flashlight and turn it on.")
    sleep(7)
    st=time.time()
    b=input("PRESS [H] to hold on!").title()
    rt=time.time()-st
    if b =="H" and rt < 2:
      print("You manage to hold on after being jumped by the scene of a hundred bats hanging around nearby.")
      print("You continue climbing down the ladder.")
      sleep(4)
      print("You reach the bottom of the ladder and turn around.")
      print("The area opens up into a lot of paths.")
      c=input("1.Go far left. 2.Go second left. 3.Go third left. 4.Go far right. 5.Go second right. 6.Go third right.")
      if c =="1":
        print("You decide to go through the path in the far left.")
        sleep(3)
        print("Something about the air is bothering you. You start walking faster.")
        sleep(3)
        print("You've been holding your breath for the past ten seconds. Where's the other end of the corridor?")
        sleep(3)
        print("Scratching the floor in your final moments didn't help. You suffocated in the thick air of the caverns.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You decide to head down the second left corridor. Something about it seems good.")
        sleep(3)
        print("The air is getting thicker. You've got to get to the other side. You start walking faster.")
        sleep(5)
        print("The air is unbreathable now. You start running down the corridor.")
        sleep(4)
        print("You gasp and quickly gulp down as much oxygen as you can once you make it to the end of the corridor.")
        print("After recovering enough oxygen, you take a good look at your surroundings.")
        print("'Woah...' You are in a massive cavern, with a massive hole down the middle.")
        print("You can't see the other end of the hole.")
        sleep(3)
        print("Suddenly, the whole cavern shakes.")
        d=input("1.Run to the other side of the cavern. 2.Run back the way you came.")
        if d =="1":
          print("You start running to the other side of the cavern, and the cave walls and floor behind you start cracking and shooting lava out of them. You make your way to the other end of the cavern and enter the corridor there.")
          sleep(6)
          print("Up ahead, you see an incoming junction.")
          st=time.time()
          e=input("1.Go left! 2.Go right! 3.Go straight!")
          rt=time.time()-st
          if rt>2:
            print("You couldn't make a decision in time and the lava caught up with you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            if e =="1":
              print("You decided to go left.")
              sleep(3)
              print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
              print("Which way do you go?")
              f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
              if f =="1":
                print("You decide to go left.")
                print("The lava raining from the ceiling made you regret your decision.")
                print("You totally regretted it as you screamed when the lava melted through you.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You decide to go second left.")
                print("You were spared from a horrible death from the lava.")
                sleep(4)
                print("Instead, you were crushed by falling debris.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to go right.")
                sleep(3)
                print("The corridor eventually led to a collapsed dead end.")
                print("You were roasted alive. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                print("Your destination is upwards. You head up.")
                player1.newSkill()
                nextChapter(player1)#####################
            elif e =="2":
              print("You decided to go right, but unfortunately for you, it was a dead end.")
              print("Your screams were pretty intense when your legs were burning off.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go straight ahead.")
              sleep(3)
              print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
              print("Your screams filled the caves as you died.")
              print("YOU DIED! THE END!")
              die(player1)
        else:
          print("You decide to head back the way you came, only to have the walls crack and release lava through them.")
          print("You made a good human kebab.")
          print("YOU DIED! THE END!")
          die(player1)
      elif c =="3":
        print("You decide to head down the third left corridor. You stepped on a weird rock. 'Huh.'")
        print("It starts beeping.")
        print("Before you could run away, the whole corridor falls down onto you. YOU DIED! THE END!")
        die(player1)
      elif c =="4":
        print("You decide to head down the far right corridor. You managed to go ten steps before it collapsed onto you.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="5":
        print("You decided to head down the second right tunnel. Seems legit, right?")
        sleep(4)
        print("The stalactite that pierced through your back was pretty legit. Too bad you are stuck there now. Forever.")
        print("YOU DIED! THE END!")
        die(player1)
      else:
        print("You decide to head down the third right corridor. The corridor seems a bit shaky, but it's barely holding on.")
        sleep(3)
        print("You managed to make it to the other end of the corridor without a hitch.")
        print("'Woah.' You say, after discovering that the corridor opened up into a massive cavern with a huge hole down the middle.")
        print("You can't see the bottom of the hole from here.")
        sleep(3)
        print("Suddenly, the whole cavern shakes.")
        d=input("1.Run to the other side of the cavern. 2.Run back the way you came.")
        if d =="1":
          print("You start running to the other side of the cavern, and the cave walls and floor behind you start cracking and shooting lava out of them. You make your way to the other end of the cavern and enter the corridor there.")
          sleep(6)
          print("Up ahead, you see an incoming junction.")
          st=time.time()
          e=input("1.Go left! 2.Go right! 3.Go straight!")
          rt=time.time()-st
          if rt>2:
            print("You couldn't make a decision in time and the lava caught up with you.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            if e =="1":
              print("You decided to go left.")
              sleep(3)
              print("You manage to escape the lava temporarily, but the corridor has opened up into another junction.")
              print("Which way do you go?")
              f=input("1.Left. 2.Second left. 3.Right. 4.Second right.")
              if f =="1":
                print("You decide to go left.")
                print("The lava raining from the ceiling made you regret your decision.")
                print("You totally regretted it as you screamed when the lava melted through you.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You decide to go second left.")
                print("You were spared from a horrible death from the lava.")
                sleep(4)
                print("Instead, you were crushed by falling debris.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to go right.")
                sleep(3)
                print("The corridor eventually led to a collapsed dead end.")
                print("You were roasted alive. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to go second right. The lava was approaching from behind, slowly, but eventually you managed to outrun it and reach some sort of cavern that led upwards.")
                print("Your destination is upwards. You head up.")
                player1.newSkill()
                nextChapter(player1)#####################
            elif e =="2":
              print("You decided to go right, but unfortunately for you, it was a dead end.")
              print("Your screams were pretty intense when your legs were burning off.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to go straight ahead.")
              sleep(3)
              print("You've almost made it to the other end, but unfortunately you tripped over a rock and you fell onto the rocky ground. You start to push yourself up, but the lava has already reached your leg.")
              print("Your screams filled the caves as you died.")
              print("YOU DIED! THE END!")
              die(player1)
        else:
          print("You decide to head back the way you came, only to have the walls crack and release lava through them.")
          print("You made a good human kebab.")
          print("YOU DIED! THE END!")
          die(player1)
    else:
      print("You failed to hold on to the ladder after being surprised and fell off.")
      print("Your neck was snapped in weird places. And so were your bones.")
      print("YOU DIED! THE END!")
      die(player1)
 
def desert(player1):#Used in Ranger Scenes. Fromatted for a single ranger.
  print("The sands seem to stretch forever.")
  print("You know that if you keep walking north you'll reach the mountains, but what if the heat kills you before you can make it there?")
  a=input("1.Go northeast. 2.Continue going north. 3.Go northwest.")
  if a =="1":
    print("You decide to head northeast.")
    print("The sand stretches on a bit more, but there seems to be an oasis up ahead!")
    b=input("1.Head to the oasis. 2.Ignore it and keep walking.")
    if b =="1":
      print("You decide to head to the oasis, and freshen yourself up. 'Whew.'")
      print("You refill your bottle and take a deep breath.")
      print("You might have to curve back to the mountains soon, in case the desert isn't a complete square.")
      c=input("1.Head northeast. 2.Head north. 3.Head northwest.")
      if c =="1":
        print("You head further northeast, and the desert eventually becomes some sort of savanna.")
        print("A sniper tower spotted you and you died within the blink of an eye.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You decide to head north. You arrived at a plains. Some sort of smoke is coming from something up ahead. What is that? It's coming towards you...")
        sleep(3)
        print("Some sort of bomb drops right next to you.")
        print("YOU DIED! THE END!")
        die(player1)
      else:
        print("You head northwest, and are back on track to your destination.")
        sleep(5)
        print("You're starting to get a bit tired...")
        d=input("1.Take a break. 2.Take a break later and keep moving now.")
        if d =="1":
          print("You decide to take a break. The ground ahead of you starts trembling, and you can feel the tremors from your position. You are in no threat from it, though.")
          print("The earthquake trembles towards the north, and forms massive chasms in the desert ahead of you.")
          sleep(4)
          print("After a good break, you stand back up and try to see how far the chasms go. You can't tell.")
          e=input("1.Go far left and around. 2.Go left and around. 3.Go close left and around. (hugging the edge of the chasm) 4.Go close right and around. 5.Go right and around. 6.Go far right and around.")
          if e =="1":
            print("You decide to go far left and around.")
            sleep(3)
            print("The ground suddenly shakes beneath you, and you unfortunately fell into the chasms next to you.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="2":
            print("You decide to go left and around.")
            sleep(3)
            print("The ground suddenly shakes beneath you, and you unfortunately fell into the chasms next to you.")
            print("YOU DIED! THE END!")
          elif e =="3":
            print("You decide to go close left, hugging the chasm next to you.")
            sleep(3)
            print("The ground nearby starts shaking dramatically, and you lower yourself to keep yourself from falling into the chasms next to you.")
            print("Thankfully, the tremors were more noticeable on the left side of the chasms, so you remain mostly unaffected.")
            sleep(5)
            print("After a bit more of careful navigation, you make it past the chasms. The land starts to merge into the mountain base up ahead.")
            sleep(5)
            st=time.time()
            f=input("PRESS [D] to dodge laser targetting!").title()
            rt=time.time()-st
            if f =="D" and rt<2:
              print("You narrowly dodge a laser from a sniper nearby, and you slowly snuck your way to the mountains, unseen.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You were seen by a sniper nearby and they sniped you.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="4":
            print("You decide to go close right and around.")
            sleep(3)
            print("You stepped into a bear trap. Who on earth puts a bear trap in the middle of the desert?")
            print("The pain made you scream, and you quickly drop down to deal with the trap. The only problem is, you were next to a chasm when you 'dropped down'.")
            print("Your pain was relieved.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="5":
            print("You decide to go right and around.")
            sleep(3)
            print("The area is filled to the brim with bear traps. You managed to notice because the ground shook a bit and revealed some of them through the sand.")
            print("Now you throw rocks in front of you to make sure it's safe.")
            sleep(4)
            print("After some careful navigation, you make it past the chasms. The land starts to merge into the mountain base up ahead.")
            sleep(5)
            st=time.time()
            f=input("PRESS [D] to dodge laser targetting!").title()
            rt=time.time()-st
            if f =="D" and rt<2:
              print("You narrowly dodge a laser from a sniper nearby, and you slowly snuck your way to the mountains, unseen.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You were seen by a sniper nearby and they sniped you.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to go far right and around, but suddenly the ground shakes, and you lose your balance.")
            print("You barely manage to avoid falling down a chasm, but you've stepped into a bear trap.")
            print("The pain made you scream, and you quickly drop down to deal with the trap. The only problem is, you were next to a chasm when you 'dropped down'.")
            print("Your pain was relieved.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You decide to get a move on and keep walking. Suddenly, the ground beneath you shakes.")
          print("There seems to be some sort of earthquake. The ground is breaking up behind you, and you start running in order to prevent falling through the chasms forming behind you.")
          sleep(3)
          print("You managed to run quite a bit, but your stamina is drained fully from the running.")
          print("You fell into the chasms and the fall killed you.")
          print("YOU DIED! THE END!")
    else:
      print("You decide to ignore the oasis and keep walking.")
      sleep(3)
      print("The heat is getting hard to bear.")
      print("Your vision is acting funny. There seems to be an oasis up ahead. You slowly trudge towards it.")
      sleep(4)
      print("You've reached it, and collapse onto the sand. Wait... Where's the water?")
      print("The heat got the best of you. YOU DIED! THE END!")
      die(player1)
  elif a =="2":
    print("You decide to keep heading north.")
    sleep(3)
    print("The sun is directly overhead now. The heat really is getting hard to bear.")
    b=input("1.Go northeast. 2.Continue down north. 3.Go northwest.")
    if b =="1":
      print("You decide to go northeast.")
      sleep(3)
      print("You've found some sort of building. You quickly head inside to hide from the burning sunlight.")
      sleep(3)
      print("Your carelessness meant that a bullet ended up in your head.")
      print("The monster that killed you smiles at your body.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="2":
      if player1.s3 == True:
        print("You endured through the heat and made it to some sort of well.")
        print("You quickly brought yourself a few buckets and poured it over yourself to cool yourself down, then drank another.")
        sleep(4)
        print("After hiding in the shade of the well for a break, you think that you should reach the mountains before sunset. You keep heading north.")
        sleep(3)
        print("You see a vehicle up ahead.")
        c=input("1.Hide behind a pile of dunes. 2.Sneak into the vehicle. 3.Scout the area for the vehicle owner. 4.Curve around the area and don't interact at all.")
        if c =="1":
          print("You decide to hide behind a pile of dunes.")
          sleep(3)
          print("A monster sneaks up on you and notices you.")
          print("The blood from your head paints the dunes a bright red.")
          die(player1)
        elif c =="2":
          print("You slowly head towards the vehicle.")
          sleep(6)
          st=time.time()
          d=input("PRESS [D] to duck behind cover!").title()
          rt=time.time()-st
          if d =="D" and rt<2:
            print("You quickly dive behind a sand dune to hide from the vision from the monster, presumably the owner of the vehicle.")
            print("You wonder how you should approach this.")
            e=input("1.Guns a blazing. 2.Sneak into the vehicle. 3.Use a distraction. 4.Stealth kill them.")
            if e =="1":
              print("You burst out of your hiding spot, guns a blazing.")
              print("Since the monster was not prepared for it, your bullets ended up riddled all over their corpse.")
              print("The flurry of bullets also revealed that there was a bear trap on the sand.")
              print("You carefully avoided the trap, looted the monster and hop onto the vehicle.")
              sleep(6)
              print("You drive your way towards the mountains.")
              sleep(5)
              st=time.time()
              f=input("PRESS [A] to avoid laser targetting!").title()
              rt=time.time()-st
              if f =="A" and rt<2:
                print("You narrowly dodge a laser from a sniper nearby, and you park your vehicle hidden in the bushes.")
                print("You take a deep breath at the mountains before you. This will be quite a climb.")
                player1.newSkill()
                nextChapter(player1)#####################
              else:
                print("You were seen by a sniper nearby and they sniped you.")
                print("YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You carefully sneak into the vehicle, and quickly start the engine and drive off, long before the monster realized what was going on.")
              print("You drove off into the desert landscape, and eventually the mountains are just up ahead.")
              sleep(7)
              st=time.time()
              f=input("PRESS [A] to avoid laser targetting!").title()
              rt=time.time()-st
              if f =="A" and rt<2:
                print("You narrowly dodge a laser from a sniper nearby, and you park your vehicle hidden in the bushes.")
                print("You take a deep breath at the mountains before you. This will be quite a climb.")
                player1.newSkill()
                nextChapter(player1)#####################
              else:
                print("You were seen by a sniper nearby and they sniped you.")
                print("YOU DIED! THE END!")
                die(player1)
            elif e =="3":
              print("You decide to use a distraction.")
              print("You throw a rock past their head. They don't notice.")
              print("You throw a rock next to their head. They don't notice.")
              sleep(5)
              print("You throw a rock -")
              sleep(3)
              print("-And it hit them in the back of the head.")
              print("They quickly turned around and since you weren't prepared, they drew their gun faster than you and your head blew up.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You slowly sneak towards the monster to kill them...")
              sleep(4)
              print("'OWWWW!!!!'")
              print("You stepped into a bear trap, which alerted the monster of your prescence.")
              print("It was the cleanest 180 flick you've ever witnessed.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You failed to duck behind cover and the owner saw you.")
            print("They shot you in the head and probably ate you for dinner.")
            print("YOU DIED! THE END!")
            die(player1)
        elif c =="3":
          print("You decide to sneak around the area, to look for the owner of the vehicle.")
          sleep(3)
          print("You made one too many loud steps and alerted the vehicle owner. They snuck behind you and shot you in the head. YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to curve around the area and ignore the vehicle altogther.")
          print("You seem to making some good distance, but you are starting to get tired.")
          d=input("1.Take a break. 2.Take a break later and keep moving now.")
          if d =="1":
            print("You decide to take a break. The ground ahead of you starts trembling, and you can feel the tremors from your position. You are in no threat from it, though.")
            print("The earthquake trembles towards the north, and forms massive chasms in the desert ahead of you.")
            sleep(4)
            print("After a good break, you stand back up and try to see how far the chasms go. You can't tell.")
            e=input("1.Go far left and around. 2.Go left and around. 3.Go close left and around. (hugging the edge of the chasm) 4.Go close right and around. 5.Go right and around. 6.Go far right and around.")
            if e =="1":
              print("You decide to go far left and around.")
              sleep(3)
              print("The ground suddenly shakes beneath you, and you unfortunately fell into the chasms next to you.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="2":
              print("You decide to go left and around.")
              sleep(3)
              print("The ground suddenly shakes beneath you, and you unfortunately fell into the chasms next to you.")
              print("YOU DIED! THE END!")
            elif e =="3":
              print("You decide to go close left, hugging the chasm next to you.")
              sleep(3)
              print("The ground nearby starts shaking dramatically, and you lower yourself to keep yourself from falling into the chasms next to you.")
              print("Thankfully, the tremors were more noticeable on the left side of the chasms, so you remain mostly unaffected.")
              sleep(5)
              print("After a bit more of careful navigation, you make it past the chasms. The land starts to merge into the mountain base up ahead.")
              sleep(5)
              st=time.time()
              f=input("PRESS [D] to dodge laser targetting!").title()
              rt=time.time()-st
              if f =="D" and rt<2:
                print("You narrowly dodge a laser from a sniper nearby, and you slowly snuck your way to the mountains, unseen.")
                player1.newSkill()
                nextChapter(player1)#####################
              else:
                print("You were seen by a sniper nearby and they sniped you.")
                print("YOU DIED! THE END!")
                die(player1)
            elif e =="4":
              print("You decide to go close right and around.")
              sleep(3)
              print("You stepped into a bear trap. Who on earth puts a bear trap in the middle of the desert?")
              print("The pain made you scream, and you quickly drop down to deal with the trap. The only problem is, you were next to a chasm when you 'dropped down'.")
              print("Your pain was relieved.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="5":
              print("You decide to go right and around.")
              sleep(3)
              print("The area is filled to the brim with bear traps. You managed to notice because the ground shook a bit and revealed some of them through the sand.")
              print("Now you throw rocks in front of you to make sure it's safe.")
              sleep(4)
              print("After some careful navigation, you make it past the chasms. The land starts to merge into the mountain base up ahead.")
              sleep(5)
              st=time.time()
              f=input("PRESS [D] to dodge laser targetting!").title()
              rt=time.time()-st
              if f =="D" and rt<2:
                print("You narrowly dodge a laser from a sniper nearby, and you slowly snuck your way to the mountains, unseen.")
                player1.newSkill()
                nextChapter(player1)#####################
              else:
                print("You were seen by a sniper nearby and they sniped you.")
                print("YOU DIED! THE END!")
                die(player1)
            else:
              print("You decide to go far right and around, but suddenly the ground shakes, and you lose your balance.")
              print("You barely manage to avoid falling down a chasm, but you've stepped into a bear trap.")
              print("The pain made you scream, and you quickly drop down to deal with the trap. The only problem is, you were next to a chasm when you 'dropped down'.")
              print("Your pain was relieved.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to get a move on and keep walking. Suddenly, the ground beneath you shakes.")
            print("There seems to be some sort of earthquake. The ground is breaking up behind you, and you start running in order to prevent falling through the chasms forming behind you.")
            sleep(3)
            print("You managed to run quite a bit, but your stamina is drained fully from the running.")
            print("You fell into the chasms and the fall killed you.")
            print("YOU DIED! THE END!")
      else:
        print("The heat got the best of you, and you collapsed in the middle of the desert. No one will find your body.")
        print("YOU DIED! THE END!")
        die(player1)
    else:
      print("You decide to go northwest. There is nothing there but heat, sand and now... bones.")
      print("Your bones.")
      print("The heat got the best of you. YOU DIED! THE END!")
      die(player1)
  else:
    print("You decide to go northwest.")
    sleep(3)
    print("Before you know it, you've found some sort of abandoned settlement. You could catch a break there. Maybe even get some more resources.")
    b=input("1.Catch a break in the settlement. 2.Loot the place. 3.Ignore it. 4.Take a break on the sand.")
    if b =="1":
      print("You snuck into the settlement and went into the one farthest from the core of the settlement area. You had a good break and good shade from the sun, as well.")
      print("You snuck back out into the desert and take a deep breath to ready yourself.")
      print("It might be clever to curve back towards the mountains soon.")
      c=input("1.Head northeast. 2.Head north. 3.Head northwest.")
      if c =="1":
        print("You head northeast, and are back on track to your destination.")
        sleep(5)
        print("You're starting to get a bit tired...")
        d=input("1.Take a break. 2.Take a break later and keep moving now.")
        if d =="1":
          print("You decide to take a break. The ground ahead of you starts trembling, and you can feel the tremors from your position. You are in no threat from it, though.")
          print("The earthquake trembles towards the north, and forms massive chasms in the desert ahead of you.")
          sleep(4)
          print("After a good break, you stand back up and try to see how far the chasms go. You can't tell.")
          e=input("1.Go far left and around. 2.Go left and around. 3.Go close left and around. (hugging the edge of the chasm) 4.Go close right and around. 5.Go right and around. 6.Go far right and around.")
          if e =="1":
            print("You decide to go far left and around.")
            sleep(3)
            print("The ground suddenly shakes beneath you, and you unfortunately fell into the chasms next to you.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="2":
            print("You decide to go left and around.")
            sleep(3)
            print("The ground suddenly shakes beneath you, and you unfortunately fell into the chasms next to you.")
            print("YOU DIED! THE END!")
          elif e =="3":
            print("You decide to go close left, hugging the chasm next to you.")
            sleep(3)
            print("The ground nearby starts shaking dramatically, and you lower yourself to keep yourself from falling into the chasms next to you.")
            print("Thankfully, the tremors were more noticeable on the left side of the chasms, so you remain mostly unaffected.")
            sleep(5)
            print("After a bit more of careful navigation, you make it past the chasms. The land starts to merge into the mountain base up ahead.")
            sleep(5)
            st=time.time()
            f=input("PRESS [D] to dodge laser targetting!").title()
            rt=time.time()-st
            if f =="D" and rt<2:
              print("You narrowly dodge a laser from a sniper nearby, and you slowly snuck your way to the mountains, unseen.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You were seen by a sniper nearby and they sniped you.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="4":
            print("You decide to go close right and around.")
            sleep(3)
            print("You stepped into a bear trap. Who on earth puts a bear trap in the middle of the desert?")
            print("The pain made you scream, and you quickly drop down to deal with the trap. The only problem is, you were next to a chasm when you 'dropped down'.")
            print("Your pain was relieved.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="5":
            print("You decide to go right and around.")
            sleep(3)
            print("The area is filled to the brim with bear traps. You managed to notice because the ground shook a bit and revealed some of them through the sand.")
            print("Now you throw rocks in front of you to make sure it's safe.")
            sleep(4)
            print("After some careful navigation, you make it past the chasms. The land starts to merge into the mountain base up ahead.")
            sleep(5)
            st=time.time()
            f=input("PRESS [D] to dodge laser targetting!").title()
            rt=time.time()-st
            if f =="D" and rt<2:
              print("You narrowly dodge a laser from a sniper nearby, and you slowly snuck your way to the mountains, unseen.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You were seen by a sniper nearby and they sniped you.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to go far right and around, but suddenly the ground shakes, and you lose your balance.")
            print("You barely manage to avoid falling down a chasm, but you've stepped into a bear trap.")
            print("The pain made you scream, and you quickly drop down to deal with the trap. The only problem is, you were next to a chasm when you 'dropped down'.")
            print("Your pain was relieved.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You decide to get a move on and keep walking. Suddenly, the ground beneath you shakes.")
          print("There seems to be some sort of earthquake. The ground is breaking up behind you, and you start running in order to prevent falling through the chasms forming behind you.")
          sleep(3)
          print("You managed to run quite a bit, but your stamina is drained fully from the running.")
          print("You fell into the chasms and the fall killed you.")
          print("YOU DIED! THE END!")
      elif c =="2":
        print("You decide to head north. You arrived at a plains. Some sort of smoke is coming from something up ahead. What is that? It's coming towards you...")
        sleep(3)
        print("Some sort of bomb drops right next to you.")
        print("YOU DIED! THE END!")
        die(player1)
      else:
        print("You head further northwest, and the desert eventually becomes some sort of savanna.")
        print("A sniper tower spotted you and you died within the blink of an eye.")
        print("YOU DIED! THE END!")
        die(player1)
    elif b =="2":
      print("Expecting no one to be living in these terrible conditions, you head right into the settlement to loot the place.")
      sleep(3)
      print("The monster behind you begs to differ, and introduces a bullet into the back of your head.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="3":
      print("You decide to ignore it and keep moving, but some monsters in the settlement saw you and they had a sniper.")
      print("One shot, one kill.")
      print("YOU DIED! THE END!")
      die(player1)
    else:
      print("You decide to take a quick break on the sand, and although it wasn't great, you recovered enough energy to keep going.")
      print("However, it might be clever to curve back towards the mountains soon.")
      c=input("1.Head northeast. 2.Head north. 3.Head northwest.")
      if c =="1":
        print("You head northeast, and are back on track to your destination.")
        sleep(5)
        print("You're starting to get a bit tired...")
        d=input("1.Take a break. 2.Take a break later and keep moving now.")
        if d =="1":
          print("You decide to take a break. The ground ahead of you starts trembling, and you can feel the tremors from your position. You are in no threat from it, though.")
          print("The earthquake trembles towards the north, and forms massive chasms in the desert ahead of you.")
          sleep(4)
          print("After a good break, you stand back up and try to see how far the chasms go. You can't tell.")
          e=input("1.Go far left and around. 2.Go left and around. 3.Go close left and around. (hugging the edge of the chasm) 4.Go close right and around. 5.Go right and around. 6.Go far right and around.")
          if e =="1":
            print("You decide to go far left and around.")
            sleep(3)
            print("The ground suddenly shakes beneath you, and you unfortunately fell into the chasms next to you.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="2":
            print("You decide to go left and around.")
            sleep(3)
            print("The ground suddenly shakes beneath you, and you unfortunately fell into the chasms next to you.")
            print("YOU DIED! THE END!")
          elif e =="3":
            print("You decide to go close left, hugging the chasm next to you.")
            sleep(3)
            print("The ground nearby starts shaking dramatically, and you lower yourself to keep yourself from falling into the chasms next to you.")
            print("Thankfully, the tremors were more noticeable on the left side of the chasms, so you remain mostly unaffected.")
            sleep(5)
            print("After a bit more of careful navigation, you make it past the chasms. The land starts to merge into the mountain base up ahead.")
            sleep(5)
            st=time.time()
            f=input("PRESS [D] to dodge laser targetting!").title()
            rt=time.time()-st
            if f =="D" and rt<2:
              print("You narrowly dodge a laser from a sniper nearby, and you slowly snuck your way to the mountains, unseen.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You were seen by a sniper nearby and they sniped you.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="4":
            print("You decide to go close right and around.")
            sleep(3)
            print("You stepped into a bear trap. Who on earth puts a bear trap in the middle of the desert?")
            print("The pain made you scream, and you quickly drop down to deal with the trap. The only problem is, you were next to a chasm when you 'dropped down'.")
            print("Your pain was relieved.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="5":
            print("You decide to go right and around.")
            sleep(3)
            print("The area is filled to the brim with bear traps. You managed to notice because the ground shook a bit and revealed some of them through the sand.")
            print("Now you throw rocks in front of you to make sure it's safe.")
            sleep(4)
            print("After some careful navigation, you make it past the chasms. The land starts to merge into the mountain base up ahead.")
            sleep(5)
            st=time.time()
            f=input("PRESS [D] to dodge laser targetting!").title()
            rt=time.time()-st
            if f =="D" and rt<2:
              print("You narrowly dodge a laser from a sniper nearby, and you slowly snuck your way to the mountains, unseen.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You were seen by a sniper nearby and they sniped you.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to go far right and around, but suddenly the ground shakes, and you lose your balance.")
            print("You barely manage to avoid falling down a chasm, but you've stepped into a bear trap.")
            print("The pain made you scream, and you quickly drop down to deal with the trap. The only problem is, you were next to a chasm when you 'dropped down'.")
            print("Your pain was relieved.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You decide to get a move on and keep walking. Suddenly, the ground beneath you shakes.")
          print("There seems to be some sort of earthquake. The ground is breaking up behind you, and you start running in order to prevent falling through the chasms forming behind you.")
          sleep(3)
          print("You managed to run quite a bit, but your stamina is drained fully from the running.")
          print("You fell into the chasms and the fall killed you.")
          print("YOU DIED! THE END!")
      elif c =="2":
        print("You decide to head north. You arrived at a plains. Some sort of smoke is coming from something up ahead. What is that? It's coming towards you...")
        sleep(3)
        print("Some sort of bomb drops right next to you.")
        print("YOU DIED! THE END!")
        die(player1)
      else:
        print("You head further northwest, and the desert eventually becomes some sort of savanna.")
        print("A sniper tower spotted you and you died within the blink of an eye.")
        print("YOU DIED! THE END!")
        die(player1)

def redDesert(player1):#Used in 3 scenes. Formatted for ALONE WITH APPRENTICE
  print("You decide to head towards the mountains through the red desert.")
  print("The landscape might be rough, but that means you'll have less of a chance of running into any monsters.")
  sleep(3)
  print("The heat is getting hard to bear, and the red tinge across the landscape isn't exactly soothing either.")
  print("The mountains are roughly north of here.")
  print("You glance at Haley. She seems to be struggling with the heat.")
  a=input("1.Go north. 2.Go northwest. 3.Go northeast. 4.Go east. 5.Go west.")
  if a =="1":
    print("You decide to go straight north.")
    sleep(4)
    print("Unfortunately, the landscape did not get any better and he both of you collapsed in due time.")
    print("YOU DIED! THE END!")
  elif a =="2":
    print("You decide to go northwest.")
    sleep(2)
    print("Thankfully, there was a small abandoned village in that direction and you were able to take a break in one of the houses and refill your bottles using the well, which was surprisingly not dried out.")
    print("After a good enough break, you and Haley start to prepare to leave, only to hear the sound of a car engine approaching the village.")
    b=input("1.Hide in the house you are in right now. 2.Relocate and hide in a different house. 3.Don't hide. Sneak around the place to avoid them. 4.Stealthily attack them.")
    if b =="1":
      print("You stay where you are, deciding to wait them out.")
      print("You hear the car stop nearby, and you hear someone dismount. Someone? Or were there multiple someones?")
      print("You supress your thoughts, and remain stationary in the house you are in.")
      sleep(5)
      print("Eventually, the car drives away.")
      print("After a suitable period of waiting for confirmation, you and Haley head out once again.")
      c=input("1.Head north. 2.Head northeast. 3.Head northwest.")
      if c =="1":
        print("You head north.")
        sleep(3)
        print("The heat is becoming hard to bear.")
        print("You find some sort of underground cave, so you and Haley went inside to take a break.")
        sleep(3)
        print("The ground suddenly trembles and the cave entrance collapses. You won't be getting out that way.")
        print("You bring out a lighter and create a makeshift torch.")
        print("You venture deeper into the cave, looking for a way out.")
        sleep(3)
        print("Eventually, you reach a crossroads in the cave.")
        d=input("1.Go left. 2.Go straight. 3.Go right.")
        if d =="1":
          print("Fingers crossed, you go left.")
          sleep(3)
          print("Your fingers were still crossed when the cave collapsed onto you. Probably could've used those to mitigate some of the damage.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You decide to head straight forwards. It eventually opens up back to the surface.")
          print("You quickly duck back down. There was a sniper tower really close by.")
          print("You would have to sneak right under it.")
          sleep(5)
          print("You slowly leave the cave, and sneak towards directly under the tower.")
          sleep(3)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You decide to turn right.")
          sleep(3)
          print("Eventually, it leads you back to the surface.")
          print("There seems to be some sort of ancient shrine thing up ahead.")
          e=input("1.Check it out. 2.Leave it alone, and head north. 3.Leave it alone, and head northeast. 4.Leave it alone, and head northwest.")
          if e =="1":
            print("You walk over to the shrine.")
            print("A jug of water is placed on the shrine.")
            print("You pick it up and some sort of mechanism runs behind the shrine.")
            sleep(5)
            print("The whole statue shakes, and blows up.")
            print("You quickly drop down to dodge the flying debris.")
            print("A light behind the shrine starts flashing red.")
            print("Perhaps some monsters are on their way here now.")
            f=input("1.Run north. 2.Run northeast. 3.Run northwest.")
            if f =="1":
              print("You start running north, but the barren landscape leads to even more barren landscape, with nothing providing cover for you and Haley.")
              sleep(3)
              print("Eventually, you've exhausted your resources and still have not found the mountains.")
              print("You drop onto the sand in exhaustion.")
              sleep(5)
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You decide to run northeast, only to run directly into the approaching monsters.")
              print("They shot you with no mercy.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to run northwest, successfully avoiding the monsters.")
              sleep(4)
              print("Eventually, you reach the mountains. You take a deep breath.")
              print("This is going to be a long hike.")
              player1.newSkill()
              nextChapter(player1)##################### 
          elif e =="2":
            print("You leave it alone, and head north.")
            sleep(4)
            print("You see some sort of massive statue up ahead.")
            f=input("1.Investigate the statue. 2.Hide. 3.Keep walking. 4.Blow the statue up.")
            if f =="1":
              print("You walk up to the statue.")
              sleep(4)
              print("Suddenly, two monsters jump out from either side of the statue, guns raised.")
              print("You were shot so, so many times.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You quickly hide behind a rock.")
              sleep(4)
              print("Nothing happens.")
              sleep(6)
              print("Nothing happens.")
              g=input("1.Stay. 2.Leave the hiding spot.")
              if g =="1":
                print("You decide to stay.")
                sleep(5)
                print("Eventually, you hear a group of four monsters leaving from behind the statue.")
                print("You surprise attack them, and since all of them had their backs to you in was an easy victory.")
                print("You head north once more and arrive at the base of the mountians.")
                print("'Here we go.' You say.")
                player1.newSkill()
                nextChapter(player1)##################### 
              else:
                print("You leave the hiding spot, and the moment you made a step, two monsters jump out from either side of the statue, guns raised.")
                print("Your body was littered with bullets.")
                print("YOU IDED! THE END!")
                die(player1)
            elif f =="3":
              print("You decide to keep walking.")
              sleep(4)
              print("Suddenly, two monsters jump out from either side of the statue, guns raised.")
              print("You were shot so, so many times.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You blow the hell out of the statue, which also meant you blew up the hidden monsters behind the statue, too.")
              print("You quickly looted the monsters' bodies and head north.")
              sleep(4)
              print("You eventually arrived at the base of the mountains.")
              print("'Here we go.' You say.")
              player1.newSkill()
              nextChapter(player1)##################### 
          elif e =="3":
            print("You leave it alone, and head northeast.")
            sleep(3)
            print("You wandered into the range of a sniper tower.")
            print("One shot, one kill.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You leave it alone, and head northwest.")
            sleep(3)
            print("You wandered into the range of a sniper tower.")
            print("One shot, one kill.")
            print("YOU DIED! THE END!")
            die(player1)
      elif c =="2":
        print("You head northeast, bringing you back on track for the path for the mountains.")
        sleep(3)
        print("You quickly take cover behind a rock when you see the tower up ahead.")
        print("You slowly peek out and scan the area. It looks like it's only the tower, but there may be other monsters about.")
        d=input("1.Sneak under and past the tower. 2.Try to fight the sniper on the tower. 3.Sneak around, far away from the tower. 4.Cause a distraction.")
        if d =="1":
          print("You decide to sneak directly under the tower.")
          print("You found an opening, and quickly ran towards the under side of the tower. They shouldn't be able to see you here.")
          sleep(4)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to shoot at the sniper, but surprisingly, they're a better shot than you.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to double back and curve around the tower the long way.")
          print("But what you didn't realize...")
          print("Was that there was another tower in the area you tried to curve around through.")
          print("Your skull cracked open smoothly.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to distract the sniper.")
          print("You bring out a bottle, and put a rag inside it. You pour some oil inside it, and set it alight.")
          print("You throw it off into the distance, catching the sniper's attention.")
          sleep(4)
          print("You hear three monsters get dispatched to the molotov's location to check it out.")
          print("There probably aren't any monsters left at the tower other than the sniper.")
          e=input("1.Run under the tower. 2.Run around the tower. 3.Stay here. 4.Kill the monsters.")
          if e =="1":
            print("You quickly run under the tower unseen.")
            sleep(3)
            print("The monsters still seem to be focused on the molotov, but you are unsure whether you have enough time to run far enough by the time they stop investigating it.")
            f=input("1.Make a run for it. 2.Stay hidden under the tower. 3.Cause another distraction.")
            if f =="1":
              print("You make a run for it, only to be seen by the sniper at the top of the tower.")
              print("You were shot right in the leg before a clean headshot.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You stay hidden under the tower, and after a good enough wait, you peek out to ensure the coast is clear.")
              sleep(3)
              print("The coast is clear.")
              print("You slowly sneak towards the forest at the base of the mountains and reached there successfully without being seen.")
              sleep(4)
              print("You take in the size of the mountains up ahead and take a deep breath.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You try to set up another distraction, but you were so distracted by setting up the next distraction that you didn't notice the monster sneaking up behind you.")
              print("They strangled you to death. After they shot you with a shotgun.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to run around the tower unseen, but it took too long and the sniper saw you running across.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You stay where you are, but eventually one of the monsters saw your location and they were too much for you to fight off.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You attack the monsters while they are distracted and they died swiftly.")
            print("Now there's only the sniper left at the tower.")
            f=input("1.Peek the sniper and shoot. 2.Wait. 3.Run across to the next bit of cover, and so on. 4.Run straight north.")
            if f =="1":
              print("You quickly peek the sniper and try to shoot back, but unfortunately the sniper was watching your angle and headshotted you.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You wait where you are.")
              sleep(7)
              print("Suddenly, you peek out, and the sniper wasn't ready.")
              print("They missed their shot and you somehow managed to headshot them.")
              print("With the tower dealt with, you reached the mountains without any more hitches.")
              player1.newSkill()
              nextChapter(player1)##################### 
            elif f =="3":
              print("You quickly relocate to the next bit of cover, baiting out a shot from the sniper.")
              sleep(5)
              print("You do it again, and they miss again.")
              sleep(4)
              print("You do it a third time, and this time, rather than running all the way to the next bit of cover, you stop right in the middle between the covers and aim for the sniper's head.")
              print("It was a clean headshot.")
              print("With that out of the way, you reached the mountains easily.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You start running straight north.")
              sleep(4)
              print("You managed to dodge the first few shots, but your luck ran out eventually and you were shot right in the back, and later on, your neck.")
              print("YOU DIED! THE END!")
              die(player1)
      else:
        print("You decide to head northwest.")
        sleep(3)
        print("That's strange. The desert ends here. There's a forest right ahead of you.")
        print("Suddenly, you've been shot in the head.")
        print("A sniper hidden in the forest must have seen you. YOU DIED! THE END!")
        die(player1)
    elif b =="2":
      print("You decide to leave the house you're currently in, and relocate to a new one.")
      print("Unfortunately, one of the monsters noticed your movement and they snuck up on you with some shotguns.")
      print("It was not pretty.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="3":
      print("You slowly lead Haley out of the house, and the two of you stealthily sneak around the houses when you hear any footsteps. After doing this for a while, the monsters got back to their car and drove off.")
      c=input("1.Head north. 2.Head northeast. 3.Head northwest.")
      if c =="1":
        print("You head north.")
        sleep(3)
        print("The heat is becoming hard to bear.")
        print("You find some sort of underground cave, so you and Haley went inside to take a break.")
        sleep(3)
        print("The ground suddenly trembles and the cave entrance collapses. You won't be getting out that way.")
        print("You bring out a lighter and create a makeshift torch.")
        print("You venture deeper into the cave, looking for a way out.")
        sleep(3)
        print("Eventually, you reach a crossroads in the cave.")
        d=input("1.Go left. 2.Go straight. 3.Go right.")
        if d =="1":
          print("Fingers crossed, you go left.")
          sleep(3)
          print("Your fingers were still crossed when the cave collapsed onto you. Probably could've used those to mitigate some of the damage.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You decide to head straight forwards. It eventually opens up back to the surface.")
          print("You quickly duck back down. There was a sniper tower really close by.")
          print("You would have to sneak right under it.")
          sleep(5)
          print("You slowly leave the cave, and sneak towards directly under the tower.")
          sleep(3)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You decide to turn right.")
          sleep(3)
          print("Eventually, it leads you back to the surface.")
          print("There seems to be some sort of ancient shrine thing up ahead.")
          e=input("1.Check it out. 2.Leave it alone, and head north. 3.Leave it alone, and head northeast. 4.Leave it alone, and head northwest.")
          if e =="1":
            print("You walk over to the shrine.")
            print("A jug of water is placed on the shrine.")
            print("You pick it up and some sort of mechanism runs behind the shrine.")
            sleep(5)
            print("The whole statue shakes, and blows up.")
            print("You quickly drop down to dodge the flying debris.")
            print("A light behind the shrine starts flashing red.")
            print("Perhaps some monsters are on their way here now.")
            f=input("1.Run north. 2.Run northeast. 3.Run northwest.")
            if f =="1":
              print("You start running north, but the barren landscape leads to even more barren landscape, with nothing providing cover for you and Haley.")
              sleep(3)
              print("Eventually, you've exhausted your resources and still have not found the mountains.")
              print("You drop onto the sand in exhaustion.")
              sleep(5)
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You decide to run northeast, only to run directly into the approaching monsters.")
              print("They shot you with no mercy.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to run northwest, successfully avoiding the monsters.")
              sleep(4)
              print("Eventually, you reach the mountains. You take a deep breath.")
              print("This is going to be a long hike.")
              player1.newSkill()
              nextChapter(player1)##################### 
          elif e =="2":
            print("You leave it alone, and head north.")
            sleep(4)
            print("You see some sort of massive statue up ahead.")
            f=input("1.Investigate the statue. 2.Hide. 3.Keep walking. 4.Blow the statue up.")
            if f =="1":
              print("You walk up to the statue.")
              sleep(4)
              print("Suddenly, two monsters jump out from either side of the statue, guns raised.")
              print("You were shot so, so many times.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You quickly hide behind a rock.")
              sleep(4)
              print("Nothing happens.")
              sleep(6)
              print("Nothing happens.")
              g=input("1.Stay. 2.Leave the hiding spot.")
              if g =="1":
                print("You decide to stay.")
                sleep(5)
                print("Eventually, you hear a group of four monsters leaving from behind the statue.")
                print("You surprise attack them, and since all of them had their backs to you in was an easy victory.")
                print("You head north once more and arrive at the base of the mountians.")
                print("'Here we go.' You say.")
                player1.newSkill()
                nextChapter(player1)##################### 
              else:
                print("You leave the hiding spot, and the moment you made a step, two monsters jump out from either side of the statue, guns raised.")
                print("Your body was littered with bullets.")
                print("YOU IDED! THE END!")
                die(player1)
            elif f =="3":
              print("You decide to keep walking.")
              sleep(4)
              print("Suddenly, two monsters jump out from either side of the statue, guns raised.")
              print("You were shot so, so many times.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You blow the hell out of the statue, which also meant you blew up the hidden monsters behind the statue, too.")
              print("You quickly looted the monsters' bodies and head north.")
              sleep(4)
              print("You eventually arrived at the base of the mountains.")
              print("'Here we go.' You say.")
              player1.newSkill()
              nextChapter(player1)##################### 
          elif e =="3":
            print("You leave it alone, and head northeast.")
            sleep(3)
            print("You wandered into the range of a sniper tower.")
            print("One shot, one kill.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You leave it alone, and head northwest.")
            sleep(3)
            print("You wandered into the range of a sniper tower.")
            print("One shot, one kill.")
            print("YOU DIED! THE END!")
            die(player1)
      elif c =="2":
        print("You head northeast, bringing you back on track for the path for the mountains.")
        sleep(3)
        print("You quickly take cover behind a rock when you see the tower up ahead.")
        print("You slowly peek out and scan the area. It looks like it's only the tower, but there may be other monsters about.")
        d=input("1.Sneak under and past the tower. 2.Try to fight the sniper on the tower. 3.Sneak around, far away from the tower. 4.Cause a distraction.")
        if d =="1":
          print("You decide to sneak directly under the tower.")
          print("You found an opening, and quickly ran towards the under side of the tower. They shouldn't be able to see you here.")
          sleep(4)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to shoot at the sniper, but surprisingly, they're a better shot than you.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to double back and curve around the tower the long way.")
          print("But what you didn't realize...")
          print("Was that there was another tower in the area you tried to curve around through.")
          print("Your skull cracked open smoothly.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to distract the sniper.")
          print("You bring out a bottle, and put a rag inside it. You pour some oil inside it, and set it alight.")
          print("You throw it off into the distance, catching the sniper's attention.")
          sleep(4)
          print("You hear three monsters get dispatched to the molotov's location to check it out.")
          print("There probably aren't any monsters left at the tower other than the sniper.")
          e=input("1.Run under the tower. 2.Run around the tower. 3.Stay here. 4.Kill the monsters.")
          if e =="1":
            print("You quickly run under the tower unseen.")
            sleep(3)
            print("The monsters still seem to be focused on the molotov, but you are unsure whether you have enough time to run far enough by the time they stop investigating it.")
            f=input("1.Make a run for it. 2.Stay hidden under the tower. 3.Cause another distraction.")
            if f =="1":
              print("You make a run for it, only to be seen by the sniper at the top of the tower.")
              print("You were shot right in the leg before a clean headshot.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You stay hidden under the tower, and after a good enough wait, you peek out to ensure the coast is clear.")
              sleep(3)
              print("The coast is clear.")
              print("You slowly sneak towards the forest at the base of the mountains and reached there successfully without being seen.")
              sleep(4)
              print("You take in the size of the mountains up ahead and take a deep breath.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You try to set up another distraction, but you were so distracted by setting up the next distraction that you didn't notice the monster sneaking up behind you.")
              print("They strangled you to death. After they shot you with a shotgun.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to run around the tower unseen, but it took too long and the sniper saw you running across.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You stay where you are, but eventually one of the monsters saw your location and they were too much for you to fight off.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You attack the monsters while they are distracted and they died swiftly.")
            print("Now there's only the sniper left at the tower.")
            f=input("1.Peek the sniper and shoot. 2.Wait. 3.Run across to the next bit of cover, and so on. 4.Run straight north.")
            if f =="1":
              print("You quickly peek the sniper and try to shoot back, but unfortunately the sniper was watching your angle and headshotted you.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You wait where you are.")
              sleep(7)
              print("Suddenly, you peek out, and the sniper wasn't ready.")
              print("They missed their shot and you somehow managed to headshot them.")
              print("With the tower dealt with, you reached the mountains without any more hitches.")
              player1.newSkill()
              nextChapter(player1)##################### 
            elif f =="3":
              print("You quickly relocate to the next bit of cover, baiting out a shot from the sniper.")
              sleep(5)
              print("You do it again, and they miss again.")
              sleep(4)
              print("You do it a third time, and this time, rather than running all the way to the next bit of cover, you stop right in the middle between the covers and aim for the sniper's head.")
              print("It was a clean headshot.")
              print("With that out of the way, you reached the mountains easily.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You start running straight north.")
              sleep(4)
              print("You managed to dodge the first few shots, but your luck ran out eventually and you were shot right in the back, and later on, your neck.")
              print("YOU DIED! THE END!")
              die(player1)
      else:
        print("You decide to head northwest.")
        sleep(3)
        print("That's strange. The desert ends here. There's a forest right ahead of you.")
        print("Suddenly, you've been shot in the head.")
        print("A sniper hidden in the forest must have seen you. YOU DIED! THE END!")
        die(player1)
    else:
      print("You and Haley exit the house, and slowly sneak towards the sound of the engine. You approach a corner, and just as you are about to turn around it, you find two large monsters wielding shotguns.")
      print("You were not victorious in that encounter.")
      print("YOU DIED! THE END!")
      die(player1)
  elif a =="3":
    print("You decide to head northeast.")
    sleep(4)
    print("The red sand stings your eyes. You can't seem to move forwards any more.")
    print("You look to your left. Where is Haley? Where... is...")
    print("You collapsed and died. THE END!")
    die(player1)
  elif a =="4":
    print("You decide to head east.")
    sleep(5)
    print("You come across an oasis. You and Haley take a good break there and refill your bottles.")
    print("After a sufficient break, you two head off once again.")
    sleep(5)
    print("The wind suddenly starts howling behind you.")
    print("You turn to find a sandstorm roaring through the desert behind you.")
    b=input("1.Run left. 2.Run right. 3.Run forwards. 4.Run forwards and to the left. 5.Run forwards and ro the right.")
    if b =="1":
      print("You decide to run towards the left, but the terrain does not get better, and eventually the sandstorm catches up.")
      print("The dust and sand fill up your lungs.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="2":
      print("You decide to run towards the right, and thankfully the sandstorm didn't follow you.")
      print("Something feels a bit weird. You don't recall being this short.")
      print("You look down, and find yourself sinking in quicksand. You look at Haley, who is already fully submerged. You take a deep breath, but unfortunately for you, that isn't going to help.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="3":
      print("You decide to run forwards, with the sandstorm is following closely behind you. ")
      sleep(3)
      print("You trip over, and you and Haley roll down into some sort of cave.")
      print("The sandstorm blows over above you, but you are protected against it thanks to the cave.")
      sleep(7)
      st=time.time()
      c=input("PRESS [D] to dodge the bullet!").title()
      rt=time.time()-st
      if c =="D" and rt<2:
        print("You quickly drop down to the ground, dodging the bullet.")
        sleep(5)
        st=time.time()
        d=input("PRESS [S] to shoot back!").title()
        rt=time.time()
        if d =="S" and rt<3:
          print("You quickly draw your pistol and shoot the monster in the head.")
          print("The gun drops from their hands and their body drops onto the ground, lifeless.")
          sleep(3)
          print("You anxiously check the area to make sure there's no one else.")
          print("The sandstorm has blown over, and you continue your journey.")
          sleep(4)
          print("Eventually, you see a sniper tower up ahead.")
          print("You decide to throw a molotov cocktail out to distract them.")
          sleep(4)
          print("You hear three monsters get dispatched to the molotov's location to check it out.")
          print("There probably aren't any monsters left at the tower other than the sniper.")
          e=input("1.Run under the tower. 2.Run around the tower. 3.Stay here. 4.Kill the monsters.")
          if e =="1":
            print("You quickly run under the tower unseen.")
            sleep(3)
            print("The monsters still seem to be focused on the molotov, but you are unsure whether you have enough time to run far enough by the time they stop investigating it.")
            f=input("1.Make a run for it. 2.Stay hidden under the tower. 3.Cause another distraction.")
            if f =="1":
              print("You make a run for it, only to be seen by the sniper at the top of the tower.")
              print("You were shot right in the leg before a clean headshot.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You stay hidden under the tower, and after a good enough wait, you peek out to ensure the coast is clear.")
              sleep(3)
              print("The coast is clear.")
              print("You slowly sneak towards the forest at the base of the mountains and reached there successfully without being seen.")
              sleep(4)
              print("You take in the size of the mountains up ahead and take a deep breath.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You try to set up another distraction, but you were so distracted by setting up the next distraction that you didn't notice the monster sneaking up behind you.")
              print("They strangled you to death. After they shot you with a shotgun.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to run around the tower unseen, but it took too long and the sniper saw you running across.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You stay where you are, but eventually one of the monsters saw your location and they were too much for you to fight off.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You attack the monsters while they are distracted and they died swiftly.")
            print("Now there's only the sniper left at the tower.")
            f=input("1.Peek the sniper and shoot. 2.Wait. 3.Run across to the next bit of cover, and so on. 4.Run straight north.")
            if f =="1":
              print("You quickly peek the sniper and try to shoot back, but unfortunately the sniper was watching your angle and headshotted you.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You wait where you are.")
              sleep(7)
              print("Suddenly, you peek out, and the sniper wasn't ready.")
              print("They missed their shot and you somehow managed to headshot them.")
              print("With the tower dealt with, you reached the mountains without any more hitches.")
              player1.newSkill()
              nextChapter(player1)##################### 
            elif f =="3":
              print("You quickly relocate to the next bit of cover, baiting out a shot from the sniper.")
              sleep(5)
              print("You do it again, and they miss again.")
              sleep(4)
              print("You do it a third time, and this time, rather than running all the way to the next bit of cover, you stop right in the middle between the covers and aim for the sniper's head.")
              print("It was a clean headshot.")
              print("With that out of the way, you reached the mountains easily.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You start running straight north.")
              sleep(4)
              print("You managed to dodge the first few shots, but your luck ran out eventually and you were shot right in the back, and later on, your neck.")
              print("YOU DIED! THE END!")
              die(player1)
        else:
          print("You reacted too slowly and you were shot in the chest this time.")
          print("YOU DIED! THE END!")
          die(player1)
      else:
        print("You failed to dodge an incoming bullet and you drop dead on the ground.")
        print("YOU DIED! THE END!")
        die(player1)
    elif b =="4":
      print("You decide to run forwards and to the left.")
      sleep(3)
      print("The sandstorm is following closely, and there seems to be a settlement up ahead.")
      print("You don't think you'd be able to reach it before the sandstorm catches up.")
      c=input("1.Run there anyways. 2.Take cover behind a rock. 3.Run backwards, through the storm.")
      if c =="1":
        print("You decide to keep running towards the settlement.")
        print("Unfortunately, as you anticipated, the storm caught up with you and you died.")
        print("YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You drop down and take cover behind a huge rock.")
        print("The rock blocks most of the storm and you barely managed to survive as it passed by.")
        sleep(4)
        print("After regrouping at the settlement, you head north once again.")
        print("You see a sniper tower up ahead, and quickly take cover behind a few dunes.")
        print("You only see the sniper, but there could be more monsters about.")
        d=input("1.Sneak under and past the tower. 2.Try to fight the sniper on the tower. 3.Sneak around, far away from the tower. 4.Cause a distraction.")
        if d =="1":
          print("You decide to sneak directly under the tower.")
          print("You found an opening, and quickly ran towards the under side of the tower. They shouldn't be able to see you here.")
          sleep(4)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to shoot at the sniper, but surprisingly, they're a better shot than you.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to double back and curve around the tower the long way.")
          print("But what you didn't realize...")
          print("Was that there was another tower in the area you tried to curve around through.")
          print("Your skull cracked open smoothly.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to distract the sniper.")
          print("You bring out a bottle, and put a rag inside it. You pour some oil inside it, and set it alight.")
          print("You throw it off into the distance, catching the sniper's attention.")
          sleep(4)
          print("You hear three monsters get dispatched to the molotov's location to check it out.")
          print("There probably aren't any monsters left at the tower other than the sniper.")
          e=input("1.Run under the tower. 2.Run around the tower. 3.Stay here. 4.Kill the monsters.")
          if e =="1":
            print("You quickly run under the tower unseen.")
            sleep(3)
            print("The monsters still seem to be focused on the molotov, but you are unsure whether you have enough time to run far enough by the time they stop investigating it.")
            f=input("1.Make a run for it. 2.Stay hidden under the tower. 3.Cause another distraction.")
            if f =="1":
              print("You make a run for it, only to be seen by the sniper at the top of the tower.")
              print("You were shot right in the leg before a clean headshot.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You stay hidden under the tower, and after a good enough wait, you peek out to ensure the coast is clear.")
              sleep(3)
              print("The coast is clear.")
              print("You slowly sneak towards the forest at the base of the mountains and reached there successfully without being seen.")
              sleep(4)
              print("You take in the size of the mountains up ahead and take a deep breath.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You try to set up another distraction, but you were so distracted by setting up the next distraction that you didn't notice the monster sneaking up behind you.")
              print("They strangled you to death. After they shot you with a shotgun.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to run around the tower unseen, but it took too long and the sniper saw you running across.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You stay where you are, but eventually one of the monsters saw your location and they were too much for you to fight off.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You attack the monsters while they are distracted and they died swiftly.")
            print("Now there's only the sniper left at the tower.")
            f=input("1.Peek the sniper and shoot. 2.Wait. 3.Run across to the next bit of cover, and so on. 4.Run straight north.")
            if f =="1":
              print("You quickly peek the sniper and try to shoot back, but unfortunately the sniper was watching your angle and headshotted you.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You wait where you are.")
              sleep(7)
              print("Suddenly, you peek out, and the sniper wasn't ready.")
              print("They missed their shot and you somehow managed to headshot them.")
              print("With the tower dealt with, you reached the mountains without any more hitches.")
              player1.newSkill()
              nextChapter(player1)##################### 
            elif f =="3":
              print("You quickly relocate to the next bit of cover, baiting out a shot from the sniper.")
              sleep(5)
              print("You do it again, and they miss again.")
              sleep(4)
              print("You do it a third time, and this time, rather than running all the way to the next bit of cover, you stop right in the middle between the covers and aim for the sniper's head.")
              print("It was a clean headshot.")
              print("With that out of the way, you reached the mountains easily.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You start running straight north.")
              sleep(4)
              print("You managed to dodge the first few shots, but your luck ran out eventually and you were shot right in the back, and later on, your neck.")
              print("YOU DIED! THE END!")
              die(player1)
      else:
        print("You decide to run back through the sandstorm.")
        print("It was the last decision of your life.")
        print("YOU DIED! THE END!")
        die(player1)
    else:
      print("You decide to run forwards and to the right, and thankfully the sandstorm didn't follow you.")
      print("Something feels a bit weird. You don't recall being this short.")
      print("You look down, and find yourself sinking in quicksand. You look at Haley, who is already fully submerged. You take a deep breath, but unfortunately for you, that isn't going to help.")
      print("YOU DIED! THE END!")
      die(player1)
  else:
    print("You decide to go west.")
    sleep(3)
    print("You managed to find an abandoned village just in time.")
    print("You took a good break and refilled your bottles from the well, which surprisingly, still worked.")
    sleep(3)
    print("Just as you are about to leave, you hear the rumble of a car engine approaching the village.")
    b=input("1.Hide in the house you are in right now. 2.Relocate and hide in a different house. 3.Don't hide. Sneak around the place to avoid them. 4.Stealthily attack them.")
    if b =="1":
      print("You stay where you are, deciding to wait them out.")
      print("You hear the car stop nearby, and you hear someone dismount. Someone? Or were there multiple someones?")
      print("You supress your thoughts, and remain stationary in the house you are in.")
      sleep(5)
      print("Eventually, the car drives away.")
      print("After a suitable period of waiting for confirmation, you and Haley head out once again.")
      c=input("1.Head north. 2.Head northeast. 3.Head northwest.")
      if c =="1":
        print("You head north.")
        sleep(3)
        print("The heat is becoming hard to bear.")
        print("You find some sort of underground cave, so you and Haley went inside to take a break.")
        sleep(3)
        print("The ground suddenly trembles and the cave entrance collapses. You won't be getting out that way.")
        print("You bring out a lighter and create a makeshift torch.")
        print("You venture deeper into the cave, looking for a way out.")
        sleep(3)
        print("Eventually, you reach a crossroads in the cave.")
        d=input("1.Go left. 2.Go straight. 3.Go right.")
        if d =="1":
          print("Fingers crossed, you go left.")
          sleep(3)
          print("Your fingers were still crossed when the cave collapsed onto you. Probably could've used those to mitigate some of the damage.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You decide to head straight forwards. It eventually opens up back to the surface.")
          print("You quickly duck back down. There was a sniper tower really close by.")
          print("You would have to sneak right under it.")
          sleep(5)
          print("You slowly leave the cave, and sneak towards directly under the tower.")
          sleep(3)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You decide to turn right.")
          sleep(3)
          print("Eventually, it leads you back to the surface.")
          print("There seems to be some sort of ancient shrine thing up ahead.")
          e=input("1.Check it out. 2.Leave it alone, and head north. 3.Leave it alone, and head northeast. 4.Leave it alone, and head northwest.")
          if e =="1":
            print("You walk over to the shrine.")
            print("A jug of water is placed on the shrine.")
            print("You pick it up and some sort of mechanism runs behind the shrine.")
            sleep(5)
            print("The whole statue shakes, and blows up.")
            print("You quickly drop down to dodge the flying debris.")
            print("A light behind the shrine starts flashing red.")
            print("Perhaps some monsters are on their way here now.")
            f=input("1.Run north. 2.Run northeast. 3.Run northwest.")
            if f =="1":
              print("You start running north, but the barren landscape leads to even more barren landscape, with nothing providing cover for you and Haley.")
              sleep(3)
              print("Eventually, you've exhausted your resources and still have not found the mountains.")
              print("You drop onto the sand in exhaustion.")
              sleep(5)
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You decide to run northeast, only to run directly into the approaching monsters.")
              print("They shot you with no mercy.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to run northwest, successfully avoiding the monsters.")
              sleep(4)
              print("Eventually, you reach the mountains. You take a deep breath.")
              print("This is going to be a long hike.")
              player1.newSkill()
              nextChapter(player1)##################### 
          elif e =="2":
            print("You leave it alone, and head north.")
            sleep(4)
            print("You see some sort of massive statue up ahead.")
            f=input("1.Investigate the statue. 2.Hide. 3.Keep walking. 4.Blow the statue up.")
            if f =="1":
              print("You walk up to the statue.")
              sleep(4)
              print("Suddenly, two monsters jump out from either side of the statue, guns raised.")
              print("You were shot so, so many times.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You quickly hide behind a rock.")
              sleep(4)
              print("Nothing happens.")
              sleep(6)
              print("Nothing happens.")
              g=input("1.Stay. 2.Leave the hiding spot.")
              if g =="1":
                print("You decide to stay.")
                sleep(5)
                print("Eventually, you hear a group of four monsters leaving from behind the statue.")
                print("You surprise attack them, and since all of them had their backs to you in was an easy victory.")
                print("You head north once more and arrive at the base of the mountians.")
                print("'Here we go.' You say.")
                player1.newSkill()
                nextChapter(player1)##################### 
              else:
                print("You leave the hiding spot, and the moment you made a step, two monsters jump out from either side of the statue, guns raised.")
                print("Your body was littered with bullets.")
                print("YOU IDED! THE END!")
                die(player1)
            elif f =="3":
              print("You decide to keep walking.")
              sleep(4)
              print("Suddenly, two monsters jump out from either side of the statue, guns raised.")
              print("You were shot so, so many times.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You blow the hell out of the statue, which also meant you blew up the hidden monsters behind the statue, too.")
              print("You quickly looted the monsters' bodies and head north.")
              sleep(4)
              print("You eventually arrived at the base of the mountains.")
              print("'Here we go.' You say.")
              player1.newSkill()
              nextChapter(player1)##################### 
          elif e =="3":
            print("You leave it alone, and head northeast.")
            sleep(3)
            print("You wandered into the range of a sniper tower.")
            print("One shot, one kill.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You leave it alone, and head northwest.")
            sleep(3)
            print("You wandered into the range of a sniper tower.")
            print("One shot, one kill.")
            print("YOU DIED! THE END!")
            die(player1)
      elif c =="2":
        print("You head northeast, bringing you back on track for the path for the mountains.")
        sleep(3)
        print("You quickly take cover behind a rock when you see the tower up ahead.")
        print("You slowly peek out and scan the area. It looks like it's only the tower, but there may be other monsters about.")
        d=input("1.Sneak under and past the tower. 2.Try to fight the sniper on the tower. 3.Sneak around, far away from the tower. 4.Cause a distraction.")
        if d =="1":
          print("You decide to sneak directly under the tower.")
          print("You found an opening, and quickly ran towards the under side of the tower. They shouldn't be able to see you here.")
          sleep(4)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to shoot at the sniper, but surprisingly, they're a better shot than you.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to double back and curve around the tower the long way.")
          print("But what you didn't realize...")
          print("Was that there was another tower in the area you tried to curve around through.")
          print("Your skull cracked open smoothly.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to distract the sniper.")
          print("You bring out a bottle, and put a rag inside it. You pour some oil inside it, and set it alight.")
          print("You throw it off into the distance, catching the sniper's attention.")
          sleep(4)
          print("You hear three monsters get dispatched to the molotov's location to check it out.")
          print("There probably aren't any monsters left at the tower other than the sniper.")
          e=input("1.Run under the tower. 2.Run around the tower. 3.Stay here. 4.Kill the monsters.")
          if e =="1":
            print("You quickly run under the tower unseen.")
            sleep(3)
            print("The monsters still seem to be focused on the molotov, but you are unsure whether you have enough time to run far enough by the time they stop investigating it.")
            f=input("1.Make a run for it. 2.Stay hidden under the tower. 3.Cause another distraction.")
            if f =="1":
              print("You make a run for it, only to be seen by the sniper at the top of the tower.")
              print("You were shot right in the leg before a clean headshot.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You stay hidden under the tower, and after a good enough wait, you peek out to ensure the coast is clear.")
              sleep(3)
              print("The coast is clear.")
              print("You slowly sneak towards the forest at the base of the mountains and reached there successfully without being seen.")
              sleep(4)
              print("You take in the size of the mountains up ahead and take a deep breath.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You try to set up another distraction, but you were so distracted by setting up the next distraction that you didn't notice the monster sneaking up behind you.")
              print("They strangled you to death. After they shot you with a shotgun.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to run around the tower unseen, but it took too long and the sniper saw you running across.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You stay where you are, but eventually one of the monsters saw your location and they were too much for you to fight off.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You attack the monsters while they are distracted and they died swiftly.")
            print("Now there's only the sniper left at the tower.")
            f=input("1.Peek the sniper and shoot. 2.Wait. 3.Run across to the next bit of cover, and so on. 4.Run straight north.")
            if f =="1":
              print("You quickly peek the sniper and try to shoot back, but unfortunately the sniper was watching your angle and headshotted you.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You wait where you are.")
              sleep(7)
              print("Suddenly, you peek out, and the sniper wasn't ready.")
              print("They missed their shot and you somehow managed to headshot them.")
              print("With the tower dealt with, you reached the mountains without any more hitches.")
              player1.newSkill()
              nextChapter(player1)##################### 
            elif f =="3":
              print("You quickly relocate to the next bit of cover, baiting out a shot from the sniper.")
              sleep(5)
              print("You do it again, and they miss again.")
              sleep(4)
              print("You do it a third time, and this time, rather than running all the way to the next bit of cover, you stop right in the middle between the covers and aim for the sniper's head.")
              print("It was a clean headshot.")
              print("With that out of the way, you reached the mountains easily.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You start running straight north.")
              sleep(4)
              print("You managed to dodge the first few shots, but your luck ran out eventually and you were shot right in the back, and later on, your neck.")
              print("YOU DIED! THE END!")
              die(player1)
      else:
        print("You decide to head northwest.")
        sleep(3)
        print("That's strange. The desert ends here. There's a forest right ahead of you.")
        print("Suddenly, you've been shot in the head.")
        print("A sniper hidden in the forest must have seen you. YOU DIED! THE END!")
        die(player1)
    elif b =="2":
      print("You decide to leave the house you're currently in, and relocate to a new one.")
      print("Unfortunately, one of the monsters noticed your movement and they snuck up on you with some shotguns.")
      print("It was not pretty.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="3":
      print("You slowly lead Haley out of the house, and the two of you stealthily sneak around the houses when you hear any footsteps. After doing this for a while, the monsters got back to their car and drove off.")
      c=input("1.Head north. 2.Head northeast. 3.Head northwest.")
      if c =="1":
        print("You head north.")
        sleep(3)
        print("The heat is becoming hard to bear.")
        print("You find some sort of underground cave, so you and Haley went inside to take a break.")
        sleep(3)
        print("The ground suddenly trembles and the cave entrance collapses. You won't be getting out that way.")
        print("You bring out a lighter and create a makeshift torch.")
        print("You venture deeper into the cave, looking for a way out.")
        sleep(3)
        print("Eventually, you reach a crossroads in the cave.")
        d=input("1.Go left. 2.Go straight. 3.Go right.")
        if d =="1":
          print("Fingers crossed, you go left.")
          sleep(3)
          print("Your fingers were still crossed when the cave collapsed onto you. Probably could've used those to mitigate some of the damage.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You decide to head straight forwards. It eventually opens up back to the surface.")
          print("You quickly duck back down. There was a sniper tower really close by.")
          print("You would have to sneak right under it.")
          sleep(5)
          print("You slowly leave the cave, and sneak towards directly under the tower.")
          sleep(3)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        else:
          print("You decide to turn right.")
          sleep(3)
          print("Eventually, it leads you back to the surface.")
          print("There seems to be some sort of ancient shrine thing up ahead.")
          e=input("1.Check it out. 2.Leave it alone, and head north. 3.Leave it alone, and head northeast. 4.Leave it alone, and head northwest.")
          if e =="1":
            print("You walk over to the shrine.")
            print("A jug of water is placed on the shrine.")
            print("You pick it up and some sort of mechanism runs behind the shrine.")
            sleep(5)
            print("The whole statue shakes, and blows up.")
            print("You quickly drop down to dodge the flying debris.")
            print("A light behind the shrine starts flashing red.")
            print("Perhaps some monsters are on their way here now.")
            f=input("1.Run north. 2.Run northeast. 3.Run northwest.")
            if f =="1":
              print("You start running north, but the barren landscape leads to even more barren landscape, with nothing providing cover for you and Haley.")
              sleep(3)
              print("Eventually, you've exhausted your resources and still have not found the mountains.")
              print("You drop onto the sand in exhaustion.")
              sleep(5)
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You decide to run northeast, only to run directly into the approaching monsters.")
              print("They shot you with no mercy.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to run northwest, successfully avoiding the monsters.")
              sleep(4)
              print("Eventually, you reach the mountains. You take a deep breath.")
              print("This is going to be a long hike.")
              player1.newSkill()
              nextChapter(player1)##################### 
          elif e =="2":
            print("You leave it alone, and head north.")
            sleep(4)
            print("You see some sort of massive statue up ahead.")
            f=input("1.Investigate the statue. 2.Hide. 3.Keep walking. 4.Blow the statue up.")
            if f =="1":
              print("You walk up to the statue.")
              sleep(4)
              print("Suddenly, two monsters jump out from either side of the statue, guns raised.")
              print("You were shot so, so many times.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You quickly hide behind a rock.")
              sleep(4)
              print("Nothing happens.")
              sleep(6)
              print("Nothing happens.")
              g=input("1.Stay. 2.Leave the hiding spot.")
              if g =="1":
                print("You decide to stay.")
                sleep(5)
                print("Eventually, you hear a group of four monsters leaving from behind the statue.")
                print("You surprise attack them, and since all of them had their backs to you in was an easy victory.")
                print("You head north once more and arrive at the base of the mountians.")
                print("'Here we go.' You say.")
                player1.newSkill()
                nextChapter(player1)##################### 
              else:
                print("You leave the hiding spot, and the moment you made a step, two monsters jump out from either side of the statue, guns raised.")
                print("Your body was littered with bullets.")
                print("YOU IDED! THE END!")
                die(player1)
            elif f =="3":
              print("You decide to keep walking.")
              sleep(4)
              print("Suddenly, two monsters jump out from either side of the statue, guns raised.")
              print("You were shot so, so many times.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You blow the hell out of the statue, which also meant you blew up the hidden monsters behind the statue, too.")
              print("You quickly looted the monsters' bodies and head north.")
              sleep(4)
              print("You eventually arrived at the base of the mountains.")
              print("'Here we go.' You say.")
              player1.newSkill()
              nextChapter(player1)##################### 
          elif e =="3":
            print("You leave it alone, and head northeast.")
            sleep(3)
            print("You wandered into the range of a sniper tower.")
            print("One shot, one kill.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You leave it alone, and head northwest.")
            sleep(3)
            print("You wandered into the range of a sniper tower.")
            print("One shot, one kill.")
            print("YOU DIED! THE END!")
            die(player1)
      elif c =="2":
        print("You head northeast, bringing you back on track for the path for the mountains.")
        sleep(3)
        print("You quickly take cover behind a rock when you see the tower up ahead.")
        print("You slowly peek out and scan the area. It looks like it's only the tower, but there may be other monsters about.")
        d=input("1.Sneak under and past the tower. 2.Try to fight the sniper on the tower. 3.Sneak around, far away from the tower. 4.Cause a distraction.")
        if d =="1":
          print("You decide to sneak directly under the tower.")
          print("You found an opening, and quickly ran towards the under side of the tower. They shouldn't be able to see you here.")
          sleep(4)
          print("You accidentally kicked over a bucket of water.")
          e=input("1.Run!! 2.Hide behind the crate. 3.Stand completely still. 4.Guns-a-blazing!")
          if e =="1":
            print("You start running, which draws the attention of the monsters nearby. They shoot you in the back of the head and you died. THE END!")
            die(player1)
          elif e =="2":
            print("You quickly hide behind a crate, and wait it out.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="3":
            print("You stand completely still.")
            sleep(3)
            print("No one reacts to the bucket.")
            f=input("1.Make a run for it. 2.Stay here.")
            if f =="1":
              print("You make a run for it, and you manage to make it to the forest at the base of the mountains without anyone pursuing you.")
              player1.newSkill()
              nextChapter(player1)#####################
            else:
              print("You stay where you are, only to be seen by a monster behind you.")
              print("You died a gruesome death.")
              print("YOU DIED! THE END!")
              die(player1)
          else:
            print("You start shooting all over the place, drawing the attention of the monsters nearby.")
            print("They all peeked at the same time, and you couldn't flick to all of their heads.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to shoot at the sniper, but surprisingly, they're a better shot than you.")
          print("YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to double back and curve around the tower the long way.")
          print("But what you didn't realize...")
          print("Was that there was another tower in the area you tried to curve around through.")
          print("Your skull cracked open smoothly.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to distract the sniper.")
          print("You bring out a bottle, and put a rag inside it. You pour some oil inside it, and set it alight.")
          print("You throw it off into the distance, catching the sniper's attention.")
          sleep(4)
          print("You hear three monsters get dispatched to the molotov's location to check it out.")
          print("There probably aren't any monsters left at the tower other than the sniper.")
          e=input("1.Run under the tower. 2.Run around the tower. 3.Stay here. 4.Kill the monsters.")
          if e =="1":
            print("You quickly run under the tower unseen.")
            sleep(3)
            print("The monsters still seem to be focused on the molotov, but you are unsure whether you have enough time to run far enough by the time they stop investigating it.")
            f=input("1.Make a run for it. 2.Stay hidden under the tower. 3.Cause another distraction.")
            if f =="1":
              print("You make a run for it, only to be seen by the sniper at the top of the tower.")
              print("You were shot right in the leg before a clean headshot.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You stay hidden under the tower, and after a good enough wait, you peek out to ensure the coast is clear.")
              sleep(3)
              print("The coast is clear.")
              print("You slowly sneak towards the forest at the base of the mountains and reached there successfully without being seen.")
              sleep(4)
              print("You take in the size of the mountains up ahead and take a deep breath.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You try to set up another distraction, but you were so distracted by setting up the next distraction that you didn't notice the monster sneaking up behind you.")
              print("They strangled you to death. After they shot you with a shotgun.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to run around the tower unseen, but it took too long and the sniper saw you running across.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You stay where you are, but eventually one of the monsters saw your location and they were too much for you to fight off.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You attack the monsters while they are distracted and they died swiftly.")
            print("Now there's only the sniper left at the tower.")
            f=input("1.Peek the sniper and shoot. 2.Wait. 3.Run across to the next bit of cover, and so on. 4.Run straight north.")
            if f =="1":
              print("You quickly peek the sniper and try to shoot back, but unfortunately the sniper was watching your angle and headshotted you.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You wait where you are.")
              sleep(7)
              print("Suddenly, you peek out, and the sniper wasn't ready.")
              print("They missed their shot and you somehow managed to headshot them.")
              print("With the tower dealt with, you reached the mountains without any more hitches.")
              player1.newSkill()
              nextChapter(player1)##################### 
            elif f =="3":
              print("You quickly relocate to the next bit of cover, baiting out a shot from the sniper.")
              sleep(5)
              print("You do it again, and they miss again.")
              sleep(4)
              print("You do it a third time, and this time, rather than running all the way to the next bit of cover, you stop right in the middle between the covers and aim for the sniper's head.")
              print("It was a clean headshot.")
              print("With that out of the way, you reached the mountains easily.")
              player1.newSkill()
              nextChapter(player1)##################### 
            else:
              print("You start running straight north.")
              sleep(4)
              print("You managed to dodge the first few shots, but your luck ran out eventually and you were shot right in the back, and later on, your neck.")
              print("YOU DIED! THE END!")
              die(player1)
      else:
        print("You decide to head northwest.")
        sleep(3)
        print("That's strange. The desert ends here. There's a forest right ahead of you.")
        print("Suddenly, you've been shot in the head.")
        print("A sniper hidden in the forest must have seen you. YOU DIED! THE END!")
        die(player1)
    else:
      print("You and Haley exit the house, and slowly sneak towards the sound of the engine. You approach a corner, and just as you are about to turn around it, you find two large monsters wielding shotguns.")
      print("You were not victorious in that encounter.")
      print("YOU DIED! THE END!")
      die(player1)
  

#PUZZLES

#khopesh
def pyramid(player1):#Used in 2 scenes. Formatted for ALONE
  pass

#grenades
def glacierRuins(player1):
  pass

#eternalFlame
def jungleRuins(player1):
  pass

#amuletOfLife
def lostCity(player1):
  pass