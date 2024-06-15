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
options = [rock, paper, scissors]
print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
user_choice = int(input())
computer_choice = random.randint(0,2)
if user_choice > 2 or user_choice < 0:
  print("um wut dawg?")
  print("i don't have the capabilities to understand that...")
else:
  print(options[user_choice])
  print("Computer chose:")
  print(options[computer_choice])
  if user_choice == computer_choice:
    print("Tie! Try again.")
  elif user_choice == 0:
    if computer_choice == 1:
      print("You lose!")
    else:
      print("You win!")
  elif user_choice == 1:
    if computer_choice == 2:
      print("You lose!")
    else:
      print("You win!")
  else:
    if computer_choice == 0:
      print("You lose!")
    else:
      print("You win!")
