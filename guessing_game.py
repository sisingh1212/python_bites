import random
import string
print("Welcome to Number Guessing game")
choice_d=True
while choice_d:
  choice_difficulty=input("You want to play easy, hard difficulty level: ")
  if choice_difficulty == 'easy':
    tries=10
    choice_d=False
  elif choice_difficulty == 'hard':
    tries=5
    choice_d=False
  else:
    choice_d=True
    print(f"{choice_difficulty} is not 'hard' or 'easy', please select the right options")

player_try=0
game_number=int(random.choice([number_element for number_element in range(1,101)]))
while player_try < tries:

  
  try:
    player_num_choice=int(input("Enter any number between 1-100: "))
    #int(player_num_choice)

    print(player_try)
    if player_num_choice == game_number:
      print(f"You found the number : {game_number} - HURRAY! in {player_try+1} attempts")
      break
    elif player_num_choice > game_number:
      print(f"{player_num_choice} is too high \n guess again")
    elif player_num_choice < game_number:
      print(f"{player_num_choice} is too low \n guess again")
    else:
      print("the number is not enter correctly")
    player_try=player_try+1
    if player_try == tries:
      print(f"Dear, you have tried {player_try } times, unfortunately you have exhausted the nymber of turns allowed!")
      break
  except ValueError as en:
    print(f"Number can only be a digit: {en}")



