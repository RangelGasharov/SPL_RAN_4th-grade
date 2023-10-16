import random

amount_of_dice_rolls = 6
isGoing = True


def get_sum_dices(amount):
    sum_dice_rolls = 0
    for num in range(1, amount + 1):
        random_num = random.randint(1, 6)
        sum_dice_rolls += random_num
    return sum_dice_rolls


while isGoing:
    selection = int(input("Enter 1 to start the game. Enter 2 to stop the game\n"))

    if selection == 1:
        player_points = get_sum_dices(amount_of_dice_rolls)
        computer_points = get_sum_dices(amount_of_dice_rolls)

        if player_points > computer_points:
            print("Congrats, you have won!", player_points, "is greater than", computer_points, "\n")
        elif computer_points > player_points:
            print("Sorry, you have lost.", player_points, "is smaller than", computer_points, "\n")
        else:
            print("Draw! Both you and the computer have", player_points, "points", "\n")
    if selection == 2:
        isGoing = False
