
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("Choose  1 for rock , 2 for paper, 3 for scissor"))
if choice < 1 or choice > 3:
    print("You have chosen invalid number! Please choose a correct number!")
else:
 hand_sign = [rock, paper, scissors]
 your_sign = hand_sign[choice - 1]

 print(f" Your sign{your_sign}")

 computer = random.choice(hand_sign)

 print(f"The computer chooses{computer}")


 if your_sign == rock and computer == scissors:
    print("You Win! Congratulations")
 elif your_sign == scissors and computer == paper:
    print("You Win! Congratulations")
 elif your_sign == paper and computer == rock:
    print("You Win! Congratulations")
 elif your_sign == computer:
    print("It is a draw")
 else:
    print("You Lose!")



