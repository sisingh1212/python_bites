import random
import string
print("""

   _____                                                     _                 _ 
  / ____|                                                   | |               | |
 | |  __ _   _  ___  ___ ___    __ _   _ __  _   _ _ __ ___ | |__   ___ _ __  | |
 | | |_ | | | |/ _ \/ __/ __|  / _` | | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| | |
 | |__| | |_| |  __/\__ \__ \ | (_| | | | | | |_| | | | | | | |_) |  __/ |    |_|
  \_____|\__,_|\___||___/___/  \__,_| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|    (_)
                                                                                 
                                                                                 

""")
print("Welcome to Number Guessing game")
easy_turns=10
hard_turns=5
def difficulty_choice():
  choice_d=True
  while choice_d:
    choice_difficulty=input("You want to play easy, hard difficulty level: ")
    if choice_difficulty == 'easy':
      
      choice_d=False
      return easy_turns
    elif choice_difficulty == 'hard':
      
      choice_d=False
      return hard_turns
    else:
      choice_d=True
      print(f"{choice_difficulty} is not 'hard' or 'easy', please select the right options")

def game_check(tries, game_number):
  player_try=0
  
  while player_try < tries:

  
    try:
      if player_try == (tries-1):
        print(f"This is your last try , c'mon!!!!")
      else:
        print(f"You have {tries-player_try} turns remaining!")
      player_num_choice=int(input("Enter any number between 1-100: "))
      
    #int(player_num_choic
      player_try=player_try+1
      if player_num_choice == game_number:
        print(f"You found the number : {game_number} - HURRAY! in {player_try} attempts")
        break
      elif player_num_choice > game_number:
        print(f"{player_num_choice} is too high)")
        if player_try == tries:
          pass
        else:
          print("guess again")
      elif player_num_choice < game_number:
        print(f"{player_num_choice} is too low" )
        if player_try == tries:
          pass
        else:
          print("guess again")
      else:
        print("the number is not enter correctly")
      
      if player_try == tries:
        print(f"Dear, you have tried {player_try } times, unfortunately you have exhausted the number of turns allowed!")
        break
    except ValueError as en:
      print(f"Number can only be a digit: {en}")

def main():
  tries=difficulty_choice()
  game_number=int(random.choice([number_element for number_element in range(1,101)]))
  game_check(tries=tries, game_number=game_number)
if __name__== '__main__':
  main()
