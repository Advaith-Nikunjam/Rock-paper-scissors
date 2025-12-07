import random

print("Hai Buddy Welcome to Rock Paper Scissors")
ready = input("Are you ready to play? ")
if ready != "yes":
    print("See you when you are ready to play!")
    quit()

options = ["rock","paper","scissors"]

point = 0

while True:
    choice = input("Enter Rock/Paper/Scissors or Q to quit: ")
    if choice.lower() == "q": 
        print(f"Your total point is {point}")
        if point>0:
            print("You won!")
        elif point == 0:
            print("Its a draw")
        else:
            print("You lost")

        print("Thanks for playing! See you later")
        quit()


    if choice.lower() not in options:
        print("Enter a correct choice.")
        continue


    random_number = random.randint(0,2)
    computer_choice = options[random_number]

    if computer_choice == "rock" and choice == "paper":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("You got one point!")
        point+=1
        continue

    elif computer_choice == "rock" and choice == "rock":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("No point no loss")
        continue

    elif computer_choice == "paper" and choice == "scissors":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("You got one point!")
        point+=1
        continue

    elif computer_choice == "paper" and choice == "paper":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("No point no loss")
        continue


    elif computer_choice == "scissors" and choice == "rock":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("You got one point!")
        point+=1
        continue

    elif computer_choice == "scissors" and choice == "scissors":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("No point no loss")
        continue


    elif computer_choice == "paper" and choice == "rock":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("You lost one point!")
        point-=1
        continue

    elif computer_choice == "scissors" and choice == "paper":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("You lost one point!")
        point-=1
        continue

    elif computer_choice == "rock" and choice == "scissors":
        print(f"Your choice is {choice} and computer choice is {computer_choice}")
        print("You lost one point!")
        point-=1
        continue
