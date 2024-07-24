import random
import time
print("\nWelcome to the Rocks Papers Scissors Game!!\n")
print("Here are the rules of this game: \n\nRock vs Paper --> Paper wins \nRock vs Scissors --> Rock wins \nPaper vs Scissors --> Scissors wins\n")

list = ["Rocks","Papers","Scissors"]
for i in list:
     print(i)

while True:
    user_input = input("\nEnter your choice or press q to quit the game: ")
    if user_input == "q":
        break
    if user_input == "Rocks":
        print("You chose", user_input)
    elif user_input == "Scissors":
        print("Your choice is", user_input)
    elif user_input == "Papers":
        print("Your choice is", user_input)
    else:
        print("Invalid Option.")

    print("Let's Wait for Computers turn...")
    time.sleep(2)
    computer_input = random.choice(list)
    print("Computer's choice is:", computer_input)
    print(user_input, "Vs", computer_input)
    if user_input == "Rocks" and computer_input == "Papers":
        print("Computer wins")
    elif user_input == "Rocks" and computer_input == "Scissors":
        print("User wins.")
    elif user_input == "Papers" and computer_input == "Scissors":
        print("Computer wins.")
    elif user_input == "Rocks" and computer_input == "Rocks":
        print("It's a Draw")
    elif user_input == "Papers" and computer_input == "Papers":
        print("It's a Draw")
    elif user_input == "Scissors" and computer_input == "Rocks":
        print("Computer wins.")
    elif user_input == "Scissors" and computer_input == "Papers":
        print("User wins.")
    elif user_input == "Scissors" and computer_input == "Scissors":
        print("It's a Draw.")
    elif user_input == "Rocks" and computer_input == "Rocks":
        print("It's a Draw.")
    elif user_input == "Papers" and computer_input == "Rocks":
        print("User wins.")
    else:
        pass
