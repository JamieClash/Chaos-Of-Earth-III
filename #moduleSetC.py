#ALL SKILL TIER 1 
import time
from time import sleep
from player import *

'''
player1.newSkill()
nextChapter(player1)#############
'''

def die(player1):
  pass

def volcanoBadlands(player1):#Used in Dream team, Ranger, and Nico. Written for DREAMTEAM.
  #IMPORTANT: NICO GOES TO BARREN MOUNTAINS, NOT CAVES AFTER THIS
  print("'Woah, this place is hot...' Jess wipes her forehead. 'You sure this is the way to go?'")
  print("You take a deep breath and continue navigating through the cracked rocky ground.")
  sleep(3)
  print("'The landscape isn't the best, but that means there probably won't be any monsters out and about here...'")
  print("The two of you suddenly come to a stop. 'Is the ground rumbling?' You ask, only to have your question answered moments later when a volcano nearby erupts, and lava begins spilling around it.")
  sleep(5)
  print("You take a moment to look for a safe place to go, and you've found several options.")
  a=input("1.Go into a cave. 2.Keep walking. 3.Start running. 4.Climb onto a small rocky hill.")
  if a =="1":
    print("You decide to take cover by running into a nearby cave, but just when you got decently deep into it, your surroundings start vibrating.")
    print("'That can't be good.'")
    sleep(4)
    print("The cave walls around you start spuring out lava and your skin is burned away whilst you scream at the top of your lungs.")
    print("YOU DIED! THE END!")
    die(player1)
  elif a =="2":
    print("You decide to calmly continue walking. The lava is quite viscuous and you can easily outwalk it.")
    print("You continue to navigate through the badlands. The heat is starting to get hard to bear.")
    b=input("1.Take a rest right now. 2.Head up a rocky hill. 3.Keep walking on flat ground. 4.Head to a nearby cave to rest.")
    if b =="1":
      print("You decide to take a break where you are. The lava is catching up, forcing you to stand up and walk again. However, the ground beneath you starts shaking and it knocks you down onto the ground, just as the lava arrives.")
      print("Your legs were burnt off first.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="2":
      print("You decide to head up a rocky hill.")
      print("The hill suddenly trembles underneath you and you realize that it's an active volcano.")
      print("Lava bursts out of the top of the volcano and you were unable to avoid it as it falls onto you. Your vision turns red as it burns through you.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="3":
      if player.s3:
        print("You are able to endure the hot temperatures and keep on moving.")
        sleep(4)
        print("Eventually, you are far away from the volcano that erupted and you take a break on the ground to recover.")
        sleep(5)
        st=time.time()
        c=input("PRESS [J] to jump away!").title()
        rt=time.time()-st
        if c =="J" and rt<3:
          print("You managed to jump out of the way of some falling lava just in time.")
          print("You look behind you and see chains of eruptions from volcanoes all around you.")
          print("'How will we get out of this?' Jess asks.")
          d=input("1.Run East. 2.Run South. 3.Run West. 4.Run North.")
          if d =="1":
            print("You try to run towards the east, but the earth shakes underneath you, knocking you off balance and causing you to fall.")
            print("The lava caught up with you and you slowly burnt away.")
            print("YOU DIED! THE END!")
            die(player1)
          elif d =="2":
            print("You decide to run towards the south.")
            sleep(3)
            print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
            sleep(3)
            print("'There!' Jess points out some towers off in the distance.")
            e=input("1.Go for the tallest tower. 2.Go for the shortest tower. 3.Go for the nearest tower. 4.Go for the farthest tower.")
            if e =="1":
              print("You decide to head towards the tallest tower.")
              sleep(3)
              print("The steel door creaked as you open it, but it didn't seem to have any problems. You slammed the door behind you two and ran up the stairs towards the top.")
              print("'Whew.' Jess pants from both the heat and the physical exertion.")
              print("You take heavy breaths as you look around the landscape around you. You are able to clearly identify the other end of the badlands, and which direction it is.")
              sleep(6)
              print("You and Jess take a decent break in the tower. The lava couldn't reach you, and completely dried by the time you are ready to move again.")
              print("You and Jess arrive at the steel door at the bottom of the tower, prepared to leave. It doesn't seem to budge.")
              f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
              if f =="1":
                print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
                print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
                print("You never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
                print("You passed out and never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You try shooting at the joints, but the joints themselves seem to be very strong.")
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
              else:
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
            elif e =="2":
              print("You decide to head to the shortest tower.")
              print("You were able to knock down the wooden door to enter the tower, but it was way shorter than you thought. The barrage of lava all over the place eventually causes you to have nowhere left to run, even inside the tower.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You run towards the nearest tower, only for it to take the brunt of the eruptions all around you, causing it to collapse.")
              print("You've got nowhere left to run.")
              print("You accept your fate.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You use up the last of your strength to run to the farthest tower, slamming the steel door behind you just in time to collapse onto the floor.")
              sleep(5)
              print("After a long break, you climb up the tower and manage to find the exit to the badlands. You head down to open the door... except it seems to be stuck.")
              f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
              if f =="1":
                print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
                print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
                print("You never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
                print("You passed out and never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You try shooting at the joints, but the joints themselves seem to be very strong.")
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
              else:
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
          elif d =="3":
            print("You decide to run towards the west.")
            sleep(3)
            print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
            sleep(3)
            print("'There!' Jess points out some sort of village off in the distance.")
            e=input("1.Go for the village. 2.Ignore it and keep running west. 3.Ignore it and run north. 4.Ignore it and run south.")
            if e =="1":
              print("You head towards the village and realize it's abandoned.")
              print("Thankfully, the eruptions have ceased and you are able to take a break at the village without anything crazy happening.")
              sleep(5)
              print("You manage to find some sort of map in an old chest, complete with markers. However, its edges are burnt off, so you can't see which marker's direction leads to the exit of the badlands.")
              f=input("1.Head towards the 'tower' marker. 2.Head towards the 'ruins' marker. 3.Head towards the 'house' marker. 4.Head towards the 'tree' marker.")
              if f =="1":
                print("You decide to head towards the marker with the tower.")
                sleep(3)
                print("You spot a tall tower up ahead along with some other towers.")
                print("You climb up the tower and get a good look around, successfully finding the exit to the badlands.")
                print("You smile to yourself and head towards the way out.")
                player1.newSkill()
                nextChapter(player1)##############
              elif f =="2":
                print("You decide to head towards the ruins marker.")
                print("As expected, you found some sort of ruins. You decide to check it out.")
                sleep(3)
                print("You were too exhausted to see the pressure plate at the entrance.")
                sleep(3)
                print("Pieces of your body flew everywhere from the explosion.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to head towards the marker with the house.")
                sleep(4)
                print("'That's strange...' You say. 'There's nothing here...'")
                print("Suddenly, an earthquake causes you to lose balance just as a volcano erupts next to you.")
                print("YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to check out the tree marker.")
                sleep(4)
                print("'That's strange...' You say. 'There's nothing here...'")
                print("Suddenly, an earthquake causes you to lose balance just as a volcano erupts next to you.")
                print("YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You ignore the village and continue running west.")
              sleep(3)
              print("The eruptions keep on happening on this side of the badlands, and you eventually run out of stamina and collapse onto the ground, passing out.")
              print("You never woke up again.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You decide to ignore it and head north instead.")
              sleep(3)
              print("You find some sort of ruins up ahead, but due to your exhausted state you didn't notice the pressure plate at the entrance.")
              sleep(3)
              print("Pieces of your body flew everywhere from the explosion.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to change your mind and head south. You see a few towers up ahead, in which you may take refuge from the eruptions.")
              f=input("1.Head to the tallest tower. 2.Head to the shortest tower. 3.Head to the closest tower. 4.Head to the farthest tower.")
              if f =="1":
                print("You decide to head to the tallest tower.")
                print("You made it there just as the eruptions stopped, so you left the door open as you went to the top floor to look for the way out of the badlands.")
                sleep(4)
                print("'Ah, there it is.' Jess points it out to you.")
                print("You take a deep breath and head down again.")
                sleep(4)
                print("You can see the end of the badlands not far ahead. You yawn.")
                player1.newSkill()
                nextChapter(player1)##############
              elif f =="2":
                print("You head towards the shortest tower.")
                print("Thankfully, the eruptions have stopped just in time for you to reach the tower. It's not very tall, but you were barely able to make out the way out of the badlands.")
                print("You smile as you stare at the border of the badlands up ahead.")
                player1.newSkill()
                nextChapter(player1)##############
              elif f =="3":
                print("You decide to head to the closest tower.")
                sleep(3)
                print("Unfortunately, the eruptions were still going on nearby as you attempted to enter the tower, and some stray lava got onto you.")
                print("YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to head to the farthest tower.")
                sleep(5)
                print("Thankfully, the eruptions have stopped just in time for you to reach the tower without collapsing. After a good rest, you went up to the top and could barely see the way out of the badlands.")
                print("You smile as you stare at the border of the badlands up ahead.")
                player1.newSkill()
                nextChapter(player1)##############
          else:
            print("You decide to run towards the north.")
            sleep(3)
            print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
            sleep(3)
            print("'There!' Jess points out some ruins off in the distance.")
            e=input("1.Head to the ruins. 2.Ignore it and head east. 3.Ignore it and head south. 4.Ignore it and head west.")
            if e =="1":
              print("You decide to head towrads the ruins.")
              sleep(4)
              print("Unfortunately, you did not realize that it was trapped.")
              print("You stepped on the pressure plate and was blown into smithereens.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="2":
              print("You decide to ignore the ruins and head east.")
              print("The eruptions are more powerful in this direction, and eventually your luck ran out.")
              print("Some stray lava flew onto your stomach and it burnt straight into your intestines.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You decide to turn back and head south, towards the direction where the eruptions first came from.")
              sleep(5)
              print("Luckily, it was also the direction where the eruptions stopped first.")
              print("You were able to slowly head south after the eruptions subsided, and you came across several towers.")
              print("You climbed onto the tallest one and found the direction you need to go to leave the badlands.")
              sleep(5)
              print("'Umm...' Jess says as she tries to open the steel door to exit the tower.")
              print("'It seems to be stuck.' She confirms.")
              f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
              if f =="1":
                print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
                print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
                print("You never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
                print("You passed out and never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You try shooting at the joints, but the joints themselves seem to be very strong.")
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
              else:
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
            else:
              print("You decide to ignore the ruins and head west.")
              print("There is not a single safe structure in sight, and eventually your luck ran out.")
              print("Some stray lava flew onto your throat and it burnt all the way into your stomach.")
              print("YOU DIED! THE END!")
              die(player1)
        else:
          print("You failed to jump out of the way of falling lava and your back got burnt all the way through to your front.")
          print("YOU DIED! THE END!")
          die(player1)
      else:
        print("You decide to continue walking, but the heat eventually gets incredibly hard to bear. You feel as if you are about to pass out.")
        c=input("1.Keep walking. 2.Take a break.")
        if c =="1":
          print("You try your best to keep on walking, but eventually you can't take the heat any more and you pass out.")
          print("You never woke up.")
          print("YOU DIED! THE END!")
          die(player1)
        else:
          print("You decide to take a break to recover your strength.")
          sleep(4)
          print("Suddenly, you hear an eruption behind you and jump away just in time to avoid some falling lava.")
          print("You look behind you and see chains of eruptions from volcanoes all around you.")
          print("'How will we get out of this?' Jess asks.")
          d=input("1.Run East. 2.Run South. 3.Run West. 4.Run North.")
          if d =="1":
            print("You try to run towards the east, but the earth shakes underneath you, knocking you off balance and causing you to fall.")
            print("The lava caught up with you and you slowly burnt away.")
            print("YOU DIED! THE END!")
            die(player1)
          elif d =="2":
            print("You decide to run towards the south.")
            sleep(3)
            print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
            sleep(3)
            print("'There!' Jess points out some towers off in the distance.")
            e=input("1.Go for the tallest tower. 2.Go for the shortest tower. 3.Go for the nearest tower. 4.Go for the farthest tower.")
            if e =="1":
              print("You decide to head towards the tallest tower.")
              sleep(3)
              print("The steel door creaked as you open it, but it didn't seem to have any problems. You slammed the door behind you two and ran up the stairs towards the top.")
              print("'Whew.' Jess pants from both the heat and the physical exertion.")
              print("You take heavy breaths as you look around the landscape around you. You are able to clearly identify the other end of the badlands, and which direction it is.")
              sleep(6)
              print("You and Jess take a decent break in the tower. The lava couldn't reach you, and completely dried by the time you are ready to move again.")
              print("You and Jess arrive at the steel door at the bottom of the tower, prepared to leave. It doesn't seem to budge.")
              f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
              if f =="1":
                print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
                print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
                print("You never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
                print("You passed out and never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You try shooting at the joints, but the joints themselves seem to be very strong.")
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
              else:
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
            elif e =="2":
              print("You decide to head to the shortest tower.")
              print("You were able to knock down the wooden door to enter the tower, but it was way shorter than you thought. The barrage of lava all over the place eventually causes you to have nowhere left to run, even inside the tower.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You run towards the nearest tower, only for it to take the brunt of the eruptions all around you, causing it to collapse.")
              print("You've got nowhere left to run.")
              print("You accept your fate.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You use up the last of your strength to run to the farthest tower, slamming the steel door behind you just in time to collapse onto the floor.")
              sleep(5)
              print("After a long break, you climb up the tower and manage to find the exit to the badlands. You head down to open the door... except it seems to be stuck.")
              f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
              if f =="1":
                print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
                print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
                print("You never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
                print("You passed out and never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You try shooting at the joints, but the joints themselves seem to be very strong.")
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
              else:
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
          elif d =="3":
            print("You decide to run towards the west.")
            sleep(3)
            print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
            sleep(3)
            print("'There!' Jess points out some sort of village off in the distance.")
            e=input("1.Go for the village. 2.Ignore it and keep running west. 3.Ignore it and run north. 4.Ignore it and run south.")
            if e =="1":
              print("You head towards the village and realize it's abandoned.")
              print("Thankfully, the eruptions have ceased and you are able to take a break at the village without anything crazy happening.")
              sleep(5)
              print("You manage to find some sort of map in an old chest, complete with markers. However, its edges are burnt off, so you can't see which marker's direction leads to the exit of the badlands.")
              f=input("1.Head towards the 'tower' marker. 2.Head towards the 'ruins' marker. 3.Head towards the 'house' marker. 4.Head towards the 'tree' marker.")
              if f =="1":
                print("You decide to head towards the marker with the tower.")
                sleep(3)
                print("You spot a tall tower up ahead along with some other towers.")
                print("You climb up the tower and get a good look around, successfully finding the exit to the badlands.")
                print("You smile to yourself and head towards the way out.")
                player1.newSkill()
                nextChapter(player1)##############
              elif f =="2":
                print("You decide to head towards the ruins marker.")
                print("As expected, you found some sort of ruins. You decide to check it out.")
                sleep(3)
                print("You were too exhausted to see the pressure plate at the entrance.")
                sleep(3)
                print("Pieces of your body flew everywhere from the explosion.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You decide to head towards the marker with the house.")
                sleep(4)
                print("'That's strange...' You say. 'There's nothing here...'")
                print("Suddenly, an earthquake causes you to lose balance just as a volcano erupts next to you.")
                print("YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to check out the tree marker.")
                sleep(4)
                print("'That's strange...' You say. 'There's nothing here...'")
                print("Suddenly, an earthquake causes you to lose balance just as a volcano erupts next to you.")
                print("YOU DIED! THE END!")
                die(player1)
            elif e =="2":
              print("You ignore the village and continue running west.")
              sleep(3)
              print("The eruptions keep on happening on this side of the badlands, and you eventually run out of stamina and collapse onto the ground, passing out.")
              print("You never woke up again.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You decide to ignore it and head north instead.")
              sleep(3)
              print("You find some sort of ruins up ahead, but due to your exhausted state you didn't notice the pressure plate at the entrance.")
              sleep(3)
              print("Pieces of your body flew everywhere from the explosion.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to change your mind and head south. You see a few towers up ahead, in which you may take refuge from the eruptions.")
              f=input("1.Head to the tallest tower. 2.Head to the shortest tower. 3.Head to the closest tower. 4.Head to the farthest tower.")
              if f =="1":
                print("You decide to head to the tallest tower.")
                print("You made it there just as the eruptions stopped, so you left the door open as you went to the top floor to look for the way out of the badlands.")
                sleep(4)
                print("'Ah, there it is.' Jess points it out to you.")
                print("You take a deep breath and head down again.")
                sleep(4)
                print("You can see the end of the badlands not far ahead. You yawn.")
                player1.newSkill()
                nextChapter(player1)##############
              elif f =="2":
                print("You head towards the shortest tower.")
                print("Thankfully, the eruptions have stopped just in time for you to reach the tower. It's not very tall, but you were barely able to make out the way out of the badlands.")
                print("You smile as you stare at the border of the badlands up ahead.")
                player1.newSkill()
                nextChapter(player1)##############
              elif f =="3":
                print("You decide to head to the closest tower.")
                sleep(3)
                print("Unfortunately, the eruptions were still going on nearby as you attempted to enter the tower, and some stray lava got onto you.")
                print("YOU DIED! THE END!")
                die(player1)
              else:
                print("You decide to head to the farthest tower.")
                sleep(5)
                print("Thankfully, the eruptions have stopped just in time for you to reach the tower without collapsing. After a good rest, you went up to the top and could barely see the way out of the badlands.")
                print("You smile as you stare at the border of the badlands up ahead.")
                player1.newSkill()
                nextChapter(player1)##############
          else:
            print("You decide to run towards the north.")
            sleep(3)
            print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
            sleep(3)
            print("'There!' Jess points out some ruins off in the distance.")
            e=input("1.Head to the ruins. 2.Ignore it and head east. 3.Ignore it and head south. 4.Ignore it and head west.")
            if e =="1":
              print("You decide to head towrads the ruins.")
              sleep(4)
              print("Unfortunately, you did not realize that it was trapped.")
              print("You stepped on the pressure plate and was blown into smithereens.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="2":
              print("You decide to ignore the ruins and head east.")
              print("The eruptions are more powerful in this direction, and eventually your luck ran out.")
              print("Some stray lava flew onto your stomach and it burnt straight into your intestines.")
              print("YOU DIED! THE END!")
              die(player1)
            elif e =="3":
              print("You decide to turn back and head south, towards the direction where the eruptions first came from.")
              sleep(5)
              print("Luckily, it was also the direction where the eruptions stopped first.")
              print("You were able to slowly head south after the eruptions subsided, and you came across several towers.")
              print("You climbed onto the tallest one and found the direction you need to go to leave the badlands.")
              sleep(5)
              print("'Umm...' Jess says as she tries to open the steel door to exit the tower.")
              print("'It seems to be stuck.' She confirms.")
              f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
              if f =="1":
                print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
                print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
                print("You never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="2":
                print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
                print("You passed out and never woke up again.")
                print("YOU DIED! THE END!")
                die(player1)
              elif f =="3":
                print("You try shooting at the joints, but the joints themselves seem to be very strong.")
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
              else:
                print("You decide to jump out of the fourth floor window.")
                sleep(5)
                print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
                sleep(3)
                print("You smile when you see the end of the badlands just ahead of you.")
                player1.newSkill()
                nextChapter(player1)##############
            else:
              print("You decide to ignore the ruins and head west.")
              print("There is not a single safe structure in sight, and eventually your luck ran out.")
              print("Some stray lava flew onto your throat and it burnt all the way into your stomach.")
              print("YOU DIED! THE END!")
              die(player1)
    else:
      print("You decide to head to a nearby cave to rest.")
      print("Once you're adequately deep into the cave, the walls around you start shaking and lava burst out from all around you, covering your body completely.")
      print("You tried to scream, but the lava fell into your mouth and burnt your tongue and throat.")
      print("YOU DIED! THE END!")
      die(player1)
  elif a =="3":
    print("You decide to start running, and although you clear a lot of distance from the lava, your body temperature is quite high. You need to take a break and cool down.")
    b=input("1.Take a rest right now. 2.Head up a rocky hill. 3.Keep walking on flat ground. 4.Head to a nearby cave to rest.")
    if b =="1":
      print("You drop onto the ground and take a good break.")
      sleep(5)
      st=time.time()
      c=input("PRESS [J] to jump away!").title()
      rt=time.time()-st
      if c =="J" and rt<3:
        print("You managed to jump out of the way of some falling lava just in time.")
        print("You look behind you and see chains of eruptions from volcanoes all around you.")
        print("'How will we get out of this?' Jess asks.")
        d=input("1.Run East. 2.Run South. 3.Run West. 4.Run North.")
        if d =="1":
            print("You try to run towards the east, but the earth shakes underneath you, knocking you off balance and causing you to fall.")
            print("The lava caught up with you and you slowly burnt away.")
            print("YOU DIED! THE END!")
            die(player1)
        elif d =="2":
          print("You decide to run towards the south.")
          sleep(3)
          print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
          sleep(3)
          print("'There!' Jess points out some towers off in the distance.")
          e=input("1.Go for the tallest tower. 2.Go for the shortest tower. 3.Go for the nearest tower. 4.Go for the farthest tower.")
          if e =="1":
            print("You decide to head towards the tallest tower.")
            sleep(3)
            print("The steel door creaked as you open it, but it didn't seem to have any problems. You slammed the door behind you two and ran up the stairs towards the top.")
            print("'Whew.' Jess pants from both the heat and the physical exertion.")
            print("You take heavy breaths as you look around the landscape around you. You are able to clearly identify the other end of the badlands, and which direction it is.")
            sleep(6)
            print("You and Jess take a decent break in the tower. The lava couldn't reach you, and completely dried by the time you are ready to move again.")
            print("You and Jess arrive at the steel door at the bottom of the tower, prepared to leave. It doesn't seem to budge.")
            f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
            if f =="1":
              print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
              print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
              print("You never woke up again.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
              print("You passed out and never woke up again.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You try shooting at the joints, but the joints themselves seem to be very strong.")
              print("You decide to jump out of the fourth floor window.")
              sleep(5)
              print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
              sleep(3)
              print("You smile when you see the end of the badlands just ahead of you.")
              player1.newSkill()
              nextChapter(player1)##############
            else:
              print("You decide to jump out of the fourth floor window.")
              sleep(5)
              print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
              sleep(3)
              print("You smile when you see the end of the badlands just ahead of you.")
              player1.newSkill()
              nextChapter(player1)##############
          elif e =="2":
            print("You decide to head to the shortest tower.")
            print("You were able to knock down the wooden door to enter the tower, but it was way shorter than you thought. The barrage of lava all over the place eventually causes you to have nowhere left to run, even inside the tower.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You run towards the nearest tower, only for it to take the brunt of the eruptions all around you, causing it to collapse.")
            print("You've got nowhere left to run.")
            print("You accept your fate.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You use up the last of your strength to run to the farthest tower, slamming the steel door behind you just in time to collapse onto the floor.")
            sleep(5)
            print("After a long break, you climb up the tower and manage to find the exit to the badlands. You head down to open the door... except it seems to be stuck.")
            f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
            if f =="1":
              print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
              print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
              print("You never woke up again.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
              print("You passed out and never woke up again.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You try shooting at the joints, but the joints themselves seem to be very strong.")
              print("You decide to jump out of the fourth floor window.")
              sleep(5)
              print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
              sleep(3)
              print("You smile when you see the end of the badlands just ahead of you.")
              player1.newSkill()
              nextChapter(player1)##############
            else:
              print("You decide to jump out of the fourth floor window.")
              sleep(5)
              print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
              sleep(3)
              print("You smile when you see the end of the badlands just ahead of you.")
              player1.newSkill()
              nextChapter(player1)##############
        elif d =="3":
          print("You decide to run towards the west.")
          sleep(3)
          print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
          sleep(3)
          print("'There!' Jess points out some sort of village off in the distance.")
          e=input("1.Go for the village. 2.Ignore it and keep running west. 3.Ignore it and run north. 4.Ignore it and run south.")
          if e =="1":
            print("You head towards the village and realize it's abandoned.")
            print("Thankfully, the eruptions have ceased and you are able to take a break at the village without anything crazy happening.")
            sleep(5)
            print("You manage to find some sort of map in an old chest, complete with markers. However, its edges are burnt off, so you can't see which marker's direction leads to the exit of the badlands.")
            f=input("1.Head towards the 'tower' marker. 2.Head towards the 'ruins' marker. 3.Head towards the 'house' marker. 4.Head towards the 'tree' marker.")
            if f =="1":
              print("You decide to head towards the marker with the tower.")
              sleep(3)
              print("You spot a tall tower up ahead along with some other towers.")
              print("You climb up the tower and get a good look around, successfully finding the exit to the badlands.")
              print("You smile to yourself and head towards the way out.")
              player1.newSkill()
              nextChapter(player1)##############
            elif f =="2":
              print("You decide to head towards the ruins marker.")
              print("As expected, you found some sort of ruins. You decide to check it out.")
              sleep(3)
              print("You were too exhausted to see the pressure plate at the entrance.")
              sleep(3)
              print("Pieces of your body flew everywhere from the explosion.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You decide to head towards the marker with the house.")
              sleep(4)
              print("'That's strange...' You say. 'There's nothing here...'")
              print("Suddenly, an earthquake causes you to lose balance just as a volcano erupts next to you.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to check out the tree marker.")
              sleep(4)
              print("'That's strange...' You say. 'There's nothing here...'")
              print("Suddenly, an earthquake causes you to lose balance just as a volcano erupts next to you.")
              print("YOU DIED! THE END!")
              die(player1)
          elif e =="2":
            print("You ignore the village and continue running west.")
            sleep(3)
            print("The eruptions keep on happening on this side of the badlands, and you eventually run out of stamina and collapse onto the ground, passing out.")
            print("You never woke up again.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You decide to ignore it and head north instead.")
            sleep(3)
            print("You find some sort of ruins up ahead, but due to your exhausted state you didn't notice the pressure plate at the entrance.")
            sleep(3)
            print("Pieces of your body flew everywhere from the explosion.")
            print("YOU DIED! THE END!")
            die(player1)
          else:
            print("You decide to change your mind and head south. You see a few towers up ahead, in which you may take refuge from the eruptions.")
            f=input("1.Head to the tallest tower. 2.Head to the shortest tower. 3.Head to the closest tower. 4.Head to the farthest tower.")
            if f =="1":
              print("You decide to head to the tallest tower.")
              print("You made it there just as the eruptions stopped, so you left the door open as you went to the top floor to look for the way out of the badlands.")
              sleep(4)
              print("'Ah, there it is.' Jess points it out to you.")
              print("You take a deep breath and head down again.")
              sleep(4)
              print("You can see the end of the badlands not far ahead. You yawn.")
              player1.newSkill()
              nextChapter(player1)##############
            elif f =="2":
              print("You head towards the shortest tower.")
              print("Thankfully, the eruptions have stopped just in time for you to reach the tower. It's not very tall, but you were barely able to make out the way out of the badlands.")
              print("You smile as you stare at the border of the badlands up ahead.")
              player1.newSkill()
              nextChapter(player1)##############
            elif f =="3":
              print("You decide to head to the closest tower.")
              sleep(3)
              print("Unfortunately, the eruptions were still going on nearby as you attempted to enter the tower, and some stray lava got onto you.")
              print("YOU DIED! THE END!")
              die(player1)
            else:
              print("You decide to head to the farthest tower.")
              sleep(5)
              print("Thankfully, the eruptions have stopped just in time for you to reach the tower without collapsing. After a good rest, you went up to the top and could barely see the way out of the badlands.")
              print("You smile as you stare at the border of the badlands up ahead.")
              player1.newSkill()
              nextChapter(player1)##############
        else:
          print("You decide to run towards the north.")
          sleep(3)
          print("You managed to avoid the eruptions, but you still don't see an obvious way out of the badlands...")
          sleep(3)
          print("'There!' Jess points out some ruins off in the distance.")
          e=input("1.Head to the ruins. 2.Ignore it and head east. 3.Ignore it and head south. 4.Ignore it and head west.")
          if e =="1":
            print("You decide to head towrads the ruins.")
            sleep(4)
            print("Unfortunately, you did not realize that it was trapped.")
            print("You stepped on the pressure plate and was blown into smithereens.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="2":
            print("You decide to ignore the ruins and head east.")
            print("The eruptions are more powerful in this direction, and eventually your luck ran out.")
            print("Some stray lava flew onto your stomach and it burnt straight into your intestines.")
            print("YOU DIED! THE END!")
            die(player1)
          elif e =="3":
            print("You decide to turn back and head south, towards the direction where the eruptions first came from.")
            sleep(5)
            print("Luckily, it was also the direction where the eruptions stopped first.")
            print("You were able to slowly head south after the eruptions subsided, and you came across several towers.")
            print("You climbed onto the tallest one and found the direction you need to go to leave the badlands.")
            sleep(5)
            print("'Umm...' Jess says as she tries to open the steel door to exit the tower.")
            print("'It seems to be stuck.' She confirms.")
            f=input("1.Kick it down. 2.Ram against it. 3.Shoot at the joints where the door is connected to the wall. 4.Jump off the fourth floor, where the nearest window is.")
            if f =="1":
              print("You try to kick down the door, only for you to hurt your leg. You change your mind and decide to jump off the fourth floor.")
              print("Unfortunately, you weren't able to strike a good landing and landed on your head.")
              print("You never woke up again.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="2":
              print("You ram against the door, only for you to break your arm. You decide to jump out the fourth floor window as a last resort, but unfortunately you weren't able to disperse the momentum of your fall properly and you broke your leg too.")
              print("You passed out and never woke up again.")
              print("YOU DIED! THE END!")
              die(player1)
            elif f =="3":
              print("You try shooting at the joints, but the joints themselves seem to be very strong.")
              print("You decide to jump out of the fourth floor window.")
              sleep(5)
              print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
              sleep(3)
              print("You smile when you see the end of the badlands just ahead of you.")
              player1.newSkill()
              nextChapter(player1)##############
            else:
              print("You decide to jump out of the fourth floor window.")
              sleep(5)
              print("You barely managed to get a good roll on your landing, dispersing most of the momentum. You feel a bit of pain in your ankles, but it will pass.")
              sleep(3)
              print("You smile when you see the end of the badlands just ahead of you.")
              player1.newSkill()
              nextChapter(player1)##############
          else:
            print("You decide to ignore the ruins and head west.")
            print("There is not a single safe structure in sight, and eventually your luck ran out.")
            print("Some stray lava flew onto your throat and it burnt all the way into your stomach.")
            print("YOU DIED! THE END!")
            die(player1)
      else:
        print("You failed to jump out of the way of falling lava and your back got burnt all the way through to your front.")
        print("YOU DIED! THE END!")
        die(player1)
    elif b =="2":
      print("You decide to head up a rocky hill.")
      print("The hill suddenly trembles underneath you and you realize that it's an active volcano.")
      print("Lava bursts out of the top of the volcano and you were unable to avoid it as it falls onto you. Your vision turns red as it burns through you.")
      print("YOU DIED! THE END!")
      die(player1)
    elif b =="3":
      print("You try to keep on walking, but you eventually fail to endure the heat and you pass out.")
      print("You never woke up again.")
      print("YOU DIED! THE END!")
      die(player1)
    else:
      print("You decide to head to a nearby cave to rest.")
      print("Once you're adequately deep into the cave, the walls around you start shaking and lava burst out from all around you, covering your body completely.")
      print("You tried to scream, but the lava fell into your mouth and burnt your tongue and throat.")
      print("YOU DIED! THE END!")
      die(player1)
  else:
    print("You decide to climb a nearby rocky hill to escape the lava, but the hill you're climbing suddenly starts rumbling, and you realize too late that it is an active volcano.")
    print("Lava bursts out of the top of the volcano and you were unable to avoid it as it falls onto you. Your vision turns red as it burns through you.")
    print("YOU DIED! THE END!")
    die(player1)

#skill tier 1 mountains
def mountains(player1):
  pass

def tundra(player1):
  pass

def plains(player1):
  pass

def flowerForest(player1):#leads into cave village/mountains (rare occasion)
  pass

def ravine(player1):
  pass

def brokenDesert(player1):
  pass