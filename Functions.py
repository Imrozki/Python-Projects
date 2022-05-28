
def greet():
    print("Hello")
    print("Namaste")
    print("Bonjour")

#for i in range(0,3):
 #greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today {name}?")

#greet_with_name("Waqas")

# Functions with more than 1 input

def greet_with(name , location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with(location="Kolkata",name="Waqas")
