"""(Rock, Paper, Scissors game) by George or ffg22
Rules on how to play the game:
1. your only moves are r or R for Rock, p or P for paper, s or S for scissors and q or Q to quit the game.
2. and the computer chooses its own move.
3. after every round the scores are calculated"""

# importing the necessary modules for this project
import random
import time
import sys

state = "rock, paper, scissors by George"
print(state.upper())

time.sleep(0.3)

print("""Rules on how to play the game:
1. your only moves are r or R for Rock, p or P for paper, s or S for scissors and q or Q to quit the game.
2. and the computer chooses its own move
3. after every round the scores are calculated""")

# for calculating the scores after every round
player_Score = int()
computer_score = int()


# Creating a loop for the game
while True:
    # creating some unnecessary space
    print()
    # the computer's move
    # creating a random number generator, that generates a number from 1-10
    computer_move = random.randint(1, 10)
    # The player's move
    user_input = str(input("Your move> "))

    # trying to link the generated numbers to rock, paper, scissors
    # form the code block below, the probability of getting rock is higher than that of
    # getting scissors or paper
    if computer_move == 1 or computer_move == 2 or computer_move == 3 or computer_move == 4:
        computer_move = "rock"
    elif computer_move == 5 or computer_move == 6 or computer_move == 7:
        computer_move = "scissors"
    elif computer_move == 8 or computer_move == 9 or computer_move == 10:
        computer_move = "paper"

    # trying to link the user input to rock, paper, scissors
    if user_input == "r" or user_input == "R":
        user_input = "rock"
    elif user_input == "s" or user_input == "S":
        user_input = "scissors"
    elif user_input == "p" or user_input == "p":
        user_input = "paper"
    elif user_input == "q" or user_input == "Q":
        time.sleep(0.5)
        print("Goodbye")
        sys.exit()

    # the code for the game itself
    if computer_move == user_input:
        time.sleep(0.5)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.9)
        print("The computer's move is", computer_move)
        print("The game is a tie")
        print("Scores: ")
        time.sleep(0.3)
        print("Your score:", player_Score, "| The computer's score:", computer_score)
    elif computer_move == "rock" and user_input == "scissors":
        time.sleep(0.5)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.9)
        print("The computer's move is", computer_move)
        print("You Loose!!!!")
        computer_score = computer_score + 1
        print("Scores: ")
        time.sleep(0.3)
        print("Your score:", player_Score, "| The computer's score:", computer_score)
    elif computer_move == "rock" and user_input == "paper":
        time.sleep(0.5)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.9)
        print("The computer's move is", computer_move)
        print("You Win!!!!")
        player_Score = player_Score + 1
        print("Scores: ")
        time.sleep(0.3)
        print("Your score:", player_Score, "| The computer's score:", computer_score)
    elif computer_move == "paper" and user_input == "rock":
        time.sleep(0.5)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.9)
        print("The computer's move is", computer_move)
        print("You Loose!!!!")
        computer_score = computer_score + 1
        print("Scores: ")
        time.sleep(0.3)
        print("Your score:", player_Score, "| The computer's score:", computer_score)
    elif computer_move == "paper" and user_input == "scissors":
        time.sleep(0.5)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.9)
        print("The computer's move is", computer_move)
        print("You Win!!!!")
        player_Score = player_Score + 1
        print("Scores: ")
        time.sleep(0.3)
        print("Your score:", player_Score, "| The computer's score:", computer_score)
    elif computer_move == "scissors" and user_input == "rock":
        time.sleep(0.5)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.9)
        print("The computer's move is", computer_move)
        print("You Win!!!!")
        player_Score = player_Score + 1
        print("Scores: ")
        time.sleep(0.3)
        print("Your score:", player_Score, "| The computer's score:", computer_score)
    elif computer_move == "scissors" and user_input == "paper":
        time.sleep(0.5)
        print("Rock")
        time.sleep(0.5)
        print("Paper")
        time.sleep(0.5)
        print("Scissors")
        time.sleep(0.9)
        print("The computer's move is", computer_move)
        computer_score = computer_score + 1
        print("You Loose!!!!")
        print("Scores: ")
        time.sleep(0.3)
        print("Your score:", player_Score, "| The computer's score:", computer_score)
    else:
        print("Read the instructions and try again below")
        print("""Rules on how to play the game:
    1. your only moves are r or R for Rock, p or P for paper, s or S for scissors and q or Q to quit the game.
    2. and the computer chooses its own move
    3. after every round the scores are calculated""")

# thanks for playing I'm still learning python!!!!
