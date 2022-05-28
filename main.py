# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
left = 90 - int(age)

print(f"Your remaining age is {left}")

days_lived = age * 365
weeks_lived = age * 52
months_lived = age * 12

days_remaining = left * 365
weeks_remaining = left * 52
months_remaining = left * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks and{months_remaining} months remaining")








