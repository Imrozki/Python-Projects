from art import logo4
from random import randint
print(logo4)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Make a function to set difficulty
def set_difficulty():
    level = input("Choose difficulty: 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

    

#Functiomn to check against actual answer
def check_answer(guess, answer, turns):
    """ Checks answers and returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns-1
    elif guess < answer:
        print("Too low")
        return turns-1
    else:
        print(f"You guessed the correct answer which was {answer}")

def game():
    print("Welcome to the guessing Game")
    print("I am thinking of a number between 1-100")

    #Choose random int 1 and 100
    answer = randint(1,100)
    print(answer)

    turns = set_difficulty()

    #Repeat as long as attempts left and they are wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left")
        #Let User guess number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose")
            return
        else:
            print("Guess again")



game()


#Track the number of turns and reduce it by 1 when wrong








