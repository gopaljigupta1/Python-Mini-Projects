import random
def play_game():
     print("start the game")
     game = {1: "stone",
        2: "paper",
        3: "scissor"}
     you = input("your choice:")
     if you not in game.values():
      print("please enter a valid choice")
      # return
     random_choice = random.choice(list(game.values()))
     computer = random_choice
    
     print(f"computer choice: {computer}")
     if you == "stone" and computer == "paper":
       print("computer won")
     elif you == "stone" and computer == "scissor":
       print("you won")
     elif you == "paper" and computer == "stone":
       print("you won")
     elif you == "paper" and computer == "scissor":
       print("computer won")
     elif you == "scissor" and computer == "stone":
       print("computer won")
     elif you == "scissor" and computer == "paper":
       print("you won")
     else:
       print("draw")
def play_again():
     while True:
          again = input("do you want to play again? (ya/no) ")
          if again.lower() == "ya":
               play_game() 
               break
          elif again.lower() == "no":
               print("thank you for playing")
               exit()
          else:
               print("please enter ya or no")
              #  return play_again()
          
while True:
     play_game()
     play_again()