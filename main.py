import random

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

# 0 = rock
# 1 = paper
# 2 = scissors

game_images = [rock,paper,scissors]

user_input = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors. \n"))

if user_input >= 3 or user_input < 0:
  print("You typed invalid number. Try again!")
else:

  print(game_images[user_input])
  
  computer_chose = random.randint(0,2)
  print("Computer chose: ")
  print(game_images[computer_chose])

  if computer_chose == user_input:
    print("It's a draw!")
  elif computer_chose == 0 and user_input == 2:
    print("You lose!")
  elif computer_chose == 2 and user_input == 0:
    print("You win!")
  elif computer_chose > user_input: 
    print("You lose!")
  else: 
    print("You win!")