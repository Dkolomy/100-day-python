print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("Which direction do you want to go? (left or right) ")
if direction.lower() == "right":
    print("You fell into a hole. Game Over.")
elif direction.lower() == "left":
    print("You found a river. input('Do you want to swim or wait? (swim or wait) ')")
    action = input("Do you want to swim or wait? (swim or wait) ")
    if action.lower() == "swim":
        print("You were eaten by a crocodile. Game Over.")
    elif action.lower() == "wait":
        print("There are 3 doors (red, blue, yellow). ")
        door = input("Which door do you want to open? (red, blue, yellow) ")
        if door.lower() == "red":
            print("You were burned by fire. Game Over.")
        elif door.lower() == "blue":
            print("You were eaten by a dragon. Game Over.")
        elif door.lower() == "yellow":
            print("You found the treasure! You win!")
        else:
            print("Invalid door. Game Over.")
    else:
        print("Invalid action. Game Over.")
else:
    print("Invalid direction. Game Over.")