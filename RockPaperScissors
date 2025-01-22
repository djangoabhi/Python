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

game_images = [rock, paper, scissors]
game_choice = ["Rock", "Paper", "Scissors"]

user_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors:\n"))
if user_choice >=0 and user_choice <=2:
    print(f"You chose: {game_choice[user_choice]} {game_images[user_choice]}")
computer_choice = random.randint(0,2)
print(f"Computer chose {game_choice[computer_choice]}{game_images[computer_choice]}")

if user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins")
elif computer_choice > user_choice:
    print ("Computer wins")
elif user_choice > computer_choice:
    print("You win")
elif user_choice == computer_choice:
    print("It's a draw")
