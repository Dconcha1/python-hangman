import re


answer_characters = "What's Up, Doc?"

answer_characters = answer_characters.upper()


answer_guesses = []


for current_answer_character in answer_characters:
  if re.search("^[A-Z]$", current_answer_character):
    answer_guesses.append(False)
  else:
    answer_guesses.append(True)


guessed_letters = []
num_of_incorrect_guesses = 0

while num_of_incorrect_guesses < 5 and False in answer_guesses:
  print("-----------------------")
  print("Guessed letters:   ", end = "")

  for current_guessed_letters in guessed_letters:
    print(f"{current_guessed_letters} ", end = "")

  print()

  print(f"Number of incorrect gueses remaining:  {5 - num_of_incorrect_guesses}")

  print()

  for answer_index in range(len(answer_characters)):
    if answer_guesses[answer_index]:
      print(answer_characters[answer_index], end = "")
    else:
      print("_", end = "")

  print()

  letter = input("Enter a letter: ")

  letter = letter.upper()

  if letter not in guessed_letters and len(letter) == 1 and re.search("^[A-Z]$", letter):
    if letter in answer_characters:

      for current_answer_index in range(len(answer_characters)):
        if letter == answer_characters[current_answer_index]:
          answer_guesses[current_answer_index] = True
    else:
      num_of_incorrect_guesses += 1


if num_of_incorrect_guesses < 5:
  print("Congrats U Solved The Puzzle!")
else:
  print("Sorry U Ran Out of Guesses :/")

print(f"{answer_characters} is the answer to the puzzle.")