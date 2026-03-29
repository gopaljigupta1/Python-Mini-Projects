import random
def roll_dice():
     die1 = random.randrange(1, 7)
     die2 = random.randrange(1, 7)
     return die1, die2
def display_dice(dice):
     die1, die2 = dice
     print(f"player rolled {die1} + {die2} = {sum(dice)}")

die_values = roll_dice()
display_dice(die_values)
sum_of_dice = sum(die_values)
if sum_of_dice in (7, 11):
     game_status = "win"
elif sum_of_dice in (2, 3, 12):
     game_status = "lose"
else:
     game_status = "continue"
     my_point = sum_of_dice
     print('point is', my_point)

while game_status == "continue":
     die_values = roll_dice()
     display_dice(die_values)
     sum_of_dice = sum(die_values)
     if sum_of_dice == my_point:
          game_status = "win"
     elif sum_of_dice == 7:
          game_status = "lose"
if game_status == "win":
     print('player wins')
else:
     print('player loses')