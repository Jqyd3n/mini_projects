import random

print("Welcome to the Number Game!")
print("You will be prompted to choose a number.")
print("The machine will also choose a number within the range you specify.")
print("The one who chooses the higher number wins and gets a point.")
print("If both choose the same number, it's a tie and no points are awarded.")
print("You can NOT choose the same number twice")
print("If you ever want to stop playing, just type 'exit' when prompted for a number.")
print()

while True:
    max_number = input("Enter the maximum number: ")
    if not max_number.isdigit() or int(max_number) < 1:
        print("Please enter a valid positive integer for the maximum number.")
        continue
    max_points = input("Enter the points needed to win: ")
    if not max_points.isdigit() or int(max_points) < 1:
        print("Please enter a valid positive integer for the points needed to win.")
        continue

    available_user_numbers = list(range(1, int(max_number) + 1))
    available_machine_numbers = list(range(1, int(max_number) + 1))
    user_score = 0
    machine_score = 0
    used_numbers = []

    while user_score < int(max_points) and machine_score < int(max_points):
        while True:
            # Get user input and handle exit condition
            user_input = input("Choose your number: ")
            if user_input.lower() == 'exit':
                print("Thank you for playing the Number Game! Goodbye!")
                exit()

            # Validate user input
            user_number = int(user_input)
            if user_number in used_numbers:
                print("You have already chosen that number. Please choose a different number.")
            elif user_number < 1 or user_number > int(max_number):
                print(f"Please choose a number between 1 and {max_number}. Or type 'exit' to quit.")
            elif str(user_number).lower() == 'exit':
                print("Thank you for playing the Number Game! Goodbye!")
                exit()
            else:
                used_numbers.append(user_number)
                available_user_numbers.remove(user_number)
                break

        # Machine chooses a number
        machine_number = random.choice(available_machine_numbers)
        available_machine_numbers.remove(machine_number)

        # Determine the winner of the round
        if user_number > machine_number:
            user_score += 1
            print(f"You chose {user_number}, machine chose {machine_number}. You win this round!")
        elif machine_number > user_number:
            machine_score += 1
            print(f"You chose {user_number}, machine chose {machine_number}. Machine wins this round!")
        else:
            print(f"Both chose {user_number}. It's a tie!")

    # Announce the overall winner
    if user_score == int(max_points):
        print(f"Congratulations! You reached {max_points} points and won the game!")
    else:
        print(f"The machine reached {max_points} points and won the game. Better luck next time!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'y':
        print("Thank you for playing the Number Game! Goodbye!")
        break
