import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_list = [rock, paper, scissors]
choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
game_lst = ["rock", "paper", "scissors"]
random_int = random.randint(0, len(game_list)-1)
print(game_list[choice])

print('Computer chose:\n')

print(game_list[random_int])

comp_choice = game_lst[random_int]
gamer_choice = game_lst[choice]

if comp_choice == "scissors" and gamer_choice == "rock":
    print('You win')
elif gamer_choice == "scissors" and comp_choice == "rock":
    print("You lose")
elif gamer_choice == "scissors" and comp_choice == "paper":
    print("You win")
elif gamer_choice == "paper" and comp_choice == "scissors":
    print("You lose")
elif gamer_choice == "paper" and comp_choice == "rock":
    print("You win")
elif gamer_choice == "rock" and comp_choice == "paper":
    print("You lose")
else:
    print('Draw')
