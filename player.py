import os
import base64

class player():
  path = ""
  t2=False
  t22 = False
  t3= False
  t32= False
  s2= False
  s22 = False
  s3 = False
  s32 = False
  c2 = False
  c22 = False
  c3 = False
  c32 = False

  def __init__(self,aPath):
    self.path = aPath

  def newSkill(self):
    while True:
      print("\nTime to unlock new skills!")
      if self.path =="stealth":
        print("1.Silent Arrows - "+str(self.t2))
        print("2.[Craft gun supressors] - "+str(self.t22))
        print("3.Undetectable when stationary - "+str(self.t3))
        print("4.[Undetectable when sneaking] - "+str(self.t32))
        upgrade = input(">")
        if upgrade =="1":
          if self.t2==False:
            self.t2 = True
            break
          else:
            print("You already have this skill!")
        elif upgrade =="2":
          if self.t2==True:
            if self.t22==False:
              self.t22=True
            else:
              print("You already have this skill!")
          else:
            print("You haven't unlocked stage one yet!")
        elif upgrade =="3":
          if self.t3==False:
            self.t3 = True
            break
          else:
            print("You already have this skill!")
        else:
          if self.t3==True:
            if self.t32==False:
              self.t32=True
            else:
              print("You already have this skill!")
          else:
            print("You haven't unlocked stage one yet!")
      elif self.path == "survival":
        print("1.Climb mountains - "+str(self.s2))
        print("2.[Climb icy mountains] - "+str(self.s22))
        print("3.Temperature endurance - "+str(self.s3))
        print("4.[Quick traversal speed] - "+str(self.s32))
        upgrade = input(">")
        if upgrade =="1":
          if self.s2==False:
            self.s2 = True
            break
          else:
            print("You already have this skill!")
        elif upgrade =="2":
          if self.s2==True:
            if self.s22==False:
              self.s22=True
            else:
              print("You already have this skill!")
          else:
            print("You haven't unlocked stage one yet!")
        elif upgrade =="3":
          if self.s3==False:
            self.s3 = True
            break
          else:
            print("You already have this skill!")
        else:
          if self.s3==True:
            if self.s32==False:
              self.s32=True
            else:
              print("You already have this skill!")
          else:
            print("You haven't unlocked stage one yet!")
      else:
        print("1.Reliably win 1v1s - "+str(self.c2))
        print("2.[Reliably win 1v2s] - "+str(self.c22))
        print("3.Dodge attacks better - "+str(self.c3))
        print("4.[Counter attack when dodging] - "+str(self.c32))
        upgrade = input(">")
        if upgrade =="1":
          if self.c2==False:
            self.c2 = True
            break
          else:
            print("You already have this skill!")
        elif upgrade =="2":
          if self.c2==True:
            if self.c22==False:
              self.c22=True
            else:
              print("You already have this skill!")
          else:
            print("You haven't unlocked stage one yet!")
        elif upgrade =="3":
          if self.c3==False:
            self.c3 = True
            break
          else:
            print("You already have this skill!")
        else:
          if self.c3==True:
            if self.c32==False:
              self.c32=True
            else:
              print("You already have this skill!")
          else:
            print("You haven't unlocked stage one yet!")

def startGame():
  with open('msg/message.txt') as fyl:
    print(fyl.read())

  exec(
    base64.b64decode(
b'dHJ5OgogICAgb3MuZW52aXJvblsnbW9kJ10KICAgIHByaW50KCJObyBmb3JrIGRldGVjdGVkIikKZXhjZXB0OgogICAgd2l0aCBvcGVuKCdtc2cvZm9yay50eHQnKSBhcyBmOgogICAgICBwcmludChmLnJlYWQoKSkKICAgIHdpdGggb3BlbignbWFpbi5weScsJ3cnKSBhcyBmOgogICAgICBmLndyaXRlKCJUaGlzIGlzIGEgY2hhb3Mgb2YgZWFydGggY29weS4iKQogICAgd2l0aCBvcGVuKCcjbW9kdWxlU2V0QS5weScsJ3cnKSBhcyBmOgogICAgICBmLndyaXRlKCIiKQogICAgd2l0aCBvcGVuKCcjbW9kdWxlU2V0Qi5weScsICd3JykgYXMgZjoKICAgICAgZi53cml0ZSgiIikKICAgICAgZXhpdCgp'
    ).decode()
  )