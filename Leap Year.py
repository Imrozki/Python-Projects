year = int(input("Enter the year"))
if year % 4 == 0:
    if year % 100 != 0:
        print("leap Year")
elif year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


