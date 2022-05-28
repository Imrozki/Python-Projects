print("Welcome to Love Calculator")
name1 = input("Enter your name")
name2 = input("Enter their name")

sum = name1 + name2
n1 = sum.lower()

t = n1.count("t")
r = n1.count("r")
u = n1.count("u")
e = n1.count("e")

true = t + r + u + e 
l = n1.count("l")
o = n1.count("o")
v = n1.count("v")
e = n1.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} Its like cocacola and mentos")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(love_score)


