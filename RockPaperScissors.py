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
image = [rock, paper, scissors]
player =  int(input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
print(image[player])

computer = random.randint(0, 2)
print("Computer Chose:")
print(image[computer])

if player >= 3 or player < 0:
    print("Type error. You Lose!")
elif player == 0 and computer == 2:
    print("You Win!")
elif player == 2 and computer == 0:
    print("You Lose!")
elif computer > player:
    print("You Lose!")
elif player > computer:
    print("You Win!")
elif player == computer:
    print("Draw!")
