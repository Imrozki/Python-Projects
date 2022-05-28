print("Welcome to the roller coaster ride!")
height = int(input("What is your height in cm?"))
bill = 0
if height >= 120:
    print("You are eligible")
    age = int(input("Enter your age"))

    if age < 12:
        print("Child's ticket is for 5$")
        bill = 5
    elif age <= 18:
        print("Youth's ticket is for 8$")
        bill = 8
    elif age >= 45 and age <=55:
        print("Ride for free")
    else:
        print("Adult's ticket is for 12$")
        bill = 12

    photo = input("Do you want photo? Y or N?")
    if photo == "Y":
        bill += 3
        print(f"Your final bill is {bill}")
    else:
        print(f"Bill is {bill}")




else:
    print("Not eligible for the ride")







