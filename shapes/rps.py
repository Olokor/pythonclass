import random


# how many times we are playing the game
repeat = int(input("how many times you wanna the game?:  "))
point = 0



for numberofrepeat in range(repeat):

    choice = ["rock", "paper", "siscors"]#choice for my computer
    computer_choice = random.choice(choice)#computer pick at random form choice 
    # my choice
    my_choice = input("enter rock, paper, siscors:  ")
    my_choice = my_choice.casefold()

    # logic of our game

    if my_choice == "rock" or my_choice == "paper" or my_choice == "siscors":
        # check for a tie....
        if my_choice == computer_choice:
            print("it's a tie.....")
            print(f"your choice is {my_choice} and computer is choice is {computer_choice} and your point is {point}")
        # check for my winning
        elif (
            my_choice == "rock" and computer_choice == "siscors" or my_choice == "siscors" and
            computer_choice == "paper" or my_choice == "paper" and computer_choice == "rock"
        ):
            print("you win!!!")
            point = point + 1
            print(f"your choice is {my_choice} and computer is choice is {computer_choice}  and your point is {point}")

        
        else:
            print("you lost!!")
            point = point - 1
            print(f"your choice is {my_choice} and computer is choice is {computer_choice} and your point is {point}")
    else:
        print("you have entered an invalid input, only rock, paper and sioscors are valid input")