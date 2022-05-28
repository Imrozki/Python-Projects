
import random
names_string = input("Names seperated by commas")
name = names_string.split(", ")

num_of_people = len(name)
print(num_of_people)
random_choice = random.randint(0 , num_of_people-1)

# You can also use rand.choice(name) to get random strings

p_name = name[random_choice]

print("person who will pay the bill is" + " " +  p_name)






