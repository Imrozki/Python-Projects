from art import data, logo5, vs
import random

print(logo5)



def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"    # Problem
    else:
        return guess == "b"    # Problem


#Make the game repeatable

score = 0
account_b = random.choice(data)  # Account is created and stored in the account_a

game_should_continue = True

while game_should_continue == True:
    # Generate random account from game data

    account_a = account_b  # Account a is getting replaced by previous account b
    account_b = random.choice(data)

    while account_a == account_b:       # This WHILE will keep checking until account a and account b are different
        account_b = random.choice(data)

    print(f"Comapare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #Ask user to make a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ### Get followers count
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Give user feedback on their guess
    ## Keep Score
    if is_correct:
        score += 1
        print(f"You are right! Current Score is {score}")
    else:
        print(f"You are wrong. Final Score is {score}")
        game_should_continue = False
















