"""Rock paper scissors game with some cool features."""
import random
import time

# Keep track of scores. set initial score to 0 - 0
PLAYER_SCORE = 0
COMPUTER_SCORE = 0

# set acceptable choices.
choices = ['rock', 'paper', 'scissors']

# Dictionary used to map the potential outcomes.
# index 0 of the list in the key identifies a win
# index 1 identifies a draw
# index 2 identifies a loss.
outcomes = {
    'rock': ['paper', 'rock', 'scissors'],
    'paper': ['scissors', 'paper', 'rock'],
    'scissors': ['rock', 'scissors', 'paper']
}

# Player name for personalised game.
player_name = input("What is your name: ")

# As the game is held in a while loop, a way to exit the game is provided.
print(f"Hey, {player_name.title()} - enter 'Q' at any point to end the game.")

# Main while loop for the game.
while True:
    # nested while loop to ensure input from user is valid
    # Also, give user opportunity to quit the game.
    while True:
        player_choice = input("\nrock paper or scissors? Your choice: ")
        if player_choice.upper() == 'Q':
            break

        if player_choice not in choices:
            print('Your choice is not valid')
            continue
        break
    # exits and breaks the game if 'Q' is entered.
    if player_choice.upper() == 'Q':
        break

    # Computer makes a random chouce from the choices list above.
    computer_choice = random.choice(choices)

    # Sleep function used throughout to add some tension - This is used throughout.
    time.sleep(1)
    # compare inputs to the outcomes dictionary above.
    # Provide text explaining the result.
    if computer_choice == outcomes[player_choice][0]:
        print(f'\nComputer went {computer_choice}!')
        time.sleep(0.5)
        print('Computer wins')
        COMPUTER_SCORE += 1
    elif computer_choice == outcomes[player_choice][1]:
        print(f'\nComputer went {computer_choice}!')
        time.sleep(0.5)
        print("It's a draw!")
    elif computer_choice == outcomes[player_choice][2]:
        print(f'\nComputer went {computer_choice}!')
        time.sleep(0.5)
        print(f"{player_name.title()} wins")
        PLAYER_SCORE += 1

    time.sleep(1)
    # Provide score updates after every round.
    if PLAYER_SCORE > COMPUTER_SCORE:
        print(f"\n{PLAYER_SCORE} - {COMPUTER_SCORE} to {player_name.title()}!")
    elif COMPUTER_SCORE > PLAYER_SCORE:
        print(f"\n{COMPUTER_SCORE} - {PLAYER_SCORE} to the computer!")
    else:
        print(f"\n{PLAYER_SCORE} - {COMPUTER_SCORE} ..... It's a draw!")

# Once user has exited the game loop provide exit message.
time.sleep(1)
print(f"\nThank you for playing, {player_name.title()}")
print("The final score is as follows:")
# Provide final scores:
time.sleep(1)
print(f"\nThe computer won {COMPUTER_SCORE} games.")
print(f"{player_name.title()}, you won {PLAYER_SCORE} games.")

time.sleep(2)
if PLAYER_SCORE > COMPUTER_SCORE:
    print(
        f"\nThis means that {player_name.title()}, you are the overall winner.")
elif PLAYER_SCORE < COMPUTER_SCORE:
    print(
        f"\nSorry {player_name.title()}, This means that the computer won overall")
else:
    print(
        f"\nWow - Would you look at that. {player_name.title()}, it's a draw overall!")
