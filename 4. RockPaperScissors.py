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

game_image = [rock, paper, scissors]
player1 = int(input("Choose Your Weapon: Rock, Paper, Scissors!\nType\n0 for Rock\n1 for Paper\n2 for Scissors\n"))
print("\n")
if player1>2:
  print("Invalid Choice!")
else:
  computer = random.randint(0,2)

  print(f"You chose:\n{game_image[player1]}\n")
  print(f"Computer chose:\n{game_image[computer]}\n")

  if computer==player1:
    print("It's a draw!!")
  elif (player1==0 and computer==2):
    print("You win!! :)")
  elif (computer==0 and player1==2) or (player1 < computer):
    print("You Lose :(")
  else:
    print("You win!! :)")
