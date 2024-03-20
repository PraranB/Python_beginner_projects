import random
max_num = input("Type the upper Limit(> 0): ")
if max_num.isdigit():
    max_num = int(max_num)
    if max_num <= 0:
        print("Enter a Valid Number next time.")
        quit()
else:
    print("Enter a Number next time!")
    quit()

random_num = random.randrange(max_num)
#print(random_num)
guess_no= 0
while True:
    guess_no+=1
    guess = input("Guess the number : ")
    if guess.isdigit():
        guess=int(guess)
        if guess == random_num:
            print("You Guessed it right!!")
            break
        elif guess > random_num:
            print("Guessed number is Greater than the ans.")   
        else:
            print("Guessed number is Smaller than the ans.")
    else:
        print("Please Enter a Number.")
        continue
    
        
print("You guessed the correct number in",guess_no,"turns. :)")