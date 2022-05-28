print("Welcome to treasure hunt")
direction = input("Choose left or right")
direction.lower()
if direction == "right":
    a = input("There is a sea infront of you, you want to swim or wait?")
    a.lower()
    if a == "wait":
        b = input("Choose a door, red or yellow")
        b.lower()
        if b == "red":
            print("You found the teasure!")
        else:
            print("Wrong Door. GAME OVER!")
    else:
        print("You died as a shark ate you. GAME OVER!")

else:
   print ("GAME OVER!")

