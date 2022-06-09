# limited number of attempts
attempt = 5
# stored answer
answer = 42

print('You have 5 attempts. Good luck!')

# while loop condition if the attempt are greater than 0
while attempt > 0:
    while True:
        try:
            # the user will be asked and stored in user_input
            user_input = int(input('\nWhat is the answer to life, the universe and everything?'))
            if user_input == " ":
                print("Your input is empty. Try again.")
            else:
                break  # exit the loop
        except:
            print("Your guess was not an Integer. Try again.")

    # will decrease attempts if user answers incorrectly
    attempt -= 1
    # if statement to check if the user input matches the answer
    if user_input == answer:
        print('You won!')
        attempt = 0  # will end the game
    elif attempt == 0:
        print("\nYou are out of attempts! The winning number was:", answer, "\nBetter luck next time!")
    elif attempt == 1:
        print("\nSorry, that is an incorrect guess. Try again! You have 1 try remaining.")
    else:
        print("\nSorry, that not the correct number. Try again! You have {} tries remaining.".format(attempt))
