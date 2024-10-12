# import random
#
# word_list = ["aardvark", "baboon", "camel"]
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# # TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
# placeholder = ""
# word_length = len(chosen_word)
# for letter in range(word_length):
#     placeholder += "_"
# else:
#     placeholder += ""
# print(placeholder)
#
# guess = input("Guess a Letter: ").lower()
#
# # TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
# display = ""
#
# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"
# print(display)

#or

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""

for letter in chosen_word:
     placeholder += "_"
else:
    placeholder += ""
print(placeholder)


guess = input("Guess a Letter: ").lower()
display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)
