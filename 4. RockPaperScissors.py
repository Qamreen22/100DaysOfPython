# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:28:37 2023

@author: Dell
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player1 = int(input("Choose Your Weapon: Rock, Paper, Scissors!\nType\n0 for Rock\n1 for Paper\n2 for Scissors\n"))
computer = random.randint(0,2)

print("You chose:")
if player1==0:
  print(rock)
elif player1==1:
  print(paper)
else:
  print(scissors)

print("\n")

print("Computer chose:")
if computer==0:
  print(rock)
elif computer==1:
  print(paper)
else:
  print(scissors)
  
print("\n")

if computer==player1:
  print("It's a draw!!")
elif (computer==0 and player1==2) or (player1 < computer):
  print("You Lose :(")
else:
  print("You win!! :)")
