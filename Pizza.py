print("Welcome to Python Pizza")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

small = 15
medium = 20
large = 25
bill = 0

if size == "S":
    if add_pepperoni == "Y":
        bill = small + 2

elif size == "M":
    if add_pepperoni == "Y":
        bill = medium + 3

elif size == "L":
    if add_pepperoni == "Y":
    bill = large + 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is {bill}$")

else:
    print("Choose the correct option")




