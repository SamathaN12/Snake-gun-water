from random import randint
t = ["Snake", "Gun", "Water"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = True

while player == True :
#set player to True
    player = input("Snake, Gun, Water?")
    if player == computer:
        print("Tie!")
    elif player == "Snake":
        if computer == "Gun":
            print("You lose!", computer, "shoots", player)
        else:
            print("You win!", player, "drinks", computer)
    elif player == "Gun":
        if computer == "Water":
            print("You lose!", computer, "Drowns", player)
        else:
            print("You win!", player, "shoots", computer)
    elif player == "Water":
        if computer == "Snake":
            print("You lose...", computer, "drinks", player)
        else:
            print("You win!", player, "shoots", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = True
    computer = t[randint(0,2)]

