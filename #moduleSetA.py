#ALL SKILL TIER 1
import time
from time import sleep
from player import *

def die(player1):
  pass

def monsterCity(player1): #only used in 1 scene. Formatted.
  print("Following the map, you make your way to the monster city. Once you are close enough, you and Jess take cover behind a bunch of bushes.")
  sleep(3)
  print("'Alright, the map says there is a secret cave that goes straight to the mountains.' Jess sighs. 'And conveniently, this entire Monster city is built right on it.'")
  print("You nod. 'Man, there's so many ways to approach this city... and it's full of Monsters, so we'll have to remain unseen...'")
  a=input("1.North entrance. 2.East entrance. 3.South entrance. 4.West entrance.")
  if a =="1":
    print("You go through the north entrance, and you quickly take cover behind some sort of cart when some monsters come over.")
    b=input("1.Stay still. 2.Switch hiding spots. 3.Attack the monsters. 4.Create a distraction elsewhere.")
    if b =="1":
      print("You hold still, hoping not to be found.")
      if player1.t3 == True:
        print("You remain hidden in your hiding spot and the monsters walk right by. You and Jess slowly make your way out and continue moving.")
        sleep(3)
        print("You groan. 'No way.'")
        print("Ahead of you, you see a massive crowd of monsters hovering around some sort of stage. Jess sighs. 'What's our plan?'")
        c=input("1.Walk through the crowd. 2.Walk around the crowd. 3.Go back to where you were.")
        if c =="1":
          print("You grab Jess's hand and enter the crowd. You remain low to avoid being seen and you manage to curve around the entire stage without being spotted.")
          print("You and Jess take cover in a small hut to look over the map again. 'There, that could be where it is!' You nod. 'It's under...that building over there!'")
          sleep(3)
          print("Suddenly, you hear a set of footsteps near the hut. You and Jess remain silent.")
          d=input("1.Attack. 2.Remain still. 3.Find a better hiding spot. 4.Throw a bottle to another place to distract it.")
          if d =="1":
            print("You attack the Monster, and you and Jess manage to take them out before they can make a single sound. You listen for more footsteps, but there are none.")
            print("'We're clear.' You say.")
            print("Jess points to the back of some building up ahead. 'That's where the cave entrance is. It'll lead us straight to the mountains.'")
            sleep(3)
            print("You make your way into the building through the back, and you realize it's a police station.")
            e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
            if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
            else:
              print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
              sleep(3)
              print("The door creaks when you open it, and you hear gears turning underground.")
              sleep(5)
              st=time.time()
              f=input("PRESS [R] to run down the stairs!").title()
              rt = time.time()-st
              if f=="R" and rt<2:
                print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                sleep(3)
                print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                die(player1)
          elif d =="2":
            print("You remain still, hoping to not be caught.")
            if player.t3 == True:
              print("The monster walks right by without seeing you and you manage to make your way to the next stop: the building built right on top of the cave entrance.")
              print("You enter the building through the back, and you realize that you have entered a police station.")
              e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
              if e =="1":
                print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
                f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
                if f =="1":
                  print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                  print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                  sleep(4)
                  print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                  print("Jess nods. 'Let's go.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                elif f =="2":
                  print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                  die(player1)
                elif f =="3":
                  print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                  die(player1)
                else:
                  print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                  die(player1)
              elif e =="2":
                print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
                die(player1)
              else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
            else:
              print("You failed to remain hidden and the monster found you. They shoot you in the head and you die. THE END!")
              die(player1)
          elif d =="3":
            print("You try to relocate to a better spot, but the monster turns the corner just as you decided to do that. It shoots you in the head and you die. THE END!")
            die(player1)
          else:
            print("You throw a bottle across to distract the monster, but unluckily for you, the Monster was in the line of sight to see you throw it from your side. He ambushes you and shoots you in the head. YOU DIED! THE END!")
            die(player1)
        elif c=="2":
          print("You and Jess try to skirt around the crowd, but someone on the stage spots you and all the Monsters jump onto you immediately. They bite into your neck and you die. THE END!")
          die(player1)
        else:
          print("You try to head back and find a different way, but a Monster guard sees you and shoots you down on the spot. YOU DIED! THE END!")
          die(player1)
      else:
        print("You failed to remain hidden and they found you. YOU DIED! THE END!")
        die(player1)
    elif b =="2":
      print("Whilst the monsters are approaching you, you and Jess sneak over to a different hiding spot and successfully remain hidden.")
      print("The monsters walk away and you and Jess make your way to the next stop.")
      sleep(3)
      print("You groan. 'No way.'")
      print("Ahead of you, you see a massive crowd of monsters hovering around some sort of stage. Jess sighs. 'What's our plan?'")
      c=input("1.Walk through the crowd. 2.Walk around the crowd. 3.Go back to where you were.")
      if c =="1":
        print("You grab Jess's hand and enter the crowd. You remain low to avoid being seen and you manage to curve around the entire stage without being spotted.")
        print("You and Jess take cover in a small hut to look over the map again. 'There, that could be where it is!' You nod. 'It's under...that building over there!'")
        sleep(3)
        print("Suddenly, you hear a set of footsteps near the hut. You and Jess remain silent.")
        d=input("1.Attack. 2.Remain still. 3.Find a better hiding spot. 4.Throw a bottle to another place to distract it.")
        if d =="1":
          print("You attack the Monster, and you and Jess manage to take them out before they can make a single sound. You listen for more footsteps, but there are none.")
          print("'We're clear.' You say.")
          print("Jess points to the back of some building up ahead. 'That's where the cave entrance is. It'll lead us straight to the mountains.'")
          sleep(3)
          print("You make your way into the building through the back, and you realize it's a police station.")
          e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
          if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
          elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
          else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
        elif d =="2":
          print("You remain still, hoping to not be caught.")
          if player.t3 == True:
            print("The monster walks right by without seeing you and you manage to make your way to the next stop: the building built right on top of the cave entrance.")
            print("You enter the building through the back, and you realize that you have entered a police station.")
            e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
            if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
            else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
          else:
            print("You failed to remain hidden and the monster found you. They shoot you in the head and you die. THE END!")
            die(player1)
        elif d =="3":
          print("You try to relocate to a better spot, but the monster turns the corner just as you decided to do that. It shoots you in the head and you die. THE END!")
          die(player1)
        else:
          print("You throw a bottle across to distract the monster, but unluckily for you, the Monster was in the line of sight to see you throw it from your side. He ambushes you and shoots you in the head. YOU DIED! THE END!")
          die(player1)
      elif c=="2":
        print("You and Jess try to skirt around the crowd, but someone on the stage spots you and all the Monsters jump onto you immediately. They bite into your neck and you die. THE END!")
        die(player1)
      else:
        print("You try to head back and find a different way, but a Monster guard sees you and shoots you down on the spot. YOU DIED! THE END!")
        die(player1)
    elif b =="3":
      print("You and Jess jump out, guns a blazing, but there were more monsters than you anticipated and their guns shredded right through you. YOU DIED! THE END!")
      die(player1)
    else:
      print("You throw a bottle far away, which triggers the Monsters' powerful hearing. They walk away, allowing you and Jess to move on to the next place.")
      sleep(3)
      print("You groan. 'No way.'")
      print("Ahead of you, you see a massive crowd of monsters hovering around some sort of stage. Jess sighs. 'What's our plan?'")
      c=input("1.Walk through the crowd. 2.Walk around the crowd. 3.Go back to where you were.")
      if c =="1":
        print("You grab Jess's hand and enter the crowd. You remain low to avoid being seen and you manage to curve around the entire stage without being spotted.")
        print("You and Jess take cover in a small hut to look over the map again. 'There, that could be where it is!' You nod. 'It's under...that building over there!'")
        sleep(3)
        print("Suddenly, you hear a set of footsteps near the hut. You and Jess remain silent.")
        d=input("1.Attack. 2.Remain still. 3.Find a better hiding spot. 4.Throw a bottle to another place to distract it.")
        if d =="1":
          print("You attack the Monster, and you and Jess manage to take them out before they can make a single sound. You listen for more footsteps, but there are none.")
          print("'We're clear.' You say.")
          print("Jess points to the back of some building up ahead. 'That's where the cave entrance is. It'll lead us straight to the mountains.'")
          sleep(3)
          print("You make your way into the building through the back, and you realize it's a police station.")
          e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
          if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
          elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
          else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
        elif d =="2":
          print("You remain still, hoping to not be caught.")
          if player.t3 == True:
            print("The monster walks right by without seeing you and you manage to make your way to the next stop: the building built right on top of the cave entrance.")
            print("You enter the building through the back, and you realize that you have entered a police station.")
            e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
            if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
            else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
          else:
            print("You failed to remain hidden and the monster found you. They shoot you in the head and you die. THE END!")
            die(player1)
        elif d =="3":
          print("You try to relocate to a better spot, but the monster turns the corner just as you decided to do that. It shoots you in the head and you die. THE END!")
          die(player1)
        else:
          print("You throw a bottle across to distract the monster, but unluckily for you, the Monster was in the line of sight to see you throw it from your side. He ambushes you and shoots you in the head. YOU DIED! THE END!")
          die(player1)
      elif c=="2":
        print("You and Jess try to skirt around the crowd, but someone on the stage spots you and all the Monsters jump onto you immediately. They bite into your neck and you die. THE END!")
        die(player1)
      else:
        print("You try to head back and find a different way, but a Monster guard sees you and shoots you down on the spot. YOU DIED! THE END!")
        die(player1)
      
  elif a =="2":
    print("You and Jess head through the east gate and you gulp immediately. You hear monster children squeaking nearby. If they blow your cover by running towards you, you're screwed.")
    b=input("1.Take them out with your secondary weapon. 2.Hide. 3.Sneak past them. 4.Distract them with something.")
    if b =="1":
      if dagger2==True or (bow==True and player1.t2==True):
        print("You and Jess quickly take out the monster children and hide the bodies. You sneak your way into the school, since it's in between you and the cave.")
        sleep(4)
        print("Jess frowns. 'Was that an alarm?'")
        c=input("1.Run. 2.Hide.")
        if c =="1":
          print("You and Jess break into a run, but the Monster teachers see you and shoot you down on the spot. YOU DIED! THE END!")
        else:
          print("You and Jess dash into another room to hide, but nothing comes. 'False alarm?' You ask, but suddenly you hear several sets of footsteps coming from the hallway.")
          d=input("1.Leave through the window. 2.Hide in the room. 3.Ambush them when they come in. 4.Attack them now.")
          if d =="1":
            print("You and Jess escape the room through the window, and successfully evade the monsters. You find the building built on top of the cave entrance, and you enter it through the back. 'Oh, boy.' Jess says.")
            print("You realize that this building is a police station.")
            e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
            if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
            else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
          elif d =="2":
            print("You try to hide in the room, but there are too many monsters for you to hide from. They are able to scan the room properly and find you. They shoot you in the spot and you die. THE END!")
            die(player1)
          elif d =="3":
            print("You and Jess hide both sides of the door to ambush the monsters when they come in, but unfornately, they cleared both sides as they entered and because there were a lot of them, they overpowered you and you died. THE END!")
            die(player1)
          else:
            print("You and Jess kick down the door, guns-a-blazing, surprising the monsters. You kill all of them where they stand and quickly run away from the scene in case the gunfire alerted any nearby monsters.")
            print("You find the building built on top of the cave entrance, and enter it through the back.")
            sleep(5)
            print("'Oh, boy.' Jess says.")
            print("You realize that this building is a police station.")
            e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
            if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
            else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
      else:
        print("You weren't quiet enough in your takeout and the school monsters came over and shot you right in the head. YOU DIED! THE END!")
    elif b =="2":
      print("You and Jess hide inside a classroom, hoping not to be found.")
      if player1.t3 == True:
        print("You remain quiet and none of the children find you. You keep moving through the school to reach the cave.")
        sleep(4)
        print("Jess frowns. 'Was that an alarm?'")
        c=input("1.Run. 2.Hide.")
        if c =="1":
          print("You and Jess break into a run, but the Monster teachers see you and shoot you down on the spot. YOU DIED! THE END!")
        else:
          print("You and Jess dash into another room to hide, but nothing comes. 'False alarm?' You ask, but suddenly you hear several sets of footsteps coming from the hallway.")
          d=input("1.Leave through the window. 2.Hide in the room. 3.Ambush them when they come in. 4.Attack them now.")
          if d =="1":
            print("You and Jess escape the room through the window, and successfully evade the monsters. You find the building built on top of the cave entrance, and you enter it through the back. 'Oh, boy.' Jess says.")
            print("You realize that this building is a police station.")
            e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
            if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
            else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
          elif d =="2":
            print("You try to hide in the room, but there are too many monsters for you to hide from. They are able to scan the room properly and find you. They shoot you in the spot and you die. THE END!")
            die(player1)
          elif d =="3":
            print("You and Jess hide both sides of the door to ambush the monsters when they come in, but unfornately, they cleared both sides as they entered and because there were a lot of them, they overpowered you and you died. THE END!")
            die(player1)
          else:
            print("You and Jess kick down the door, guns-a-blazing, surprising the monsters. You kill all of them where they stand and quickly run away from the scene in case the gunfire alerted any nearby monsters.")
            print("You find the building built on top of the cave entrance, and enter it through the back.")
            sleep(5)
            print("'Oh, boy.' Jess says.")
            print("You realize that this building is a police station.")
            e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
            if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
            else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
      else:
        print("You weren't hiding well enough as some of the children saw you and squeaked out. The teachers came in with guns and shot you down immediately. YOU DIED! THE END!")
        die(player1)
    elif b =="3":
      print("You try to sneak past the monsters, but they see you and squeak out, signalling the teacher Monsters. They shoot you down immediately and you die. THE END!")
      die(player1)
    else:
      print("You throw something into the distance to distract the children, but one who wasn't as receptive as the others, failed to look away from your location. It spots you and squeals out, signalling your prescence to the teachers. They whip out massive shotguns and blast your brains out. YOU DIED! THE END!")
  elif a =="3":
    print("You enter through the south entrance and find some sort of massive warehouse. 'That does not look good.' Jess says. 'We should go around it.'")
    b=input("1.Ignore Jess and enter the warehouse alone. 2.Insist that both of you enter. 3.Listen to Jess and leave.")
    if b =="1":
      print("You enter the warehouse alone, and the moment you step foot inside, you trigger some sort of beeping device. You frown and look down. You stepped on a mine! Bits of you fly all over the place, and the entire warehouse collapses onto your fragmented body. THE END!")
      die(player1)
    elif b =="2":
      print("You insist Jess to come with you, and she hesitantly agrees. You prepare to enter the warehouse, but Jess stops you from entering. She kneels down at the door and brushes off some dirt. 'A mine!' You gasp. Jess nods. 'Let's find another way in.'")
      c=input("1.Break left window. 2.Break right window. 3.Boost Jess onto an opening high up, but you won't be able to join her.")
      if c =="3":
        print("You boost Jess into the opening, and she makes her way into the warehouse without you. A few minutes later, she makes her way back out the opening and you catch her. 'Thanks.' She says, and hands you some sticky bombs. You smile and the two of you head towards the cave entrance.")
        stickyBombs = True
        sleep(3)
        print("Following the map, you find that some sort of police station is built right on the cave entrance.")
        d=input("1.Approach the station from the side. 2.Approach it head on. 3.Approach it from behind. 4.Through the garage")
        if d =="1":
          print("You approach the station from the side, but a cop sees you crossing the road. They shoot you on sight and you die. THE END!")
          die(player1)
        elif d =="2":
          print("You try to approach the station head on, but lots of cops see you and shoot you in the spot. YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You curve around to enter through the back, and you manage to do so successfully. You enter the police station.")
          e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
          if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
          elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
          else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
        else:
          print("You enter the station garage without being seen and enter the station safely. 'How are we gonna reach the cave entrance?' Jess asks.")
          e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
          if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
          elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
          else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
      else:
        print("You smash a window, which triggers a silent alarm. Whilst you and Jess are looking around the warehouse, Monsters have already surrounded the building and you have nowehere to run. YOU DIED! THE END!")
        die(player1)
    else:
      print("You and Jess decide to ignore the warehouse and keep going. Up ahead you see the building built directly above the cave you need to go through.")
      print("'Seriously?' Jess groans.")
      sleep(4)
      print("You take a deep breath and start heading towards the police station.")
      sleep(5)
      st=time.time()
      c=input("PRESS [E] to evade a cop's vision!").title()
      rt = time.time()-st
      if rt<2 and c=="E":
        print("You successfully evade the cop's vision.")
        print("You and Jess slowly make your way towards the police station.")
        print("'How do we get inside?' Jess asks.")
        d=input("1.Main entrance. 2.Side entrance. 3.Back entrance. 4.Garage.")
        if d =="1":
          print("You approach the station from the side, but a cop sees you crossing the road. They shoot you on sight and you die. THE END!")
          die(player1)
        elif d =="2":
          print("You try to approach the station head on, but lots of cops see you and shoot you in the spot. YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You curve around to enter through the back, and you manage to do so successfully. You enter the police station.")
          e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
          if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
          elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
          else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
        else:
          print("You enter the station garage without being seen and enter the station safely. 'How are we gonna reach the cave entrance?' Jess asks.")
          e=input("1.Put on monster cop clothes. 2.Sneak across the station. 3.Trigger the fire alarm.")
          if e =="1":
              print("You and Jess put on the monster police apparel and have caps well over your face. You and sigficantly smaller than the average monster, so you are stopped immediately by a monster, who said something in the monster language.")
              f=input("1.Reply with random sounds. 2.Ignore the monster. 3.Keep walking. 4.Run.")
              if f =="1":
                print("You reply to the monster with random sounds, which makes him laugh and slap you in the back. The monster walks away and you and Jess reach the basement door without any more issues.")
                print("A monster cop sees you and Jess and opens the door for you. You nod and walk inside.")
                sleep(4)
                print("The door closes behind you and you and Jess walk down a flight of stairs, opening to the cave. You take a deep breath. 'You ready to head to the mountains?'")
                print("Jess nods. 'Let's go.'")
                player1.newSkill()
                nextChapter()#######################################################
              elif f =="2":
                print("You ignore the monster, but the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You and Jess keep walking, and the monster forces themselves in front of you. They take off your caps and gasp. Nearby cops see you two and shoot you right where you stand. YOU DIED! THE END!")
                die(player1)
              else:
                print("You break into a run, and the monster yells to the other monsters, who bring out their guns and shoot you dead in a matter of seconds. YOU DIED! THE END!")
                die(player1)
          elif e =="2":
              print("You and Jess start sneaking towards the station, but you are caught almost immediately by a monster. The monster signals all their friends in the area and you are trapped. You were a nice snack. YOU DIED! THE END!")
              die(player1)
          else:
                print("You trigger the fire alarm, which causes all the monster officers to run out of the building in less than two minutes. You and Jess emerge from your hiding spot and head towards the basement.")
                sleep(3)
                print("The door creaks when you open it, and you hear gears turning underground.")
                sleep(5)
                st=time.time()
                f=input("PRESS [R] to run down the stairs!").title()
                rt = time.time()-st
                if f=="R" and rt<2:
                  print("You and Jess run down the flight of stairs immediately and you make it to the bottom just as a blade slices through the entire width of the stairs, which would have cut you in half.")
                  sleep(3)
                  print("'Whew' Jess sighs in relief. She brandishes the cave to you. 'Let's head to the mountains.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You missed a step in the stairs and got chopped up to pieces! THE END!")
                  die(player1)
      else:
        print("The cop sees you and signals your prescence to the other cops. They track you down with cars and they shoot you down swiftly. YOU DIED! THE END!")
        die(player1)
  else:
    print("You and Jess make your way into the city through the west entrance, and are immediately greeted by Monster guards. They overwhelm you easily and feast upon your flesh.")
    die(player1)


def plainsVillage(player1): #Is used in multiple scenes. Formatted for ALONE. Add dialogue for others
  print("You slowly approach the monster village, evading the sniper towers that surround the perimeter.")
  print("The fastest way to the mountains is through the village, otherwise trying to curve around will be too dangerous, with no cover in the plains to avoid the snipers.")
  sleep(5)
  print("You see the front entrance up ahead, but there may be another entrance into the village.")
  a=input("1.Take the front entrance. 2.Try to find a route on the left. 3.Try to find a route on the right. 4.Steal a vehicle at the base of the sniper tower.")
  if a =="1":
    print("You deicde to take the front entrance, but you have been spotted by multiple monsters up in the sniper towers, and you are sniped before you can even set foot in the village. YOU DIED! THE END!")
    die(player1)
  elif a =="2":
    print("You head towards the left, and find a small, rough path that leads into the village, surrounded by a good amount of trees. You take the path and make it into the village, past the sniper towers.")
    sleep(3)
    print("You see a barracks up ahead. You may be able to find helpful weaponry in there.")
    b=input("1.Go into the barracks. 2.It's not worth the risk.")
    if b == "1":
      print("You head into the barracks without being seen. It is much larger inside than you thought.")
      c=input("1.Enter the door at the end of the hall. 2.Go downstairs to the basement. 3.Enter the door on the left. 4.Enter the door on the right. 5.Go upstairs.")
      if c =="1":
        print("You head over to the end of the hall, but you have been caught by a security camera. Monsters in the barracks are immediately dispatched and you are taken out swiftly. YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You go downstairs into the basement, and you are greeted by a door.")
        sleep(5)
        st=time.time()
        d=input("PRESS [H] to hide behind the door!").title()
        rt = time.time()-st
        if d=="H" and rt <2:
          print("You hide behind the door just as some monsters open it and walk through. They don't see you so they walk right by. You enter the room they came from, and found some sticky bombs. You put them in your bag.")
          stickyBombs = True
          sleep(5)
          print("You make your way out of the barracks, and head towards the other end of the village relatively safely. You sigh when you see the sniper tower guarding the exit.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        else:
          print("You failed to hide behind the door and some monsters open the door and see you. They quickdraw their revolver and you are shot in the head. YOU DIED! THE END!")
          die(player1)
      elif c =="3":
        print("You enter the door on your left, which is filled with monster guards. They shoot you on sight before you can even turn around. YOU DIED! THE END!")
        die(player1)
      elif c =="4":
        print("You head through the door to your right, and you find some sticky bombs.")
        stickyBombs = True
        print("You're about to head out, but you hear steps coming your way.")
        d=input("1.Hide behind the door. 2.Hide in a gun locker. 3.Hide under the table. 4.Kill whoever enters.")
        if d =="1":
          print("You hide behind the door, but unfortunately for you, when the monster enters the room, they turn around to close it, and they see you. They quickdraw their pistol and shoot you before you can react. They kill you and you die. THE END!")
          die(player1)
        elif d =="2":
          print("You hide inside a gun locker, holding your knife in case the monster opens it. After waiting for a minute, you start to think the monster has left, but just as you think that the monster opens the gun locker, prompting you to lash out with your knife and kill it. You push the dead monster out of your way and you make your way out of the barracks.")
          sleep(6)
          print("You manage to make it to the other end of the village relatively safely, except there is yet another sniper tower guarding the exit.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        elif d =="3":
          print("Yuo decide to hide under the table, but the monster sees you underneath it immediately and shoots you in the head just as you aim for theirs. YOU DIED! THE END!")
          die(player1)
        else:
          print("You bring out your knife, and when the monster enters the room, you slice their throat cleanly and they drop to the ground.")
          sleep(3)
          print("You make your way out of the barracks, and head towards the other end of the village relatively safely. You sigh when you see the sniper tower guarding the exit.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
      else:
        print("You make your way up the stairs and you are about to step into the vision cone of a security camera!")
        sleep(5)
        st=time.time()
        d=input("PRESS [S] to stop yourself!").title()
        rt = time.time()-st
        if d=="S" and rt<2:
          print("You prevent yourself from entering the cone of vision, and wait til the camera turns away.")
          sleep(3)
          print("You sneak right by it and enter a door at the top of the stairs.")
          print("It seems to be some sort of stock storage, and you manage to scavenge some sticky bombs from it.")
          stickyBombs = True
          print("You make your way back down the stairs and leave the barracks, heading towards the other end of the village.")
          sleep(3)
          print("You sigh when you arrive. There is yet another sniper tower guarding the entrance.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        else:
          print("You step into the vision cone of the camera and everyone in the barracks is alerted of your presence. They come from all sides and kill you immediately. YOU DIED! THE END!")
          die(player1)
    else:
      print("You ignore the barracks, but up ahead you see a group of guards walking towards your location.")
      c=input("1.Hide behind a cart. 2.Run away. 3.Sneak away. 4.Hide behind a hut. 5.Climb up a small building to evade them.")
      if c =="1":
        print("You hide behind a cart, hoping that they won't see you, but unfortunately for you, there is a gap through the cart's handles that exposes a small bit of your head. The monsters head over to you and kill you. THE END!")
        die(player1)
      elif c =="2":
        print("You break into a run, which draws the attention of the monsters. They snipe you in the back of the head and you die. THE END!")
        die(player1)
      elif c =="3":
        print("You sneak your way around the guards, but one of them suddenly make an alerted sound.")
        d=input("1.Run away! 2.Stop moving. 3.Continue sneaking around.")
        if d =="1":
          print("You make a run for it, but the guards see you running and snipe you in the back of the head. YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You stop moving altogether and the guards make another sweep of the area. They fail to find you, and they leave the area for real this time.")
          sleep(3)
          print("You make your way through the rest of the village relatively safely, but at the end of the village you see yet another problem. Another sniper tower.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        else:
          print("You continue sneaking around, but you have been caught by the guards. They kill you swiftly and feast on your corpse. YOU DIED! THE END!")
          die(player1)
      elif c =="4":
        print("You try to hide behind a hut, but a monster casually walks by and screams, alerting the guards. They surround you almost immediately and they kill you swiftly. YOU DIED! THE END!")
        die(player1)
      else:
        print("You quickly start climbing the small building next to you as the guards approach, and thankfully, you made it up the side of the building using pipes and overextended bricks. The guards walk right by, and you make your way down after they've left.")
        sleep(4)
        print("You land on the ground after making a small jump, which causes you to lose balance and accidentally smash some sort of wooden thing. A nearby monster is alerted.")
        d=input("1.Run away! 2.Climb back up the building. 3.Hide nearby.")
        if d =="1":
          print("You make a run for it, and since no one is there to see you running away, no monsters attack you. You continue to head towards the other end of the village and successfully make it... except there is yet another sniper tower.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        elif d =="2":
          print("You try to climb back up the building, but the handholds are too worn to support your weight. You crash into the ground and the monster sees you. It calls over the guards and they kill you. YOU DIED! THE END!")
          die(player1)
        else:
          print("You deicde to hide nearby, but you misread the direction the monster would be coming from, and they see your exposed foot out the side of your hiding spot. They call the guards over and they take you out. THE END!")
          die(player1)
  elif a =="3":
    print("You take a right turn and try to find another way into the village, but you stepped on a bear trap, causing you to yell out. You drew the attention of a nearby sniper tower and you are sniped. THE END!")
    die(player1)
  else:
    print("You head to the base of the sniper tower unnoticed, since they were looking in another direction, and you hop onto the motorbike at the base of the tower. You put on a hood to hide that you are human, and you drive off. The sniper realizes, but since they think you are a monster, they shout down at you as you drive into the village.")
    sleep(5)
    print("You leave the bike near the entrance to prevent the sniper from chasing you further, and you look around the village.")
    print("A barracks catches your eye. It may have valuable weaponry, but it may be risky.")
    b=input("1.Go into the barracks. 2.Leave the barracks alone.")
    if b == "1":
      print("You head into the barracks without being seen. It is much larger inside than you thought.")
      c=input("1.Enter the door at the end of the hall. 2.Go downstairs to the basement. 3.Enter the door on the left. 4.Enter the door on the right. 5.Go upstairs.")
      if c =="1":
        print("You head over to the end of the hall, but you have been caught by a security camera. Monsters in the barracks are immediately dispatched and you are taken out swiftly. YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You go downstairs into the basement, and you are greeted by a door.")
        sleep(5)
        st=time.time()
        d=input("PRESS [H] to hide behind the door!").title()
        rt = time.time()-st
        if d=="H" and rt <2:
          print("You hide behind the door just as some monsters open it and walk through. They don't see you so they walk right by. You enter the room they came from, and found some sticky bombs. You put them in your bag.")
          stickyBombs = True
          sleep(5)
          print("You make your way out of the barracks, and head towards the other end of the village relatively safely. You sigh when you see the sniper tower guarding the exit.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        else:
          print("You failed to hide behind the door and some monsters open the door and see you. They quickdraw their revolver and you are shot in the head. YOU DIED! THE END!")
          die(player1)
      elif c =="3":
        print("You enter the door on your left, which is filled with monster guards. They shoot you on sight before you can even turn around. YOU DIED! THE END!")
        die(player1)
      elif c =="4":
        print("You head through the door to your right, and you find some sticky bombs.")
        stickyBombs = True
        print("You're about to head out, but you hear steps coming your way.")
        d=input("1.Hide behind the door. 2.Hide in a gun locker. 3.Hide under the table. 4.Kill whoever enters.")
        if d =="1":
          print("You hide behind the door, but unfortunately for you, when the monster enters the room, they turn around to close it, and they see you. They quickdraw their pistol and shoot you before you can react. They kill you and you die. THE END!")
          die(player1)
        elif d =="2":
          print("You hide inside a gun locker, holding your knife in case the monster opens it. After waiting for a minute, you start to think the monster has left, but just as you think that the monster opens the gun locker, prompting you to lash out with your knife and kill it. You push the dead monster out of your way and you make your way out of the barracks.")
          sleep(6)
          print("You manage to make it to the other end of the village relatively safely, except there is yet another sniper tower guarding the exit.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        elif d =="3":
          print("Yuo decide to hide under the table, but the monster sees you underneath it immediately and shoots you in the head just as you aim for theirs. YOU DIED! THE END!")
          die(player1)
        else:
          print("You bring out your knife, and when the monster enters the room, you slice their throat cleanly and they drop to the ground.")
          sleep(3)
          print("You make your way out of the barracks, and head towards the other end of the village relatively safely. You sigh when you see the sniper tower guarding the exit.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
      else:
        print("You make your way up the stairs and you are about to step into the vision cone of a security camera!")
        sleep(5)
        st=time.time()
        d=input("PRESS [S] to stop yourself!").title()
        rt = time.time()-st
        if d=="S" and rt<2:
          print("You prevent yourself from entering the cone of vision, and wait til the camera turns away.")
          sleep(3)
          print("You sneak right by it and enter a door at the top of the stairs.")
          print("It seems to be some sort of stock storage, and you manage to scavenge some sticky bombs from it.")
          stickyBombs = True
          print("You make your way back down the stairs and leave the barracks, heading towards the other end of the village.")
          sleep(3)
          print("You sigh when you arrive. There is yet another sniper tower guarding the entrance.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        else:
          print("You step into the vision cone of the camera and everyone in the barracks is alerted of your presence. They come from all sides and kill you immediately. YOU DIED! THE END!")
          die(player1)
    else:
      print("You ignore the barracks, but up ahead you see a group of guards walking towards your location.")
      c=input("1.Hide behind a cart. 2.Run away. 3.Sneak away. 4.Hide behind a hut. 5.Climb up a small building to evade them.")
      if c =="1":
        print("You hide behind a cart, hoping that they won't see you, but unfortunately for you, there is a gap through the cart's handles that exposes a small bit of your head. The monsters head over to you and kill you. THE END!")
        die(player1)
      elif c =="2":
        print("You break into a run, which draws the attention of the monsters. They snipe you in the back of the head and you die. THE END!")
        die(player1)
      elif c =="3":
        print("You sneak your way around the guards, but one of them suddenly make an alerted sound.")
        d=input("1.Run away! 2.Stop moving. 3.Continue sneaking around.")
        if d =="1":
          print("You make a run for it, but the guards see you running and snipe you in the back of the head. YOU DIED! THE END!")
          die(player1)
        elif d =="2":
          print("You stop moving altogether and the guards make another sweep of the area. They fail to find you, and they leave the area for real this time.")
          sleep(3)
          print("You make your way through the rest of the village relatively safely, but at the end of the village you see yet another problem. Another sniper tower.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        else:
          print("You continue sneaking around, but you have been caught by the guards. They kill you swiftly and feast on your corpse. YOU DIED! THE END!")
          die(player1)
      elif c =="4":
        print("You try to hide behind a hut, but a monster casually walks by and screams, alerting the guards. They surround you almost immediately and they kill you swiftly. YOU DIED! THE END!")
        die(player1)
      else:
        print("You quickly start climbing the small building next to you as the guards approach, and thankfully, you made it up the side of the building using pipes and overextended bricks. The guards walk right by, and you make your way down after they've left.")
        sleep(4)
        print("You land on the ground after making a small jump, which causes you to lose balance and accidentally smash some sort of wooden thing. A nearby monster is alerted.")
        d=input("1.Run away! 2.Climb back up the building. 3.Hide nearby.")
        if d =="1":
          print("You make a run for it, and since no one is there to see you running away, no monsters attack you. You continue to head towards the other end of the village and successfully make it... except there is yet another sniper tower.")
          e=input("1.Use a distraction. 2.Try to sneak under it. 3.Run past it. 4.Shoot them.")
          if e =="1":
            print("You sneak towards a nearby store and steal a small box of items, and hurl it to the base of the tower, opposite to the exit. This takes the sniper's attention, but you don't have long.")
            print("Which way do you go?")
            sleep(5)
            st=time.time()
            f=input("1.Through the main exit. 2.Over the perimeter wall. 3.Distract them again with another box.")
            rt = time.time()-st
            if rt<5:
              if f =="1":
                print("You head through the main exit just as the sniper decides to stop investigating the sound.")
              elif f =="2":
                print("You vault over the perimeter wall whilst the sniper is distracted.")
              else:
                print("You throw another box, which takes the sniper's full attention. You walk through the main exit silently and make it out.")
              print("You quickly head into a nearby forest to hide, and after a quick break you start heading up the mountains nearby.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You failed to take action in time, and the sniper saw you. They sniper you in the head and you fall to the ground. THE END!")
              die(player1)
          elif e =="2":
            print("You try to sneak under the tower, but the sniper catches you in the act and does their job cleanly. You fall to the ground with a bullet in the back of your head. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You start running for the exit, which draws the attention of the sniper. They take aim.")
            sleep(5)
            st=time.time()
            f=input("PRESS [J] to jump out of the way!").title()
            rt = time.time()-st
            if f=="J" and rt<2:
              print("You manage to jump out of the way of the incoming bullet, and you keep on running. Up ahead, you see the base of the mountains, and a small forest that can cover your escape.")
              print("However, the sniper reloads their gun and is ready for another shot. They take aim.")
              sleep(7)
              st = time.time()
              f=input("PRESS [D] to dash into the forest!").title()
              rt = time.time()-st
              if f =="D" and rt<2:
                print("You dash towards and into the forest, which successfully cuts off the sniper's sightline on you. You take a quick break before heading up the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to jump for the forest and you have been hit in the back. Monster guards are dispatched and you have nowhere to run. THE END!")
                die(player1)
            else:
              print("You failed to dodge the incoming bullet and fall to the ground. You bleed to death. THE END!")
              die(player1)
          else:
            if bow == True and player1.t2 == True:
              print("You snipe down the sniper with a clean, silent arrow shot, which allows you to walk through the exit effortlessly and head towards the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You shoot the sniper with your rifle, but unfortunately the nearby monster guards heard you. They dispatch multiple vehicles to chase you, and since you are on foot, they eventually catch up and kill you. THE END!")
              die(player1)
        elif d =="2":
          print("You try to climb back up the building, but the handholds are too worn to support your weight. You crash into the ground and the monster sees you. It calls over the guards and they kill you. YOU DIED! THE END!")
          die(player1)
        else:
          print("You deicde to hide nearby, but you misread the direction the monster would be coming from, and they see your exposed foot out the side of your hiding spot. They call the guards over and they take you out. THE END!")
          die(player1)

def desertVillage(player1):#only used in 1 scene. Formatted.
  print("You trod through the desert sands, the overwhelming heat giving no mercy.")
  print("Up ahead, you see the monster village, guarding a guided path up the mountain range that will lead you to the Summit.")
  sleep(4)
  print("You sigh and wipe the sweat off your forehead. You have to save your friend. Or at least try.")
  print("The village is much closer now. There seems to be no easy way in, as the entrances to the village are guarded.")
  a=input("1.Try to sneak past the guards. 2.Scout the village more thoroughly. 3.Distract the guards with something. 4.Shoot the guards.")
  if a=="1":
    print("You try to sneak past the guards, but they saw your head poke out the side of a car and shoot you on the spot. YOU DIED! THE END!")
    die(player1)
  elif a =="2":
    print("You decide to sustain the heat a little bit more to find a better way to enter the village. Thankfully, you do manage to find some sort of sewage pipe that leads into the village, and is not guarded at all.")
    print("The problem is... it's a sewer...")
    sleep(5)
    print("You take a deep breath, and ignoring the smell, you enter the pipe.")
    print("Although the sewage water stinks, you are a bit grateful to feel the cool water against your skin after the heat of the desert sun.")
    sleep(3)
    print("Eventually, you arrive at the end of the pipe, but you hear some voices.")
    b=input("1.Exit the pipe. 2.Don't exit the pipe. 3.Hide deeper into the pipe. 4.Head a different direction through the pipes.")
    if b =="1":
      print("You start exiting the pipe, but the monsters who were talking spot you leaving the pipe and whack you so hard in the head your skull is crushed. YOU DIED! THE END!")
      die(player1)
    elif b =="2":
      if player1.t3 == True:
        print("You remain concealed within the pipe, and eventually the monsters pass. You climb out of the pipe, looking around you. The path to the mountains is still far away, with the whole village in between you and the path.")
        print("You brush off the sweat on your forehead and look ahead for a way to get to the path.")
        c=input("1.Go to the covered market. 2.Go to the open market. 3.Go straight through the middle of the village. 4.Curve around the village perimeter.")
        if c =="1":
          print("You decide to head towards the covered market. The shade is really helpful in keeping you cool, but just as you are about to make it past the entire market, a monster notices you hiding behind a box and screams.")
          print("The nearby guards are dispatched and you are killed. YOU DIED! THE END!")
          die(player1)
        elif c == "2":
          print("You deicde to head through the open market. Although the desert heat is hard to bear, because of this, there are much less monsters roaming around this area.")
          sleep(3)
          print("You manage to make it past the entire market unseen, and the path to the mountains is almost within reach.")
          sleep(3)
          print("Just one problem.")
          print("The path is also guarded.")
          d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
          if d =="1":
            print("You decide to wait til the guards' shifts are over.")
            sleep(7)
            print("...")
            sleep(5)
            print("How long will this take?")
            sleep(3)
            e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
            if e =="1":
              print("You decide to keep waiting.")
              sleep(5)
              print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
              print("You start sneaking towards the exit.")
              sleep(6)
              st=time.time()
              f=input("PRESS [S] to stand still!").title()
              rt=time.time()-st
              if f =="S" and rt<2:
                print("You stand completely still and the guard simply yawns and turns to another side.")
                sleep(3)
                print("You continue to walk past them and make it to the path. You smile.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
              print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
              sleep(3)
              print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
              die(player1)
          elif d =="2":
            print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
            die(player1)
          elif d =="3":
            print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to find a disguise in some stores nearby to help you get past the guards.")
            print("'Hmm...' You say to yourself.")
            print("What would be the most effective disguise to fool the guards?")
            e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
            if e =="1":
              print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
              print("You approach the guards, and now all you need is a cover story or method to get past them.")
              f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
              if f =="1":
                print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
                sleep(3)
                print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
                print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
                player1.newSkill()
                nextChapter()#######################################################
            elif e =="2":
              print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
              sleep(3)
              print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
              sleep(5)
              st=time.time()
              f=input("PRESS [C] to cover your face!").title()
              rt = time.time()-st
              if f =="C" and rt<2:
                print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
                die(player1)
            else:
              print("You decide to dress as an old lady, and approach the the guards.")
              print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
              print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
              die(player1)
        elif c =="3":
          print("You decide to go straight through the center of the village, hiding behind boxes and stores every time a wave of monsters approach.")
          sleep(5)
          st=time.time()
          cc = input("PRESS [D] to duck under a camera's vision!").title()
          rt = time.time()-st
          if cc == "D" and rt<2:
            print("You duck under a camera's vision, allowing you to continue down the village and towards the path to the mountains.")
            sleep(3)
            print("You finally arrive. Just one problem.")
            print("The path is guarded.")
            d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
            if d =="1":
              print("You decide to wait til the guards' shifts are over.")
              sleep(7)
              print("...")
              sleep(5)
              print("How long will this take?")
              sleep(3)
              e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
              if e =="1":
                print("You decide to keep waiting.")
                sleep(5)
                print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
                print("You start sneaking towards the exit.")
                sleep(6)
                st=time.time()
                f=input("PRESS [S] to stand still!").title()
                rt=time.time()-st
                if f =="S" and rt<2:
                  print("You stand completely still and the guard simply yawns and turns to another side.")
                  sleep(3)
                  print("You continue to walk past them and make it to the path. You smile.")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
                  die(player1)
              elif e =="2":
                print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
                print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
                die(player1)
              elif e =="3":
                print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
                sleep(3)
                print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
                die(player1)
            elif d =="2":
              print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
              die(player1)
            elif d =="3":
              print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to find a disguise in some stores nearby to help you get past the guards.")
              print("'Hmm...' You say to yourself.")
              print("What would be the most effective disguise to fool the guards?")
              e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
              if e =="1":
                print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
                print("You approach the guards, and now all you need is a cover story or method to get past them.")
                f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
                if f =="1":
                  print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
                  sleep(3)
                  print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
                  die(player1)
                elif f =="2":
                  print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
                  print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
                  player1.newSkill()
                  nextChapter()#######################################################
              elif e =="2":
                print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
                sleep(3)
                print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
                die(player1)
              elif e =="3":
                print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
                sleep(5)
                st=time.time()
                f=input("PRESS [C] to cover your face!").title()
                rt = time.time()-st
                if f =="C" and rt<2:
                  print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
                  die(player1)
              else:
                print("You decide to dress as an old lady, and approach the the guards.")
                print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
                print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
                die(player1)
          else:
            print("You have been seen by a camera, and nearby guards have been alerted. You have nowehere to run and the heat is too much for you to handle. You drop to the ground and are shot in the back of the head. YOU DIED! THE END!")
            die(player1)
        else:
          print("You decide to curve around the perimeter of the village, only to realize that the entire perimeter is full of security cameras making sure no threats are coming over the walls.")
          print("You have been seen by a camera and a bunch of guards are dispatched, ambushing you when you least expect it. YOU DIED! THE END!")
          die(player1)
      else:
        print("You remain hidden in your position, but a spider lands on your head, causing you to back away in the pipe and creating a small splash sound. The monsters head towards you in the pipe and see you. One raises a gun at you and shoots. YOU DIED! THE END!")
        die(player1)
    elif b =="3":
      print("You hide deeper down the pipe, which conceals you until the monsters walk away.")
      print("You climb out of the pipe, looking around you. The path to the mountains is still far away, with the whole village in between you and the path.")
      print("You brush off the sweat on your forehead and look ahead for a way to get to the path.")
      c=input("1.Go to the covered market. 2.Go to the open market. 3.Go straight through the middle of the village. 4.Curve around the village perimeter.")
      if c =="1":
        print("You decide to head towards the covered market. The shade is really helpful in keeping you cool, but just as you are about to make it past the entire market, a monster notices you hiding behind a box and screams.")
        print("The nearby guards are dispatched and you are killed. YOU DIED! THE END!")
        die(player1)
      elif c == "2":
        print("You deicde to head through the open market. Although the desert heat is hard to bear, because of this, there are much less monsters roaming around this area.")
        sleep(3)
        print("You manage to make it past the entire market unseen, and the path to the mountains is almost within reach.")
        sleep(3)
        print("Just one problem.")
        print("The path is also guarded.")
        d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
        if d =="1":
          print("You decide to wait til the guards' shifts are over.")
          sleep(7)
          print("...")
          sleep(5)
          print("How long will this take?")
          sleep(3)
          e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
          if e =="1":
            print("You decide to keep waiting.")
            sleep(5)
            print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
            print("You start sneaking towards the exit.")
            sleep(6)
            st=time.time()
            f=input("PRESS [S] to stand still!").title()
            rt=time.time()-st
            if f =="S" and rt<2:
              print("You stand completely still and the guard simply yawns and turns to another side.")
              sleep(3)
              print("You continue to walk past them and make it to the path. You smile.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
            print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
            sleep(3)
            print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to find a disguise in some stores nearby to help you get past the guards.")
          print("'Hmm...' You say to yourself.")
          print("What would be the most effective disguise to fool the guards?")
          e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
          if e =="1":
            print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
            print("You approach the guards, and now all you need is a cover story or method to get past them.")
            f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
            if f =="1":
              print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
              sleep(3)
              print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
              print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
              player1.newSkill()
              nextChapter()#######################################################
          elif e =="2":
            print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
            sleep(3)
            print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
            sleep(5)
            st=time.time()
            f=input("PRESS [C] to cover your face!").title()
            rt = time.time()-st
            if f =="C" and rt<2:
              print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to dress as an old lady, and approach the the guards.")
            print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
            print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
            die(player1)
      elif c =="3":
        print("You decide to go straight through the center of the village, hiding behind boxes and stores every time a wave of monsters approach.")
        sleep(5)
        st=time.time()
        cc = input("PRESS [D] to duck under a camera's vision!").title()
        rt = time.time()-st
        if cc == "D" and rt<2:
          print("You duck under a camera's vision, allowing you to continue down the village and towards the path to the mountains.")
          sleep(3)
          print("You finally arrive. Just one problem.")
          print("The path is guarded.")
          d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
          if d =="1":
            print("You decide to wait til the guards' shifts are over.")
            sleep(7)
            print("...")
            sleep(5)
            print("How long will this take?")
            sleep(3)
            e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
            if e =="1":
              print("You decide to keep waiting.")
              sleep(5)
              print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
              print("You start sneaking towards the exit.")
              sleep(6)
              st=time.time()
              f=input("PRESS [S] to stand still!").title()
              rt=time.time()-st
              if f =="S" and rt<2:
                print("You stand completely still and the guard simply yawns and turns to another side.")
                sleep(3)
                print("You continue to walk past them and make it to the path. You smile.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
              print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
              sleep(3)
              print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
              die(player1)
          elif d =="2":
            print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
            die(player1)
          elif d =="3":
            print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to find a disguise in some stores nearby to help you get past the guards.")
            print("'Hmm...' You say to yourself.")
            print("What would be the most effective disguise to fool the guards?")
            e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
            if e =="1":
              print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
              print("You approach the guards, and now all you need is a cover story or method to get past them.")
              f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
              if f =="1":
                print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
                sleep(3)
                print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
                print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
                player1.newSkill()
                nextChapter()#######################################################
            elif e =="2":
              print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
              sleep(3)
              print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
              sleep(5)
              st=time.time()
              f=input("PRESS [C] to cover your face!").title()
              rt = time.time()-st
              if f =="C" and rt<2:
                print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
                die(player1)
            else:
              print("You decide to dress as an old lady, and approach the the guards.")
              print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
              print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
              die(player1)
        else:
          print("You have been seen by a camera, and nearby guards have been alerted. You have nowehere to run and the heat is too much for you to handle. You drop to the ground and are shot in the back of the head. YOU DIED! THE END!")
          die(player1)
      else:
        print("You decide to curve around the perimeter of the village, only to realize that the entire perimeter is full of security cameras making sure no threats are coming over the walls.")
        print("You have been seen by a camera and a bunch of guards are dispatched, ambushing you when you least expect it. YOU DIED! THE END!")
        die(player1)
    else:
      print("You decide to head down another way down the piping and find a crossroads. Crosspipes?")
      sleep(3)
      print("To the left, you feel a light, dry breeze.")
      print("Up ahead, you hear a rhythmic metal sound.")
      print("To the right, you feel chilling air.")
      sleep(3)
      c=input("1.Go left. 2.Go forwards. 3.Go right. 4.Turn back.")
      if c =="1":
        print("You decide to go left, and you keep going til you reach the end of the pipe. It seems to open up to somewhere outside, but it's too bright to see.")
        print("You deicde to crawl out of the pipe-")
        sleep(3)
        print("You are falling. You realize now that the pipe was connected to the side of a cliff, and you have just... exited it.")
        print("You fall, and fall.")
        sleep(5)
        print("Your bones are crushed against the rocky cliff base, your neck broken as well. YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You keep crawling through the pipe, but suddenly you hear gunshots. You frantically turn around and try to crawl away, but the sound of you doing so alerts nearby monsters and they peek into the pipe.")
        sleep(4)
        print("They see you, and without question, raise a gun towards you and fire. YOU DIED! THE END!")
        die(player1)
      elif c =="3":
        print("You crawl through the pipe, and eventually it opens up to the other end of the village, where the path to the mountains are. How convenient!")
        sleep(3)
        print("There's just one problem.")
        print("The path is guarded.")
        d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
        if d =="1":
          print("You decide to wait til the guards' shifts are over.")
          sleep(7)
          print("...")
          sleep(5)
          print("How long will this take?")
          sleep(3)
          e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
          if e =="1":
            print("You decide to keep waiting.")
            sleep(5)
            print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
            print("You start sneaking towards the exit.")
            sleep(6)
            st=time.time()
            f=input("PRESS [S] to stand still!").title()
            rt=time.time()-st
            if f =="S" and rt<2:
              print("You stand completely still and the guard simply yawns and turns to another side.")
              sleep(3)
              print("You continue to walk past them and make it to the path. You smile.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
            print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
            sleep(3)
            print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to find a disguise in some stores nearby to help you get past the guards.")
          print("'Hmm...' You say to yourself.")
          print("What would be the most effective disguise to fool the guards?")
          e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
          if e =="1":
            print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
            print("You approach the guards, and now all you need is a cover story or method to get past them.")
            f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
            if f =="1":
              print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
              sleep(3)
              print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
              print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
              player1.newSkill()
              nextChapter()#######################################################
          elif e =="2":
            print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
            sleep(3)
            print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
            sleep(5)
            st=time.time()
            f=input("PRESS [C] to cover your face!").title()
            rt = time.time()-st
            if f =="C" and rt<2:
              print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to dress as an old lady, and approach the the guards.")
            print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
            print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
            die(player1)
      else:
        print("You decide to turn back, but just as you reach the end of the pipe, a spider drops right on your face, causing you to move and splash some water inside the pipe.")
        print("This draws the attention of the monsters near the pipe and they peek in, seeing you. They frown and fire at you. YOU DIED! THE END!")
        die(player1)
  elif a =="3":
    print("You bring out a shiny pearl you (didn't) stole from a shop while walking over to the armory yesterday, and throw it into the sand in the other direction of you from the guards. ")
    sleep(3)
    print("You wait for one of the guards to notice the glint, and while one is gone, you sneak closer to the entrance. There are still two guards left.")
    b=input("1.Shoot the remaining guards. 2.Stealth kill both of them? 3.Throw another pearl. 4.Wait.")
    if b =="1":
      print("You start shooting at the remaining guards, but this draws the attention of the distracted guard, who shoots you down before you can trasnfer your spray to them. YOU DIED! THE END!")
      die(player1)
    elif b =="2":
      print("You sneak towards the two guards, ready to take them down by surprise, but suddenly the distracted guard looks in your direction, sees you and calls you out.")
      print("The guards you were sneaking towards are alerted of your presence and kill you immediately. YOU DIED! THE END!")
      die(player1)
    elif b =="3":
      print("You throw another pearl into a different direction, which draws the attention of yet another guard. One guard remains. You take this opportunity to strike, taking down the guard by stabbing them in the throat.")
      sleep(3)
      print("Being sure not to drop any blood to the ground, you carry the dead monster through the gate and inside some boxes of fruit. You close the box lid and look around.")
      sleep(3)
      print("The path to the mountains is up ahead, but there are many different ways to approach it...")
      c=input("1.Go to the covered market. 2.Go to the open market. 3.Go straight through the middle of the village. 4.Curve around the village perimeter.")
      if c =="1":
        print("You decide to head towards the covered market. The shade is really helpful in keeping you cool, but just as you are about to make it past the entire market, a monster notices you hiding behind a box and screams.")
        print("The nearby guards are dispatched and you are killed. YOU DIED! THE END!")
        die(player1)
      elif c == "2":
        print("You deicde to head through the open market. Although the desert heat is hard to bear, because of this, there are much less monsters roaming around this area.")
        sleep(3)
        print("You manage to make it past the entire market unseen, and the path to the mountains is almost within reach.")
        sleep(3)
        print("Just one problem.")
        print("The path is also guarded.")
        d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
        if d =="1":
          print("You decide to wait til the guards' shifts are over.")
          sleep(7)
          print("...")
          sleep(5)
          print("How long will this take?")
          sleep(3)
          e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
          if e =="1":
            print("You decide to keep waiting.")
            sleep(5)
            print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
            print("You start sneaking towards the exit.")
            sleep(6)
            st=time.time()
            f=input("PRESS [S] to stand still!").title()
            rt=time.time()-st
            if f =="S" and rt<2:
              print("You stand completely still and the guard simply yawns and turns to another side.")
              sleep(3)
              print("You continue to walk past them and make it to the path. You smile.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
            print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
            sleep(3)
            print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to find a disguise in some stores nearby to help you get past the guards.")
          print("'Hmm...' You say to yourself.")
          print("What would be the most effective disguise to fool the guards?")
          e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
          if e =="1":
            print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
            print("You approach the guards, and now all you need is a cover story or method to get past them.")
            f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
            if f =="1":
              print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
              sleep(3)
              print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
              print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
              player1.newSkill()
              nextChapter()#######################################################
          elif e =="2":
            print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
            sleep(3)
            print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
            sleep(5)
            st=time.time()
            f=input("PRESS [C] to cover your face!").title()
            rt = time.time()-st
            if f =="C" and rt<2:
              print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to dress as an old lady, and approach the the guards.")
            print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
            print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
            die(player1)
      elif c =="3":
        print("You decide to go straight through the center of the village, hiding behind boxes and stores every time a wave of monsters approach.")
        sleep(5)
        st=time.time()
        cc = input("PRESS [D] to duck under a camera's vision!").title()
        rt = time.time()-st
        if cc == "D" and rt<2:
          print("You duck under a camera's vision, allowing you to continue down the village and towards the path to the mountains.")
          sleep(3)
          print("You finally arrive. Just one problem.")
          print("The path is guarded.")
          d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
          if d =="1":
            print("You decide to wait til the guards' shifts are over.")
            sleep(7)
            print("...")
            sleep(5)
            print("How long will this take?")
            sleep(3)
            e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
            if e =="1":
              print("You decide to keep waiting.")
              sleep(5)
              print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
              print("You start sneaking towards the exit.")
              sleep(6)
              st=time.time()
              f=input("PRESS [S] to stand still!").title()
              rt=time.time()-st
              if f =="S" and rt<2:
                print("You stand completely still and the guard simply yawns and turns to another side.")
                sleep(3)
                print("You continue to walk past them and make it to the path. You smile.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
              print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
              sleep(3)
              print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
              die(player1)
          elif d =="2":
            print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
            die(player1)
          elif d =="3":
            print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to find a disguise in some stores nearby to help you get past the guards.")
            print("'Hmm...' You say to yourself.")
            print("What would be the most effective disguise to fool the guards?")
            e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
            if e =="1":
              print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
              print("You approach the guards, and now all you need is a cover story or method to get past them.")
              f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
              if f =="1":
                print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
                sleep(3)
                print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
                print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
                player1.newSkill()
                nextChapter()#######################################################
            elif e =="2":
              print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
              sleep(3)
              print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
              sleep(5)
              st=time.time()
              f=input("PRESS [C] to cover your face!").title()
              rt = time.time()-st
              if f =="C" and rt<2:
                print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
                die(player1)
            else:
              print("You decide to dress as an old lady, and approach the the guards.")
              print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
              print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
              die(player1)
        else:
          print("You have been seen by a camera, and nearby guards have been alerted. You have nowehere to run and the heat is too much for you to handle. You drop to the ground and are shot in the back of the head. YOU DIED! THE END!")
          die(player1)
      else:
        print("You decide to curve around the perimeter of the village, only to realize that the entire perimeter is full of security cameras making sure no threats are coming over the walls.")
        print("You have been seen by a camera and a bunch of guards are dispatched, ambushing you when you least expect it. YOU DIED! THE END!")
        die(player1)
    else:
      print("You wait for a bit, and the previously distracted guard shakes it off and heads back to their mates. Now there are three guards at the gate.")
      print("You sigh and decide to wait there even longer, hoping that they will eventually leave for lunch or something.")
      sleep(7)
      print("The heat is about to kill you when the guards stand up from their locations and head into the village, leaving the gate wide open.")
      print("You quickly shuffle towards the gate and enter, being sure not to be seen by anyone. You chill in the shade for a while, before looking up ahead, where the path to the mountains is.")
      sleep(5)
      print("You look around the village. There are many ways to approach the path.")
      c=input("1.Go to the covered market. 2.Go to the open market. 3.Go straight through the middle of the village. 4.Curve around the village perimeter.")
      if c =="1":
        print("You decide to head towards the covered market. The shade is really helpful in keeping you cool, but just as you are about to make it past the entire market, a monster notices you hiding behind a box and screams.")
        print("The nearby guards are dispatched and you are killed. YOU DIED! THE END!")
        die(player1)
      elif c == "2":
        print("You deicde to head through the open market. Although the desert heat is hard to bear, because of this, there are much less monsters roaming around this area.")
        sleep(3)
        print("You manage to make it past the entire market unseen, and the path to the mountains is almost within reach.")
        sleep(3)
        print("Just one problem.")
        print("The path is also guarded.")
        d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
        if d =="1":
          print("You decide to wait til the guards' shifts are over.")
          sleep(7)
          print("...")
          sleep(5)
          print("How long will this take?")
          sleep(3)
          e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
          if e =="1":
            print("You decide to keep waiting.")
            sleep(5)
            print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
            print("You start sneaking towards the exit.")
            sleep(6)
            st=time.time()
            f=input("PRESS [S] to stand still!").title()
            rt=time.time()-st
            if f =="S" and rt<2:
              print("You stand completely still and the guard simply yawns and turns to another side.")
              sleep(3)
              print("You continue to walk past them and make it to the path. You smile.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
            print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
            sleep(3)
            print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
          die(player1)
        elif d =="3":
          print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to find a disguise in some stores nearby to help you get past the guards.")
          print("'Hmm...' You say to yourself.")
          print("What would be the most effective disguise to fool the guards?")
          e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
          if e =="1":
            print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
            print("You approach the guards, and now all you need is a cover story or method to get past them.")
            f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
            if f =="1":
              print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
              sleep(3)
              print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
              print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
              player1.newSkill()
              nextChapter()#######################################################
          elif e =="2":
            print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
            sleep(3)
            print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
            sleep(5)
            st=time.time()
            f=input("PRESS [C] to cover your face!").title()
            rt = time.time()-st
            if f =="C" and rt<2:
              print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
              die(player1)
          else:
            print("You decide to dress as an old lady, and approach the the guards.")
            print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
            print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
            die(player1)
      elif c =="3":
        print("You decide to go straight through the center of the village, hiding behind boxes and stores every time a wave of monsters approach.")
        sleep(5)
        st=time.time()
        cc = input("PRESS [D] to duck under a camera's vision!").title()
        rt = time.time()-st
        if cc == "D" and rt<2:
          print("You duck under a camera's vision, allowing you to continue down the village and towards the path to the mountains.")
          sleep(3)
          print("You finally arrive. Just one problem.")
          print("The path is guarded.")
          d=input("1.Wait til their shift is over. 2.Distract them. 3.Sneak past them. 4.Find a disguise.")
          if d =="1":
            print("You decide to wait til the guards' shifts are over.")
            sleep(7)
            print("...")
            sleep(5)
            print("How long will this take?")
            sleep(3)
            e=input("1.Keep waiting. 2.Distract the guards. 3.Sneak past them. 4.Find a disguise.")
            if e =="1":
              print("You decide to keep waiting.")
              sleep(5)
              print("The guards finally stand up and leave their post to grab a snack. A single guard remains at the gate, looking really tired. This is your chance.")
              print("You start sneaking towards the exit.")
              sleep(6)
              st=time.time()
              f=input("PRESS [S] to stand still!").title()
              rt=time.time()-st
              if f =="S" and rt<2:
                print("You stand completely still and the guard simply yawns and turns to another side.")
                sleep(3)
                print("You continue to walk past them and make it to the path. You smile.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("The guard notices you trying to sneak past and quickdraws his pistol, shooting you right in the head. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You try to distract the guards, but they notice you peeking out to check if they have been distracted. (They were not). They shout out, and all the monsters around the area surround you in no time.")
              print("You have nowhere to run to. The monsters kill you and feast upon your flesh. YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You try to sneak past the guards, but since there are so many, when you accidentally step on a twig, you alert one of them and the guards are immediately onto you. They shoot you in the head. YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to stop waiting and find a disguise to get past the guards, but since you have been waiting so long, your senses are a bit dull and you fail to notice a monster child staring directly at you.")
              sleep(3)
              print("The child tells their parents about you and all the monsters nearby immediately surround you. You have nowhere to run, and the monsters feast upon your flesh. YOU DIED! THE END!")
              die(player1)
          elif d =="2":
            print("You try to distract the guards with a rock, but one catches the origin of the rock and traces it back to your location. All of a sudden, the guards ambush you and feast upon your body. YOU DIED! THE END!")
            die(player1)
          elif d =="3":
            print("You decide to sneak your way past the guards. However, you suddenly feel the urge to sneeze. You are unable to suppress your sneeze reflex and the guards are alerted of your position. They shoot you multiple times. YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to find a disguise in some stores nearby to help you get past the guards.")
            print("'Hmm...' You say to yourself.")
            print("What would be the most effective disguise to fool the guards?")
            e=input("1.Children's clothes. 2.Solider. 3.Hiker. 4.Old lady.")
            if e =="1":
              print("You decide to wear the children's clothes, since you are very small compared to the average monster.")
              print("You approach the guards, and now all you need is a cover story or method to get past them.")
              f=input("1.Your ball is on the path! 2.Start crying. 3.Start screaming.")
              if f =="1":
                print("You throw a ball over the guards and onto the path, and point it out to the guards. You try to walk past them, but they don't let you through, and instead a guard heads onto the path and retrieves the ball for you.")
                sleep(3)
                print("While returning the ball, the soldier sees your face and realizes that you are human. They pull out their gun and shoot you in the head. YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You start crying and head towards the path. Since the guards have no idea what to do with you, they just levae you be.")
                print("You keep crying and walking until you make it far enough up the path. You smile and keep going.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You head over to the guards and start screaming, pointing at something in the village. All the guards come over to you and head towards the direction you are pointing at, leaving the path completely empty. You smile to yourself and walk right through, heading up the path.")
                player1.newSkill()
                nextChapter()#######################################################
            elif e =="2":
              print("You decide to dress as a soldier. You head over to the guards in your attire, and as you approach, one of the monsters say something that you (obviously) don't understand.")
              sleep(3)
              print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You deicde to put on a hiker's outfit, and head towards the guards. They allow you to pass.")
              sleep(5)
              st=time.time()
              f=input("PRESS [C] to cover your face!").title()
              rt = time.time()-st
              if f =="C" and rt<2:
                print("You cover your face just as a guard turns over, and you keep walking past. You reach the path and smirk.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You fail to cover your face, and a guard glances at you and sees that you are human. They shoot you in the head. YOU DIED! THE END!")
                die(player1)
            else:
              print("You decide to dress as an old lady, and approach the the guards.")
              print("One of the guards try to say something to you, but you just shake your head and keep walking towards the path.")
              print("You ignore them and try to keep walking, but the guards stop you in your tracks and look at your face. They discover that you are a human and immediately shoot you in the stomach. YOU DIED! THE END!")
              die(player1)
        else:
          print("You have been seen by a camera, and nearby guards have been alerted. You have nowehere to run and the heat is too much for you to handle. You drop to the ground and are shot in the back of the head. YOU DIED! THE END!")
          die(player1)
      else:
        print("You decide to curve around the perimeter of the village, only to realize that the entire perimeter is full of security cameras making sure no threats are coming over the walls.")
        print("You have been seen by a camera and a bunch of guards are dispatched, ambushing you when you least expect it. YOU DIED! THE END!")
        die(player1)
  else:
    print("You try to shoot the guards, but because you are unable to kill all of them at once, they quickly discover you after the first monster falls and shoot you to death. YOU DIED! THE END!")
    die(player1)

def hillsVillage(player1):#used in 1 scene only. Formatted.
  print("You decide to land in the hillside, since being that high up would probably be a good vantage point for the upcoming hike to the Summit.")
  print("The spaceship is parked in an obscure location, and after making sure that you have everything you need, you and Cara head towards the Summit, which is very noticeable at the horizon.")
  sleep(5)
  print("'Woah...' Cara wonders at the landscape before you, and smiles. 'I haven't seen such beautiful scenery since... Years ago, before the zombies...'")
  print("You squint and look up ahead, and frown. There seems to be a village right in your way towards the mountains. There is no alternative route around it.")
  sleep(5)
  a = input("1.Head through the village. 2.Scout out the village. 3.Find an alternative route. 4.Sneak into the village unseen.")
  if a =="1":
    print("You and Cara decide to head on into the village, only to realise that it is not a village of humans. The inhabitants of the village immediately surround you and feast upon your meaty flesh. YOU DIED! THE END!")
    die(player1)
  elif a == "2":
    print("You decide to scout out the village before making any moves. You post yourself at a distance from the village, and successfully identify that the inhabitants of the village are not humans, and most likely are hostile towards you.")
    sleep(5)
    print("After taking a record of when the entrance is guarded, you manage to sneak into the village unseen at a blind spot.")
    print("Cara sighs in relief. 'Now we just need to get to the other side of an alien-infested village. Excellent.'")
    sleep(4)
    print("You glance around, searching for the safest path across.")
    b=input("1.North. 2.East. 3.South. 4.West.")
    if b =="3":
      print("You decide to head south.")
      sleep(3)
      print("You manage to barely escape the cone of vision of some approaching aliens, and upon a closer look, realize that they are more like monsters, with their thick hide and long claws.")
      print("You follow down the path to the south, and it seemed to be relatively peaceful, until the village alarms suddenly blared, altering every monster in the vicinity.")
      c=input("1.Hide inside a nearby cart. 2.Make a run for the end of the path, where a small house could be used for cover. 3.Hide in an alleyway. 4.Stay where you are and wait out the panic.")
      if c =="1":
        print("You decide to hide inside a nearby cart. Amidst the panic from the monsters, someone grabs the cart and starts steering off somewhere. In the distance, you hear explosions. You and Cara look at each other, confused. Suddenly, the cart pusher stops, and they seem to be running away. You-")
        sleep(7)
        print("-You have been hit by a fatal explosion. YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You decide to make a run for it, to the small house at the end of the path.")
        sleep(6)
        st = time.time()
        d=input("PRESS [J] to jump over the root!").title()
        rt = time.time()-st
        if d =="J" and rt < 2:
          print("You jumped over the root of a tree, which would've tripped you up.")
          print("You and Cara make it inside the house and close the door just as an explosion is heard outside. Another explosion can be heard farther away.")
          sleep(5)
          print("Eventually, the explosions subside.")
          print("You and Cara head outside, and discover that half of the village has been blown to the ground. Monsters are running around everywhere, carrying supplies.")
          sleep(3)
          print("You and Cara turn away from that side of the village and continue heading towards the mountains.")
          print("Cara pulls you behind a boulder. 'Look! Watch tower!' She whispers to you and points towards your right. You nod.")
          e=input("1.Sneak under the watch tower. 2.Run for it when they aren't looking. 3.Wait for them to swap lookouts.")
          if e == "1":
            print("You and Cara decide to sneak under the watch tower.")
            sleep(3)
            print("You managed to make it to directly under the watch tower, but you begin to question whether you are able to make it all the way to the end of the path without being seen by them.")
            print("You wonder if taking out the guard tower is a good call.")
            f=input("1.Take out the guard tower. 2.Continue sneaking. 3.Cause a distraction. 4.Take a risky route to avoid their gaze.")
            if f =="1":
              print("You and Cara slowly climb up the ladder to the watch tower. You raise a hand to signal to Cara when you will open the trapdoor into the building.")
              print(" - TIMED EVENT INCOMING - ")
              print("(hit the key between 1 and 3 seconds)")
              sleep(6)
              st=time.time()
              g=input("PRESS [O] (the letter) to open the trapdoor between 1 and 3 seconds to get the perfect timing:").title()
              rt = time.time()-st
              if g == "O" and (rt>1 and rt<3):
                print("You timed it perfectly, and busted into the tower when the guards weren't ready.")
                print("You chopped off the head of one of the monsters, and Cara stabbed the other in its heart.")
                sleep(5)
                print("You and Cara make it down the tower and walk peacefully towards the mountains, uninterrupted.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You opened the trapdoor at an inopportune time, and you both got shot in the head by the guards. YOU DIED! THE END!")
                die(player1)
            elif f=="2":
              print("You decide to keep sneaking, since it has been working this whole time.")
              sleep(3)
              print("You and Cara head back onto the path, and you accidentally step on a twig.")
              sleep(4)
              print("You look behind you to find that the guards have seen you, guns already raised.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You grab a huge rock from the ground and lob it towards the edge of the village.")
              print("A guard notices, and signals for the other guard to look in that direction.")
              sleep(7)
              st=time.time()
              g=input("PRESS [S] to seize this opportunity!").title()
              rt = time.time()-st
              if g =="S" and rt < 2:
                print("You take this opportunity to make a run for it, and you and Cara manage to make it to the end of the path and out of the tower's sight before they stop investigating the sound.")
                print("Cara pants. 'Nice one. Hopefully these mountains will be a bit calmer.'")
                print("You calm your breathing, and look up the mountains ahead of you. 'Hopefully.'")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to make a run for it in time, and the guards see you when they stopped looking for what cause the sound.")
                print("YOU DIED! THE END!")
                die(player1)
            else:
              print("You try to walk a risky path on the side of a hill to avoid their gaze, but you slip on the slanted ground, and you roll right into a boulder, crushing your skull. YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You decide to make a run for it when the guards aren't looking.")
            sleep(5)
            st=time.time()
            f=input("PRESS [H] to hide behind a tree!").title()
            rt = time.time()-st
            if f =="H" and rt <2:
              print("You quickly slide behind a tree to avoid being seen, just as the guards turn over.")
              print("Their vision lingers on your position.")
              sleep(4)
              print("The guards turn away once more, and you and Cara quickly sneak back onto the path, and make it out of the watch tower's sight.")
              print("'Let's see what these mountains have to offer.' You say, slowly looking up the side of the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You tried to hide behind a tree, but you were too slow. The guards turned and saw you down on the path, and grenades rained from the sky, killing the both of you. YOU DIED! THE END!")
              die(player1)
          else:
            print("You and Cara decide to wait for the guards to switch with someone else.")
            sleep(3)
            print("Suddenly, you hear a growl behind you.")
            print("You turn, only to discover that a wild alien animal has managed to sneak up on you, and it just mauled Cara. It leaps at you, too, and you are dead in seconds. YOU DIED! THE END!")
            die(player1)
        else:
          print("You tripped over a branch, and just as you were able to get up from the ground, an explosion kills you. THE END!")
          die(player1)
      elif c =="3":
        print("You push Cara into a nearby alleyway as the monsters around you panic, but they run past the alleyway you are in no problem. Suddenly, you hear explosions somewhere inside the village. 'We'll be fine, right?' Cara's voice is a little shaky.")
        sleep(3)
        print("You look up, and find something flying directly into the alley. You and Cara try to run out in time, but the explosion is mostly focused to the length of the alley, which is where you two are. Or were. YOU DIED! THE END!")
        die(player1)
      else:
        print("You and Cara stay where you are, and as the monsters around the village panic, you remain exactly where you are.")
        sleep(3)
        print("Suddenly, explosions are heard in the distance.")
        print("You also hear a group of monsters approaching your hiding location.")
        print("Cara tugs on your sleeve. 'What do we do?' She mouths.")
        d=input("1.Remain in your position. 2.Make a run for it. 3.Slowly move to a different hiding position.")
        if d =="1":
          if player1.t3 == True:
            print("You remained in your position, and the monsters managed to walk by you without noticing. You and Cara slowly head away from that location, and find a clear path straight to the mountains. 'I think the village is behind us-' You start, but Cara quickly pulls you behind a boulder.")
            print("She points to the right, where a watch tower stands. You nod.")
            e=input("1.Sneak under the watch tower. 2.Run for it when they aren't looking. 3.Wait for them to swap lookouts.")
            if e == "1":
              print("You and Cara decide to sneak under the watch tower.")
              sleep(3)
              print("You managed to make it to directly under the watch tower, but you begin to question whether you are able to make it all the way to the end of the path without being seen by them.")
              print("You wonder if taking out the guard tower is a good call.")
              f=input("1.Take out the guard tower. 2.Continue sneaking. 3.Cause a distraction. 4.Take a risky route to avoid their gaze.")
              if f =="1":
                print("You and Cara slowly climb up the ladder to the watch tower. You raise a hand to signal to Cara when you will open the trapdoor into the building.")
                print(" - TIMED EVENT INCOMING - ")
                print("(hit the key between 1 and 3 seconds)")
                sleep(6)
                st=time.time()
                g=input("PRESS [O] (the letter) to open the trapdoor between 1 and 3 seconds to get the perfect timing:").title()
                rt = time.time()-st
                if g == "O" and (rt>1 and rt<3):
                  print("You timed it perfectly, and busted into the tower when the guards weren't ready.")
                  print("You chopped off the head of one of the monsters, and Cara stabbed the other in its heart.")
                  sleep(5)
                  print("You and Cara make it down the tower and walk peacefully towards the mountains, uninterrupted.")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You opened the trapdoor at an inopportune time, and you both got shot in the head by the guards. YOU DIED! THE END!")
                  die(player1)
              elif f=="2":
                print("You decide to keep sneaking, since it has been working this whole time.")
                sleep(3)
                print("You and Cara head back onto the path, and you accidentally step on a twig.")
                sleep(4)
                print("You look behind you to find that the guards have seen you, guns already raised.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You grab a huge rock from the ground and lob it towards the edge of the village.")
                print("A guard notices, and signals for the other guard to look in that direction.")
                sleep(7)
                st=time.time()
                g=input("PRESS [S] to seize this opportunity!").title()
                rt = time.time()-st
                if g =="S" and rt < 2:
                  print("You take this opportunity to make a run for it, and you and Cara manage to make it to the end of the path and out of the tower's sight before they stop investigating the sound.")
                  print("Cara pants. 'Nice one. Hopefully these mountains will be a bit calmer.'")
                  print("You calm your breathing, and look up the mountains ahead of you. 'Hopefully.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You failed to make a run for it in time, and the guards see you when they stopped looking for what cause the sound.")
                  print("YOU DIED! THE END!")
                  die(player1)
              else:
                print("You try to walk a risky path on the side of a hill to avoid their gaze, but you slip on the slanted ground, and you roll right into a boulder, crushing your skull. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You decide to make a run for it when the guards aren't looking.")
              sleep(5)
              st=time.time()
              f=input("PRESS [H] to hide behind a tree!").title()
              rt = time.time()-st
              if f =="H" and rt <2:
                print("You quickly slide behind a tree to avoid being seen, just as the guards turn over.")
                print("Their vision lingers on your position.")
                sleep(4)
                print("The guards turn away once more, and you and Cara quickly sneak back onto the path, and make it out of the watch tower's sight.")
                print("'Let's see what these mountains have to offer.' You say, slowly looking up the side of the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You tried to hide behind a tree, but you were too slow. The guards turned and saw you down on the path, and grenades rained from the sky, killing the both of you. YOU DIED! THE END!")
                die(player1)
            else:
              print("You and Cara decide to wait for the guards to switch with someone else.")
              sleep(3)
              print("Suddenly, you hear a growl behind you.")
              print("You turn, only to discover that a wild alien animal has managed to sneak up on you, and it just mauled Cara. It leaps at you, too, and you are dead in seconds. YOU DIED! THE END!")
              die(player1)
          else:
            print("You remain where you are, but unforunately one of the monsters saw your leg poking out from your hiding spot and they kill you immediately. YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You and Cara make a run for it, but unluckily for you, the monsters noticed and they were wielding guns. They shoot you in the back and you bleed out on the streets. YOU DIED! THE END!")
          die(player1)
        else:
          print("You and Cara slowly move towards a new hiding spot, but unfortunately, the monsters saw you, and they brought out their guns and shot you. THE END!")
          die(player1)
    else:
      print("You decide to head in this direction, only to be found by a set of aliens turning the corner around a building. They immediately charge at you, alerting all nearby aliens, and they all swarm over you and Cara. There was nothing you could do. YOU DIED! THE END!")
      die(player1)
  elif a =="3":
    print("You decide to scout out an alternative route by curving around the mountain. However, you suddenly lose your foothold and slip, directly into Cara.")
    print("You knock over the both of you and you roll down the hillside, crashing your skulls against a pile of boulders at the base of the mountain. YOU DIED! THE END!")
    die(player1)
  else:
    print("You decide to sneak into the village. After identifying that the inhabitants of the village are not human, you and Cara carefully crouch your way under the watch towers at the edge of the village, and manage to make it through into the village alive.")
    sleep(5)
    print("Cara sighs in relief. 'Now we just need to get to the other side of an alien-infested village. Excellent.'")
    sleep(4)
    print("You glance around, searching for the safest path across.")
    b=input("1.North. 2.East. 3.South. 4.West.")
    if b =="3":
      print("You decide to head south.")
      sleep(3)
      print("You manage to barely escape the cone of vision of some approaching aliens, and upon a closer look, realize that they are more like monsters, with their thick hide and long claws.")
      print("You follow down the path to the south, and it seemed to be relatively peaceful, until the village alarms suddenly blared, altering every monster in the vicinity.")
      c=input("1.Hide inside a nearby cart. 2.Make a run for the end of the path, where a small house could be used for cover. 3.Hide in an alleyway. 4.Stay where you are and wait out the panic.")
      if c =="1":
        print("You decide to hide inside a nearby cart. Amidst the panic from the monsters, someone grabs the cart and starts steering off somewhere. In the distance, you hear explosions. You and Cara look at each other, confused. Suddenly, the cart pusher stops, and they seem to be running away. You-")
        sleep(7)
        print("-You have been hit by a fatal explosion. YOU DIED! THE END!")
        die(player1)
      elif c =="2":
        print("You decide to make a run for it, to the small house at the end of the path.")
        sleep(6)
        st = time.time()
        d=input("PRESS [J] to jump over the root!").title()
        rt = time.time()-st
        if d =="J" and rt < 2:
          print("You jumped over the root of a tree, which would've tripped you up.")
          print("You and Cara make it inside the house and close the door just as an explosion is heard outside. Another explosion can be heard farther away.")
          sleep(5)
          print("Eventually, the explosions subside.")
          print("You and Cara head outside, and discover that half of the village has been blown to the ground. Monsters are running around everywhere, carrying supplies.")
          sleep(3)
          print("You and Cara turn away from that side of the village and continue heading towards the mountains.")
          print("Cara pulls you behind a boulder. 'Look! Watch tower!' She whispers to you and points towards your right. You nod.")
          e=input("1.Sneak under the watch tower. 2.Run for it when they aren't looking. 3.Wait for them to swap lookouts.")
          if e == "1":
            print("You and Cara decide to sneak under the watch tower.")
            sleep(3)
            print("You managed to make it to directly under the watch tower, but you begin to question whether you are able to make it all the way to the end of the path without being seen by them.")
            print("You wonder if taking out the guard tower is a good call.")
            f=input("1.Take out the guard tower. 2.Continue sneaking. 3.Cause a distraction. 4.Take a risky route to avoid their gaze.")
            if f =="1":
              print("You and Cara slowly climb up the ladder to the watch tower. You raise a hand to signal to Cara when you will open the trapdoor into the building.")
              print(" - TIMED EVENT INCOMING - ")
              print("(hit the key between 1 and 3 seconds)")
              sleep(6)
              st=time.time()
              g=input("PRESS [O] (the letter) to open the trapdoor between 1 and 3 seconds to get the perfect timing:").title()
              rt = time.time()-st
              if g == "O" and (rt>1 and rt<3):
                print("You timed it perfectly, and busted into the tower when the guards weren't ready.")
                print("You chopped off the head of one of the monsters, and Cara stabbed the other in its heart.")
                sleep(5)
                print("You and Cara make it down the tower and walk peacefully towards the mountains, uninterrupted.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You opened the trapdoor at an inopportune time, and you both got shot in the head by the guards. YOU DIED! THE END!")
                die(player1)
            elif f=="2":
              print("You decide to keep sneaking, since it has been working this whole time.")
              sleep(3)
              print("You and Cara head back onto the path, and you accidentally step on a twig.")
              sleep(4)
              print("You look behind you to find that the guards have seen you, guns already raised.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You grab a huge rock from the ground and lob it towards the edge of the village.")
              print("A guard notices, and signals for the other guard to look in that direction.")
              sleep(7)
              st=time.time()
              g=input("PRESS [S] to seize this opportunity!").title()
              rt = time.time()-st
              if g =="S" and rt < 2:
                print("You take this opportunity to make a run for it, and you and Cara manage to make it to the end of the path and out of the tower's sight before they stop investigating the sound.")
                print("Cara pants. 'Nice one. Hopefully these mountains will be a bit calmer.'")
                print("You calm your breathing, and look up the mountains ahead of you. 'Hopefully.'")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You failed to make a run for it in time, and the guards see you when they stopped looking for what cause the sound.")
                print("YOU DIED! THE END!")
                die(player1)
            else:
              print("You try to walk a risky path on the side of a hill to avoid their gaze, but you slip on the slanted ground, and you roll right into a boulder, crushing your skull. YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You decide to make a run for it when the guards aren't looking.")
            sleep(5)
            st=time.time()
            f=input("PRESS [H] to hide behind a tree!").title()
            rt = time.time()-st
            if f =="H" and rt <2:
              print("You quickly slide behind a tree to avoid being seen, just as the guards turn over.")
              print("Their vision lingers on your position.")
              sleep(4)
              print("The guards turn away once more, and you and Cara quickly sneak back onto the path, and make it out of the watch tower's sight.")
              print("'Let's see what these mountains have to offer.' You say, slowly looking up the side of the mountains.")
              player1.newSkill()
              nextChapter()#######################################################
            else:
              print("You tried to hide behind a tree, but you were too slow. The guards turned and saw you down on the path, and grenades rained from the sky, killing the both of you. YOU DIED! THE END!")
              die(player1)
          else:
            print("You and Cara decide to wait for the guards to switch with someone else.")
            sleep(3)
            print("Suddenly, you hear a growl behind you.")
            print("You turn, only to discover that a wild alien animal has managed to sneak up on you, and it just mauled Cara. It leaps at you, too, and you are dead in seconds. YOU DIED! THE END!")
            die(player1)
        else:
          print("You tripped over a branch, and just as you were able to get up from the ground, an explosion kills you. THE END!")
          die(player1)
      elif c =="3":
        print("You push Cara into a nearby alleyway as the monsters around you panic, but they run past the alleyway you are in no problem. Suddenly, you hear explosions somewhere inside the village. 'We'll be fine, right?' Cara's voice is a little shaky.")
        sleep(3)
        print("You look up, and find something flying directly into the alley. You and Cara try to run out in time, but the explosion is mostly focused to the length of the alley, which is where you two are. Or were. YOU DIED! THE END!")
        die(player1)
      else:
        print("You and Cara stay where you are, and as the monsters around the village panic, you remain exactly where you are.")
        sleep(3)
        print("Suddenly, explosions are heard in the distance.")
        print("You also hear a group of monsters approaching your hiding location.")
        print("Cara tugs on your sleeve. 'What do we do?' She mouths.")
        d=input("1.Remain in your position. 2.Make a run for it. 3.Slowly move to a different hiding position.")
        if d =="1":
          if player1.t3 == True:
            print("You remained in your position, and the monsters managed to walk by you without noticing. You and Cara slowly head away from that location, and find a clear path straight to the mountains. 'I think the village is behind us-' You start, but Cara quickly pulls you behind a boulder.")
            print("She points to the right, where a watch tower stands. You nod.")
            e=input("1.Sneak under the watch tower. 2.Run for it when they aren't looking. 3.Wait for them to swap lookouts.")
            if e == "1":
              print("You and Cara decide to sneak under the watch tower.")
              sleep(3)
              print("You managed to make it to directly under the watch tower, but you begin to question whether you are able to make it all the way to the end of the path without being seen by them.")
              print("You wonder if taking out the guard tower is a good call.")
              f=input("1.Take out the guard tower. 2.Continue sneaking. 3.Cause a distraction. 4.Take a risky route to avoid their gaze.")
              if f =="1":
                print("You and Cara slowly climb up the ladder to the watch tower. You raise a hand to signal to Cara when you will open the trapdoor into the building.")
                print(" - TIMED EVENT INCOMING - ")
                print("(hit the key between 1 and 3 seconds)")
                sleep(6)
                st=time.time()
                g=input("PRESS [O] (the letter) to open the trapdoor between 1 and 3 seconds to get the perfect timing:").title()
                rt = time.time()-st
                if g == "O" and (rt>1 and rt<3):
                  print("You timed it perfectly, and busted into the tower when the guards weren't ready.")
                  print("You chopped off the head of one of the monsters, and Cara stabbed the other in its heart.")
                  sleep(5)
                  print("You and Cara make it down the tower and walk peacefully towards the mountains, uninterrupted.")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You opened the trapdoor at an inopportune time, and you both got shot in the head by the guards. YOU DIED! THE END!")
                  die(player1)
              elif f=="2":
                print("You decide to keep sneaking, since it has been working this whole time.")
                sleep(3)
                print("You and Cara head back onto the path, and you accidentally step on a twig.")
                sleep(4)
                print("You look behind you to find that the guards have seen you, guns already raised.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You grab a huge rock from the ground and lob it towards the edge of the village.")
                print("A guard notices, and signals for the other guard to look in that direction.")
                sleep(7)
                st=time.time()
                g=input("PRESS [S] to seize this opportunity!").title()
                rt = time.time()-st
                if g =="S" and rt < 2:
                  print("You take this opportunity to make a run for it, and you and Cara manage to make it to the end of the path and out of the tower's sight before they stop investigating the sound.")
                  print("Cara pants. 'Nice one. Hopefully these mountains will be a bit calmer.'")
                  print("You calm your breathing, and look up the mountains ahead of you. 'Hopefully.'")
                  player1.newSkill()
                  nextChapter()#######################################################
                else:
                  print("You failed to make a run for it in time, and the guards see you when they stopped looking for what cause the sound.")
                  print("YOU DIED! THE END!")
                  die(player1)
              else:
                print("You try to walk a risky path on the side of a hill to avoid their gaze, but you slip on the slanted ground, and you roll right into a boulder, crushing your skull. YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You decide to make a run for it when the guards aren't looking.")
              sleep(5)
              st=time.time()
              f=input("PRESS [H] to hide behind a tree!").title()
              rt = time.time()-st
              if f =="H" and rt <2:
                print("You quickly slide behind a tree to avoid being seen, just as the guards turn over.")
                print("Their vision lingers on your position.")
                sleep(4)
                print("The guards turn away once more, and you and Cara quickly sneak back onto the path, and make it out of the watch tower's sight.")
                print("'Let's see what these mountains have to offer.' You say, slowly looking up the side of the mountains.")
                player1.newSkill()
                nextChapter()#######################################################
              else:
                print("You tried to hide behind a tree, but you were too slow. The guards turned and saw you down on the path, and grenades rained from the sky, killing the both of you. YOU DIED! THE END!")
                die(player1)
            else:
              print("You and Cara decide to wait for the guards to switch with someone else.")
              sleep(3)
              print("Suddenly, you hear a growl behind you.")
              print("You turn, only to discover that a wild alien animal has managed to sneak up on you, and it just mauled Cara. It leaps at you, too, and you are dead in seconds. YOU DIED! THE END!")
              die(player1)
          else:
            print("You remain where you are, but unforunately one of the monsters saw your leg poking out from your hiding spot and they kill you immediately. YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You and Cara make a run for it, but unluckily for you, the monsters noticed and they were wielding guns. They shoot you in the back and you bleed out on the streets. YOU DIED! THE END!")
          die(player1)
        else:
          print("You and Cara slowly move towards a new hiding spot, but unfortunately, the monsters saw you, and they brought out their guns and shot you. THE END!")
          die(player1)
    else:
      print("You decide to head in this direction, only to be found by a set of aliens turning the corner around a building. They immediately charge at you, alerting all nearby aliens, and they all swarm over you and Cara. There was nothing you could do. YOU DIED! THE END!")
      die(player1)

def caveVillage(player1):#used in multiple scenes. Formatted for NICO. Swap dialogue from NICO to CARA if need be. (#dialogueN used: search for it!)
  print("You delve deeper through the caves, and finally you break the silence.")
  print("'This place is lovely, don't you think?'")
  sleep(4)
  print("No response.")
  sleep(3)
  print("You sigh and keep on moving.")
  print("Suddenly, you hear some sort of pulley system being used in the distance, and water splashing sounds.")
  a=input("1.Investigate. 2.Hide somewhere. 3.Keep walking. 4.Stand still and listen.")
  if a=="1":
    #dialogueN
    print("You wave Nico on, and the two of you slowly inch towards the source of the pulley sounds.")
    print("As you get closer, the squeaking from the pulley system becomes more apparent.")
    sleep(3)
    print("You also hear the sploshing of water. Must be some sort of well.")
    print("Slowly, you turn the corner, and you find a monster collecting a bucket of water from the well. They may know where the Summit is.")
    b=input("1.Ask them where it is. 2.Follow them. 3.Leave them alone and head where you were headed.")
    if b =="1":
      print("You walk out to ask the monster, but they see you and immediately run away.")
      print("They drop the bucket onto the ground, and you hear a deep growl behind you.")
      sleep(5)
      print("You didn't even dare look. Something slashes at your back and crunches on your bones. YOU DIED! THE END!")
      die(player1)
    elif b =="2":
      print("You decide to follow the monster without them noticing.")
      sleep(4)
      print("Eventually, it leads you to some sort of broader cave system, and a massive cave village stands before you.")
      #dialogueN
      print("Nico tugs at you and points to the center of the village: a ladder that leads up to an icy section of the caves. That must lead to the Summit.")
      print("But where do you enter the village?")
      c=input("1.Main entrance. 2.East entrance. 3.West entrance. 4.Sneak in through the piping system.")#u
    else:
      print("You decide to leave the monster alone and find the way yourself, only to hear something growl behind you.")
      print("Something pounces on the two of you and the creature crunches straight onto your necks. YOU DIED! THE END!")
      die(player1)
  elif a =="2":
    #dialogueN
    print("You usher Nico towards some sort of indent in the cave wall to hide, in case someone is approaching. However, your collective weight causes the weak rock underneath you to crumble, leaving you two to plummet to your death. YOU DIED! THE END!")
    die(player1)
  elif a =="3":
    print("You continue walking, ignoring the sound. Suddenly, you hear a growl behind you, and you turn to find a massive hideous creature standing before you. It pounces directly onto the two of you, and the both of you are brutally eaten. YOU DIED! THE END!")
    die(player1)
  else:
    print("You decide to stand still and listen more intently.")
    sleep(5)
    print("You hear something heavy heading your way. It doesn't sound friendly.")
    b=input("1.Stand. Still. 2.Make a run for it! 3.Find somewhere to hide. 4.Slowly sneak back the way you came.")
    if b =="1":
      print("The both of you stand completely still. You can hear the creature moving just around the corner.")
      sleep(7)
      print("After an excruicating amount of time, the creature walks away with heavy steps. You let out a sigh of relief.")
      print("The two of you continue to journey through the caves, looking for a way out. Evenutally, you find a massive cave village, filled with Monsters.")
      print("'Oh my god. There's so many of them-'")
      sleep(3)
      print("You stop yourself. In the center of the village you see something.")
      print("A ladder that leads up into an icy section of the caves. That must be where the Summit is!")
      print("But how will you make it there?")
      c=input("1.Walk past the farms. 2.Walk through the market. 3.Walk past the hospital. 4.Walk through the armory.")#u
    elif b =="2":
      print("You decide to make a run for it, but the creature notices you and pounces, striking you right in the stomach. Your blood is everywhere. You close your eyes. YOU DIED! THE END!")
      die(player1)
    elif b =="3":
      print("The two of you quickly find a place to hide, just as a creature walks over.")
      sleep(5)
      if player1.t3 == True:
        print("The creature walks right by, and you hear it leaving the area.")
        print("The both of you slowly emerge from your hiding spot, and continue to journey through the caves, looking for a way out. Evenutally, you find a massive cave village, filled with Monsters.")
        print("'Oh my god. There's so many of them-'")
        sleep(3)
        print("You stop yourself. In the center of the village you see something.")
        print("A ladder that leads up into an icy section of the caves. That must be where the Summit is!")
        print("But how will you make it there?")
        c=input("1.Walk past the farms. 2.Walk through the market. 3.Walk past the hospital. 4.Walk through the armory.")#u
      else:
        print("You failed to hide silently and the creature turns towards you. You have nowhere to run, and it opens its mouth. YOU DIED! THE END!")
        die(player1)
    else:
      #dialogueN
      print("You slowly sneak back the way you came, but you accidentally trip over a stalagmite and fall onto the ground.")
      print("Nico tries to help you up, but it's too late. The creature appears in front of you and immediately slashes, taking out Nico. It jumps at you and you can see the inside of its mouth.")
      print("YOU DIED! THE END!")
      die(player1)

def forestVillage(player1):
  pass

def abandonedVillage(player1):
  pass