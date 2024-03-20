import random
user_score = 0
computer_score = 0

options = ["rock", "paper","scissor"]
while True:
    user_played = input("type Rock/Paper/Scissor or Q to Quit: ").lower()
    if user_played == "q":
        break

    if user_played not in options:
        print("Invalid Input!!")
        continue

    random_number = random.randint(0,2)
    computer_played = options[random_number]
    print("Computer Played",computer_played + ".")

    if user_played == computer_played:
        print("It's a Tie.")

    elif user_played == 'rock' and computer_played == 'scissor':
        print("you won.")
        user_score +=1

    elif user_played == 'paper' and computer_played == 'rock':
        print("you won.")
        user_score +=1

    elif user_played == 'scissor' and computer_played == 'paper':
        print("you won.")
        user_score +=1

    else:
        print("computer won")
        computer_score +=1

print("You won",user_score,"times.")
print("Computer won",computer_score,"times.")
print("GoodBye!")