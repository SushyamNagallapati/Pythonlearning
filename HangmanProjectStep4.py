# import random
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# word_list = ["aardvark", "baboon", "camel"]
#
# # TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #  Set 'lives' to equal 6.
# lives = 6
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)
#
# game_over = False
# correct_letters = []
#
# while not game_over:
#     guess = input("Guess a letter: ").lower()
#
#     display = ""
#
#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#
#     print(display)

    # # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    # #  If lives goes down to 0 then the game should stop and it should print "You lose."
    #
    # if guess not in chosen_word:
    #     lives -= 1
    #     print(lives)
    #     if lives == 0:
    #         game_over = True
    #         print("You Lose!")
    #
    #
    # if "_" not in display:
    #     game_over = True
    #     print("You win.")
    #
    #
    # # TODO-3: - print the ASCII art from 'stages'
    # #  that corresponds to the current number of 'lives' the user has remaining.
    #
    #
    # print(stages[lives])


#or

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for letter in chosen_word:
     placeholder += "_"
else:
    placeholder += ""
print(placeholder)


correct_letters = []
game = False
while not game:
    guess = input("Guess a Letter: ").lower()

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    # # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    # #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        print(lives)
        if lives == 0:
            print("You Lose!")
            game = True

    if display == chosen_word:
        game = True
        print("Yov Won!")
      
